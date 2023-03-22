import tkinter as tk
import requests
import random

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 600)
canvas1.pack()

root.title("Recipe Generator")
canvas1.configure(background="pink")


labelh = tk.Label(root, bg="pink", text=("Welcome to the Recipe Generator! What ingredients do you have?"))
canvas1.create_window(300, 150, window=labelh)

entry1 = tk.Entry(root)
canvas1.create_window(300,200, window=entry1)


#def get_recipe():
    #choice = entry1.get()

    #label1 = tk.Label(root, bg="pink", text=("{} is a great choice! Press continue to see your suggested recipe.".format(choice)))
    #canvas1.create_window(300, 300, window=label1)

#button1 = tk.Button(bg="white", fg="black", text="Click me!", command=get_recipe)
#canvas1.create_window(300,250, window=button1)

def recipe_generator():
    ingredient = entry1.get()

    YOUR_APP_ID = "" #add app id
    YOUR_APP_KEY = "" #add app key

    url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, YOUR_APP_ID, YOUR_APP_KEY)

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    results = data['hits']

    random_result = random.choice(results)

    recipe = random_result["recipe"]

    print(recipe["label"], recipe["url"])

    label2 = tk.Label(root, bg="pink", fg="black", text=recipe["label"])
    canvas1.create_window(300, 300, window=label2)

    label3 = tk.Label(root, bg="pink", fg="black", text=recipe["url"])
    canvas1.create_window(300, 350, window=label3)


button2 = tk.Button(bg="white", text="Continue", command=recipe_generator)
canvas1.create_window(300, 250, window=button2)



root.mainloop()

