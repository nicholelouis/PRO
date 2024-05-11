# *********************
# VALOR MÁXIMO Y MÍNIMO
# *********************


def run(values: list) -> tuple:
    if len(values) == 1:
        max_value = min_value = values[0]
    else:
        max_value = 0
        min_value = 0
        for value in values:
            if value > max_value:
                max_value = value
            elif value < min_value:
                min_value = value

    return max_value, min_value


if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])