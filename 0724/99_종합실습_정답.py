# =============================================================================
#  1주차 종합 실습 ― 정답  (설비 점검 리포트 만들기)
# -----------------------------------------------------------------------------
#  정답은 '하나'가 아닙니다. 결과만 같으면 다른 방법도 맞습니다.
#  미션이 서로 이어지므로 파일 전체를 실행하면 마지막에 리포트가 완성됩니다.
# =============================================================================


print("========== [1] 워밍업 ― 오류 3개 고치기 ==========")

# 오류 1: print(설비 점검 시작)   → NameError  (글자에 따옴표가 없음)
# 오류 2: print("가동률:", 87.5   → SyntaxError (닫는 괄호가 없음)
# 오류 3: print("온도: " + 91.5)  → TypeError  (글자 + 숫자는 불가)

print("설비 점검 시작")            # → 설비 점검 시작   (따옴표 추가)
print("가동률:", 87.5)            # → 가동률: 87.5    (괄호 닫기)
print("온도: " + str(91.5))       # → 온도: 91.5      (str() 로 변환)
# 오류 3은 print("온도:", 91.5) 처럼 쉼표를 써도 정답


print()
print("========== [2] 설비 기본 정보 ― 변수와 자료형 ==========")

equip_name = "PUMP-A-07"          # str   이름은 글자
equip_temp = 91.5                 # float 온도는 소수점
check_count = 3                   # int   횟수는 정수
is_running = True                 # bool  참/거짓

print(equip_name, type(equip_name))     # → PUMP-A-07 <class 'str'>
print(equip_temp, type(equip_temp))     # → 91.5 <class 'float'>
print(check_count, type(check_count))   # → 3 <class 'int'>
print(is_running, type(is_running))     # → True <class 'bool'>


print()
print("========== [3] 가동 지표 계산 ==========")

total_min = 1725
run_h = 21
all_h = 24
total = 800
defect = 28

