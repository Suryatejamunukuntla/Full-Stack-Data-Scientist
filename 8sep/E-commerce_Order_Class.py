class Order:
    def __init__(self):
        self.items={}
    def add(self,item,price):
        self.items[item]=price
    def remove(self,item):
        return self.items.pop(item)
    def calculate_total(self):
        sum=0
        for i in self.items.keys():
            sum+=self.items[i]
        return sum
    def show_items(self):
        return self.items.items()
order = Order()
order.add("Shirt", 500)
order.add("Shoes", 1500)
print("Total = ",order.calculate_total())

