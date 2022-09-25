FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /family_budget

# Install dependencies
COPY Pipfile Pipfile.lock /family_budget/
RUN pip install pipenv && pipenv install --system

COPY . /family_budget/