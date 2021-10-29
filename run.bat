rem chrome

rem pytest -v --capture=tee-sys --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=Reports\Report.html testCases\ --browser chrome
pytest -v -s -m "sanity" --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v -s -m "regression" --html=Reports\Report.html testCases\ --browser chrome

rem Firefox

rem pytest -v --capture=tee-sys --html=Reports\Report.html testCases\ --browser firefox
rem pytest -v -s -m "sanity or regression" --html=Reports\Report.html testCases\ --browser firefox
rem pytest -v -s -m "sanity" --html=Reports\Report.html testCases\ --browser firefox
rem pytest -v -s -m "regression" --html=Reports\Report.html testCases\ --browser firefox


