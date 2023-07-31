def NULL_not_found(object: any) -> int:
    if(object is None):
        print(type(object))
        return 0
   # elif(object is ):
    #    print(type(object))
    elif isinstance(object, float) and object != object:
        print(type(object))
        return 0
    elif(object == 0):
        print(type(object))
        return 0
    elif(object == ''):
        print(type(object))
        return 0
    elif(object is False):
        print(type(object))
        return 0
    else:
        print("Type Not Found")
        return 1
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
print("Nothing:",Nothing,end=' ')
NULL_not_found(Nothing)
print("Cheese:",Garlic,end=' ')
NULL_not_found(Garlic)
print("Zero:",Zero,end=' ')
NULL_not_found(Zero)
print("Empty:",Empty,end=' ')
NULL_not_found(Empty)
print("Fake:",Fake,end=' ')
NULL_not_found(Fake)
print(NULL_not_found("Brian"))