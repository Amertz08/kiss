FROM python:3.6

RUN pip install \
    jinja2==2.10 \
    click==6.0

RUN mkdir /code
WORKDIR /code
ADD kiss.py .

CMD ["python", "kiss.py"]
