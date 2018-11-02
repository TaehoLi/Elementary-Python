def outer(func):
    print("-" * 20)
    func()
    print("-" * 20)
    
def inner():
    print("결과를 출력합니다.")

outer(inner)

