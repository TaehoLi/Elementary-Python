def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para
def outname(name):
    return "이름:" +name+ "님"

@para
def outage(age):
    return "나이:" +str(age)

print(outname("김삼형"))
print(outage(29))
