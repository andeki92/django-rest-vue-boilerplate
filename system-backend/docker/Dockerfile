FROM python:3.6.6-alpine3.7

LABEL Name=zenith Version=0.0.1


ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true \
    PIPENV_DOTENV_LOCATION=config/.env


RUN apk --no-cache add \
    bash \
    build-base \
    curl \
    gcc \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    musl-dev \
    postgresql-dev \ 
    tini


COPY . /code
WORKDIR /code

# This is a special case. We need to run this script as entry point:
COPY ./docker/entrypoint.sh /docker-entrypoint.sh

RUN chmod +x "/docker-entrypoint.sh" \
    && pip install pipenv \
    && pipenv install $(test "$DJANGO_ENV" == production || echo "--dev") --deploy --system --ignore-pipfile

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]