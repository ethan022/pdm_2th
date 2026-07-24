print("=" * 10, 1, "=" * 10)

text = "정 상 가 동"

text = text.replace(" ", "")
print(text)  # 정상가동

phone = "010-1234-5678"

phone = phone.replace("-", "")
print(phone)  # 01012345678


s = "3,000"
s = s.replace(",", "")
print(type(s))
s = int(s)
print(type(s))  # int


print()
print("=" * 10, 2, "=" * 10)

s = "에스프레소 아메리카노 카페라테"
print(s.split())

s = "PUMP A 03"

print(s.split())  #  ['PUMP','A','03']


s = "PUMP,A,03,,3"
print(s.split(","))

s = "2026-07-24"
print(s.split("-"))  # [ 2026, 07, 24 ]


s = "a,b,c-,d-"

print(s.split(",", 2))

list1 = s.split(",", 2)

print("+".join(list1))

s = "감, 배  , 사과"

list1 = s.split(",")
print(list1[1].strip())

print("-".join(list1))

print()
print("=" * 10, 3, "=" * 10)

name = "홍길동"
age = 25
print()  # 홍길동님은 25살 입니다.
print(name, "님은", str(age), "살 입니다.")
print(f"{name}님은 {age}살 입니다.")


name = "PUMP_A"
temp = 87

print(f"설비 {name}, 온도 {temp}도")


a = 88
b = 92
c = 72


print()
print()
print()
print()
print()
