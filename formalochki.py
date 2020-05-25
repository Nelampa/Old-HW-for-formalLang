#������������� � ��������� ������������ ������� ��� ���� �������
def partlyConcats(a, b, stack):
    concat = a[0] + b[0]
    maxpref = a[1] + b[1] if len(a[0]) == a[1] else a[1]
    stack.append([concat, maxpref])

def starForList(a):
    res = [['', 0]]
    res.extend(a) 
    for word in a:
          if len(word[0]) == word[1]: #����� �����, ��������� ������ �� ������ ����
               for i in range(prefLen // word[1] + 1):
                    res.append([i * word[0], i * word[1]])
                    for word2 in a:
                        if i * word[1] + word2[1] <= prefLen:
                            res.append([i * word[0] + word2[0], i * word[1] + word2[1]])
    stack.append(res)

#The Truth is horrible...
def trueSum(stack):
    b, a = stack.pop(), stack.pop()
    #����� ���� ������ -- ����
    if type(a[0]) == list and type(b[0]) == list: 
        a.extend(b)
        stack.append(a)
    #����� ����� � �������� 
    elif type(a[0]) == list:
        a.append(b)
        stack.append(a)
    elif type(b[0]) == list:
        b.append(a)
        stack.append(b)
    #���� ���������� letter � �������� ���������, �� ���� ���������� �����
    elif a[1] == b[1]:
        stack.append(a if len(a[0]) < len(b[0]) else b)
    #� ������ �� ���� ��� x � ������
    #���� ��� ����� ����������, ��������� ���, ��� ����� ��� �����������!
    elif a[1] == 0 and len(b[0]) <= len(a[0]):
        stack.append(b)
    elif b[1] == 0 and len(a[0]) <= len(b[0]):
        stack.append(a)
    else:
        stack.append([a, b])
    return stack

def trueConcats(stack):
    b, a = stack.pop(), stack.pop()
    if type(a[0]) == list and type(b[0]) == list:
        for word1 in a:
            for word2 in b:
                partlyConcats(word1, word2, stack)
    elif type(a[0]) == list:
        for word in a:
            partlyConcats(word, b, stack)
    elif type(b[0]) == list:
        for word in b:
            partlyConcats(a, word, stack)
    else:
        partlyConcats(a, b, stack)
    return stack

def trueStar(stack):
    a = stack.pop()
    if type(a[0]) != list:
        #���� �������� ��� ����������� (�� �������� x � ������), ����� ��� ����� ����������
        if a[1] == 0:
            stack.append(['', 0])
        #�������� ��������� ������� �� letter -- ����� ����� ��� ������� ������ ���!
        #(�� �� ����� prefLen)
        elif len(a[0]) == a[1]:
            res = []
            for i in range(prefLen // a[1] + 1):
                res.append([i * a[0], i * a[1]])
            stack.append(res)
        #�������� ����� ��������� ����� �������� � � ������
        #��� ��� ��������� ���� � ������, ����� ��� ����� �������� � ����� (�.�. �� ����� ������ ����)
        else:
            res = [['', 0], a]
            stack.append(res)
    #��� ���������� ��� ������ �� �����?
    #��� ��������� ���������� ���� � ��������������� ������ �������� �� �
    #������� ������������� �� ����, ��������� ������ �� �
    else:
        starForList(a)
    return stack

def operations(s, letter, prefLen):
    oper = '+.*'
    stack = []
    enoughOper = 1
    for i in s:
        if i not in oper:
            if i == '1':
                i = ''
            stack.append([i, 1 if i == letter else 0])
            enoughOper -= 1
        elif i == '+':
            enoughOper += 1
            trueSum(stack)
        elif i == '.':
            enoughOper += 1
            trueConcats(stack)
        elif i == '*':
            trueStar(stack)
    return stack, enoughOper

def f(s, letter, prefLen):
    enoughOper = 1
    stack, enoughOper = operations(s, letter, prefLen)
    reslen = 'INF'
    for i in stack:
        if enoughOper != 0:
            reslen = 'ERROR'
        elif type(i[0]) == list:
            for j in i:
                if j[1] >= prefLen and (reslen == 'INF' or len(j[0]) < reslen):
                    reslen = len(j[0])
        elif i[1] >= prefLen and (reslen == 'INF' or len(i[0]) < reslen):
            reslen = len(i[0])
    return reslen


pshe, letter, prefLen = input().split()
prefLen = int(prefLen)
try:
    print(f(pshe, letter, prefLen))
except:
    print('ERROR')