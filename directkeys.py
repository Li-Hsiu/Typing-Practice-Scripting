import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

Space = 0x039
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
Num0 = 0x52
Num1 = 0x4F
Num2 = 0x50
Num3 = 0x51
Num4 = 0x4B
Num5 = 0x4C
Num6 = 0x4D
Num7 = 0x47
Num8 = 0x48
Num9 = 0x49
NumDel = 0x53
NumAdd = 0x4E
Ctrl = 0x1D
Alt = 0x38
Enter = 0x1C
Shift = 0x36

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)

def PressCharacter(character):
    if character == 'a':
        PressKey(A)
        ReleaseKey(A)
    elif character == 'b':
        PressKey(B)
        ReleaseKey(B)
    elif character == 'c':
        PressKey(C)
        ReleaseKey(C)
    elif character == 'd':
        PressKey(D)
        ReleaseKey(D)
    elif character == 'e':
        PressKey(E)
        ReleaseKey(E)
    elif character == 'f':
        PressKey(F)
        ReleaseKey(F)
    elif character == 'g':
        PressKey(G)
        ReleaseKey(G)
    elif character == 'h':
        PressKey(H)
        ReleaseKey(H)
    elif character == 'i':
        PressKey(I)
        ReleaseKey(I)
    elif character == 'j':
        PressKey(J)
        ReleaseKey(J)
    elif character == 'k':
        PressKey(K)
        ReleaseKey(K)
    elif character == 'l':
        PressKey(L)
        ReleaseKey(L)
    elif character == 'm':
        PressKey(M)
        ReleaseKey(M)
    elif character == 'n':
        PressKey(N)
        ReleaseKey(N)
    elif character == 'o':
        PressKey(O)
        ReleaseKey(O)
    elif character == 'p':
        PressKey(P)
        ReleaseKey(P)
    elif character == 'q':
        PressKey(Q)
        ReleaseKey(Q)
    elif character == 'r':
        PressKey(R)
        ReleaseKey(R)
    elif character == 's':
        PressKey(S)
        ReleaseKey(S)
    elif character == 't':
        PressKey(T)
        ReleaseKey(T)
    elif character == 'u':
        PressKey(U)
        ReleaseKey(U)
    elif character == 'v':
        PressKey(V)
        ReleaseKey(V)
    elif character == 'w':
        PressKey(W)
        ReleaseKey(W)
    elif character == 'x':
        PressKey(X)
        ReleaseKey(X)
    elif character == 'y':
        PressKey(Y)
        ReleaseKey(Y)
    elif character == 'z':
        PressKey(Z)
        ReleaseKey(Z)
    elif character == 'A':
        PressKey(Shift)
        PressKey(A)
        ReleaseKey(A)
        ReleaseKey(Shift)
    elif character == 'B':
        PressKey(Shift)
        PressKey(B)
        ReleaseKey(B)
        ReleaseKey(Shift)
    elif character == 'C':
        PressKey(Shift)
        PressKey(C)
        ReleaseKey(C)
        ReleaseKey(Shift)
    elif character == 'D':
        PressKey(Shift)
        PressKey(D)
        ReleaseKey(D)
        ReleaseKey(Shift)
    elif character == 'E':
        PressKey(Shift)
        PressKey(E)
        ReleaseKey(E)
        ReleaseKey(Shift)
    elif character == 'F':
        PressKey(Shift)
        PressKey(F)
        ReleaseKey(F)
        ReleaseKey(Shift)
    elif character == 'G':
        PressKey(Shift)
        PressKey(G)
        ReleaseKey(G)
        ReleaseKey(Shift)
    elif character == 'H':
        PressKey(Shift)
        PressKey(H)
        ReleaseKey(H)
        ReleaseKey(Shift)
    elif character == 'I':
        PressKey(Shift)
        PressKey(I)
        ReleaseKey(I)
        ReleaseKey(Shift)
    elif character == 'J':
        PressKey(Shift)
        PressKey(J)
        ReleaseKey(J)
        ReleaseKey(Shift)
    elif character == 'K':
        PressKey(Shift)
        PressKey(K)
        ReleaseKey(K)
        ReleaseKey(Shift)
    elif character == 'L':
        PressKey(Shift)
        PressKey(L)
        ReleaseKey(L)
        ReleaseKey(Shift)
    elif character == 'M':
        PressKey(Shift)
        PressKey(M)
        ReleaseKey(M)
        ReleaseKey(Shift)
    elif character == 'N':
        PressKey(Shift)
        PressKey(N)
        ReleaseKey(N)
        ReleaseKey(Shift)
    elif character == 'O':
        PressKey(Shift)
        PressKey(O)
        ReleaseKey(O)
        ReleaseKey(Shift)
    elif character == 'P':
        PressKey(Shift)
        PressKey(P)
        ReleaseKey(P)
        ReleaseKey(Shift)
    elif character == 'Q':
        PressKey(Shift)
        PressKey(Q)
        ReleaseKey(Q)
        ReleaseKey(Shift)
    elif character == 'R':
        PressKey(Shift)
        PressKey(R)
        ReleaseKey(R)
        ReleaseKey(Shift)
    elif character == 'S':
        PressKey(Shift)
        PressKey(S)
        ReleaseKey(S)
        ReleaseKey(Shift)
    elif character == 'T':
        PressKey(Shift)
        PressKey(T)
        ReleaseKey(T)
        ReleaseKey(Shift)
    elif character == 'U':
        PressKey(Shift)
        PressKey(U)
        ReleaseKey(U)
        ReleaseKey(Shift)
    elif character == 'V':
        PressKey(Shift)
        PressKey(V)
        ReleaseKey(V)
        ReleaseKey(Shift)
    elif character == 'W':
        PressKey(Shift)
        PressKey(W)
        ReleaseKey(W)
        ReleaseKey(Shift)
    elif character == 'X':
        PressKey(Shift)
        PressKey(X)
        ReleaseKey(X)
        ReleaseKey(Shift)
    elif character == 'Y':
        PressKey(Shift)
        PressKey(Y)
        ReleaseKey(Y)
        ReleaseKey(Shift)
    elif character == 'Z':
        PressKey(Shift)
        PressKey(Z)
        ReleaseKey(Z)
        ReleaseKey(Shift)
    elif character == '-':
        PressKey(Space)
        ReleaseKey(Space)
    elif character == 'ctrl':
        PressKey(Ctrl)
        ReleaseKey(Ctrl)