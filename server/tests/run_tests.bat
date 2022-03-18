@echo off
::Runs test coverage and creates a web page at htmlcov/index.html.
::Run with the -o flag to automatically open trhe webpage after the tests are done.
python -m coverage run -m pytest
python -m coverage html
if "%~1"=="-o" (
start "" "htmlcov/index.html"
)