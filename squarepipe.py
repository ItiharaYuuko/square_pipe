import re

class strComplex(str):
    def judgeDecimal(self):
        if (self.count('.') == 1):
            temparr = self.split('.')
            if (temparr[0].isdigit() and temparr[1].isdigit()):
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    while True:
    
        ptypeR = input('Please input the type for the pipe: ')
        ptypeRComStr = r'\d*[x]\d*[x]\d*'
        ptypeRCom = re.compile(ptypeRComStr)
        ptypeAD = []
        if (ptypeRCom):
            ptypeA = ptypeR.split('x')
            for ite in ptypeA:
                if (ite.isdigit()):
                    ptypeAD.append(float(ite))
                else:
                    continue
        else:
            continue
        phight = strComplex(input('Please input the hight for the pipe: '))

        if ((phight.judgeDecimal() or phight.isdigit()) and (len(ptypeAD) == 3)):
            wightAnswer = (((ptypeAD[0] * ptypeAD[1]) - \
                            ((ptypeAD[0] - 2 * ptypeAD[2]) * \
                            (ptypeAD[1] - 2 * ptypeAD[2])))\
                            * 7.85 * float(phight) / 1000000)
            print('wight = ',wightAnswer)
        else:
            continue