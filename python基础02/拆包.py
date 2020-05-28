def demo(*args,**kv):
    print(args)
    print(kv)
a=(1,2,3)
b={"name":"小","age":"大"}
demo(*a,**b)