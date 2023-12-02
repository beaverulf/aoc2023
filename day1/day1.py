
def main():    
    with open('./day1/data.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        total = 0
        for line in data:
            digits = [x for x in line if x.isdigit()]
            print(line, int(digits[0]+digits[-1]))
            total += int(digits[0]+digits[-1])
        print(total)
        
    

words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def findWordOrDigits(input:str):
    parsed = ""
    digits = ""
    for c in input:
        if c.isdigit():
            digits += str(c)
        else:
            parsed += c
            for word in words:
                if word in parsed:
                    digits += str(words[word])
                    parsed = parsed[-1] #for the case where one letter digit ends with the same letter as another digit, ex twone, 21
                    continue
    return int(digits[0]+digits[-1])

        
def parseStringsAsNumbers():
    with open('./day1/data.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        total = 0
        for line in data:
            k = findWordOrDigits(line)
            #print(line, k)
            total += k
        print(total)
parseStringsAsNumbers()