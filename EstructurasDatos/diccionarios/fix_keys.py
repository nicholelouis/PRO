# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    # TU CÓDIGO AQUÍ
    fitems = {k.replace(' ', '') : v for k, v in items.items()}

    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})