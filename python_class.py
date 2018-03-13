import sys

class home(object):
    total_item = []
    num = 0

    def __init__(self,name):
        self.name = name
        self.myitem = []
    def add_item(self,item):
        home.total_item.append(item)
        self.myitem.append(item)
    def my_num(self):
        print(self.name + 'has '+ str(len(self.myitem))+' items')
    def my_what(self):
        if len(self.myitem) == 0:
            print('nothing')
        else:
            for i in self.myitem:
                print(i,)
            print("\n")
    def who(self):
        return self.name
