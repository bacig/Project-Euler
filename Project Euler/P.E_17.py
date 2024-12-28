import time

def numbers_to_words(n):

    one_to_ten = {1:'one', 2:'two', 3:'three', 4: 'four', 5:'five',

                  6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

    eleven_to_nineteen = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',

                          16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

    twenty_to_ninety = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',

                        60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    hundreds = {100:'onehundred', 200:'twohundred', 300:'threehundred', 400:'fourhundred', 500:'fivehundred',

                600:'sixhundred', 700:'sevenhundred', 800:'eighthundred', 900:'ninehundred'}

    onethousand = {1000:'onethousand'} 

    if n <= 10:

        return one_to_ten[n]

    elif 11 <= n <= 19:

        return eleven_to_nineteen[n]

    elif 20 <= n <= 99:

        if n % 10 == 0:

            return twenty_to_ninety[n]

        else:

            return twenty_to_ninety[(n // 10) * 10] + one_to_ten[n % 10]       

    elif 100 <= n <= 999:

        if n % 100 == 0:

            return hundreds[n]

        elif n % 10 == 0:

            if n % 100 == 10:

                return hundreds[n - n % 100] + 'and' + one_to_ten[n % 100]

            else:

                return hundreds[n - n % 100] + 'and' + twenty_to_ninety[n % 100]

        else:

            if n % 100 < 10:

                return hundreds[n - n % 100] + 'and' + one_to_ten[n % 100]

            elif 11 <= n % 100 <= 19:

                return hundreds[n - n % 100] + 'and' + eleven_to_nineteen[n % 100]

            else:

                return hundreds[n - n % 100] + 'and' + twenty_to_ninety[n - (n // 100) * 100 - n % 10] + one_to_ten[n % 10]

    else:

        return onethousand[n] 


def main(n):
    one_to_thousand = [number for number in range(1, n + 1)]
    sum = 0

    for number in one_to_thousand:

        sum += len(numbers_to_words(number))

    return sum


start = time.perf_counter()

print(main(1000))

end = time.perf_counter()

print(end - start)
