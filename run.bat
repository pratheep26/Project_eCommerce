rem chrome

rem pytest -v --capture=tee-sys --html=Reports\Report.html testCases\ --browser chrome
pytest -v --capture=tee-sys -m "sanity or regression" --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v --capture=tee-sys -m "sanity" --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v --capture=tee-sys -m "regression" --html=Reports\Report.html testCases\ --browser chrome

rem Firefox

rem pytest -v --capture=tee-sys --html=Reports\Report.html testCases\ --browser firefox
rem pytest -v --capture=tee-sys -m "sanity or regression" --html=Reports\Report.html testCases\ --browser firefox
rem pytest -v --capture=tee-sys -m "sanity" --html=Reports\Report.html testCases\ --browser firefox
rem pytest -v --capture=tee-sys -m "regression" --html=Reports\Report.html testCases\ --browser firefox


