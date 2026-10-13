name: Python CI validator tests
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: projects/python-ci-validator
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install pytest
      - run: python -m pytest -q
