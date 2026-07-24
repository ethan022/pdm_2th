# =============================================================================
#  7/22 복습 연습문제 ― 정답  (01_01 ~ 02_04)
# -----------------------------------------------------------------------------
#  정답은 '하나'가 아닙니다. 결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  다만 아직 배우지 않은 문법(문자열 메서드 · if · for · 리스트 · 함수 정의)은
#  쓰지 않았습니다.
# =============================================================================


print("========== [1] print 와 주석 ==========")

# 제목은 글자, 측정값은 숫자. 이름표와 값은 쉼표로 이어서.
print("=== 2번 설비 점검 ===")
print("온도(℃):", 68)              # 정상 범위
print("진동(mm/s):", 1.7)


print()
print("========== [2] 계산과 괄호 ==========")

print("합:", 64 + 78)              # → 합: 142
print("차:", 78 - 64)              # → 차: 14
print("평균:", (64 + 78) / 2)       # → 평균: 71.0

# 괄호를 빼먹으면? 나누기가 먼저 계산되어 완전히 다른 값이 나온다
print("괄호 없이:", 64 + 78 / 2)    # → 괄호 없이: 103.0


print()
print("========== [3] 변수와 재할당 ==========")

# = 는 '저장'. 오른쪽을 먼저 계산해서 다시 왼쪽에 넣는다.
x = 20
print(x)                          # → 20
x = x - 5                         # 20 - 5
print(x)                          # → 15
x = x * 3                         # 15 * 3
print(x)                          # → 45


print()
print("========== [4] 값 복사 ==========")

a = 50
b = a                             # 지금 a의 값(50)을 b에 '복사'
a = 777                           # a만 바꿈
print(a)                          # → 777
print(b)                          # → 50
# b가 50인 이유: b = a 는 두 변수를 묶는 것이 아니라
#               그 순간의 값을 복사한 것뿐이라서, 이후 a가 바뀌어도 b는 그대로.


print()
print("========== [5] 자료형 맞히기 ==========")

print(type(42))                   # → <class 'int'>     따옴표·소수점 없음
print(type(42.0))                 # → <class 'float'>   소수점 있음
print(type("42"))                 # → <class 'str'>     따옴표 있음
print(type(False))                # → <class 'bool'>    True/False
print(type(10 > 3))               # → <class 'bool'>    비교의 결과는 항상 bool


print()
print("========== [6] 자료형에 맞는 변수 만들기 ==========")

equip_name = "MOTOR_B"            # str   이름은 글자
equip_temp = 62.4                 # float 온도는 소수점이 있을 수 있음
run_count = 15                    # int   횟수는 딱 떨어짐
is_running = True                 # bool  가동 중 / 아님 두 상태

print(equip_name, type(equip_name))    # → MOTOR_B <class 'str'>
print(equip_temp, type(equip_temp))    # → 62.4 <class 'float'>
print(run_count, type(run_count))      # → 15 <class 'int'>
print(is_running, type(is_running))    # → True <class 'bool'>


print()
print("========== [7] 사칙연산 ==========")

