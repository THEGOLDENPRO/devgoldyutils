build:
	python -m build --wheel

install:
	pip install . -U

install-editable:
	pip install -e . --config-settings editable_mode=compat