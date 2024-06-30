def is_good_password(string):
    if len(string) >= 9 and string.lower() != string and not string.isalpha():
        return True
    else:
        return False


print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))
