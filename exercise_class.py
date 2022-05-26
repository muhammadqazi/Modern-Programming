def display(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="\t")


def delStudent(filename, id):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if line[0:8] != id:
                f.write(line)


def main():
    display('students.txt')


if __name__ == '__main__':
    main()