a = 23
b = 4
print("합:", a + b)                # → 합: 27
print("차:", a - b)                # → 차: 19
print("곱:", a * b)                # → 곱: 92
print("나눗셈:", a / b)            # → 나눗셈: 5.75      (항상 실수)
print("몫:", a // b)               # → 몫: 5
print("나머지:", a % b)            # → 나머지: 3
print("거듭제곱:", a ** b)          # → 거듭제곱: 279841


print()
print("========== [8] 시간 변환 ==========")

minutes = 275
print("가동 시간:", minutes // 60, "시간", minutes % 60, "분")
# → 가동 시간: 4 시간 35 분
#   //(몫)이 시간, %(나머지)가 분


print()
print("========== [9] 설비 지표 계산 ==========")

total = 1200
defect = 42
print("불량률(%):", defect / total * 100)      # → 불량률(%): 3.5000000000000004
#   3.5 가 나올 줄 알았는데 뒤에 이상한 숫자가 붙는다.
#   02_02 에서 배운 '실수 계산의 작은 오차'가 바로 이것 (0.1 + 0.2 와 같은 현상).
#   버그가 아니라 컴퓨터가 소수를 저장하는 방식 때문이다.

run_h = 19
all_h = 24
print("가동률(%):", run_h / all_h * 100)       # → 가동률(%): 79.16666666666666

# 소수점이 지저분하면 round(값, 자릿수) 로 다듬는다
print("불량률(%):", round(defect / total * 100, 1))  # → 불량률(%): 3.5
print("가동률(%):", round(run_h / all_h * 100, 1))   # → 가동률(%): 79.2


print()
print("========== [10] 비교·논리 연산으로 정상 판정 ==========")

temp = 72
pressure = 8.5

temp_ok = 60 <= temp and temp <= 90        # 60 이상 '그리고' 90 이하
pres_ok = 3 <= pressure and pressure <= 7

print("온도 정상:", temp_ok)                # → 온도 정상: True
print("압력 정상:", pres_ok)                # → 압력 정상: False  (8.5는 7을 넘음)
print("모두 정상:", temp_ok and pres_ok)    # → 모두 정상: False
print("이상 있음:", not (temp_ok and pres_ok))   # → 이상 있음: True


print()
print("========== [11] 복합 할당으로 재고 추적 ==========")

stock = 80
print(stock)                      # → 80
stock += 120                      # 입고
print(stock)                      # → 200
stock -= 65                       # 출고
print(stock)                      # → 135
stock -= 8                        # 불량 폐기
print(stock)                      # → 127
stock += 3                        # 반품 입고
print(stock)                      # → 130

# stock += 120 은 stock = stock + 120 의 줄임말


print()
print("========== [12] 형변환 ==========")

a_input = "120"
b_input = "45"

# (1) 글자끼리 더하면 '이어 붙이기'
print(a_input + b_input)                   # → 12045

# (2) 숫자로 변환한 뒤 더하면 '계산'
print(int(a_input) + int(b_input))         # → 165

# (3) 왜 다른가?
#     input() 으로 받은 값은 숫자를 입력해도 자료형이 str(글자) 이다.
#     같은 + 기호라도 글자끼리는 연결, 숫자끼리는 덧셈으로 동작한다.
#     그래서 계산 전에 반드시 int() / float() 로 '변환'해야 한다.
print(type(a_input))                       # → <class 'str'>
print(type(int(a_input)))                  # → <class 'int'>


print()
print("========== [도전] 입력 → 변환 → 계산 → 출력 ==========")

# 실제 입력을 받으려면 아래 주석을 풀고, 그 아래 흉내내기 4줄을 지우세요
# device = input("설비명: ")
# temp = float(input("온도(℃): "))
# pressure = float(input("압력(bar): "))
# count = int(input("점검 횟수: "))

# ↓ 여기서는 입력 결과를 흉내내어 실행 (input 결과는 항상 글자라는 점에 주목)
device = "PUMP_A"                          # input("설비명: ")
temp = float("85.5")                       # float(input("온도(℃): "))
pressure = float("5.2")                    # float(input("압력(bar): "))
count = int("7")                           # int(input("점검 횟수: "))

temp_ok = 60 <= temp and temp <= 90
pres_ok = 3 <= pressure and pressure <= 7

print("=" * 25)
print("설비:", device)
print("온도:", temp, "℃")
print("압력:", pressure, "bar")
print("점검 횟수:", count, "회")
print("온도 정상(60~90):", temp_ok)
print("압력 정상(3~7):", pres_ok)
print("모두 정상:", temp_ok and pres_ok)
print("=" * 25)

# → =========================
# → 설비: PUMP_A
# → 온도: 85.5 ℃
# → 압력: 5.2 bar
# → 점검 횟수: 7 회
# → 온도 정상(60~90): True
# → 압력 정상(3~7): True
# → 모두 정상: True
# → =========================


print()
print("정답 확인 완료 - 틀린 문제는 해당 단원 파일을 다시 보세요")
