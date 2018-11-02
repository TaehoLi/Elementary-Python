def makeHello(message):
    def hello(name):
        print(message + ", " + name)
    return hello

enghello = makeHello("Good Morning")
hanhello = makeHello("안녕하세요")

enghello("Mr Kim")
hanhello("홍길동")
