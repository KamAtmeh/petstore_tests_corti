@echo off

@echo off

rem Set the number of workers or default to 8 if not provided
set WORKERS=%1
if "%WORKERS%"=="" set WORKERS=8

pytest -n %WORKERS% -v petstore_tests.py --alluredir allure-results 

rem Generate Allure report
allure generate -c --name "Report" allure-results

rem Open Allure report
allure serve --name "Report" allure-results