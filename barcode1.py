import cv2, numpy as np, math

a = cv2.imread('b6.jpg',0)
a = cv2.resize(a,(440,341))

r,c = a.shape
img = cv2.Canny(a,50,100)

xm = int(r/2)
width = []
tmp = 0
for j in range(c):
    if img[xm,j] == 255:
        width.append(j-tmp)
        tmp=j

width = np.array(width[1:])
width[width==9] = 8
width = np.vectorize(math.ceil)((width/4))
width = width[3:len(width)-3]
width = np.concatenate((width[:24] , width[29:]) , 0)

enc = [
    'LLLLLL',
    'LLGLGG',
    'LLGGLG',
    'LLGGGL',
    'LGLLGG',
    'LGGLLG',
    'LGGGLL',
    'LGLGLG',
    'LGLGGL',
    'LGGLGL'
]

lgr = [
    {
        "L" : "0001101",
        "G" : "0100111",
        "R" : "1110010",
    },

    {
        "L" : "0011001",
        "G" : "0110011",
        "R" : "1100110",
    },

    {
        "L" : "0010011",
        "G" : "0011011",
        "R" : "1101100",
    },

    {
        "L" : "0111101",
        "G" : "0100001",
        "R" : "1000010",
    },

    {
        "L" : "0100011",
        "G" : "0011101",
        "R" : "1011100",
    },

    {
        "L" : "0110001",
        "G" : "0111001",
        "R" : "1001110",
    },

    {
        "L" : "0101111",
        "G" : "0000101",
        "R" : "1010000",
    },

    {
        "L" : "0111011",
        "G" : "0010001",
        "R" : "1000100",
    },

    {
        "L" : "0110111",
        "G" : "0001001",
        "R" : "1001000",
    },

    {
        "L" : "0001011",
        "G" : "0010111",
        "R" : "1110100",
    },
]

cnt = 0
f_num=ans=""
for i in range(0,len(width),4):
    string=""

    if i<24:
        for k in range(4):
            for l in range(width[i + k]):
                if k % 2:
                    string += "1"
                else:
                    string += "0"

        for j,l in enumerate(lgr):
            if l["L"] == string:
                ans+=str(j)
                f_num+="L"

            elif l["G"] == string:
                ans+=str(j)
                f_num+="G"

            elif l["R"] == string:
                ans+=str(j)
                f_num+="R"


    else:
        for k in range(4):
            for l in range(width[i + k]):
                if k % 2:
                    string += "0"
                else:
                    string += "1"

        for j, l in enumerate(lgr):
            if l["R"] == string:
                ans+=str(j)
    cnt+=1

ans = str(enc.index(f_num)) + ans
print(ans)