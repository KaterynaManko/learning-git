print("Вправа 1")
print("Список покупок")
shopping_list = {"пекарня": ["хліб", "булки ", "пончик"],
  "продуктовий": ["морква", "селера", "рукола"]}
for shops, products in shopping_list.items():
  print(f"Я йду до {shops.title()} і купую там {[i.title() for i in products]}")
quantity_of_products = sum([len(i) for i in shopping_list.values()])
print(f"Я разом купую {quantity_of_products} товарів")

print("Вправа 2")
list_of_numbers = [i for i in range(0,101) if i % 5 == 0 ]
print(list_of_numbers)
new_list_of_numbers = [i**3 for i in list_of_numbers]
print(new_list_of_numbers)