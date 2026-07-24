# =============================================================================
#  03_03  문자열 연산과 검색  ―  복습용
# -----------------------------------------------------------------------------
#  배운 것 : 문자열 연결(+)·반복(*), len(), in / not in, count(), find(),
#            index(), startswith(), endswith(), == 비교
#  사용법  : "→" 결과를 먼저 예상한 뒤 실행해서 맞춰보기
# =============================================================================

print("========== 1. 연결(+) 과 반복(*) ==========")

# ---------------------------------------------------------------------------
# +  로 여러 문자열을 한 줄로 이어 붙인다.
#    사이에 넣는 ' / ', ' - ' 같은 것을 '구분자'라 하고, 구분자에 따라 모양이 달라진다.
# *  로 같은 글자를 반복한다. 구분선 만들 때 유용.
# ---------------------------------------------------------------------------

code = "EQP-001"
status = "정상"
date = "2025-01-15"

print(code + " / " + status + " / " + date)     # → EQP-001 / 정상 / 2025-01-15
print(code + " - " + status + " - " + date)     # → EQP-001 - 정상 - 2025-01-15

line = "=" * 20
print(line)                                     # → ====================
print("상태: " + status)                         # → 상태: 정상
print("횟수: " + str(5))                         # → 횟수: 5     (숫자는 str() 로!)
print("-" * 20)                                 # → --------------------


print()
print("========== 2. len() ― 글자 수 세기 ==========")

# ---------------------------------------------------------------------------
# 형식:  len(문자열)   →  글자 수를 '숫자'로 알려준다
#   · 공백도 한 글자로 센다
#   · 빈 문자열의 길이는 0
# ---------------------------------------------------------------------------

print(len("PYTHON"))          # → 6
print(len("AI 분석"))          # → 5     (A, I, 공백, 분, 석 → 공백도 한 글자)
print(len(""))                # → 0     (빈 문자열)
print(len(" "))               # → 1     (공백 한 개)
print(len("설비 점검 완료"))     # → 8     (한글도 한 글자는 1)

# 활용 : 입력값이 규칙에 맞는 자릿수인지 점검
phone = "01012345678"
print(len(phone))             # → 11    (휴대폰 번호는 11자리)

code = "EQP-001"
print(len(code))              # → 7     (설비 코드는 7자리)

# 지금은 눈으로 확인만 한다. 자동 판단은 조건문(04_02)을 배운 뒤에.


print()
print("========== 3. in / not in ― 포함 여부 ==========")

# ---------------------------------------------------------------------------
# 형식:  "찾을것" in 문자열       →  들어 있으면 True, 없으면 False
#        "찾을것" not in 문자열   →  in 의 반대
#
# 결과는 항상 True / False (bool). 같은 상황에서 in 과 not in 은 늘 반대 결과.
# 어느 쪽을 쓸지는 '문장으로 읽어서 자연스러운 쪽'을 고른다.
# ---------------------------------------------------------------------------

msg = "설비 고장 발생"
print("고장" in msg)           # → True
print("정상" in msg)           # → False
print("정상" not in msg)       # → True
print("고장" not in msg)       # → False

# 활용 : 로그에서 위험 키워드 탐색
message = "2025-01-15 WARNING temp exceeded"
print("WARNING" in message)   # → True
print("ERROR" in message)     # → False

# 활용 : 컬럼명에 특정 단어가 있는지
column = "temp_sensor_1"
print("sensor" in column)     # → True
print("vibration" in column)  # → False

# → 다음 단원에서 배울 '데이터 필터링'의 기초 개념


print()
print("========== 4. count() ― 몇 번 나오는지 세기 ==========")

# ---------------------------------------------------------------------------
# 형식:  문자열.count("찾을것")   →  나온 횟수를 '숫자'로
#   · 없으면 0  (오류가 아니라 정상 결과)
# ---------------------------------------------------------------------------

print("banana".count("a"))            # → 3
print("a,b,c,d".count(","))           # → 3     (쉼표 3개 → 항목은 4개)
print("sensor-01-temp".count("-"))    # → 2
print("정상".count("고장"))             # → 0     (없으면 0)

