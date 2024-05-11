# **************
# HIPERFACTORIAL
# **************


def hyperfactorial(n: int) -> int:
    if n == 1:
        return 1
    return n ** n * hyperfactorial(n-1)

