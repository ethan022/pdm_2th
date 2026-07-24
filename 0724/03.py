text = "   정상  "
print(text, 1)

# text = text.strip()
# print(text, 1)

l_text = text.lstrip()
print("[", l_text, "]", sep="")

r_text = text.rstrip()
print("[", r_text, "]", sep="")


s = "    대기       "
strip_s = s.strip()
lstrip_s = s.lstrip()
rstrip_s = s.rstrip()
print("[", strip_s, "]", sep="")  # [대기]
print("[" + strip_s + "]")  # [대기]

print("[" + lstrip_s + "]")  # [대기]
print("[" + rstrip_s + "]")  # [대기]


print()
print("=" * 5 + " 4 " + "=" * 5)

s = "##대기###"
s = s.strip("#")
print(s)

s = "#$!대기!$#"
# s = s.strip("#")
# s = s.strip("$")
# s = s.strip("#")

s = s.strip("#").strip("$").strip("!")

# s = s.strip("#$")

print(s)  # 대기

print()
print("=" * 5 + " 5 " + "=" * 5)
s = "#$#python#$#"
s = s.strip("#$#").upper()
print(s)  # PYTHON

# 실습 문제
print("=" * 8, "실습 문제", "=" * 8)
s = "#$!python!$#"
# s = s.strip("#$!").title()
s = s.strip("#$!").capitalize()

print(s)  # Python

s = "Sensor log"
print("title", s.title())
print("capitalize", s.capitalize())


# 종합 문제
print()
print("=" * 8, "종합 문제", "=" * 8)
s = "python"

# print("s[2]", s[2])
# print(s[2].upper())
s = s[:2] + s[2].upper() + s[3:]

# s = s.replace("t", "T")

# 변수 s가 pyThon으로 나오게변경하세요.
print(s)  # pyThon


print()
print()
print()
print()
print()
print()
