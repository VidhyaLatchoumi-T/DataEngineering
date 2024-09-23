a=10
b=3
add=a+b
sub=a-b
mul=a*b
div1=a/b
div2=a//b
mod=a%b
exp=a**b
print("addition",add)
print("subtraction",sub)
print("multiplication",mul)
print("division",div1)
print("floor division",div2)
print("modulus",mod)
print("exponent",exp)


num_str='100'
num_int=int(num_str)

num_float=12.34
num_int_from_float=int(num_float)

print("str to int:",num_int)
print("Float to int",num_int_from_float)

x=10
y=5
is_great=x>y
is_eq=x==y
print("a>b:",is_great)
print("a==b:",is_eq)
aa=True
bb=False
andop=aa and bb
orop=aa or bb
notop= not aa
print("and:",andop)
print("or:",orop)
print("not:",notop)

boolint=bool(9)
boolzero=bool(0)
boolstr=bool("Hello")
boolemp=bool("")
print("boolean from integer: ",boolint)
print("boolean from zero: ",boolzero)
print("boolean from string: ",boolstr)
print("boolean from empty string: ",boolemp)
