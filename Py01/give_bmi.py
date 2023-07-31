def main():
    from typing import List, Union

    def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
        res = []
        for i in range(len(height)):
            bmi = weight[i] / (height[i] ** 2)
            res.append(bmi)
        return res
    def apply_limit(bmi: List[Union[int, float]], limit: int) -> list[bool]:
        ab=[]
        for i in range(len(bmi)):
            if(bmi[i]>limit):
                ab.append(True)
            else:
                ab.append(False)
        return ab
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
if __name__=="__main__":
    main()