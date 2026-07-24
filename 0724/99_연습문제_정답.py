# =============================================================================
#  7/24 복습 연습문제 ― 정답  (03_04 ~ 03_06  문자열 정리와 f-string)
# -----------------------------------------------------------------------------
#  정답은 '하나'가 아닙니다. 결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  다만 아직 배우지 않은 문법(if · for · 함수 정의)은 쓰지 않았고,
#  리스트는 split 결과를 읽는 맛보기 수준만 썼습니다.
# =============================================================================


print("========== [1] 대문자 · 소문자로 바꾸기 ==========")

s = "ready"
big = s.upper()                    # 결과를 새 변수에 받는다
print(big)                         # → READY

s = "WARNING"
small = s.lower()
print(small)                       # → warning


print()
print("========== [2] 원본은 바뀌지 않는다 ==========")

s = "sensor"
s.upper()                          # 결과를 안 받으면 그냥 버려진다
print(s)                           # → sensor    ← 안 바뀐다!

# 고친 코드 : 결과를 다시 받아야 반영된다
s = s.upper()
print(s)                           # → SENSOR

# 원본을 남기고 싶으면 새 변수에 받는다
raw = "sensor"
big = raw.upper()
print(raw, big)                    # → sensor SENSOR


print()
print("========== [3] capitalize() 와 title() ==========")

print("park min ho".title())              # → Park Min Ho          (1) 단어마다 첫 글자
print("sensor data report".capitalize())  # → Sensor data report   (2) 문장 첫 글자만
print("SENSOR DATA REPORT".capitalize())  # → Sensor data report   (3)

# (2)와 (3)의 결과가 똑같다!
#   capitalize() 는 첫 글자를 대문자로 올릴 뿐 아니라
#   '나머지 글자를 전부 소문자로 내린다'.
#   그래서 원래 대문자였던 DATA REPORT 도 data report 가 된다.


print()
print("========== [4] isupper() / islower() 검사 ==========")

print("EQP".isupper(), "EQP".islower())   # → True False
print("eqp".isupper(), "eqp".islower())   # → False True
print("Eqp".isupper(), "Eqp".islower())   # → False False

# 대문자와 소문자가 섞여 있으면 둘 다 False.
# is 로 시작하는 메서드는 '바꾸는 것'이 아니라 '검사'라서 True/False 를 돌려준다.


print()
print("========== [5] 대소문자 무시하고 비교하기 ==========")

a = "Fault"
b = "FAULT"

print(a == b)                      # → False   (1) 대소문자가 달라 다른 값
print(a.lower() == b.lower())      # → True    (2) 소문자로 통일한 뒤 비교

# 데이터를 다룰 때 표준처럼 쓰는 패턴이다


print()
print("========== [6] 앞뒤 공백 제거 ==========")

s = "  가동중  "
print("[" + s + "]")               # → [  가동중  ]   (1) 정리 전

clean = s.strip()                  # 결과를 다시 받는 것 잊지 말기
print("[" + clean + "]")           # → [가동중]       (2) 정리 후

# 공백은 눈에 안 보이니 [ ] 로 감싸서 확인하는 습관


print()
print("========== [7] 한쪽 공백만 제거 ==========")

s = "  대기  "
print("[" + s.lstrip() + "]")      # → [대기  ]   왼쪽(left)만
print("[" + s.rstrip() + "]")      # → [  대기]   오른쪽(right)만
print("[" + s.strip() + "]")       # → [대기]     양쪽 다

# 보통은 strip() 하나면 충분하다. 한쪽을 살려야 할 때만 lstrip/rstrip 을 쓴다.


print()
print("========== [8] 특정 문자 제거 ==========")

print("***경고***".strip("*"))      # → 경고    (1)
print("#$#대기#$#".strip("#$"))     # → 대기    (2) 여러 글자를 넣으면 그 중 아무거나 제거

