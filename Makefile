
unittests:
	python -m unittest discover tests/

zip:
	rm -f alexa.zip
	zip -j alexa.zip src/* -x *.pyc* -x *__init__.py
	chmod 644 alexa.zip
