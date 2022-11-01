class convertor():
    def __init__(self) -> None:
        pass

    def dectobin(self, num:str):
        for i in str(num):
            if i not in '1234567890.':
                return 'Please choose appropriate data type'
        a = int(float(num))
        b = str(num%1)
        #int

        d = str(bin(a))
        d = d[2:]

        #frac
        f, q = 0, ''

        while f<5:
            e = float(b)*2
            if e == 1:
                q = q + '1'
                break
            q = q + str(int(e))
            b = e%1
            f += 1
            
        return float(d+'.'+ q)
        
        

    def bintodec(self, num:str):
        for i in str(num):
            if i not in '10.':
                return 'Please choose appropriate data type'
                
        else:
            a = str(int(float(num)))
            b = str(round(float(num)%1, 5))
            b = b[2:]

            #int
            l = []
            for i in a:
                l.append(i)

            l, s = l[::-1], 0

            for j in range(len(l)):
                s = s + int(l[j])*(2**j)
            
            #frac
            q = []
            for k in b:
                q.append(k)
            d, p = 0, 0
            for o in range(1, len(q)+1):
                d = d + int(q[p])*(2**(-o))
                p += 1
            d = str(d)
            d = d[2:]
            return float(str(s)+'.'+d)

    def dectooct(self, num:str):
        for i in str(num):
            if i not in '1234567890.':
                return 'Please choose appropriate data type'
        a = int(float(num))
        b = str(float(num)%1)
        #int
        d = str(oct(a))
        d = d[2:]
        
        #frac
        q = []
        for i in b:
            q.append(i)
        count = 0
        e = ''
        for i in q:
            e = e + i
        y = ''
        while count < 5:
            r = float(e)*8
            if r%1 == 0:
                y = y + str(int(r//1))
                break
            y = y + str(int(r//1))
            e = float(e)%1

        return float(d+'.'+y)
        

    def octtodec(self, num:str):
        for i in str(num):
            if i not in '12345670.':
                return 'Please choose appropriate data type'
                
        else:
            a = str(int(float(num)))
            b = str(round(float(num)%1, 5))
            b = str(int(b[2:]))
            
            #int
            l = []
            for i in a:
                l.append(i)

            l, s = l[::-1], 0

            for j in range(len(l)):
                s = s + int(l[j])*(8**j)
            
            #frac
            q = []
            for k in b:
                q.append(k)
            d, p = 0, 0
            for o in range(1, len(q)+1):
                d = d + int(q[p])*(8**(-o))
                p += 1
            d = str(d)
            d = d[2:]

            return float(str(s)+'.'+d)

    def dectohex(self, num:str):
        for i in str(num):
            if i not in '1234567890.':
                return 'Please choose appropriate data type'
        a = int(float(num))
        b = float(num)%1
        
        #int
        s = str(hex(a))
        s = s[2:]

        #frac
        index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        h, count = '', 0

        while count <5:
            r = b*16
            if r%1 == 0:
                h = h + index[int(r//1)]
                break
            h = h + index[int(r//1)]
            b = b%1
            return r//1
        
        return (s+'.'+h).upper()

        
    def hextodec(self, num:str):
        num = num.upper()
        a = ''
        for i in num:
            if i not in '12567890.ABCDEF':
                return 'Please choose appropriate data type'
        global d
        d = 0
        for i in num:
            if i == '.':
                d = num.index(i)
                break
            a = a + i
        b = num[d+1:]
        
        w = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
            '0':'0', 'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
        
        g, h = [], []

        for i in a:
            g.append(w[i])
        for i in b:
            h.append(w[i])

        s, f = 0, 0
        g, h = g[::-1], h[::-1]

        for i in range(len(g)):
            s = s + int(g[i])*(16**i)
        p = -1
        for i in range(len(h)):
            f = f + int(h[i])*(16**p)
            p -= 1

        return s + f

    def bintooct(self, num:str):
        for i in str(num):
            if i not in '10.':
                return 'Please choose appropriate data type'
        a = self.bintodec(num)
        b = self.dectooct(a)

        return b

    def octtobin(self, num:str):
        for i in str(num):
            if i not in '12345670.':
                return 'Please choose appropriate data type'
        a = self.octtodec(num)
        b = self.dectobin(a)

        return b
    
    def bintohex(self, num:str):
        for i in str(num):
            if i not in '10.':
                return 'Please choose appropriate data type'
        a = self.bintodec(num)
        b = self.dectohex(a)

        return b

    def hextobin(self, num:str):
        for i in num:
            if i not in '12567890.ABCDEF':
                return 'Please choose appropriate data type'
        num = num.upper()
        a = self.hextodec(num)
        b = self.dectobin(a)

        return b

    def octtohex(self, num:str):
        for i in str(num):
            if i not in '12345670.':
                return 'Please choose appropriate data type'
        a = self.octtodec(num)
        b = self.dectohex(a)

        return b

    def hextooct(self, num:str):
        for i in num:
            if i not in '12567890.ABCDEF':
                return 'Please choose appropriate data type'
        num = num.upper()
        a = self.hextodec(num)
        b = self.dectooct(a)

        return b

    