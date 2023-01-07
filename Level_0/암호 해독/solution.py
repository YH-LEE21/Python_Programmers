def decryption(cipher, code):
    return "".join([cipher[i] for i in range(len(cipher)) if (i+1)%code==0])

cipher = "dfjardstddetckdaccccdegk"	
code = 4
print(decryption(cipher,code))

cipher = "pfqallllabwaoclk"
code = 2
print(decryption(cipher,code))
