# if {([が来たら)}]をstack
# if )}]が来たら{([をpop
#最後に残ってたらFalse

def validate_format(chars: str) -> bool:
    stack = []
    lookup = {'{':'}','[':']','(':')'}

    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False

    if stack:
        return False

    return True

text ="{'1':['a'],'2':['b'],'1':['a']}"
print(validate_format(text))
