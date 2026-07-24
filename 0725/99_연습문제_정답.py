# =============================================================================
#  7/25 복습 연습문제 ― 정답  (04_01 리스트, 04_02 조건문)
# -----------------------------------------------------------------------------
#  정답은 '하나'가 아닙니다. 결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  다만 아직 배우지 않은 문법(for · while · 함수 정의)은 쓰지 않았습니다.
# =============================================================================


print("========== [1] 리스트 만들기와 len ==========")

temps = [22, 25, 27, 24, 26]
print(temps)                       # → [22, 25, 27, 24, 26]
print(len(temps))                  # → 5

empty = []
print(len(empty))                  # → 0


print()
print("========== [2] 인덱싱 ==========")

print(temps[0])                    # → 22   (1) 첫 번째 = 0번
print(temps[2])                    # → 27   (2) 세 번째 = 2번
print(temps[-1])                   # → 26   (3) 마지막
print(temps[-2])                   # → 24   (4) 뒤에서 두 번째

# temps[5] 는?
#   → IndexError: list index out of range
#     5개짜리 리스트의 인덱스는 0~4까지. 마지막 인덱스 = 개수 - 1


print()
print("========== [3] 인덱스로 꺼낸 값 계산하기 ==========")

output = [140, 90, 120, 105, 95, 110]
first = output[0]                  # 140
last = output[-1]                  # 110
print(first + last)                # → 250
print((first + last) / 2)          # → 125.0


print()
print("========== [4] 슬라이싱 ==========")

temps = [22, 24, 27, 29, 26, 23, 25, 28, 30, 21]
print(temps[:3])                   # → [22, 24, 27]     (1) 앞 3개
print(temps[-3:])                  # → [28, 30, 21]     (2) 뒤 3개

first = temps[:5]                  # (3) 앞 5개
second = temps[5:]                 #     뒤 5개
print(first)                       # → [22, 24, 27, 29, 26]
print(second)                      # → [23, 25, 28, 30, 21]
print(len(first), len(second))     # → 5 5              (4)


print()
print("========== [5] 이상값 찾아 바로잡기 ==========")

temps = [25, 26, 270, 28, 27]
print(270 in temps)                # → True    (1) 이상값 있음
i = temps.index(270)
print(i)                           # → 2       (2) 위치
temps[i] = 27                      # (3) 그 자리만 올바른 값으로 교체
print(temps)                       # → [25, 26, 27, 28, 27]
print(270 in temps)                # → False   (4) 사라짐 확인


print()
print("========== [6] 값 추가 ==========")

collected = []
collected.append(31)               # 끝에 추가
print(collected)                   # → [31]
collected.insert(0, 29)            # 맨 앞에 끼워 넣기
print(collected)                   # → [29, 31]
collected.extend([32, 33])         # 리스트 이어붙이기
print(collected)                   # → [29, 31, 32, 33]


print()
print("========== [7] 값 제거 ==========")

temps = [25, 26, 888, 24, 28, 25]
temps.remove(888)                  # (1) '값' 기준 제거
print(temps)                       # → [25, 26, 24, 28, 25]

x = temps.pop(2)                   # (2) '위치' 기준, 꺼내면서 제거
print(x)                           # → 24
print(temps)                       # → [25, 26, 28, 25]

del temps[0]                       # (3) '위치' 기준, 그냥 삭제
print(temps)                       # → [26, 28, 25]


print()
print("========== [8] 정렬과 탐색 ==========")

temps = [27, 23, 30, 23, 26, 28]
temps.sort()                       # (1) 오름차순 — 원본이 바뀜!
print(temps)                       # → [23, 23, 26, 27, 28, 30]

print(temps.count(23))             # → 2    (2) 23의 개수
print(temps.index(23))             # → 0    (2) 처음 위치

print(temps[0], temps[-1])         # → 23 30    (3) 정렬 후 첫 값=최소, 끝 값=최대

temps.reverse()                    # (4) 순서 뒤집기
print(temps)                       # → [30, 28, 27, 26, 23, 23]


print()
print("========== [9] if 기본 구조 ― 출력 예측 ==========")

temp = 65
if temp > 80:                      # 65 > 80 → 거짓
    print("위험")                   # (건너뜀 — 블록 안)
print("측정 완료")                  # → 측정 완료   (블록 밖 — 항상 실행)

# temp = 85 로 바꾸면?  →  위험 / 측정 완료  두 줄이 출력된다
temp = 85
if temp > 80:
    print("위험")                   # → 위험
print("측정 완료")                  # → 측정 완료


print()
print("========== [10] if-else ― 짝수/홀수 판정 ==========")

n = 14
if n % 2 == 0:                     # 2로 나눈 나머지가 0이면 짝수
    print("짝수")                   # → 짝수
else:
    print("홀수")

n = 7
if n % 2 == 0:
    print("짝수")
else:
    print("홀수")                   # → 홀수


print()
print("========== [11] if-elif-else ― 점수 등급 ==========")

score = 88
if score >= 90:                    # 높은 기준부터!
    print("A")
elif score >= 80:                  # 88 >= 80 → 참
    print("B")                     # → B
elif score >= 70:
    print("C")
else:
    print("F")

# 넓은 조건(예: score >= 60)을 맨 위에 두면?
#   95점도 60 이상이라 첫 조건에서 걸려버려, 아래의 A/B 판정에 영영 도달하지 못한다.
#   오류도 나지 않고 결과만 틀리므로 발견하기 어렵다.
#   → 좁고 까다로운 조건(높은 기준)을 위에, 넓은 조건을 아래에!


print()
print("========== [12] 범위 조건과 or ==========")

temp = 55
pressure = 7.5

if 20 <= temp <= 60:               # (1) 연쇄 비교 (= temp >= 20 and temp <= 60)
    print("정상 범위")              # → 정상 범위
else:
    print("범위 벗어남")

if temp > 60 or pressure > 7:      # (2) 하나라도 기준을 넘으면
    print("점검 필요")              # → 점검 필요   (압력 7.5 > 7)


print()
print("========== [도전] 측정 데이터 정리와 판정 리포트 ==========")

temps = [24, 26, 25, 999, 27, 92]

# (1) 이상값 제거
if 999 in temps:
    temps.remove(999)
print(temps)                       # → [24, 26, 25, 27, 92]

# (2) 최근 측정값 — 정렬하기 '전에' 꺼내 둔다!
last = temps[-1]
print(last)                        # → 92

# (3) 판정 결과를 변수에 저장
if last > 80:
    level = "위험"
elif last > 60:
    level = "주의"
else:
    level = "정상"
print(level)                       # → 위험

# (4) 정렬 후 최소·최대
temps.sort()
print(temps)                       # → [24, 25, 26, 27, 92]
low = temps[0]
high = temps[-1]

# (5) f-string 리포트
print()
print("=" * 30)
print("측정 데이터 리포트")
print(f"측정 개수 : {len(temps)}개")
print(f"최소 / 최대 : {low}도 / {high}도")
print(f"최근 측정 : {last}도 ({level})")
print("=" * 30)

# → ==============================
# → 측정 데이터 리포트
# → 측정 개수 : 5개
# → 최소 / 최대 : 24도 / 92도
# → 최근 측정 : 92도 (위험)
# → ==============================


print()
print("정답 확인 완료 - 틀린 문제는 해당 단원 파일을 다시 보세요")
