#Dictionaries for reference
ones = {"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six", "7":"Seven","8":"Eight","9":"Nine"}
afterones = {"10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen", "17":"Seventeen","18":"Eighteen","19":"Nineteen"}
tens = {"2":"Twenty","3":"Thirty","4":"Fourty","5":"Fifty","6":"Sixty", "7":"Seventy","8":"Eighty","9":"Ninety"}
grand={0:" Billion, ",1:" Million, ",2:" Thousand, ",3:""}

#Function converting number to words of 3 digit
def num_to_wrds(val):
    if val != "000":
        ans = ""
        if val[0] in ones:
            x = val
            ans = ans + ones[val[0]] + " Hundered and "
        if val[1:] in afterones:
            ans = ans + afterones[val[1:]] + " "
        elif val[1] in tens:
            ans = ans + tens[val[1]] + " "
        if val[2] in ones and val[1:] not in afterones:
            ans = ans + ones[val[2]]
        return ans


num = input("Enter the number: ")

# Paddiing with zeros
pad = 12-len(str(num))
numinwrds = "0"*pad + str(num)

final =""
numlis = [numinwrds[0:3],numinwrds[3:6],numinwrds[6:9],numinwrds[9:12]]

for key,grp in enumerate(numlis):

    print(key,grp)

    if grp!="000":
        final = final + num_to_wrds(grp) + grand[key]

print (final)



