
unittests:
	python -m unittest discover tests/

build-deploy:
	zip -r alexa.zip src -x *.pyc*
