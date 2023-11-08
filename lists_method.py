```py
shopping_list = ['milk', 'avokado']
shopping_list.extend(['bananas', 'chocolate', 'nuts'])
print(shopping_list)

item_to_delete = input("kuru elementu dzēst?")

if item_to_delete in shopping_list:
    shopping_list.remove(item_to_delete)
else:
    print("item not in list")
print(shopping_list)

```
