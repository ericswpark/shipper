# Stage 1

FROM python:3.9-alpine as builder

# Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /usr/src/shipper

# Install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/shipper/wheels -r requirements.txt

# Stage 2

FROM python:3.9-alpine

# create directory for the shipper user
RUN mkdir -p /home/shipper

# create the shipper user
RUN addgroup -S shipper && adduser -S shipper -G shipper

# create the appropriate directories
ENV HOME=/home/shipper
ENV APP_HOME=/home/shipper/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/media
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/shipper/wheels /wheels
COPY --from=builder /usr/src/shipper/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the shipper user
RUN chown -R shipper:shipper $APP_HOME

# change to the shipper user
USER shipper

# Run entrypoint.sh
ENTRYPOINT ["/home/shipper/web/entrypoint.sh"]
