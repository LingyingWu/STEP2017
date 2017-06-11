def readNumber(line, index):
    number = 0.0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def readMul(line, index):
    token = {'type': 'MUL'}
    return token, index + 1


def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1


def readLeftPar(line, index):
    token = {'type': 'LPAR'}
    return token, index + 1


def readRightPar(line, index):
    token = {'type': 'RPAR'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index] == ' ': # ignore space between numbers and operators
            index += 1
        
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == 'x':
            (token, index) = readMul(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        elif line[index] == '(':
            (token, index) = readLeftPar(line, index)
        elif line[index] == ')':
            (token, index) = readRightPar(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def calculate(tokens):
    answer = 0.0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1

    # Part 1: first deal with multiplication and division
    while index < len(tokens):
        if tokens[index]['type'] in {'MUL','DIV'}:
            temp = 0
            if tokens[index]['type'] == 'MUL':
                temp = tokens[index - 1]['number'] * tokens[index + 1]['number']
            elif tokens[index]['type'] == 'DIV':
                temp = tokens[index - 1]['number'] / tokens[index + 1]['number']
            tokens[index-1:index+2] = [{'type': "NUMBER", 'number': temp}]
        index += 1

    # Part 2: deal with addition and subtraction
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax: '
        index += 1

    return answer


def evaluate(tokens):
    tokens_new = []
    index = 0
    leftP = []

    # calculate the values inside the parentheses first
    while index < len(tokens):
        item = tokens[index]
        if item['type'] == 'LPAR':
            leftP.append(index)
        elif leftP == []:
            tokens_new.append(item)
        elif item['type'] == 'RPAR':
            left = leftP.pop()
            if len(leftP) > 0:
                tokens[left:index+1] = [{'type': "NUMBER", 'number': calculate(tokens[left+1:index])}]
                index -= index-left            
            else:
                calculate(tokens[left+1:index])
                tokens_new.append({'type': 'NUMBER','number': calculate(tokens[left+1:index])})
        index += 1

    return calculate(tokens_new)


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("1",1)
    test("1+2", 3)
    test("1 +2", 3)
    test("1+ 2", 3)
    test("1 + 2 - 4", -1)
    test("1.0+2.1-3", 0.1)
    test("1x2+3/4",2.75)
    test("1.2x3-4/5.0",2.8)

    test("3x(1+2)",9)
    test("3.0x(1+2)-4/(10-8.0)",7)
    test("20/(2x(5-3))",5)
    test("16/( (2+8)-(7-1) )",4)
    print "==== Test finished! ====\n"

runTest()

print 'Enter \'quit\' to exit the program.'
while True:
    print '> ',
    line = raw_input()
    if line == 'quit':
        break
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer