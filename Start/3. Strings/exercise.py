#python code below
#use print("messages...") to debug your solution
import string
showExpectedRes = False
showHints = False

def processStr(str, term):
    # punc = sum(c in string.punctuation for c in str)
    # whiteSpace = sum(c in string.whitespace for c in str)
    # uc = sum(c in string.ascii_uppercase for c in str)
    # lc = sum(c in string.ascii_lowercase for c in str)
    # isTermFound = term in str
    # termIndex = -1
    # if isTermFound == True:
    #     termIndex = str.index(term)
    # res = {
    #     "Punctuation": punc,
    #     "Whitespace": whiteSpace,
    #     "Uppercase": uc,
    #     "Lowercase": lc,
    #     "Found":isTermFound,
    #     "Index": termIndex
    # }
    res = {
        "Punctuation": 0,
        "Whitespace": 0,
        "Uppercase": 0,
        "Lowercase": 0,
        "Found": False,
        "Index": -1
    }
    
    for c in str:
        if c in string.punctuation:
            res["Punctuation"] += 1
        elif c in string.whitespace:
            res["Whitespace"] += 1
        elif c in string.ascii_uppercase:
            res["Uppercase"] += 1
        elif c in string.ascii_lowercase:
            res["Lowercase"] =+ 1
        
    res["Index"] = str.upper().find(term.upper())
    res["Found"] = res["Index"] >= 0
    return res

print(processStr("The quick, brown fox! jumps over the lazy dog.", "fox"))