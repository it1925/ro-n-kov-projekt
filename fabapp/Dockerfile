FROM python:3.11

WORKDIR /fabapp
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]