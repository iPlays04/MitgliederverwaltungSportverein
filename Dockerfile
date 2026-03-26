FROM python:3

WORKDIR /MVS/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["fastapi", "run", "./src/main.py", "--port", "80"]
