class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            tempList = [0] + result[-1] + [0]
            rowList = []
            for j in range(len(result[-1])+1):
                rowList.append(tempList[j] + tempList[j+1])

            result.append(rowList)

        return result
