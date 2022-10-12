FROM python:3.9-alpine as base

FROM base as builder
WORKDIR /work

COPY requirements-dev.txt .
COPY requirements.txt .

RUN pip install --prefix=/install -r requirements-dev.txt -r requirements.txt

###############################################################

FROM base
WORKDIR /work

ENV LOGGING_ENABLED="false"
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apk add bash make

COPY analyzer/ ./analyzer/
COPY samples/ ./samples/
COPY tests/ ./tests/

COPY main.py .
COPY Makefile .
COPY pytest.ini .
COPY .coveragerc .
COPY requirements-dev.txt .
COPY requirements.txt .

COPY --from=builder /install /usr/local

CMD ["/usr/bin/make", "sample"]
