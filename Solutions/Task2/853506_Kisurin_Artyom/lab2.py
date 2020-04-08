import tempfile


def len_of_file(filename):
    i = 0
    with open(filename) as f:
        for lines in f:
            i += 1
        f.close()
    return i


def get_line(filename, num):
    i = 0
    with open(filename, 'r', encoding='utf-8') as file1:
        for line in file1:
            if i == int(num):
                return line
            i += 1
        file1.close()


def change_line_infile(filename1, num, str1):
    i = 0
    temp = tempfile.NamedTemporaryFile
    with open(filename1, 'r') as file1:
        with open(temp.__name__, 'w') as file2:
            for lines in file1:
                if i == num:
                    file2.write(str1)
                else:
                    file2.write(lines)
                i += 1
            file1.close()
            file2.close()
    with open(filename1, 'w') as file1:
        with open(temp.__name__, 'r') as file2:
            for lines in file2:
                file1.write(lines)
            file1.close()
            file2.close()


def set_value(filename1, filename2, num1, num2):
    j = 0
    str2 = ""
    with open(filename2, 'r') as file2:
        for lines in file2:
            if j == num2:
                str2 = lines
            j += 1
        file2.close()
    change_line_infile(filename1, num1, str2)


def merge(my_file):
    cur_len = len_of_file(my_file)
    if cur_len > 1:
        mid = cur_len // 2
        L = tempfile.TemporaryFile(delete=False)
        R = tempfile.TemporaryFile(delete=False)
        i = 1
        with open(my_file, 'r', encoding='utf-8') as g:
            with open(L.name, 'w', encoding='utf-8') as L:
                with open(R.name, 'w', encoding='utf-8') as R:
                    for line in g:
                        if i <= mid:
                            L.write(line)
                        else:
                            R.write(line)
                        i += 1
                    L.close()
                    R.close()
                    g.close()
        merge(L.name)
        merge(R.name)
        i = j = k = 0
        while i < len_of_file(L.name) and j < len_of_file(R.name):
            if float(get_line(L.name, i)) < float(get_line(R.name, j)):
                set_value(my_file, L.name, k, i)
                i += 1
            else:
                set_value(my_file, R.name, k, j)
                j += 1
            k += 1
        while i < len_of_file(L.name):
            set_value(my_file, L.name, k, i)
            i += 1
            k += 1
        while j < len_of_file(R.name):
            set_value(my_file, R.name, k, j)
            j += 1
            k += 1


if __name__ == "__main__":
    print("Start sort...")
    merge("nums.txt")
    print("Sort completed")
