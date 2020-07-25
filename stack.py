def correctbracket(expression):
    stack=[]
    for element in expression:
        if element in ['(','[','{']:
            stack.append(element)
        else:
            if stack == []:
                return False
            else:
                current_element = stack.pop()
                if current_element == '(':
                    if element != ')':
                        return False
                if current_element == '[':
                    if element != ']':
                        return False
                if current_element == '{':
                    if element != '}':
                        return False
    return(stack==[])

print(correctbracket('()()[]{()}'))