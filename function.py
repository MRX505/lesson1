def get_summ(one, two, delimiter="&"):
    result = one.upper() + delimiter + two.capitalize()
    return result

print(get_summ("learn", "python", delimiter="1"))