FROM python:3.6

RUN pip install \
    jinja2==2.10 \
    click==6.0

RUN mkdir /code
WORKDIR /code
ADD setup.py .
ADD ./kiss kiss
RUN pip install -e .

CMD ["kiss"]
