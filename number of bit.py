print('binary of 20 is {}'.format(bin(20)))


def number_of_bit(number):
    # num_binary = bin(number)
    num_bit = 0
    for i in list(bin(number)):
        if i == '1':
            num_bit += 1
    return num_bit


print(number_of_bit(1234))


def adds(num1: int, num2: int) -> int:
    return num1 + num2


def high_low(numbers):
    resolve = numbers.split(' ')
    new_num = []
    for i in resolve:
        new_num.append(int(i))
    new_num.sort()
    answer = str(new_num[-1]) + '' + str(new_num[0])
    return answer


print(high_low('1 2 -2 3 4254 5'))


def longest(s1: str, s2: str) -> str:
    merge = sorted(list(set(s1).union(set(s2))))
    answer = ''.join(merge)
    return answer


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))

jim = [2, 1, 3, 653, -3]
jim.sort()
print(jim)


def filter_list(lists: list) -> list:
    answer = []
    for i in lists:
        if type(i) == int:
            answer.append(i)
    return answer


print(filter_list([1000, 23, 'a', 'b']))


def digital_root(n):
    an = 0
    while len(str(n)) > 1:
        for i in list(str(n)):
            an += int(i)
        n = an
    return n


print(digital_root(1237))


def spin_words(sentence):
    soted = []
    for word in sentence.split(' '):
        if len(word) >= 5:
            words = list(word)
            words.reverse()
            soted.append(''.join(words))
        else:
            soted.append(word)
    return ' '.join(soted)


print(spin_words("Welcome back you preak"))


def find_even_index(arr):
    for n in range(len(arr)):
        if sum(arr[:n]) == sum(arr[n+1:]):
            answer = n
            break
        else:
            answer = -1
    return answer


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 100, 50, -51, 1, 1]))


def to_camel_case(text):
    answer = []
    if '-' in text:
        text = text.split('-')
        answer.append(text[0])
        for word in text[1:]:
            answer.append(str(word).capitalize())
    elif '_' in text:
        text = text.split('_')
        answer.append(text[0])
        for word in text[1:]:
            answer.append(str(word).capitalize())
    # elif '-' and '_' in text:
    return ''.join(answer)


print(to_camel_case('this is not the_stealth-warrior'))


def namelist(names):
    if names == list():
        answer = ''
    elif len(names) <= 1:
        answer = ''.join(names[0].values())
    else:
        names = [x for i in names for x in i.values()]
        sepe = ', '.join(names[:-1])
        end = str(names[-1])
        answer = sepe + ' & ' + end
    return answer


print(namelist([{'name': 'brad'}, {'name': 'josh'}]))


def unique_in_order(iterable):
    if iterable == [] or iterable == '':
        answer = []
    else:
        answer = [iterable[0]]
        for i in range(len(iterable)):
            if iterable[i] == answer[-1]:
                continue
            else:
                answer.append(iterable[i])
    return answer


print(unique_in_order('AAABBBCCBbaaA'))
