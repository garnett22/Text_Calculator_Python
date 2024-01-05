from num2words import num2words
def calc(string):
    values = {
              'ноль': '0',
              'один': '1',
              'два': '2',
              'три': '3',
              'четыре': '4',
              'пять': '5',
              'шесть': '6',
              'семь': '7',
              'восемь': '8',
              'девять': '9',
              'десять': '10',
              'одинадцать': '11',
              'двенадцать': '12',
              'тринадцать': '13',
              'четырнадцать': '14',
              'пятнадцать': '15',
              'шестнадцать': '16',
              'семнадцать': '17',
              'восемнадцать': '18',
              'девятнадцать': '19',
              'двадцать': '20',
              'тридцать': '30',
              'сорок': '40',
              'пятьдесят': '50',
              'шестьдесят': '60',
              'семьдесят': '70',
              'восемьдесят': '80',
              'девяносто': '90',
              'плюс': '+',
              'минус': '-',
              'умножить': '*',

             }


    list1 = string.split(' ')


    if len(list1) == 6:
        value1 = int(values[list1[0]]) + int(values[list1[1]])
        value2 = int(values[list1[4]]) + int(values[list1[5]])
        result = value1 * value2
        print (num2words(result, lang='ru'))


    elif len(list1) == 5:
        if 'умножить' in list1:
            index = list1.index('умножить')
            if index == 1:
                value1 = int(values[list1[0]])
                value2 = int(values[list1[3]]) + int(values[list1[4]])
                result = value1 * value2
                print (num2words(result, lang='ru'))
            elif index == 2:
                value1 = int(values[list1[0]]) + int(values[list1[1]])
                value2 = int(values[list1[4]])
                result = value1 * value2
                print (num2words(result, lang='ru'))
        elif 'плюс' in list1:
            value1 = int(values[list1[0]]) + int(values[list1[1]])
            value2 = int(values[list1[3]]) + int(values[list1[4]])
            result = value1 + value2
            print(result)
        elif 'минус' in list1:
            value1 = int(values[list1[0]]) + int(values[list1[1]])
            value2 = int(values[list1[3]]) + int(values[list1[4]])
            result = value1 - value2
            print (num2words(result, lang='ru'))


    elif len(list1) == 4:
        if 'умножить' in list1:
            index = list1.index('умножить')
            if index == 1:
                value1 = int(values[list1[0]])
                value2 = int(values[list1[3]])
                result = value1 * value2
                print (num2words(result, lang='ru'))
        elif 'плюс' in list1:
            index = list1.index('плюс')
            if index == 1:
                value1 = int(values[list1[0]])
                value2 = int(values[list1[2]]) + int(values[list1[3]])
                result = value1 + value2
                print (num2words(result, lang='ru'))
            elif index == 2:
                value1 = int(values[list1[0]]) + int(values[list1[1]])
                value2 = int(values[list1[3]])
                result = value1 + value2
                print (num2words(result, lang='ru'))
        elif 'минус' in list1:
            index = list1.index('минус')
            if index == 1:
                value1 = int(values[list1[0]])
                value2 = int(values[list1[2]]) + int(values[list1[3]])
                result = value1 - value2
                print (num2words(result, lang='ru'))
            elif index == 2:
                value1 = int(values[list1[0]]) + int(values[list1[1]])
                value2 = int(values[list1[3]])
                result = value1 - value2
                print (num2words(result, lang='ru'))


    elif len(list1) == 3:
        if 'плюс' in list1:
            value1 = int(values[list1[0]])
            value2 = int(values[list1[2]])
            result = value1 + value2
            print (num2words(result, lang='ru'))
        elif 'минус' in list1:
            value1 = int(values[list1[0]])
            value2 = int(values[list1[2]])
            result = value1 - value2
            print (num2words(result, lang='ru'))



calc('шестьдесят шесть умножить на тридцать семь')

