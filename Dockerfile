FROM python:3.6

RUN pip install \
    jinja2==2.10 \
    click==6.0 \
    pyyaml==3.12

RUN mkdir /code
WORKDIR /code
ADD setup.py .
ADD ./kiss kiss
RUN pip install .

RUN mkdir /example
WORKDIR /example

CMD ["kiss"]