# 활용 : 경로에서 폴더 깊이 세기
path = "data/2025/01/sensor.csv"
print(path.count("/"))                # → 3


print()
print("========== 5. find() ― 처음 나오는 위치 찾기 ==========")

# ---------------------------------------------------------------------------
# 형식:  문자열.find("찾을것")   →  처음 나오는 위치(번호)를 '숫자'로
#   · 위치 번호는 인덱싱과 똑같이 0부터
#   · 없으면 -1  ("못 찾았다"는 신호. 오류가 아님)
#   · 찾은 위치를 슬라이싱의 끝 번호로 활용하면 강력하다
# ---------------------------------------------------------------------------

email = "hong@company.com"
#        h  o  n  g  @  c  o  m ...
#        0  1  2  3  4  5  6  7
at = email.find("@")
print(at)                     # → 4
print(email[:at])             # → hong              (@ 앞부분 = 아이디)
print(email[at+1:])           # → company.com       (@ 뒷부분 = 도메인)

print("정상".find("고장"))      # → -1    (없으면 -1)

text = "temp_2024"
print(text.find("_"))         # → 4     (첫 밑줄 위치)
print(text.find("z"))         # → -1    (없음)

# 활용 : 파일명에서 확장자 앞부분만 꺼내기
fname = "sensor_log.csv"
dot = fname.find(".")
print(dot)                    # → 10
print(fname[:dot])            # → sensor_log


print()
print("========== 6. index() ― find 의 짝 ==========")

# ---------------------------------------------------------------------------
# 사용법은 find() 와 완전히 동일. 차이는 '못 찾았을 때'뿐이다.
#
#     find()   →  없으면 -1 을 돌려주고 계속 진행
#     index()  →  없으면 오류(ValueError)를 내고 멈춤
#
# 없어도 멈추면 안 되면  find,  반드시 있어야 하는 값이면  index.
# ---------------------------------------------------------------------------

email = "hong@company.com"
print(email.index("@"))       # → 4     (find 와 같은 결과)
print(email.find("@"))        # → 4

# print("정상".index("고장"))   → ValueError: substring not found
print("정상".find("고장"))      # → -1    (이쪽은 오류 없이 -1)


print()
print("========== 7. startswith() / endswith() ― 시작·끝 확인 ==========")

# ---------------------------------------------------------------------------
#   문자열.startswith("접두어")   →  그것으로 '시작'하면 True
#   문자열.endswith("접미어")     →  그것으로 '끝나면' True
#
#   in 과의 차이 : in 은 '어디든' 포함,  startswith 는 '맨 앞'만
#   startswith 는 앞, endswith 는 뒤 → 짝으로 기억
# ---------------------------------------------------------------------------

code = "EQP-001"
print(code.startswith("EQP"))         # → True
print(code.startswith("PUMP"))        # → False

fname = "cmapss.csv"
print(fname.endswith(".csv"))         # → True    (확장자 확인의 단골 도구)
print(fname.endswith(".xlsx"))        # → False

fname2 = "sensor_log.csv"
print(fname2.startswith("sensor"))    # → True
print(fname2.endswith(".csv"))        # → True

# in 과 startswith 의 차이를 확실히
name = "data_log"
print("log" in name)                  # → True    (어딘가에 들어 있음)
print(name.startswith("log"))         # → False   (맨 앞은 'data')
print(name.endswith("log"))           # → True    (맨 뒤는 'log')


print()
print("========== 8. == ― 완전히 같은지 비교 ==========")

# ---------------------------------------------------------------------------
#   등호 하나(=)는 저장,  등호 두 개(==)는 비교!
#   두 문자열이 '완전히' 같아야 True.
#     · 대소문자가 다르면 다른 값     'NORMAL' != 'normal'
#     · 앞뒤 공백 하나만 달라도 다른 값 '정상' != '정상 '
# ---------------------------------------------------------------------------

status = "정상"
print(status == "정상")        # → True
print(status == "고장")        # → False

label = "WARNING"
print(label == "WARNING")     # → True
print(label == "warning")     # → False   (대소문자 구분!)

