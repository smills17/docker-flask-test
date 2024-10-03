FROM python:3.12-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8087
ENTRYPOINT ["python"]
CMD ["src/app.py"]
