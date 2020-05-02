'''密码要求如下：
            密码长度不小于6,不大于20
            至少包含一个数字,一个小写字母,一个大写字母
            单个字符不允许连续重复三次以上'''
import re
# s = '232333dAsssww.,.,.$#'

def strongPasswordChecker(s):
    if not s.strip() or re.search('\s+',s):
        print('密码不允许为空或者包含空格！')
    elif len(s) >= 6 and len(s) <= 20:
        nums = 0
        if re.search('[a-z]+',s) and re.search('[A-Z]+',s) and re.search('[0-9]+',s):
            count = []
            for i in s:
                count.append(s.count(i))
            if max(count) < 3:
                return 0
            else:
                for i in range(len(s)):
                    if len(s[i:]) >= 3:
                        if set(s[i:i+3]) == set(s[i]):
                            nums+=1
                if nums > 0:
                    print('密码不合格，单个字符不允许连续重复三次！')
                return nums
        elif not re.search('[a-z]+',s):
            nums +=1
            print('密码不合格，密码中需至少包含一位小写字母！')
        if not re.search('[A-Z]+',s):
            nums +=1
            print('密码不合格，密码中需至少包含一位大写字母！')
        if not re.search('[0-9]+',s):
            nums +=1
            print('密码不合格，密码中需至少包含一位数字！')
        return nums
    elif len(s) < 6:
        print('密码不合格，密码长度不少于6位！')
        return 6 - len(s)
    elif len(s) > 20:
        print('密码不合格，密码长度不大于20位！')
        return len(s) - 20

i = 0
while i < 3:
    s = input('请输入您的密码：')
    print('您设置的密码长度为:{}'.format(len(s)))
    ss = strongPasswordChecker(s)
    if ss == 0:
        print('密码等级高，符合要求！')
        break
    else:
        print('密码不符合要求,密码合规需要修改的次数为:{}'.format(ss))
        i+=1





