def get_summ(one, two, delimiter='&'):
    return(f'{one.upper()}{delimiter}{two.upper()}')
print(get_summ('Learn','python'))