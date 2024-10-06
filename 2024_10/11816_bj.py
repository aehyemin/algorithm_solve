N = input()

   
if N[0] == "0" and N[1] == "x": #16진수인경우
   print(int(N, 16))
elif N[0] == "0": #8진수인경우
    print(int(N, 8))

else : #10진수인경우
    print(int(N, 10))