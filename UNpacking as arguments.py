def general(arg1="snvs", arg2="komal"):
    print(arg1 + " " + arg2)


data = {'arg1': 'hi', 'arg2': "snvskomal"}
general(**data)

# here the keys of the dictionary must match with a function's argument
data1 = {'arg1': 'this', 'naem': 'snkvs'}
general(**data1)