# (1) 몫(//)이 시간, 나머지(%)가 분
print("가동 시간:", total_min // 60, "시간", total_min % 60, "분")
# → 가동 시간: 28 시간 45 분

# (2)(3) 리포트에서 다시 쓸 것이므로 변수에 저장
run_rate = run_h / all_h * 100
defect_rate = defect / total * 100
print("가동률(%):", run_rate)             # → 가동률(%): 87.5
print("불량률(%):", defect_rate)          # → 불량률(%): 3.5000000000000004
#   3.5 뒤에 이상한 오차가 붙는다! 02_02에서 배운 '실수 계산의 작은 오차'다.
#   버그가 아니며, 보기 좋게 만들려면 round() 또는 f-string 의 :.1f 를 쓴다.
print("불량률(%):", round(defect_rate, 1))   # → 불량률(%): 3.5


print()
print("========== [4] 로그 한 줄 받기 ― 앞뒤 공백 정리 ==========")

raw_log = "  20260724, PUMP-A-07 , WARNING , temp=91.5  "

print("[" + raw_log + "]")        # → [  20260724, PUMP-A-07 , WARNING , temp=91.5  ]
log = raw_log.strip()             # 결과를 다시 받아야 반영!
print("[" + log + "]")            # → [20260724, PUMP-A-07 , WARNING , temp=91.5]


print()
print("========== [5] 쉼표로 나누고 조각 정리 ==========")

# (1) 나눠 보면 조각 안에 공백이 남아 있다
parts = log.split(",")
print(parts)
# → ['20260724', ' PUMP-A-07 ', ' WARNING ', ' temp=91.5']

# (2) 조각을 번호로 꺼내 strip 으로 정리
date_text = parts[0].strip()
code = parts[1].strip()
status_text = parts[2].strip()
measure_text = parts[3].strip()

# (3) 공백이 사라졌는지 확인
print("[" + date_text + "]")      # → [20260724]
print("[" + code + "]")           # → [PUMP-A-07]
print("[" + status_text + "]")    # → [WARNING]
print("[" + measure_text + "]")   # → [temp=91.5]


print()
print("========== [6] 날짜 성형 ― 슬라이싱 ==========")

#  2 0 2 6 0 7 2 4
#  0 1 2 3 4 5 6 7
date = date_text[:4] + "-" + date_text[4:6] + "-" + date_text[6:]
print(date)                       # → 2026-07-24


print()
print("========== [7] 설비 코드 분석 ==========")

print(code[0])                    # → P      (1) 첫 글자
print(code.startswith("PUMP"))    # → True   (2) 접두어 확인
print(code.count("-"))            # → 2      (3) 하이픈 개수

code_parts = code.split("-")      # (4) ['PUMP', 'A', '07']
kind = code_parts[0]
line = code_parts[1]
num = code_parts[2]
print(kind, line, num)            # → PUMP A 07


print()
print("========== [8] 상태 라벨 표준화와 비교 ==========")

status = status_text.lower()      # (1) 소문자로 통일
print(status)                     # → warning
print(status == "warning")        # → True    (2) 통일 후 비교
print(status_text == "warning")   # → False   (3) 통일 전엔 대소문자가 달라 False!
# 같은 상태가 'WARNING' 'Warning' 'warning' 으로 섞여 들어와도
# lower() 로 통일하면 하나로 정확하게 셀 수 있다


print()
print("========== [9] 측정값 추출 ==========")

#  t e m p = 9 1 . 5
#  0 1 2 3 4 5 6 7 8
eq = measure_text.find("=")
print(eq)                             # → 4       (1) = 의 위치
print(measure_text[:eq])              # → temp    (2) 항목 이름

value_text = measure_text[eq + 1:]    # (3) = 다음 칸부터 끝까지
print(value_text, type(value_text))   # → 91.5 <class 'str'>   ← 아직 글자!

value = float(value_text)             # (4) 계산하려면 숫자로 변환
print(value, type(value))             # → 91.5 <class 'float'>


print()
print("========== [10] 종합 판정 ==========")

temp_ok = 60 <= value and value <= 90        # 60 이상 '그리고' 90 이하
print(temp_ok)                    # → False   (91.5는 90을 넘음)

is_warning = status == "warning"
print(is_warning)                 # → True

need_check = (not temp_ok) or is_warning     # 범위 밖 '또는' 경고 라벨
print(need_check)                 # → True


print()
print("========== [11] 최종 리포트 ― f-string ==========")

print("=" * 34)
print(f"설비 점검 리포트  ({date})")
print("-" * 34)
print(f"설비 코드 : {code}  ({kind} 계열 / {line} 라인 / {num}호기)")
print(f"상태 라벨 : {status}")
print(f"온도 측정 : {value:.1f} 도")
print(f"정상 범위(60~90) : {temp_ok}")
print(f"가동 시간 : {total_min // 60}시간 {total_min % 60}분")
print(f"가동률 : {run_rate:.1f}%  /  불량률 : {defect_rate:.1f}%")
print(f"정비 필요 여부 : {need_check}")
print("=" * 34)

# → ==================================
# → 설비 점검 리포트  (2026-07-24)
# → ----------------------------------
# → 설비 코드 : PUMP-A-07  (PUMP 계열 / A 라인 / 07호기)
# → 상태 라벨 : warning
# → 온도 측정 : 91.5 도
# → 정상 범위(60~90) : False
# → 가동 시간 : 28시간 45분
# → 가동률 : 87.5%  /  불량률 : 3.5%
# → 정비 필요 여부 : True
# → ==================================


print()
print("========== [도전] 현장 입력 버전 ==========")

# 실제 입력을 받으려면 아래 두 줄의 주석을 풀고, 흉내 두 줄을 지우세요
# temp = float(input("온도(℃): "))
# vib = float(input("진동(mm/s): "))

# ↓ 여기서는 입력 결과를 흉내내어 실행 (input 결과는 항상 글자 → float 변환)
temp = float("85.5")                  # 온도 입력 흉내
vib = float("3.4")                    # 진동 입력 흉내

temp_ok = 60 <= temp and temp <= 90
vib_ok = 0.5 <= vib and vib <= 3.0

print(f"온도 정상: {temp_ok} / 진동 정상: {vib_ok}")
# → 온도 정상: True / 진동 정상: False   (3.4는 3.0을 넘음)
print(f"모두 정상: {temp_ok and vib_ok}")
# → 모두 정상: False


print()
print("정답 확인 완료 - 틀린 미션은 해당 단원 복습 파일을 다시 보세요")
