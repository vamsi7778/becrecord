d=[{"v":"5001"},{"v":"5002"},{"v1":"5001"},{"v1":"5005"},{"v11":"5005"},{"v":"5009"},{"v111":"5007"}]
print("original list:",d)
unique_value=set(value for dic in d for value in dic.values())
print("unique value:",unique_value)