#basinda ve sonundaki bosluklari atiyor 
txt = ("             Hello World             ")

print(txt.strip())


# replace H nin yerine j harfini koyutor
txt = "Hello World"
txt = txt.replace("H", "j")
print(txt)



#insert ile index belirterek eleman ekliyoruz 
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)


# setin icine eleman ekleme update() ile oluyor cikarma remove() ile 
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

print(fruits)


#set icinden discard ile de cikarma yapiliyor 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

print(fruits)


#dictinary de biilgi cagirma get() komutu ile de oluyor 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)

#dict da bilgi degisi mi ve atamasi 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#dict key ve value atama 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"


#dict pop ile silme islemi
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)


#if olmadan da else kullaniliyor 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#class dan obje uretme 
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)



# init islevi olusturma 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age




