doc:
	cd docs && make html

view-doc: doc
	open docs/_build/html/index.html
