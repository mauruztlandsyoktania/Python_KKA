umur = 12
harga = 12.5
nama = "Nia"
absen = [1,2,3,4,5,6]

print(f'umur ={umur} ({type(umur)})')
print(f'harga ={harga} ({type(harga)})')
print(f'nama ={nama} ({type(nama)})')
print(f'absen ={absen} ({type(absen)})')

belanja = ["beras", "minyak", "telur"]
belanja append("gula")
belanja append("kopi")
for item in belanja:
    print(item)

    hargabelanja = {
        "beras":12000,
        "minyak":17000,
        "telur":24000,
        "gula":15000,
        "kopi":20000,
    }

    total = sum(hargabelanja.values())
print("Total harga belanja:", total)

print("\n--- Fungsi ---")

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

luas, keliling = persegi_panjang(5, 3)
print(f"Luas: {luas}, Keliling: {keliling}")

print("\n--- Percabangan ---")

usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")



    # cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))

# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is",
type(integer_to_str))

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

# Equal to
8 == 8
# Not equal to
8 != 9
# Greater than
8 > 9
# Less than
8 < 9
# Less than
8 <= 9
# Less than
9 >= 9

a = True
b = True
print(a and b)
print(a or b)
print(not b)
#logic
5 > 6 and 6 < 7

e = 8
f = 2
# Summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")
# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}\n")
# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")
# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")
# Power
pow = e ** f
print(f"The power of e of f is : {pow}\n")

name = str(input("What is your name : "))
age = int(input("What's your age : "))
print("Name: ", name)
print("Age: ", age)

# normal print
print('Hi all! I am', name, 'age', age, 'years old')
Hi all! I am Parman age 24 years old
# format print
print(f'Hi all! I am {name} age {age} years old')
Hi all! I am Parman age 24 years old
# format print
print(f'Hi all! I am %s age %d years old'%(name, age))
# fortmat output
print(30*"=")
print("Temperature Calculator Program")
print(30*"=")

try:
your_GPA = float(input("Enter your GPA: "))
if 4.0 >= your_GPA >= 0.0:
if 4.0 >= your_GPA >= 3.80:
print(f"Damn you've got a magna cumlaude with your {your_GPA}
GPA")
elif 3.50 <= your_GPA < 3.80:
print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
elif 3.00 <= your_GPA < 3.50:
print(f"You've got a stable GPA tho")
elif your_GPA < 3.0:
print(f"You need a stable GPA")
else:
print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
print("Please enter a valid GPA")

try:
status_code = int(input("Enter your status code: "))
print("Your code means")
match status_code:
case 200:
print("Success!")
case 400:
print("Bad Request")
case 401:
print("Unauthorized")
case 402:
print("Payment Required")
case 403:
print("Forbidden")
case 404:
print("Not Found")
case 500:
print("Internal Server Error")
except :
print("Please enter a valid status code")

a = 3
b = "Even Numbers" if a % 2 == 0 else "Odd Numbers"
print(b)

for i in range(5):
print(i)
0
1
2
3
4
# For loop with range
for i in range(5):
print("Data science is easy!")
print(50*"=")
for i in range(1, 5, 2):
print("Data science is easy!")

word = "I want to master data science"
for letter in word:
print(letter)

# You can use it with enumerate function
for m, n in enumerate(word):
print(f"Index {m}. {n}")

# It can go backwards
for i in range(5,1,-1):
print("I want big data's")

for i in range(5):
if i == 2:
continue # skip theis loop when i is equal to 2
if i == 4:
break # stops the loop when i is equal to 4
print(i)

count = 0
while count < 4:
print("Keep the spirits up interns!")
count += 1
