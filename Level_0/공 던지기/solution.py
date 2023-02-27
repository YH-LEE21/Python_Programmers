def ball_throw(numbers, k):
    answer = numbers[0::2] if len(numbers)%2==0 else numbers[0::2]+numbers[1::2]
    return answer[k%len(answer)-1]

print(ball_throw([1, 2, 3, 4]  ,2))
print(ball_throw([1, 2, 3, 4, 5, 6]  ,5))
print(ball_throw([1, 2, 3]  ,3))
