#문자열 실습
#내장함수 : 파이썬 안에 자체적으로 내장되어 있는 함수

#문자열 덧셈
str1 = "멋쟁이 사자처럼"
str2 = "은 좋은 동아리입니다."
print(str1 + str2)

#문자열 곱셈
print(str1 * 3)

#문자열의 인덱싱
# print(str1[4])
# print(str2[5])

#문자열의 슬라이싱
# print(str1[0:3])

#1_문자열의 길이를 구하는 내장함수 : len(문자열)
print(len(str1))

#2_문자열 내에서 특정 문자의 등장 횟수를 반환하는 내장함수 : 문자열변수.count('특수문자')
str3 = "멋쟁이 사자처럼은 사랑스러워"
print(str3.count('사'))

#3_문자열을 (특정 기준으로) 나누는 내장함수: 문자열변수.split()
print(str3.split())

str4 = "사과,바나나,포도"
print(str4.split(','))

#4_특정 문자 인덱스를 찾아주는 내장함수: find('문장'), index('문장')
print("find: ", str3.find('사'))
print("index: ", str3.index('사'))

#find와 index의 차이점
#오류 발생 시 find는 -1을 반환, index는 ValueError라는 오류를 발생시킴
print("find: ", str3.find('무'))
# print("index: ", str3.index('무'))