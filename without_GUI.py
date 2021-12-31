import time

user_input = int(input("Please input how many plates you want to test"))

towerA=[]
towerB=[]
towerC=[]

for x in range(user_input):
    towerA.append(x + 1)
towerA.sort(reverse=True)
start = time.perf_counter()
def hanoi(plates, start, temp, goal):
    if plates > 0:
        hanoi(plates - 1, start, goal, temp)
        goal.append(start.pop())
        print(f' Tower A {start}')
        print(f' Tower B {temp}')
        print(f' Tower C {goal}')
        print("------------------")
        hanoi(plates - 1, temp, start, goal)

hanoi(user_input, towerA, towerB, towerC)

end = time.perf_counter()
final_result = end - start

print(f'Time: ->  {final_result}')