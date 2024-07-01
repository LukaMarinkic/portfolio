import random 
characters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",1,2,3,4,5,6,7,8,9,0,"!","§","%","$"]
lenght=int(input("Wie Zeichen soll das Paswort haben? :"))
for n in range (lenght) :
 print(characters[random.randint(0,len(characters))])

input("Drücken sie Enter")