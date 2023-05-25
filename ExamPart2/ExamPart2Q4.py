def request():
    name = input("My name is: ")
    print("Name Reversal: ", reversename(name))


def reversename(name):
    revname= ''.join(reversed(name))
    return revname


request()