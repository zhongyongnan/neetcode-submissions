class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count=[a,b,c] #保存剩余量
        res=[] #构造字符串

        def getMax(repeated):
            idx=-1
            maxCnt=0
            for i in range(3):
                if i==repeated or count[i]==0:
                    continue
                if maxCnt<count[i]:
                    maxCnt=count[i]
                    idx=i
            return idx
        
        repeated=-1
        while True:
            maxChar=getMax(repeated)
            if maxChar==-1:
                break
            res.append(chr(ord('a')+maxChar)) #把数字索引 maxChar 转换成对应的字母插入
            count[maxChar]-=1
            if len(res)>1 and res[-1]==res[-2]:
                repeated=maxChar
            else:
                repeated=-1
        
        return ''.join(res)