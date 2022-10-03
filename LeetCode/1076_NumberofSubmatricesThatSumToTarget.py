class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        if len(matrix)>len(matrix[0]):
            new=[[0]*len(matrix) for i in range(len(matrix[0]))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    new[j][i]=matrix[i][j]
            return self.numSubmatrixSumTarget(new,target)
          
        self.dp=[[0]*(len(matrix[0])+1)for i in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.dp[i][j]=self.dp[i][j-1]+self.dp[i-1][j]-self.dp[i-1][j-1]+matrix[i-1][j-1]

        ans=0
        for row1 in range(len(matrix)):
            for row2 in range(row1,len(matrix)):
                pres=0
                myhash={0:1}
                for col1 in range(len(matrix[0])):
                        pres=self.dp[row2+1][col1+1]-self.dp[row1][col1+1]
                        if pres-target in myhash:
                            ans+=myhash[pres-target]
                        myhash[pres]=myhash.get(pres,0)+1
                        
        return(ans)
        