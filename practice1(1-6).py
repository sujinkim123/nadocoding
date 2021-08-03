print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print("풍선")
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

# 변수
# 애완동물을 소개해주세요
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3
print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "이며, " + hobby + "을 아주 좋아해요")
print(name , "는 " , age , "이며, " , hobby , "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 주석
# 으로 시작하면 한 줄이 주석처리가 돼요
''' (작은따옴표 3개) 이렇게
하면
여러 문장이
주석처리가
됩니다 '''

# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : "사당" , "신도림" , "인천공항" 순서대로 입력
# 출력 문장 : XX행 열차가 들어오고 있습니다.
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2
print(2**3) # 2^3=8
print(5%3) # 나머지 2
print(10//3) # 몫 1
print(10//3) # 몫 3
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True
print(1 != 3) # True
print(not(1 != 3)) # False
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 5 # 1
print(number)

# 숫자 처리 함수
print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 4 * 4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 , 4
print(ceil(3.14)) # 올림 , 4
print(sqrt(16)) # 제곱근 , 4

# 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 미만의 임의의 값 생성

# Quiz 2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안항 최소 일수인 28 이내로 정함
# 조건 3 :  매월 1~3일은 스터디 준비를 해야 하므로 제외
# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매일 x일로 선정되었습니다.

# import random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매일 " + str(date) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연도 : " + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4]) # 2부터 4 직전까지 (2, 3)
print("일 : " + jumin[4:6]) # 4부터 6 직전까지 (4, 5)
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 (0, 1, 2, 3, 4, 5)
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로
print(python.upper()) # 모든 문자를 대문자로
print(python[0].isupper()) # 첫번째 문자가 대문자인가 => True
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java")) # Python 글자를 Java로 바꿈
index = python.index("n") # n 위치를 찾음 => 5
print(index)
index = python.index("n", index + 1) # 5+1=6번째부터 n을 찾음
print(index) # 15
print(python.find("Java")) # -1 => find : 찾고자 하는 값이 변수에 포함되어 있지 않을 경우 -1 반환
# print(python.index("Java")) # index : 찾고자 하는 값이 변수에 포함되어 있지 않을 경우 오류 발생
print(python.count("n")) # python 변수에 n이 몇 개 있는지 출력

# 문자열 포맷
# print("a" + "b")
# print("a", "b")
# 방법 1
print("나는 %d살입니다" % 20) # %d는 정수
print("나는 %s을 좋아해요" % "파이썬") # %s는 문자열
print("Apple은 %c로 시작해요" % "A") # %c는 문자
print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강"))
# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요
print("나는 {0}색과 {1}색을 좋아해요".format("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요
print("나는 {1}색과 {0}색을 좋아해요".format("파랑", "빨강")) # 나는 빨강색과 파랑색을 좋아해요
# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨강"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨강" , age=20))
# 방법 4 (v3.6 이상~)
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출 문자
print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈
print("저는 \"김수진\"입니다") # 저는 "김수진"입니다
print("저는 \'김수진\'입니다") # 저는 '김수진'입니다
print("C:\\python_youtube>") # C:\python_youtube>
print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동 => PineApple
print("Redd\bApple") # \b : 백스페이스 (한 글자 삭제) => RedApple
print("Red\tApple") # \t : 탭 => Red    Apple

# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver.com
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + '!'로 구성
#                  (nav)               (5)           (1)           (!)
# 예) 생성된 비밀번호 : nav51!
url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1
my_str = my_str[:my_str.index(".")] # my_str 문자열에서 .이 나오는 위치 직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))  

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)
# 조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호")) # 1
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)
# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") 
print(subway)
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
# 순서 뒤집기 가능
num_list.reverse()
print(num_list)
# 모두 지우기
num_list.clear()
print(num_list)
# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3:"유재석", 100:"김태호"} # 사전은 {} , key는 3, value는 유재석
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
print(cabinet.get(100))
# print(cabinet[5]) # key 값이 없음. 오류 발생, 프로그램 종료
# print("hi") # 윗줄에서 프로그램 종료가 되었기에 실행 X
print(cabinet.get(5)) # key 값이 없음. None 출력
print(cabinet.get(5, "사용 가능")) # key 값이 없음. "사용 가능" 출력
print("hi") # 실행 O
print(3 in cabinet) # True
print(5 in cabinet) # False
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호
# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # key A-3의 값에 "김종국"을 넣음 
cabinet["C-20"] = "조세호" # cabinet에 C-20 이라는 key를 만들고, 키 값에 "조세호"를 넣음
print(cabinet)
# 간 손님
del cabinet["A-3"]
print(cabinet)
# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())
# 목욕탕 폐점
cabinet.clear()
print(cabinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") # 오류 => 튜플은 add 라는 기능 제공 X
(name , age , hobby) = ("김종국" , 20 , "코딩")
print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}
java = {"유재석", "김태호", "양세형"} # set 정의
python = set(["유재석", "박명수"]) # set 정의
# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))
# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) 
print(java.difference(python))
# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)
# java를 잊어버렸어요
java.remove("김태호")
print(java)

# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

# Quiz 4) 
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다
# 추첨 프로그램을 작성하시오
# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle과 sample을 활용
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --
# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))
from random import *
id = range(1, 21) # 1부터 20까지 숫자를 생성
id = list(id)
print(id)
shuffle(id)
print(id)
winners = sample(id, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

# if
# 날씨
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어요")
# 기온
temp = int(input("기온은 어때요?"))
if temp >= 30 :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")
# for
for waiting_no in [0, 1, 2, 3, 4] :
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(5) : # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1, 6) : # 1, 2, 3, 4, 5
    print("대기번호 {0}".format(waiting_no))
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if (index == 0) :
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# while True :
#     print("{0}님, 커피가 준비되었습니다. 호출 {1}회.".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknown"

while (person != customer) :
    print("{0}님, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요? ")

# continue와 break
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11) : # 1부터 10번까지 
    if student in absent :
        continue
    elif student in no_book :
        print("오늘수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}야, 책을 읽어봐.".format(student))

# 한 줄 for
# 출석 번호 1 2 3 4 , 앞에 100을 붙이기로 함 => 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)
# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)
# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# Quiz 5
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [ ] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2 분
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51) : # 1에서 50까지의 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 사이의 소요시간
    if (5 <= time <= 15) : # 5분 ~ 15분 이내의 손님 , 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else : # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))
