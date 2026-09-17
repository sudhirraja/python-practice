def check_temperature(temp, limit=85):
        if temp > limit:
            return "FAIL"
        else:
            return "PASS"
print(check_temperature(70))
print(check_temperature(90))
print(check_temperature(90, limit=95))
#print(check_temperature())

