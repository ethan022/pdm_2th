# =============================================================================
#  7/23 복습 연습문제 ― 정답  (03_01 ~ 03_03  문자열 다루기)
# -----------------------------------------------------------------------------
#  정답은 '하나'가 아닙니다. 결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  다만 아직 배우지 않은 문법(strip·upper 같은 정리 메서드 · if · for ·
#  리스트 · 함수 정의)은 쓰지 않았습니다.
# =============================================================================


print("========== [1] 따옴표 안에 따옴표 ==========")

# 핵심: 안과 밖을 서로 '다른' 따옴표로
print("It's a normal signal")            # → It's a normal signal
print('작업자가 "정상"이라고 기록했다')      # → 작업자가 "정상"이라고 기록했다

# 이스케이프로 푸는 방법도 있다 (같은 종류 따옴표를 쓰고 싶을 때)
print('It\'s a normal signal')            # → It's a normal signal
print("작업자가 \"정상\"이라고 기록했다")     # → 작업자가 "정상"이라고 기록했다

# print('It's a normal signal')  → SyntaxError
#   중간의 ' 에서 문자열이 끝나버려 문법이 깨진다.


print()
print("========== [2] 여러 줄 문자열 ==========")

# (1) 삼중 따옴표 — 줄바꿈을 그대로 담는다
note1 = """일일 점검표
1. 온도 확인
2. 진동 확인"""
print(note1)
# → 일일 점검표
# → 1. 온도 확인
# → 2. 진동 확인

print("-" * 20)

# (2) \n 이스케이프 — 한 줄로 쓰되 줄바꿈 문자를 끼워 넣는다
note2 = "일일 점검표\n1. 온도 확인\n2. 진동 확인"
print(note2)
# → 위와 완전히 같은 결과

print(note1 == note2)              # → True   (두 방법의 결과는 같은 문자열)


print()
print("========== [3] 빈 문자열 vs 공백 문자열 ==========")

empty = ""
space = " "

print(len(empty))                  # → 0    글자가 0개
print(len(space))                  # → 1    공백 글자 1개
print(empty == space)              # → False  컴퓨터에겐 완전히 다른 값

# 눈으로는 구분이 안 되니 대괄호로 감싸서 확인하는 습관
print("[" + empty + "]")           # → []
print("[" + space + "]")           # → [ ]


print()
print("========== [4] 설비 정보 카드 만들기 ==========")

code = "MOTOR_B"
state = "점검필요"
hours = 3400                       # 숫자!
day = "2025-03-20"

# \n 으로 줄을 나누고, 숫자는 str() 로 바꿔서 이어 붙인다
card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hours) + "시간\n점검: " + day
print(card)
# → 설비: MOTOR_B
# → 상태: 점검필요
# → 가동: 3400시간
# → 점검: 2025-03-20

# str(hours) 를 빼먹으면?
#   → TypeError: can only concatenate str (not "int") to str


print()
print("========== [5] 인덱싱 ==========")

word = "MONITOR"
#       M  O  N  I  T  O  R
#       0  1  2  3  4  5  6
#      -7 -6 -5 -4 -3 -2 -1

print(word[0])                # → M    (1) 첫 글자
print(word[3])                # → I    (2) 3번 자리
print(word[-1])               # → R    (3) 마지막 (음수 인덱스)
print(word[-2])               # → O    (4) 끝에서 두 번째

# word[7] 을 실행하면?
#   → IndexError: string index out of range
#     "MONITOR"는 7글자지만 번호는 0~6까지만 있다. 7번은 없는 자리.
#     마지막 인덱스 = 글자 수 - 1


print()
print("========== [6] 슬라이싱 기본 ==========")

word = "MONITOR"

print(word[0:3])              # → MON    (1) 0,1,2번 — 3은 제외!
print(word[3:])               # → ITOR   (2) 3번부터 끝까지
print(word[:4])               # → MONI   (3) 앞 4글자
print(word[-3:])              # → TOR    (4) 뒤 3글자

# (1)은 word[:3] 으로도 같은 결과


print()
print("========== [7] step 과 뒤집기 ==========")

word = "MONITOR"

print(word[::2])              # → MNTR     (1) 0,2,4,6번
print(word[1::2])             # → OIO      (2) 1,3,5번
print(word[::-1])             # → ROTINOM  (3) 뒤집기
print(word[0:100])            # → MONITOR  (4) 범위를 넘겨도 오류 없음

# (4) 왜 오류가 안 나나?
#     슬라이싱은 '너그럽다' — 범위를 벗어나면 가능한 만큼만 가져온다.
#     반면 인덱싱은 '엄격하다' — 없는 번호를 쓰면 IndexError.
print(word[10:20])            # →          (가져올 게 없으면 빈 문자열)


print()
print("========== [8] 슬라이싱으로 데이터 쪼개기 ==========")

