class Solution:
    def evalRPN(self, t: List[str]) -> int:
        st=[]
        for i in t:
            if len(st)>=2 and i=="+":
                temp=st[-2]+st[-1]
                st.pop()
                st.pop()
                st.append(temp)
            elif len(st)>=2 and i=="-":
                temp=st[-2]-st[-1]
                st.pop()
                st.pop()
                st.append(temp)
            elif len(st)>=2 and i=="*":
                temp=st[-1]*st[-2]
                st.pop()
                st.pop()
                st.append(temp)
            elif len(st)>=2 and i=="/":
                temp=int(st[-2]/st[-1])
                st.pop()
                st.pop()
                st.append(temp)
            else:
                st.append(int(i))
        return sum(st)
            