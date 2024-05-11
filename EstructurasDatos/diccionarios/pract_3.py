rsum = []
with open(data_path) as f:
    for line in f:
        row_numbers = []
        stripped_line = line.strip().split()
        for number in stripped_line:
            row_numbers.append(int(number))
        line_sum = sum(row_numbers)
        rsum.append(line_sum)
    rsum = tuple(rsum)