# (1) 날짜
date = "20260315"
#       2 0 2 6 0 3 1 5
#       0 1 2 3 4 5 6 7
print(date[:4] + "년 " + date[4:6] + "월 " + date[6:] + "일")
# → 2026년 03월 15일

# (2) 전화번호
phone = "01098765432"
#        0 1 0 9 8 7 6 5 4 3 2
#        0 1 2 3 4 5 6 7 8 9 10
print(phone[:3] + "-" + phone[3:7] + "-" + phone[7:])
# → 010-9876-5432

# 쉼표로 출력하면 사이에 공백이 자동으로 들어가므로 이때는 + 로 이어 붙인다


print()
print("========== [9] len 과 count ==========")

fname = "vibration_sensor_07.csv"

print(len(fname))                  # → 23   (1) 전체 글자 수
print(fname.count("_"))            # → 2    (2) 밑줄 개수
print(fname.count("s"))            # → 3    (3) s 는 sensor 에 2번, csv 에 1번
print(fname.count("z"))            # → 0    (4) 없으면 0 (오류가 아니다!)


print()
print("========== [10] in / startswith / endswith ==========")

fname = "vibration_sensor_07.csv"

print("sensor" in fname)                   # → True    (1)
print(fname.startswith("vibration"))       # → True    (2)
print(fname.endswith(".csv"))              # → True    (3)
print(fname.endswith(".xlsx"))             # → False   (4)
print("temp" not in fname)                 # → True    (5) 들어있지 않으므로 True

print()

name = "data_log"
print("log" in name)                       # → True    어딘가에 들어 있음
print(name.startswith("log"))              # → False   맨 앞은 'data'
print(name.endswith("log"))                # → True    맨 뒤는 'log'

# (6) 왜 다른가?
#     in 은 '어디든' 포함되어 있으면 True,
#     startswith 는 '맨 앞'만, endswith 는 '맨 뒤'만 본다.
#     목적에 맞는 도구를 골라 써야 한다.


print()
print("========== [11] find 와 슬라이싱 조합 ==========")

email = "kim@factory.co.kr"
#        k  i  m  @  f  a  c  t  o  r  y  .  c  o  .  k  r
#        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

at = email.find("@")
print(at)                          # → 3     (1) @ 의 위치
print(email[:at])                  # → kim              (2) 아이디
print(email[at + 1:])              # → factory.co.kr    (3) 도메인
print(email.find("#"))             # → -1    (4) 없으면 -1

# index() 를 썼다면?
#   email.index("#")  →  ValueError: substring not found  (오류로 멈춤)
#   없을 수도 있으면 find, 반드시 있어야 하는 값이면 index.


print()
print("========== [12] == 비교의 함정 ==========")

label = "WARNING"

print(label == "WARNING")          # → True
print(label == "warning")          # → False   대소문자는 다른 글자
print(label == "WARNING ")         # → False   뒤 공백 하나 차이

# 왜 문제가 되나?
#   같은 상태인데 'NORMAL' / 'Normal' / 'normal' 로 섞여 들어오면
#   컴퓨터는 이를 세 가지 다른 상태로 보고 따로 집계한다.
#   → 분석 전에 대소문자와 앞뒤 공백을 통일해야 한다.
#     (7/24 03_04 공백과 대소문자 정리에서 배움)


print()
print("========== [도전] 설비 로그 한 줄 분석 ==========")

log = "20250115 EQP-001 WARNING temp=95.2"
#      2 0 2 5 0 1 1 5 ␣ E  Q  P  -  0  0  1  ␣  W  A  R  N  I  N  G  ␣  t  e  m  p  =  9  5  .  2
#      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33

# (1) 날짜를 2025-01-15 형태로
date = log[:4] + "-" + log[4:6] + "-" + log[6:8]
print("날짜:", date)                        # → 날짜: 2025-01-15

# (2) 설비 코드
equip = log[9:16]
print("설비 코드:", equip)                   # → 설비 코드: EQP-001

# (3) 경고인지 여부
is_warning = "WARNING" in log
print("경고?", is_warning)                  # → 경고? True

# (4) 측정값을 '숫자'로 꺼내기
eq = log.find("=")                # = 의 위치를 찾고
print("= 위치:", eq)                        # → = 위치: 29
value_text = log[eq + 1:]         # 그 다음 칸부터 끝까지 → 아직 '글자'
value = float(value_text)         # 비교하려면 숫자로 변환
print("측정값(글자):", value_text, type(value_text))
# → 측정값(글자): 95.2 <class 'str'>
print("측정값(숫자):", value, type(value))
# → 측정값(숫자): 95.2 <class 'float'>

# (5) 90 초과인지
print("90 초과?", value > 90)               # → 90 초과? True

# (6) 리포트로 정리
print()
print("=" * 30)
print("설비:", equip)
print("일시:", date)
print("온도:", value, "℃")
print("경고 상태:", is_warning)
print("기준(90) 초과:", value > 90)
print("=" * 30)


print()
print("정답 확인 완료 - 틀린 문제는 해당 단원 파일을 다시 보세요")
