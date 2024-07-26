def reverse_complementing(string):
    warning_issued = False
    new_string = []
    accepted_nucleotides = ("A", "C", "T", "G")
    replacments = {"A":"T", "G":"C", "T":"A", "C":"G"}
    invalid_count = 0
    for e in string:
        if e in accepted_nucleotides:
            new_string.append(replacments[e])

        else:
            print(f"warning: invalid character {e}")
            invalid_count += 1

            if invalid_count > 4:
                print(f"Warning: five invalid characters found. Function stops now")
                new_string.reverse()
                result = "".join(new_string)
                return result
    new_string.reverse()
    result = "".join(new_string)
    return result


print(reverse_complementing("AATGUC"))
