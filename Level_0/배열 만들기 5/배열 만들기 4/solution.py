def solution(intStrs, k, s, l):
    return [int(ins[s:s+l]) for ins in intStrs if k < int(ins[s:s+l])]