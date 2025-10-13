# DjangoCourseWork

Welcome — this repository contains curated Django coursework, example projects, and practical exercises that cover core and advanced web development topics using Django and its ecosystem.

The materials focus on real-world skills: building REST APIs, background task processing, search integration, message queues, deployment patterns, and reusable components (mixins).

## Table of contents

- About
- Highlights / Tech stack
- Example projects and labs
- Getting started (dev setup)
- Components and patterns covered
- Deployment notes
- Contributing
- License

## About

This repo is a learning and reference workspace for Django developers. It includes hands-on projects and small apps that demonstrate how to architect and ship Django applications with production-ready components:

- Django best-practices, project structure and apps
- Django REST Framework (DRF) for APIs
- Background processing with Celery and Redis (and RabbitMQ where applicable)
- Full-text search via Elasticsearch (or OpenSearch)
- Message queue examples using RabbitMQ
- Useful Mixins and utility modules for views, serializers, and models
- Deployment guides and examples (Docker, Gunicorn, Nginx, systemd)

Whether you are following these exercises as part of a course or browsing for reference patterns, the code is intentionally practical and modular.

## Highlights / Tech stack

- Python 3.10+ (project uses modern typing and Django-compatible patterns)
- Django (core web framework)
- Django REST Framework (DRF)
- Celery — async/background task processing
- Redis — broker/result backend for Celery (also used as a cache)
- RabbitMQ — alternative message broker examples
- Elasticsearch / OpenSearch — search and document indexing
- Docker & Docker Compose — reproducible local environment
- PostgreSQL (recommended for production examples)
- Gunicorn + Nginx — WSGI server + reverse proxy examples

## Example projects and labs (what you'll find)

- Simple blog app — models, admin, templates, and basic views
- API-first bookstore — fully documented DRF API with pagination, filtering, and authentication
- Background tasks lab — sending emails, image processing, CSV import with Celery + Redis
- Search workshop — indexing models into Elasticsearch and building search endpoints
- Messaging demo — producer/consumer patterns using RabbitMQ
- Mixins & utilities — reusable view/serializer mixins (search, soft-delete, audit, bulk actions)
- Deployment samples — Docker Compose stacks for local development and sample production configs

Each example contains a README with focused instructions and small test data so you can run the lab quickly.

## Getting started (development setup)

The repo is intentionally flexible. Below is a minimal local development setup using Python venv and Docker Compose for services (Redis, RabbitMQ, Elasticsearch). Adjust versions to match your system.

1. Clone the repo

   git clone https://github.com/allosharma/DjangoCourseWork.git
   cd DjangoCourseWork

2. Create and activate a virtual environment

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install Python dependencies

   pip install -r requirements.txt

4. Start supporting services with Docker Compose (optional but recommended)

   docker compose up -d

   Services commonly used in the exercises:
   - redis:6379 (Celery broker/result)
   - rabbitmq:5672 (alternate broker)
   - elasticsearch:9200 (search index)
   - postgres:5432 (database)

5. Run migrations and start the dev server

   python manage.py migrate
   python manage.py runserver

6. Start Celery worker (in a separate terminal)

   celery -A firstproject worker -l info

Replace `firstproject` with the Django project name of the sample or app you want to run.

If you prefer Windows native services, install Redis/RabbitMQ locally or run them inside Docker containers.

## Components & Patterns covered

- Django project layout and app modularization
- Models: relationships, constraints, signals, custom managers
- Admin: customizations and ergonomics for real data
- Views: class-based views, function-based views, and custom Mixins
- DRF: ViewSets, Routers, Serializers, permission classes, throttling
- Mixins: reusable view/serializer mixins (search, soft-delete, audit, bulk actions)
- Background tasks: Celery tasks, periodic tasks (beat), task retries and monitoring
- Caching: Redis integration and cache patterns
- Messaging: RabbitMQ examples for pub/sub and work queues
- Search: indexing models, mapping, analyzers, and search endpoints
- Testing: unit tests for models, views, APIs and integration tests for Celery tasks
- DevOps: Docker Compose, Dockerfiles, environment configurations, and tips for deploying to VPS or cloud

## Deployment notes

This repo includes example deployment configurations and guidance:

- Dockerfile examples per service
- Docker Compose for local stacks and CI-friendly builds
- Gunicorn configuration and systemd unit snippets
- Nginx reverse proxy sample for static/media handling and TLS termination
- Using environment variables for secrets and 12-factor app patterns

Quick production checklist:

1. Use PostgreSQL (production-ready settings) and migrate data
2. Configure environment variables and a secrets manager
3. Run collectstatic and serve static files via Nginx or a CDN
4. Run Celery workers (and beat if scheduled tasks are used) with a robust process manager
5. Configure SSL/TLS and appropriate headers in Nginx
6. Set up monitoring (logging, Sentry, Prometheus/Grafana)

## Contributing

Contributions are welcome. Typical ways to contribute:

- Open an issue with a reproducible problem or feature request
- Send a pull request that fixes a bug or adds a small, well-documented feature
- Improve examples and documentation for labs

When contributing, follow these guidelines:

- Keep PRs small and focused
- Add/update tests when changing behavior
- Document new configuration or external dependencies

## License

This repository is provided for educational purposes. Add a license (e.g., MIT) at the root if you want to allow reuse. If you need a license added now, say which one and I can add an appropriate LICENSE file.

## Where to start

- Try the `home` app to explore models and templates.
- Run the API examples to see DRF and serializer patterns in action.
- Start a Celery worker and run the background task lab to learn async processing.

If you'd like, I can also:

- Add a Docker Compose file that wires up Redis, RabbitMQ, Elasticsearch, and Postgres for a complete local dev environment
- Add example environment files (.env.sample)
- Create short README files for each example app with step-by-step exercises
