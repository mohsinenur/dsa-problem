T = int(input())

number_of_problem = []
computer_set = []

for n in range(T):
    number_of_problem.append(int(input()))

for computer in number_of_problem:
    first_computer = computer_set.count(computer)
    second_computer = computer - first_computer
    if computer > 10:
        first_computer = first_computer + (computer-10)
        second_computer = computer - first_computer

    if computer != 0:
        computer_set.append(computer)

    print(str(first_computer) + " " + str(second_computer))
