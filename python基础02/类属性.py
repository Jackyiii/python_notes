class Tool:
    count=0
    def __init__(self,name):
        self.name=name
        Tool.count+=1
tool1=Tool("斧头")
print("创建了%s,类属性数量为%d"%(tool1.name,Tool.count))
tool2=Tool("剪刀")
print("创建了%s,类属性数量为%d"%(tool2.name,Tool.count))
tool3=Tool("刀子")
print("创建了%s,类属性数量为%d"%(tool3.name,Tool.count))
tool4=Tool("直尺")
print("创建了%s,类属性数量为%d"%(tool4.name,Tool.count))