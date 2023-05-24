def solution(ineq, eq, n, m):
    answer = ""
    if eq == "=":
        answer = str(n) + ineq + eq + str(m)
    else:
        answer = str(n) + ineq + str(m)
    return int(bool(eval(answer)))