FROM python:3.11-buster
RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app
# COPY requirements.txt .
COPY poetry.lock .
COPY pyproject.toml .
# RUN pip install --upgrade -r requirements.txt
RUN poetry install

ADD . /app

EXPOSE 80

CMD ["poetry","run","python", "-m","uvicorn", "run:app", "--proxy-headers", "--reload","--host","0.0.0.0","--port","80"]
# CMD [ "poetry", "run", "python", "run.py" ]
# CMD [ "uvicorn", "run:app", "--proxy-headers", "--reload","--host","0.0.0.0","--port","80"]