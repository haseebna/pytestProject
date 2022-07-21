1. Install dependencies
```shell  
    cd [your_repo_path]/pytestProject
    python -m pip install -r requirements.txt
```
3. Run the tests at directory Tests:

```shell   
    cd Tests
    pytest test_LoginPages.py
```
4. If you want to get the report
```shell   
    cd Tests
    pytest test_LoginPages.py -v --html=./report.html
```
5. If you want to run test in parallel
```shell   
    cd Tests
    pytest test_LoginPages.py -v -n 2  --html=./report.html
```
* Edit the requirements.txt to add the new module/s

