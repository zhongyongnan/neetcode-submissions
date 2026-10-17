class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 记录三个字符最后出现的位置
        last=[-1]*3
        answer=0
        for i,c in enumerate(s):
            last[ord(c)-97]=i #将字母转化为ascii码，a为97
            answer+=min(last)+1 #每一轮加以当前位置 i 为结尾的合法子串数量（最小的往后就肯定abc都有）
        return answer
