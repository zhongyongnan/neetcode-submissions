class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        output=[]
        visit, cycle=set(),set()

        def dfs(crs): # dfs为true代表从这个节点开始可以遍历完，无环（可以上完课）
            if crs in visit:
                return True 
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs) # 退回到上一个节点
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return output