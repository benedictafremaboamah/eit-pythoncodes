
my_dict=[{"id":24, "name":"Frema", "email":"bfboamah@gmail.com", "phonenumber":2340,"number of visits":3, "posts":[{"postid":1,"title":"Mobile", "summary":"Mobile phone revolution" },{"postid":2,"title":"Little Dazo", "summary":"It failed" }]},
                        {"id":25, "name":"Akosua", "email":"a@gmail.com", "phonenumber":2678,"number of visits":4, "posts":[{"postid":1,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":26, "name":"Pius", "email":"p@gmail.com", "phonenumber":5618,"number of visits":5, "posts":[{"postid":1,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":27, "name":"Philip", "email":"phil@gmail.com", "phonenumber":2782,"number of visits":2, "posts":[{"postid":2,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":28, "name":"Adesola", "email":"ade@gmail.com", "phonenumber":1967,"number of visits":1, "posts":[{"postid":3,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":29, "name":"Somto", "email":"somto@gmail.com", "phonenumber":4517,"number of visits":7, "posts":[{"postid":4,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":30, "name":"Aminu", "email":"aminu@gmail.com", "phonenumber":3718,"number of visits":5, "posts":[{"postid":4,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":31, "name":"Abyna", "email":"abyna@gmail.com", "phonenumber":9102,"number of visits":8, "posts":[{"postid":5,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":32, "name":"Aba", "email":"abyna@gmail.com", "phonenumber":5261,"number of visits":9, "posts":[{"postid":6,"title":"Mobile", "summary":"Mobile phone revolution" }]},
                        {"id":33, "name":"Eben", "email":"eben@gmail.com", "phonenumber":6273,"number of visits":4, "posts":[{"postid":6,"title":"Mobile", "summary":"Mobile phone revolution" },]},
                        ]


# users=["Frema", "Akosua", "Pius", "Aminu", "Philip", "Adesola", "Somto", "Abyna","Aba", "Eben"]
# for user in users:
# print(my_dict.get("users")[0].get("name"))
# print(my_dict.get("users")[0].get("number of visits"))


for user in my_dict:
    print(user.get("name"))
    print(user.get("number of visits"))
    print(len(user.get("posts")))
    print(user["posts"][0].get("title"))
    
    for post in user.get("posts"):
        print("post",post['title'])
    

