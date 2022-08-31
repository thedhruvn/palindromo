

from itertools import count, islice


def _getNoDecimalPoint(num) -> str:
    if((isinstance(num, float) or isinstance(num, str)) and "." in str(num)):
        return str(num).replace('.', '')
    return str(num)

def isPalindrome(num):
    strnum = _getNoDecimalPoint(num)
    return strnum==strnum[::-1]

def generatePalindromes():
    """Generate numbers that are palindromes in base 10."""
    yield 0
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2)-1::-1])


def doBetterLinearSearch(price: float, min_range = 10, max_range=999):
    """
    Slow linear algorithm that tests for palindromic tip and total

    More efficient palindrome generation
    """
    palindromeGenerator = generatePalindromes()
    for i, tip in islice(enumerate(palindromeGenerator),min_range,max_range):
        tip = tip/100.0
        total:float = price + tip
        total_str = f"{total:.02f}"
        if isPalindrome(total_str):
            return {"solution": True, "price": price, "tip": tip, "total": total_str}
    
    return {"solution": False, "price": price}


def doLinearSearch(price: float, min_range = 100, max_range=99999):
    """
    Slow linear algorithm that tests for palindromic tip and total
    """
    
    # len_price = len(_getNoDecimalPoint(price))
    # max_range = int(str([1 for i in len_price])

    for tip in filter(isPalindrome,range(min_range,max_range)):
        tip = tip/100.0
        total:float = price + tip
        total_str = f"{total:.02f}"
        if isPalindrome(total_str):
            return {"solution": True, "price": price, "tip": tip, "total": total_str}
    
    return {"solution": False, "price": price}

if __name__ == "__main__":
    results = {}

    # for pr in range(1000,1100):
    #     price = pr/100.0
    #     results.update({pr: doLinearSearch(price)})

    # failed_results = {k: v for k,v in results.items() if "solution" in v and v["solution"] == False}
    # print(failed_results.keys())


    # Selected Failed Results
    # 1020, 1031, 1041, 1240, 1171
    palindromeGenerator = generatePalindromes()
    for i, tip in islice(enumerate(palindromeGenerator),195,205):
        print(i, tip)
    # print(doBetterLinearSearch(10.19,1100,))
    # print(doLinearSearch(99.99))