class Solution:
    def getRow(self, rowIndex: int) -> List[int]: #type: ignore
        
        triangle = []

        for i in range(0, rowIndex+1):

            row = [1]

            for n in range(0, i-1):
                n1 = triangle[i-1][n]
                n2 = triangle[i-1][n+1]

                couple = n1 + n2
                row.append(couple)

            if i != 0:
                row.append(1)
                
            triangle.append(row)

        return triangle[rowIndex]