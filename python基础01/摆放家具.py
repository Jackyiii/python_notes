class House:
    def __init__(self, houseType, area):
        self.houseType = houseType
        self.area = area
        self.freeArea = area
        self.itemList = []

    def addItem(self, item):
        if item.area>self.freeArea:
            print("%s面积太大无法添加"%item.name)
            return

        self.itemList.append(item.name)
        self.freeArea-=item.area
        # itemList = HouseItem(item)
        # self.freeArea -= item.area
        print("添加%s" % item)

    def __str__(self):
        return (
                "户型是%s,面积是%s,%.1f剩余面积，家具有:%s"
                % (self.houseType,
                   self.area,
                   self.freeArea,
                   self.itemList)
        )


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家居是:%s,面积是%.2f" % (self.name, self.area)


bed = HouseItem("希梦斯", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

house1 = House("超大户型", 100)
print(house1)
house1.addItem(bed)
house1.addItem(chest)
house1.addItem(table)
print(house1)