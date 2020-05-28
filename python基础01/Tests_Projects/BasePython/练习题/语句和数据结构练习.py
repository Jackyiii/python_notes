a={"b":"python","a":"java","c":"c++","d":"R"}
b=dict([x,a[x]] for x in sorted(a.keys()))
print(b)
c=list(b.keys())[list(b.values()).index("java")]
print(c)
#[k for k,v in d.items() if v == value]



