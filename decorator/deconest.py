def div(func):
    def wrapper():
        return "<div>" + str(func()) + "</div>"
    return wrapper

def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@div
@para
def outname():
    return "김상형"

@para
@div
def outage():
    return "29"

print(outname())
print(outage())
