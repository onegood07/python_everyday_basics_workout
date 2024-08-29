# 09. 처음과 마지막 요소 찾기

# 함수 - 시퀀스(리스트, 튜플, 문자열)을 입력받아 처음과 마지막 요소를 추출하고 둘을 결합해 원래 시퀀스로 리턴하는 함수
def firstlast(sequence):
    return sequence[:1] + sequence[-1:] # 어떤 시퀀스가 들어올지 모르고 원래 형태를 유지하기 위해 '추출'이 아니라 '슬라이싱'을 사용함

# 실행
print(firstlast([100, 200, 300])) # 리스트
print(firstlast((12, 34, 56, 78))) # 튜플
print(firstlast('sequence')) # 문자열


# 함수 - 숫자로 구성된 리스트 또는 튜플을 매개변수로 받아 [홀수인_숫자의_합, 짝수인_숫자의_합] 형태의 리스트를 리턴하는 함수
def even_odd_sum(input_ints):
    output_even_odd_sum = [0, 0]
    
    for one_int in input_ints:
        if one_int % 2 == 0: # 짝수일 때
            output_even_odd_sum[1] += one_int
        else:
            output_even_odd_sum[0] += one_int
    
    return output_even_odd_sum

# 실행
print(even_odd_sum([11, 22, 33, 44]))
