


def transcription(string):
    warning_issued = False
    new_string = []
    accepted_nucleotides = ("A", "C", "T", "G")
    invalid_count = 0
    for e in string:
        if e == "T":
            new_string.append("U")
        
        elif e in accepted_nucleotides:
            new_string.append(e)

        if e not in accepted_nucleotides:
            print(f"warning: invalid character {e}")
            invalid_count += 1

            if invalid_count > 4:
                print(f"Warning: five invalid characters found. Function stops now")
                result = "".join(new_string)
                return result
    
    result = "".join(new_string)
    return result

print(transcription("AAATCH...TI"))


# super simpel sulution

def transcription_simple(string):
    transcribed = string.replace("T", "U")
    return transcribed