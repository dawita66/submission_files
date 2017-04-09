
Nums = {'0':'zero', '1':'one', '2':'two', '3': 'three', '4':'four',
        '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
Place = {1:'one', 4:'thousand', 7: 'million', 10:'billion', 13: 'trillion'}
Tens = { '0':'b','2':'twenty', '3': 'thirty', '4':'fourty', '5':'fifty',
         '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
Teens = {'0':'ten', '1':'eleven', '2':'twelve', '3': 'thirteen', '4':'fourteen',
        '5':'fifteen', '6':'sixteen', '7':'seventeen', '8':'eighteen', '9':'nineteen'}


def num_converter(num):

    if num == 0:
        print('zero')

    lst = list(str(num))
    print(lst)
    i=0
    ret = []
    flag = False
    tracker = 0
    string = ''

    if num == 0:
        print('zero')

    while i < len(lst):
        mod = len(lst)%3
        print(tracker)
        if mod == 0:
            if lst[i] == '0':
                lst.pop(0)
                continue
            else:
                ret.append(Nums[lst[i]])
                ret.append('hundred')
                tracker +=1
                lst.pop(0)
        elif mod == 1:
            if len(lst) > 1:
                if flag:
                    ret.append(Teens[lst[i]])
                    ret.append(Place[len(lst)])
                    flag = False
                else:
                    if lst[i] == '0':
                        """print(tracker)"""
                        if tracker > 0:

                            """ret.append(Nums[lst[i]])"""
                            ret.append(Place[len(lst)])
                            tracker = 0
                        else:
                            lst.pop(0)
                            continue
                    else:
                        ret.append(Nums[lst[i]])
                        ret.append(Place[len(lst)])
                tracker = 0
            else:
                if flag:
                    ret.append(Teens[lst[i]])
                    flag = False
                else:
                    if lst[i] == '0':
                        lst.pop(0)
                        continue
                    else:
                        ret.append(Nums[lst[i]])
            lst.pop(0)
        else:
            if lst[i] == '1':
                flag = True
                tracker += 1
            else:
                if lst[i] != '0':
                    tracker +=1
                    ret.append(Tens[lst[i]])
            lst.pop(0)

        string = ' '.join(ret)

    print string



"""number = input("Number you want to convert: ")
while number:

    if number == 'stop':
        print('kdjakj')
    else:
        num_converter(number)
        number = input("Number you want to convert: ")
"""

if __name__ == "__main__":
    num_converter


num_converter(4232)
num_converter(123)
num_converter(123456089)
num_converter(0)
