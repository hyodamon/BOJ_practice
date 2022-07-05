import opcode
from pickletools import OpcodeInfo
import sys
from collections import deque

opcodes = {'ADD' : '00000', 'ADDC' : '00001',
'SUB' : '00010',
'SUBC' : '00011',
'MOV' : '00100',
'MOVC' : '00101',
'AND' : '00110',
'ANDC' : '00111',
'OR' : '01000',
'ORC' : '01001',
'NOT' : '01010',
'MULT' : '01100',
'MULTC' : '01101',
'LSFTL' : '01110',
'LSFTLC' : '01111',
'LSFTR' : '10000',
'LSFTRC' : '10001',
'ASFTR' : '10010',
'ASFTRC' : '10011',
'RL' : '10100',
'RLC' : '10101',
'RR' : '10110',
'RRC' : '10111'}


def toBin(n) :
    bin = ''
    while n > 0 :
        bin += str(n % 2)
        n //= 2
    return bin[::-1]

N = int(sys.stdin.readline())
for _ in range(N) :
    command = list(sys.stdin.readline().split())
    opcode = opcodes[command[0]]
    
    rD = toBin(int(command[1]))
    
    if opcode == 'MOV' or opcode == 'MOVC' or opcode == 'NOT' :
        rA = '000'
    else :
        rA = toBin(int(command[2]))
    print(opcode, rD.zfill(3), rA.zfill(3))
    
    if command[0][-1] == 'C' :
        C = toBin(int(command[3]))
        print("%s0%s%s%s"%(opcode, rD.zfill(3), rA.zfill(3), C.zfill(4)))
    else :
        rB = toBin(int(command[3]))
        print("%s0%s%s%s0"%(opcode, rD.zfill(3), rA.zfill(3), rB.zfill(3)))