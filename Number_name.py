Nums = {'1':'one', '2':'two', '3': 'three', '4':'four',
        '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
Place = {4:'thousand', 7: 'million', 10:'billion', 13: 'trillion'}
Tens = {'2':'twenty', '3': 'thirty', '4':'fourty', '5':'fifty',
         '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
Teens = {'0':'ten', '1':'eleven', '2':'twelve', '3': 'thirteen', '4':'fourteen',
        '5':'fifteen', '6':'sixteen', '7':'seventeen', '8':'eighteen', '9':'nineteen'}


def num_converter(num):

    #temp list to store result
    ret = []
    #set to true for teens (eleven, tweleve ..)
    flag = False
    # track if previous two values are non-zero
    # used to decide whether to append place values (thousand, million...)
    # if tracker = 0 and current value = 0, skip
    tracker = 0
    #return string
    string = ''

    #corner case where num = 0
    if num == 0:
        string = 'zero'
    #convert num to iterable list
    lst = list(str(num))

    # check first vale in list, append value to temp list and pop that value off
    # mod 3 returns the values place (ones, tens or hundreds)
    i=0
    while i < len(lst):

        mod = len(lst)%3

        #if mod = 0, the number in hundreds place. look up its value and
        # append 'hundred'. if the value is 0, pop number from list and skip
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

    print(string)

number = int(raw_input("Number you want to convert: "))

while number > -1:

    if number == 'stop':
        exit
    else:
        num_converter(number)
        number = int(raw_input("Number you want to convert: "))

"""
num_converter(4232)
num_converter(123)
num_converter(123456089)

"""
