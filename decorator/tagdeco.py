def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para
def outname():
    return "김상형"

@para
def outage():
    return "29"

print(outname())
print(outage())
