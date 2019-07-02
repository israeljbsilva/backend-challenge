PIP := pip install -r

PROJECT_NAME := backend-challenge
PYTHON_VERSION := 3.6.6
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

# Environment setup
.pip:
	pip install pip --upgrade

setup-dev: .pip
	$(PIP) requirements/base.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

code-convention:
	flake8
	pycodestyle

test:
	py.test --cov-report=term-missing  --cov-report=html --cov=.

all: create-venv setup-dev
