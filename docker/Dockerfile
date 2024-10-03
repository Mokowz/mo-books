FROM python:3.13.0rc3-slim-bookworm

ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR app/django/mo_books/

COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]
