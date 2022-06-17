class Solution(object):
    d_unit={
            0:'',
            1:'I',
            2:'II',
            3:'III',
            4:'IV',
            5:'V',
            6:'VI',
            7:'VII',
            8:'VIII',
            9:'IX'
        }
    d_tens={
            0:'',
            1:'X',
            2:'XX',
            3:'XXX',
            4:'XL',
            5:'L',
            6:'LX',
            7:'LXX',
            8:'LXXX',
            9:'XC'
        }
    d_hund={
            0:'',
            1:'C',
            2:'CC',
            3:'CCC',
            4:'CD',
            5:'D',
            6:'DC',
            7:'DCC',
            8:'DCCC',
            9:'CM'
        }
    d_thou={
            1:'M',
            2:'MM',
            3:'MMM'
        }
    def intToRoman(self, num):
        if num<10:
            return self.d_unit[num]
        if num<100:
            return self.d_tens[num//10]+ self.d_unit[num%10]
        if num<1000:
            return self.d_hund[num//100]+self.d_tens[(num//10)%10]+self.d_unit[num%10]
        if num>999:
            return self.d_thou[num//1000]+self.d_hund[(num//100)%10]+self.d_tens[(num//10)%10]+self.d_unit[num%10]




obj = Solution()
#num = 3689 # MMMDCLXXXIX
num = 3000 # MMM
print(obj.intToRoman(num))