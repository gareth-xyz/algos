# Array represents an integer
# Return the number incremented by one
# e.g.[1,2,3] return [124]

def plus_one(digits):
    n = 1
    if digits[-n] != 9:
        digits[-n] += 1
        return digits

    while n <= len(digits):    
        if digits[-n] == 9:
            digits[-n] = 0
            if n == len(digits):
                digits.insert(0, 1)
                break
            n += 1
        else:
            digits[-n] += 1
            break

    return digits

if __name__ == '__main__':
    print(plus_one( [1,2,3,9,9,9,9] ))