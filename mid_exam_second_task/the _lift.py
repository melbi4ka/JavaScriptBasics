people = int(input())
current_state = list(map(int, input().split()))
all_people = people


for k in range(len(current_state)):

    if current_state[k] < 4:
        if all_people >= 4 - current_state[k]:
            all_people -= 4 - current_state[k]
            current_state[k] = 4

        else:
            current_state[k] += all_people
            all_people = 0

counter = current_state.count(4)
if all_people == 0 and counter == len(current_state):
    print(" ".join([str(x) for x in current_state]))

elif all_people == 0 and counter < len(current_state):
    print(f"The lift has empty spots!")
    print(f"{' '.join([str(x) for x in current_state])}")

elif all_people > 0 and counter == len(current_state):
    print(f"There isn't enough space! {all_people} people in a queue!\n"
          f"{' '.join([str(x) for x in current_state])}")


# print(people)
# print(current_state)
# print(counter)





