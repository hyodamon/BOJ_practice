from tkinter import SOLID


def solution(people, tshirts):
    answer = 0

    people.sort()
    tshirts.sort()
    print("people : ", people, "tshirts : ", tshirts)  

    for tshirt in tshirts :
        for person in people :
            if tshirt >= person :
                print("person : ", person, "tshirt : ", tshirt)  
                answer += 1
                people.remove(person)
                break

    return answer

print(solution([1, 3], [1, 1]))