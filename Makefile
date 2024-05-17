.PHONY: run
run:
	echo 'rep'
	echo 'biun'
	@echo 'vjk'
	python main.py

.PHONY: check
check:
	@echo 'Starting code correction...'
	black .
	isort .
	flake8 .
	pytest .
	@echo 'Finish'