# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    l = []
    with open(name) as f:
        for line in f:
            l.append(line)
    first_line = l[0].split(" ")
    time_diff, errors_num = int(first_line[0]), int(first_line[1])
    l.pop(0)

    errors = []

    class Error:
        def __init__(self, dt):
            self.dt = dt

    for line in l:

        splitted = line.split(" ")
        status = splitted[2]
        if status != 'ERROR':
            continue
        date = splitted[0][1:]
        time = splitted[1][:-1]
        dt = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M:%S')

        errors.append(Error(dt))
        # 'Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        diff = (dt - errors[0].dt).total_seconds()

        while diff >= time_diff:
            errors.pop(0)
            diff = (dt - errors[0].dt).total_seconds()
        if len(errors) >= errors_num:
            print(dt)
            exit()
    print(-1)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
