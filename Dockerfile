FROM python:3.8-slim-buster as python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# builder-base is used to build dependencies
FROM python-base as builder-base
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    vim \
    netcat \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/*


# Install poetry
ENV POETRY_VERSION=1.1.5
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    chmod a+x /opt/poetry/bin/poetry


FROM python-base as production

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
COPY . /app
RUN poetry install --no-dev

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]