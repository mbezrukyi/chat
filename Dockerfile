ARG WORKDIR=/home/chat \
    VIRTUALENV=$WORKDIR/env \
    VPATH=$VIRTUALENV/bin


FROM python:3.12-slim AS build

ARG WORKDIR \
    VIRTUALENV \
    VPATH

ENV PATH=$VPATH:$PATH

WORKDIR $WORKDIR

RUN python3 -m venv $VIRTUALENV

COPY . .

RUN pip install .


FROM python:3.12-slim AS final

ARG WORKDIR \
    VIRTUALENV \
    VPATH

ENV PATH=$VPATH:$PATH

WORKDIR $WORKDIR

COPY --from=build $VIRTUALENV $VIRTUALENV

CMD server & client
