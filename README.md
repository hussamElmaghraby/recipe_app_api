# recipe_app_api


# Commands

- docker-compose run --rm app sh -c "django-admin startproject app ."

- docker-compose up

# Test
- docker-compose run --rm app sh -c "python manage.py test"

# Lint
- docker-compose run --rm sh -c "flake8"
