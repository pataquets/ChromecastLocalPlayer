FROM python:3

RUN  \
  pip install --no-cache-dir \
    bottle \
    pychromecast

WORKDIR /usr/src/app/
COPY . /usr/src/app/

ENTRYPOINT [ "python", "./Main.py" ]
