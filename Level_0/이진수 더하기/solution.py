def binarySum(bin1, bin2, width=None):
    sum_dec = int(bin1, 2) + int(bin2, 2)
    sum_bin = bin(sum_dec)[2:]
    if width is not None:
        sum_bin = sum_bin.zfill(width)
    return sum_bin


print(binarySum("10","11"))
print(binarySum("10001","11"))