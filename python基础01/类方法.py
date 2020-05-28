class Tool:
    count=0
    @classmethod
    def toolCount(cls):
        print("类方法，数量是%s"%(cls.count))
    def __init__(self,name):
        self.name=name
        Tool.count+=1
tool1=Tool("斧头")
tool2=Tool("刀子")
tool3=Tool("刀子")
tool4=Tool("刀子")
tool5=Tool("刀子")


Tool.toolCount()