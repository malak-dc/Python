def main():
    try:
        a=input(" ")
        b=int(input(" "))
        words=a.split()
        result=[]
        for word in words:
            c=len(word)
            if(c>=b):
                result.append(word)
        print(result)
    except ValueError:
        print("AssertionError: the arguments are bad")
if __name__ == "__main__":
    main()