def main():
    slow = input("input slow down comand")
    print(myFunction(slow))


def myFunction(text):
    text2 = text.replace(" ","...")
    return text2
main()
