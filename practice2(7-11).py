# 함수
def open_account() :
    print("새로운 계좌가 생성되었습니다.")
open_account()

# 전달값과 반환값
def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money) : # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money) : # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance , 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 기본값
def profile(name, age, main_lang) :
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬") :
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))
profile("유재석")
profile("김태호")

# 키워드 값
def profile(name, age, main_lang) :
    print(name, age, main_lang)
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language) :
    print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수와 전역변수
gun = 10
def checkpoint(soldiers) : # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# Quiz 6) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

#  조건 1 : 표준 체중은 별도의 함수 내에서 계산
#           * 함수명 : std_weight
#           * 전달값 : 키(height) , 성별 (gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender) :
    if gender == "남자" :
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100,gender), 2)
print("키 {0}cm {1}남자의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# 표준 입출력
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items() :
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4))
# ljust(숫자) : 숫자만큼의 공간을 확보하고 왼쪽 정렬
# rjust(숫자) : 숫자만큼의 공간을 확보하고 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ....
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3))
# zfill(숫자) : 숫자만큼의 공간을 확보하고 나머지 빈 공간만큼은 0으로 채운다

# 사용자 입력을 통해서 입력을 받으면 항상 문자열 형태로 받는다
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 때는  +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >-10}".format(500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000000000))
print("{0:-,}".format(10000000000000))

# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수까지만 표시 (소수점 셋째자리에서 반올림)
print("{0:.2f}".format(5/3))

# 파일 입출력

score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a는 append => 추가
score_file.write("과학: 80")
score_file.write("\n코딩: 100") # write에는 줄바꿈이 없음. 따라서, \n을 사용해서 줄 바꿈을 해줘야함
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True :
    line = score_file.readline()
    if not line :
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines :
    print(line, end="")
score_file.close()

# pickle

# import pickle
# profile_file = open("profile.pickle", "wb") #b는 binary
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with
import pickle
with open("profile.pickle", "rb") as profile_file :
    print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as sutdy_file :
#     sutdy_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r", encoding="utf8") as study_file :
    print(study_file.read())

# Quiz 7) 
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로  출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# for i in range(1, 51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file :
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")

# 클래스

from random import *

# 일반 유닛
class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name # 멤버변수
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다".format(self.name))

# 메소드
# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit) :
    def __init__(self) :
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 공격 속도를 증가, 체력 10 감소
    def stimpack(self) :
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit) :
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self) :
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self) :
        if Tank.seize_developed == False :
            return 
        
        # 현재 시즈모드 아닐 때 => 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 => 시즈모드 해제
        else :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

    # def damaged(self, damage) :
    #     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    #     self.hp -= damage
    #     print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
    #     if self.hp <= 0 :
    #         print("{0} : 파괴되었습니다".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
    
    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 다중 상속
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location) :
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit) :
    def __init__(self) :
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)
    
    def clocking(self) :
        if self.clocked == True : # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else : # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start() :
    print("[알림] 새로운 게임을 시작합니다.")

def game_over() :
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2개 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units :
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린:스팀팩 , 탱크:시즈모드 , 레이스:클로킹)
for unit in attack_units :
    if isinstance(unit, Marine) :
        unit.stimpack()
    elif isinstance(unit, Tank) :
        unit.set_seize_mode()
    elif isinstance(unit, Wraith) :
        unit.clocking()

# 전군 공격
for unit in attack_units :
    unit.attack("1시")

# 전군 피해
for unit in attack_units :
    unit.damaged(randint(5, 21)) # 공격을 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()

# # 연산자 오버로딩
# # 벌쳐 : 지상 유닛 , 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛. 체력도 굉장히 좋음, 공력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# super
# 건물
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location) :
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # super를 쓸 때는 super()라고 쓰고, self를 쓰지 않는다
#         self.location = location        

class Unit :
    def __init__(self) :
        print("Unit 생성자")

class Flyable :
    def __init__(self) :
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable) :
    def __init__(self) :
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

# Quiz 8)
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# 코드
class House :
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year) :
       self.location = location
       self.house_type = house_type
       self.deal_type = deal_type
       self.price = price
       self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3=  House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print ("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses :
    house.show_detail()

# 예외처리
# try :
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError :
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError :
#     print(err)
# except Exception as err:
#     print("알 수 없는 오류가 발생하였습니다.")
#     print(err)

# try :
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10 :
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError :
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")

# 사용자 정의 예외처리
# class BigNumberError(Exception) :
#     def __init__(self, msg) :
#         self.msg = msg

#     def __str__(self) :
#         return self.msg

# try :
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10 :
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError :
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally :
#     print("계산기를 이용해 주셔서 감사합니다.")

# Quiz 9)
# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건 1 : 1보다 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#          출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#          치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#          출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
# class SoldOutError(Exception) :
#     pass

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# while (True) :
#     try :  
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken : # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0 :
#             raise ValueError
#         else :
#             print("[대기번호 {0}] {1} 미리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
            
#         if chicken == 0 :
#             raise SoldOutError

#     except ValueError :
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError :
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조할인 영화를 보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화를 보러 갔을 때

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)

# from theater_module import price_soldier as price
# price(5)

# 패키지
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__
# from random import *
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 외장 함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder) :
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else :
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d-%H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일 되는 날은 ", today + td) # 오늘부터 100일 후

# Quiz 10)
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모든 파일명은 byme.py로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 김수진에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : alicekim0429@naver.com

import byme
byme.sign()