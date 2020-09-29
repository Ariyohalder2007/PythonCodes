def display(func):
    def wrapper():
        print('Wrapper')
        func()
    return wrapper
@display
def show():
    print('Show')
show()