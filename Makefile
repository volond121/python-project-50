
gendiff-run:
	poetry run gendiff file1.json file2.json

package-install:
		python3 -m pip install --user --force-reinstall dist/*.whl

build:
		poetry build

publish:
		poetry publish --dry-run

lint:
		poetry run flake8 gendiff