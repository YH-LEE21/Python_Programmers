def allwinRockScissorsPaper(rsp):
    rsp_dic = {"0":"5", "2":"0", "5":"2"}
    return "".join([rsp_dic[i] for i in rsp ])

print(allwinRockScissorsPaper("2"))
print(allwinRockScissorsPaper("205"))
