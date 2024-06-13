

#new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [number*number for number in numbers]
print(numbers)
print(new_list)

name = "Dave"
name_list = [letter for letter in name]
print(name_list)

range_list = [n*2 for n in range(1,5)]
print(range_list)

#new_list = [new_item for item in list if test]
even_numbers = [n for n in range(1,20) if n%2 == 0]
print(even_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Elanor"]
names_highlighted = [name.upper() for name in names if len(name) >= 5]
names_short = [name for name in names if len(name) < 5]
one_comp = [name.upper() if len(name) >= 5 else name.lower() for name in names]
names_highlighted = names_highlighted + names_short
print(names_short)
print(names_highlighted)
print(one_comp)