print("##정상##상태##".strip("#"))  # → 정상##상태   (3)
# (3) 왜 가운데 ## 는 남는가?
#     strip 은 '양 끝'에서만 제거한다. 더 이상 해당 글자가 없으면 거기서 멈춘다.
#     가운데 글자는 절대 건드리지 않는다.


print()
print("========== [9] strip 이 못 지우는 것 ==========")

s = "  정 상  "
print("[" + s.strip() + "]")       # → [정 상]

# 가운데 공백이 남는 이유:
#   strip 은 '앞뒤 전용'이다. 글자 사이의 공백은 손대지 않는다.
#   중간 공백을 지우려면 다음 시간에 배울 replace 를 써야 한다.
#     s.strip().replace(" ", "")  →  정상


print()
print("========== [10] 체이닝 ==========")

raw = "  WARNING  "

# (1) 두 줄로 나눠서
step1 = raw.strip()                # 'WARNING'
step2 = step1.lower()              # 'warning'
print(step2)                       # → warning

# (2) 체이닝으로 한 줄에 (왼쪽 → 오른쪽 순서로 읽는다)
print(raw.strip().lower())         # → warning

# 입력값이 들어오면 일단 strip() → lower() 로 정리부터 하는 습관


print()
print("========== [11] 파일명 규칙 점검 ==========")

fname = "Vibration_DATA_03.CSV"

print(fname.endswith(".csv"))           # → False   (1)
# (1) 왜 False 인가?
#     실제 확장자가 대문자 .CSV 라서. == 나 endswith 는 대소문자를 구분한다.

low = fname.lower()
print(low)                              # → vibration_data_03.csv   (2)
print(low.startswith("vibration"))      # → True                    (3)
print(low.endswith(".csv"))             # → True                    (4)

print(fname.lower().endswith(".csv"))   # → True                    (5) 체이닝 한 줄


print()
print("========== [12] replace ― 바꾸기와 제거 ==========")

print("설비 고장 발생".replace("고장", "점검"))     # → 설비 점검 발생

s = "정 상 가 동"
print(s.replace(" ", ""))                        # → 정상가동

# strip() 으로 안 되는 이유:
#   strip 은 '앞뒤 전용'이라 글자 사이의 공백은 못 지운다.
#   replace(" ", "") 는 위치와 상관없이 공백을 전부 제거한다.
print("[" + s.strip() + "]")                     # → [정 상 가 동]   (가운데 그대로)


print()
print("========== [13] replace 체이닝과 숫자 변환 ==========")

price = "1,250,000"
# print(int(price))                              → ValueError  (쉼표는 숫자가 아님)

n = int(price.replace(",", ""))                  # (1) 쉼표 제거 후 변환
print(n, type(n))                                # → 1250000 <class 'int'>   (2)
print(n * 0.9)                                   # → 1125000.0               (3) 10% 할인가


print()
print("========== [14] split ― 나누고 번호로 꺼내기 ==========")

print("PUMP A 03".split())                       # → ['PUMP', 'A', '03']   (1)

date = "2026-03-15"
parts = date.split("-")                          # (2) 하이픈 기준으로 나누기
print(parts[0])                                  # → 2026   (연)
print(parts[1])                                  # → 03     (월)
print(parts[2])                                  # → 15     (일)


print()
print("========== [15] split 과 join ― 구분자 통째로 바꾸기 ==========")

raw = "2026/03/15"
parts = raw.split("/")                           # ['2026', '03', '15']
print("-".join(parts))                           # → 2026-03-15   (1)

fruits = "사과,배,감"
print(" / ".join(fruits.split(",")))             # → 사과 / 배 / 감   (2) 체이닝 한 줄도 가능


print()
print("========== [16] f-string 기본과 계산 ==========")

name = "MOTOR_B"
temp = 62.5
print(f"설비 {name}, 온도 {temp}도")               # → 설비 MOTOR_B, 온도 62.5도

