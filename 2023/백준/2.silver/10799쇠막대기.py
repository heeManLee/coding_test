array = list(input())
st = []

result = 0
bar = 0
for i in range(len(array)):
    if array[i] == '(':
        st.append('(')
    else:
        if array[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1

print(result)