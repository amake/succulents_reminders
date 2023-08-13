SHELL := /bin/bash -O extglob
venv := .env
payload := dist/lambda-deploy.zip
lambda_name := SuccsRemindersNorthBot
python := python3.11
aws_args ?=

flavors := North South
secrets = $(addsuffix _clientcred.secret,$(flavors))

.PHONY: zip
zip: $(payload)

$(venv):
	$(python) -m venv $(@)
	$(@)/bin/pip install -e .

dist:
	mkdir -p $(@)

.PHONY: clean
clean: ## Clean generated files
clean:
	rm -rf dist

.PHONY: update
update: ## Update dependencies and data
update: | $(venv)
	$(venv)/bin/pip install --upgrade pip
	$(venv)/bin/pip install --upgrade --upgrade-strategy eager -e .

$(payload): $(wildcard *.py) config.ini $(secrets) | $(venv) dist
	rm -rf $(@)
	zip $(@) $(^) -x \*.pyc
	root=$$(pwd); cd $(venv)/lib/$(python)/site-packages && \
		zip -r $$root/$(@) ./!(pip*|wheel*|setuptools*|easy_install*) -x \*.pyc

.PHONY: secrets
secrets: $(secrets)

$(secrets): | $(venv)
	$(venv)/bin/python auth_setup.py

.PHONY: deploy
deploy: ## Deploy to AWS Lambda
deploy: $(payload)
	aws $(aws_args) lambda update-function-code \
		--function-name $(lambda_name) \
		--zip-file fileb://$$(pwd)/$(<)

.PHONY: invoke
invoke: ## Invoke AWS Lambda
invoke:
	aws $(aws_args) lambda invoke \
		--function-name $(lambda_name) \
		--cli-binary-format raw-in-base64-out \
		--payload '{"date": "2023-03-01"}' \
		/dev/null

heics = $(wildcard assets/*.HEIC)

.PHONY: assets
assets: ## Generate assets
assets: $(heics:.HEIC=.jpg)

%.jpg: %.HEIC
	heif-convert -q 80 $(<) $(@)

.PHONY: deploy-assets
deploy-assets: ## Deploy assets to S3
deploy-assets: assets
	aws $(aws_args) s3 sync --exclude '*' --include '*.jpg' assets/ s3://amake-bots/succs

.PHONY: test
test: ## Test locally
test: test-execute test-unittest

.PHONY: test-execute
test-execute: | $(venv)
	$(venv)/bin/python succs.py 2023-03-01
	$(venv)/bin/python succs.py 2023-03-01 Southern

.PHONY: test-unittest
test-unittest: | $(venv)
	$(venv)/bin/python -m unittest tests/test_*.py

.PHONY: help
help: ## Show this help text
	$(info usage: make [target])
	$(info )
	$(info Available targets:)
	@awk -F ':.*?## *' '/^[^\t].+?:.*?##/ \
         {printf "  %-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
