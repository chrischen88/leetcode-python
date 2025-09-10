def myAtoi(s: str) -> int:
    if len(s) == 0:
        return 0
    idx = 0
    is_negative = False
    final_num = 0
    # Check for leading white space
    while s[idx] == ' ':
        idx += 1
        if idx >= len(s): return 0
    # Check for signedness
    if s[idx] == '-':
        is_negative = True
        idx += 1
    elif s[idx] == '+':
        idx += 1
    # Check for digits
    while idx < len(s):
        if s[idx] >= '0' and s[idx] <= '9':
            final_num = final_num * 10 + int(s[idx])
            idx += 1
        else: break
    # Check number within integer range
    print(is_negative)
    print(final_num, pow(2,31))
    if is_negative and final_num > pow(2, 31):
        return -pow(2,31)
    elif not is_negative and final_num >= pow(2,31):
        return pow(2,31)-1
    else:
        return final_num if not is_negative else -final_num
    
if __name__ == '__main__':
    print(myAtoi("-2147483648"))