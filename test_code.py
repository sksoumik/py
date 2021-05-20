from collections import ChainMap

salary = {"SDE": 100000, "HR": 80000, "MTO": 60000}
office_hq = {"Asia": "Singapore", "Europe": "Dublin", "North America": "USA"}
age_limit = {"SDE": 40, "HR": 50}

employee_info = ChainMap(salary, office_hq, age_limit)

print(employee_info)
