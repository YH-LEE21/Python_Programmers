import time
def age_Now(age):
    now = time.gmtime(time.time())
    return now.tm_year - age + 1
print(age_Now(40))
print(age_Now(24))