print("Welcome to the love Calculator ")
name1 = input("Enter the fisrt name : ")
name2 = input("Enter the second name: ")
comb_name = name1 + name2 

lower_name = comb_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

sec_digit = l+o+v+e

score = int(str(first_digit) + str(sec_digit))


if (score < 10) or (score > 90):
    print(f"You love score is {score} , you go together like apple and ketchup , Try and make sense of That ")
elif (score > 40) and (score <= 50):
    print(f"Your love score is {score} , you two are ok I guess")
else : 
    print(f"Your love score is {score } , Macth made , awwww ")