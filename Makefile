all: wheel

.PHONY: update-deps
update-deps:
	pip install --upgrade pip-tools pip setuptools
	pip-compile --upgrade --build-isolation --generate-hashes --output-file requirements/dev.txt requirements/dev.in

.PHONY: init
init:
	pip install --editable .
	pip install --upgrade pip-tools pip setuptools
	rm -rf .tox
	pip install --upgrade tox pre-commit pytest
	pre-commit install

.PHONEY: update
update: update-deps init

.PHONY: test
test: $(testdata)
	pytest tests

wheel:
	pip wheel -e .

cleanup=tests/__pycache__        \
        src/primo/__pycache__    \
        src/primo/primo.egg_info \
        build                    \
        *.whl

.PHONY: clean
clean:
	-rm -rf $(cleanup)

