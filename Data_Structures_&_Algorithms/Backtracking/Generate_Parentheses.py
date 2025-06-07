class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]

        def backtrack(openedN,ClosedN):
            if openedN==ClosedN==n:
                res.append("".join(stack))
                return
            
            if openedN<n:
                stack.append("(")
                backtrack(openedN+1,ClosedN)
                stack.pop()
            if ClosedN<openedN:
                stack.append(")")
                backtrack(openedN,ClosedN+1)
                stack.pop()
        backtrack(0,0)
        return res
        