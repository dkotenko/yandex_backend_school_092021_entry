# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.





def print_hi(name):
    f = open(name, 'r')
    n = int(f.readline())
    if n == 1:
        print(0)
        exit()

    answer = [0] * n
    m = []
    num = set()
    for _ in range(n):
        m.append(list(map(int, f.readline().split(" "))))


    for i in range(len(m)):
        value = 0
        for n in m[i]:
            if n == -1:
                continue
            value |= n
        answer[i] = value


    for i in range(len(answer) - 1):
        print(str(answer[i]) + ' ', end='')
    print(answer[-1])









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('input.txt')