print("정상" == "정상 ")       # → False   (뒤 공백 하나 차이)
print("NORMAL" == "Normal")   # → False

# 왜 중요한가?
#   같은 상태인데 'NORMAL' / 'Normal' / 'normal' 로 섞여 들어오면
#   컴퓨터는 세 가지 다른 상태로 따로 집계한다.
#   → 비교 전에 대소문자·공백을 통일해야 한다 (03_04 정리 메서드에서 배움)


print()
print("========== 9. 도구 정리 ==========")

# ---------------------------------------------------------------------------
#  결과 형태로 묶어서 기억하면 헷갈리지 않는다.
#
#   도구                              용도            결과        못 찾으면
#   ------------------------------------------------------------------------
#   +  /  *                          연결 · 반복      문자열       -
#   len()                            길이            숫자         -
#   count()                          횟수            숫자         0
#   find()                           위치            숫자         -1
#   index()                          위치            숫자         오류!
#   in  /  not in                    포함 여부        참·거짓      False
#   startswith() / endswith() / ==   시작·끝·비교     참·거짓      False
# ---------------------------------------------------------------------------


print("========== 10. 실전 : 파일명·컬럼명 점검 ==========")

fname = "temp_sensor_01.csv"

print("파일명:", fname)                        # → 파일명: temp_sensor_01.csv
print("길이:", len(fname))                     # → 길이: 18
print("csv 파일인가?", fname.endswith(".csv"))  # → csv 파일인가? True
print("temp 로 시작?", fname.startswith("temp"))# → temp 로 시작? True
print("sensor 포함?", "sensor" in fname)       # → sensor 포함? True
print("밑줄 개수:", fname.count("_"))           # → 밑줄 개수: 2
print("점 위치:", fname.find("."))              # → 점 위치: 14
print("확장자 뺀 이름:", fname[:fname.find(".")])# → 확장자 뺀 이름: temp_sensor_01

print()

# 설비 로그 한 줄 점검
log = "2025-01-15 EQP-001 WARNING temp=95.2"
print("로그:", log)
print("길이:", len(log))                        # → 길이: 36
print("경고 포함?", "WARNING" in log)            # → 경고 포함? True
print("고장 포함?", "ERROR" in log)              # → 고장 포함? False
print("2025 로 시작?", log.startswith("2025"))   # → 2025 로 시작? True
print("하이픈 개수:", log.count("-"))            # → 하이픈 개수: 3
print("= 위치:", log.find("="))                 # → = 위치: 31
print("측정값:", log[log.find("=") + 1:])       # → 측정값: 95.2


# =============================================================================
#  스스로 확인해보기 (실행 전에 답을 먼저 적어보기)
# -----------------------------------------------------------------------------
#  Q1.  len("AI 분석") 은?
#       A. 5   (공백도 한 글자)
#
#  Q2.  "banana".count("a") 는?
#       A. 3
#
#  Q3.  "정상".find("고장") 과 "정상".index("고장") 의 차이는?
#       A. find 는 -1 을 돌려주고, index 는 ValueError 로 멈춘다.
#
#  Q4.  "data_log" 에서 "log" 를 찾을 때
#       "log" in name  /  name.startswith("log")  /  name.endswith("log") 의 결과는?
#       A. True / False / True
#
#  Q5.  "NORMAL" == "normal" 의 결과는? 왜?
#       A. False. 컴퓨터는 대문자와 소문자를 다른 글자로 본다.
#
#  Q6.  "sensor_log.csv" 가 csv 파일인지 확인하는 코드는?
#       A. fname.endswith(".csv")
#
#  Q7.  "hong@company.com" 에서 '@' 앞의 아이디만 꺼내려면?
#       A. at = email.find("@")  →  email[:at]
#
#  Q8.  결과가 '숫자'인 도구와 '참·거짓'인 도구를 각각 나열하면?
#       A. 숫자   : len, count, find, index
#          참·거짓 : in, not in, startswith, endswith, ==
# =============================================================================

print()
print("03_03 복습 완료")
