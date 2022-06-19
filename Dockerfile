#FROM python:3 AS BUILDER
FROM debian:unstable AS BUILDER

RUN apt-get update && apt-get --yes install python3-minimal python-is-python3

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python build-rootfs.py

FROM scratch

COPY --from=BUILDER /usr/src/app/rootfs/ /

ENTRYPOINT [ "/bin/toybox", "sh" ]
