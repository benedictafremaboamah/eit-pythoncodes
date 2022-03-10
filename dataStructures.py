my_list=["apple", "orange","strawberry"]
print(my_list)

my_list.append("Vero")
print(my_list[1])

my_list[0]="Blackberry"
print(my_list)

my_list.insert(-1, "Pineapple")
print(my_list)

my_list.remove("Pineapple")
print
print(my_list)

my_dict={"id":24, "name":"Frema", "is programmer":True, "salary":1.2,"loans":[{"package":"Student loan", "amount":3500}, {"package":"Car loan", "amount":425}] ,"languages":[{"lang":"French", "proficiency":100}, {"lang":"Spanish", "proficiency":60}]}
print(my_dict.get("loans")[0].get("amount"))