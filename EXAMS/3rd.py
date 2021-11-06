def shopping_list(*args, **kwargs):
     budget = float(args[0])
     basket = 0
     products = kwargs
     shop_list = []
     if budget>=100:
        for product,value in products.items():
            if basket==5:
                break
            price = float(value[0])
            quantity = float(value[1])
            total_cost = price*quantity
            if total_cost<=budget:
                budget-=total_cost
                text = f"You bought {product} for {total_cost:.2f} leva."
                shop_list.append(text)
                basket+=1
        return '\n'.join(shop_list)
     else:
         return 'You do not have enough budget.'


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))