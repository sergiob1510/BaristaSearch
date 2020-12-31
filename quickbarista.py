import urllib.request, urllib.parse, urllib.error
import json
import time

#API link
serviceurl = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='

repeat = "yes"
while repeat == "yes":
    #Asking user input to search in database
    address = input('Please, enter cocktail: ')
    if len(address) < 1: break
    address = address.replace(' ', '%20')
    url = serviceurl + address

    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    # print ('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    null = None

    if not js or js["drinks"] == None:
        print ('===Failure to retrieve===')
        continue

    drink = js["drinks"][0]["strDrink"]
    glass = js["drinks"][0]["strGlass"]
    instr = js["drinks"][0]["strInstructions"]
    ingr1 = js["drinks"][0]["strIngredient1"]
    msr1 = js["drinks"][0]["strMeasure1"]
    ingr2 = js["drinks"][0]["strIngredient2"]
    msr2 = js["drinks"][0]["strMeasure2"]
    ingr3 = js["drinks"][0]["strIngredient3"]
    msr3 = js["drinks"][0]["strMeasure3"]
    ingr4 = js["drinks"][0]["strIngredient4"]
    msr4 = js["drinks"][0]["strMeasure4"]
    ingr5 = js["drinks"][0]["strIngredient5"]
    msr5 = js["drinks"][0]["strMeasure5"]
    ingr6 = js["drinks"][0]["strIngredient6"]
    msr6 = js["drinks"][0]["strMeasure6"]
    ingr7 = js["drinks"][0]["strIngredient7"]
    msr7 = js["drinks"][0]["strMeasure7"]


    print('Drink:', drink)
    print('Suggested type of glass:', glass)
    print('Ingredients:')
    print('1.', ingr1, '- Quantity:', msr1)
    print('2.', ingr2, '- Quantity:', msr2)
    if ingr3 is not None and len(ingr3) > 1:
        print('3.', ingr3, '- Quantity:', msr3)
    if ingr4 is not None and len(ingr4) > 1:
        print ('4.', ingr4, '- Quantity:', msr4)
    if ingr5 is not None and len(ingr5) > 1:
        print ('5.', ingr5, '- Quantity:', msr5)
    if ingr6 is not None and len(ingr6) > 1:
        print ('6.', ingr6, '- Quantity:', msr6)
    if ingr7 is not None and len(ingr7) > 1:
        print ('7.', ingr7, '- Quantity:', msr7)

    print('How to?:', instr)




    repeat = input('Still thirsty?(yes/no) ')

print("Thank you very much and happy drinking")
print("Hasta la vista, baby")

time.sleep(3)
