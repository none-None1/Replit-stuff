from random import *
import sys
"""
1 Interpreter
Supports 4 dialects
for specification of the esolang, please see https://esolangs.org/wiki/1
"""
def pop(stack):
    if not stack:
        return randint(0,255)
    else:
        return stack.pop()
def top(stack):
    if not stack:
        return randint(0,255)
    else:
        return stack[-1]
def pop_pure1(stack):
    if not stack:
        raise SyntaxError('empty stack')
    else:
        return stack.pop()
def top_pure1(stack):
    if not stack:
        raise SyntaxError('empty stack')
    else:
        return stack[-1]
def inputdecimal():
    try:
        return int(input())
    except:
        return 0
def inputcharacter():
    c=sys.stdin.read(1)
    if c:
        return ord(c)
    else:
        return 0
def mod(x,y):
    return x%y if y else 0
def common1(code):
    brac=[]
    matches={}
    tape=[0]*1000000
    for i,j in enumerate(code):
        if j=='[':
            brac.append(i)
        if j==']':
            m=brac.pop()
            matches[m]=i
            matches[i]=m
    stack=[]
    ip=0
    while ip<len(code):
        cmd=code[ip]
        if cmd=='*':
            a,b,c=pop(stack),pop(stack),pop(stack)
            d=[a+b,a-b,a*b,mod(a,b)]
            stack.append(d[c%4])
        elif cmd==',':
            a,b=pop(stack),['print(chr(pop(stack)),end="")','print(pop(stack))','stack.append(inputcharacter())','stack.append(inputdecimal())']
            eval(b[a%4])
        elif cmd=='_':
            stack.append(randint(0,255))
        elif cmd=='[':
            if not top(stack):
                ip=matches[ip]
        elif cmd==']':
            if top(stack):
                ip=matches[ip]
        elif cmd=='1':
            stack.append(1)
        else:
            stack.append(ord(cmd))
        ip+=1
def adv1(code):
    brac=[]
    matches={}
    tape=[0]*1000000
    for i,j in enumerate(code):
        if j=='[':
            brac.append(i)
        if j==']':
            m=brac.pop()
            matches[m]=i
            matches[i]=m
    stack=[]
    ip=0
    while ip<len(code):
        cmd=code[ip]
        if cmd=='*':
            a,b,c=pop(stack),pop(stack),pop(stack)
            d=[a+b,a-b,a*b,mod(a,b)]
            stack.append(d[c%4])
        elif cmd==',':
            a,b=pop(stack),['print(chr(pop(stack)),end="")','print(pop(stack))','stack.append(inputcharacter())','stack.append(inputdecimal())']
            eval(b[a%4])
        elif cmd=='_':
            stack.append(randint(0,255))
        elif cmd=='[':
            if not top(stack):
                ip=matches[ip]
        elif cmd==']':
            if top(stack):
                ip=matches[ip]
        elif cmd=='1':
            stack.append(1)
        else:
            raise SyntaxError('Unknown character')
        ip+=1
def pure1(code):
    brac=[]
    matches={}
    tape=[0]*1000000
    for i,j in enumerate(code):
        if j=='[':
            brac.append(i)
        if j==']':
            m=brac.pop()
            matches[m]=i
            matches[i]=m
    stack=[]
    ip=0
    while ip<len(code):
        cmd=code[ip]
        if cmd=='*':
            a,b,c=pop_pure1(stack),pop_pure1(stack),pop_pure1(stack)
            d=[a+b,a-b,a*b,mod(a,b)]
            stack.append(d[c%4])
        elif cmd==',':
            a,b=pop(stack),['print(chr(pop(stack)),end="")','print(pop(stack))','stack.append(inputcharacter())','stack.append(inputdecimal())']
            eval(b[a%4])
        elif cmd=='[':
            if not top_pure1(stack):
                ip=matches[ip]
        elif cmd==']':
            if top(stack):
                ip=matches[ip]
        elif cmd=='1':
            stack.append(1)
        else:
            raise SyntaxError('Unknown character')
        ip+=1
def dead1(code):
    brac=[]
    matches={}
    tape=[0]*1000000
    for i,j in enumerate(code):
        if j=='[':
            brac.append(i)
        if j==']':
            m=brac.pop()
            matches[m]=i
            matches[i]=m
    stack=[]
    ip=0
    while ip<len(code):
        cmd=code[ip]
        if cmd=='*':
            x=pop_pure1(stack)
            if x%8<4:
                a,b=pop_pure1(stack),pop_pure1(stack)
                d=[a+b,a-b,a*b,mod(a,b)]
                stack.append(d[x%4])
            else:
                d=['print(chr(pop(stack)),end="")','print(pop(stack))','stack.append(inputcharacter())','stack.append(inputdecimal())']
                eval(d[x%4])
        elif cmd=='[':
            if not top_pure1(stack):
                ip=matches[ip]
        elif cmd==']':
            if top(stack):
                ip=matches[ip]
        elif cmd=='1':
            stack.append(1)
        else:
            raise SyntaxError('Unknown character')
        ip+=1
dia=input('1 interpreter\nChoose dialect:\n\t1: Common1\n\t2: Advanced1\n\t3: Pure1\n\t4: Dead1\n')
[common1,adv1,pure1,dead1][int(dia)-1](input('Please enter some {} code: '.format(['Common1','Advanced1','Pure1','Dead1'][int(dia)-1])))
