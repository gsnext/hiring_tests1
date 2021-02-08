Selenium Hybrid Framework Improvements and suggestions
(Python, Selenium, PyTest, Page Object Model, HTML Reports)

Changes Made:
I faced environment setup issues because VM link was broken and scripts were looking for modules because their visibility was limited.

1.Added to api and webui in regards to required tests.
2.Verified elements and locators provided in page objects. Had to change only one element rest were fine.
3. Had to provide chromebrowser path to test_base.py
4. config.ini works better with configparser scripts instead of the config.py file


Suggestions

1. Create new project and Install Packages/plugins

-Selenium Libraries
-Pytest: Python unittest framework
-py-test html reports  (USE PYTEST and pytest fixture feature instead of unittest)
-pytest-xdist : Run tests parallel
-Allure-pytest: for allure reports

2. Create folder structure
-pageObjects(package)
-testCases(package)
-utilities(package)
-TestData(Folder)
-Configurations(Folder)
-Logs(Folder)
-Screenshots(Folder)
-Reports(Folder)
Run.bat

3. Read Common values from .ini file: config.ini files instead of config.py
-Create utility script "readProperties.py" to read common data
created sample "config.ini" in Configurations folder and utility script "readProperties.py" file in "Utilities" folder.

4. Add logs test case and screenshots where necessary

5. Run tests on desired browser/cross browser/parallel