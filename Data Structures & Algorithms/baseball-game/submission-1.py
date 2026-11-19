class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ScoreList=[]
        for op in operations:
            if op == "C":
                ScoreList.pop()
            elif op == "D":
                ScoreList.append(ScoreList[-1]*2)
            elif op == "+":
                ScoreList.append(ScoreList[-1] + ScoreList[-2])
            else:
                ScoreList.append(int(op))

        ScoreSum = 0
        for i in ScoreList:
            ScoreSum += int(i)
        return ScoreSum