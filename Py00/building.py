def main():
    a=input()
    upper_letters=0
    lower_letters=0
    punctuation_marks=0
    spaces=0
    digits=0
    for i in a:
        if(i >='0' and i <='9'):
            digits=digits+1
        elif(i==' '):
            spaces=spaces+1
        elif(i=='!' or i=='.' or i=='-' or i=='?' or i==','):
            punctuation_marks=punctuation_marks+1
        elif(i >= 'A' and i<='Z'):
            upper_letters=upper_letters+1
        elif(i>='a' and i<='z'):
            lower_letters=lower_letters+1
    print(f'the text contains {len(a)} characters')
    print(f'{upper_letters} upper letters')
    print(f'{lower_letters} lower letters')
    print(f'{punctuation_marks} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')
if __name__ == "__main__":
    main()