a = 80
b = 91
c = 90
print(f"평균 {(a + b + c) / 3}")                  # → 평균 87.0   (중괄호 안에서 계산)


print()
print("========== [17] f-string 소수점 자리 지정 ==========")

rate = 87.456
print(f"{rate:.1f}")                             # → 87.5    (반올림)
print(f"{rate:.2f}")                             # → 87.46

run_h = 19
all_h = 24
print(f"가동률 {run_h / all_h * 100:.1f}%")       # → 가동률 79.2%
# :.1f 가 없으면 79.16666666666666 처럼 지저분하게 나온다


print()
print("========== [도전 1] 설비 상태 라벨 표준화 ==========")

raw1 = "  NORMAL  "
raw2 = "Normal"
raw3 = "normal  "
raw4 = "##normal##"

# (1) 정리 전에는 모두 다른 값
print("정리 전 raw1 == raw2:", raw1 == raw2)     # → 정리 전 raw1 == raw2: False
print("정리 전 raw2 == raw3:", raw2 == raw3)     # → 정리 전 raw2 == raw3: False

print()

# (2) 표준 형태로 정리
clean1 = raw1.strip().lower()                    # 공백 제거 → 소문자
clean2 = raw2.strip().lower()
clean3 = raw3.strip().lower()
clean4 = raw4.strip().strip("#").lower()         # 공백 → # → 소문자 순으로

print("[" + clean1 + "]")                        # → [normal]
print("[" + clean2 + "]")                        # → [normal]
print("[" + clean3 + "]")                        # → [normal]
print("[" + clean4 + "]")                        # → [normal]

print()

# (3) 정리 후에는 모두 같은 값
print("정리 후 clean1 == clean2:", clean1 == clean2)   # → 정리 후 clean1 == clean2: True
print("정리 후 clean2 == clean3:", clean2 == clean3)   # → 정리 후 clean2 == clean3: True
print("정리 후 clean3 == clean4:", clean3 == clean4)   # → 정리 후 clean3 == clean4: True

# (4) 리포트
print()
print("=" * 30)
print("원본 1:", "[" + raw1 + "]")
print("원본 2:", "[" + raw2 + "]")
print("원본 3:", "[" + raw3 + "]")
print("원본 4:", "[" + raw4 + "]")
print("-" * 30)
print("정리 결과:", "[" + clean1 + "]")
print("네 값 모두 동일:", clean1 == clean2 and clean2 == clean3 and clean3 == clean4)
print("=" * 30)

# 정리하지 않으면 컴퓨터는 이를 서로 다른 네 상태로 보고 따로 집계한다.
# 정리하면 하나의 상태로 정확하게 셀 수 있다.


print()
print("========== [도전 2] 센서 로그 한 줄 정리 리포트 ==========")

raw = "  7 , sensor_5 , FAULT , 1.23456  "

# (1) strip 먼저, split 나중
parts = raw.strip().split(",")
print(parts)                          # → ['7 ', ' sensor_5 ', ' FAULT ', ' 1.23456']
#   앞뒤 공백은 사라졌지만, 나눈 '각 조각'에는 아직 공백이 남아 있다

# (2)(3)(4) 조각별 정리
sid = parts[1].strip()                # 센서 이름
status = parts[2].strip().lower()     # 상태: 공백 정리 + 소문자
value = float(parts[3].strip())       # 측정값: 공백 정리 + 숫자 변환

print(sid)                            # → sensor_5
print(status)                         # → fault
print(value)                          # → 1.23456

# (5) f-string 한 줄 리포트 (소수점 2자리 = :.2f)
print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")
# → [센서 sensor_5] 상태 fault, 측정값 1.23

# 흐름 정리: 공백제거(strip) → 나누기(split) → 조각정리(strip·lower·float)
#           → f-string 출력.  이번 파트의 완성형 패턴이다.


print()
print("정답 확인 완료 - 틀린 문제는 해당 단원 파일을 다시 보세요")
