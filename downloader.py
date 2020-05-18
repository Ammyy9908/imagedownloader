import requests
import random


def download(key):
      image_url = 'https://source.unsplash.com/1600x900/?'+key
      response = requests.get(image_url).content
      random_num = random.randint(0,99999)
      random_num = str(random_num)
      image_name = random_num + '.jpg'
      with open('downloads/'+image_name, 'wb') as handler:
            handler.write(response)
      print("Image SuccessFully Downloaded! with name "+image_name)



while(1):
      print("Choose a Option:-> ")
      print("1.Download Image\n2.Exit Program")
      categories = ('boys','girls','mounatins','cars','beach','mountains','architectures','portraits')
      ch = input()
      count = 0
      if ch == '1':
            print("Choose a number from below categories of Image:\n")
            for items in categories:
                  count = count + 1
                  print(f'{count}.{items}')
            print("Enter Categories by its number, e.g 1 for boys 2 for girls")
            cat = input()
            download(categories[int(cat)-1])

            
      elif ch == "2":
            exit()
      else:
            print("Invalid Option! Try Again")
      

      