install:
	@pip install -e .

install_requirements:
	@pip install -r requirements.txt

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit=$(VIRTUAL_ENV)/lib/python*
