test:
	@python rest_framework_captcha/tests/runtests.py

clean-pycache:
	@rm -r **/__pycache__

clean: clean-pycache

.PHONY: clean


