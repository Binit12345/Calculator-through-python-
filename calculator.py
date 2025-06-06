first=input("")
operators=input("")
second=input("")
first=int(first)
second=int(second)
if operators == "+":
    print( first + second )
elif operators == "-":
    print( first - second)
elif operators == "*":
    print( first * second )
elif operators == "/":
    print( first / second )
#elif operators =="**":
    #print(first ** second)
    
else:
    print("invalid")