install-dev:
	@pip install -r requirements-dev.txt
	
install-reqs:
	@pip install -r requirements.txt

build: clean
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf build dist youtube.*

check-build:
	@twine check dist/*

test-upload:
	@twine upload --repository testpypi dist/*

upload:
	@twine upload dist/*

bump-tag:
	@cz bump --changelog