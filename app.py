print('Hello world')


class Item():
    def calculate_total_price(self,x,y):
        return x*y
item1= Item()
item1.name ='John'
item1.price =20
item1.quantity = 10
print(item1.calculate_total_price(item1.price,item1.quantity))

item2 =Item()
item2.name ='Elpo'
item2.price = 20
item2.quantity = 150
print(item2.calculate_total_price(item2.price,item2.quantity))