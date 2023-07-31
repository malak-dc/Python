def main():
    def slice_me(family: list, start: int, end: int) -> list:
        row=len(family)
        column=len(family[0])
        if not isinstance(family,list):
            raise ValueError("family isn't list")
        for i in family:
            if not isinstance(i,list):
                raise ValueError("family must be a list of lists")
        for i in family:
                if len(i)>len(family[0]):
                    raise ValueError("All lists must have the same size")
        print(f'My shape is: ({row},{column})')
        new=family[start:end]
        new_row=len(new)
        new_column=len(new[0])
        print(f'My new shape is : ({new_row},{new_column})')
        print(new)
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
if __name__=="__main__":
    main()