import re

file = open("input.txt")
string = file.read()

pattern = r"do\(\).*?don't\(\)"
pattern2 = r"mul\(\d+,\d+\)"
patternRemove = r"don't\(\).*?do\(\)"

y = re.findall(pattern, string)
# x = re.findall("", string)
remove = re.findall(patternRemove, string)

# begin = ";(,)<mul(595,110)~ #(select()-?who():mul(732,729)+/;%@mul(924,700) }&when()}why()mul(633,308)$~;what()&"
# end = "do()+mul(835,113)when();/how()'mul(516,246)@from()}do()):;;{why()how()-^mul(866,121)(/mul(289,117)select()}^who()*>@,/)mul(494,764)why()how()where();mul(263,332)%,%^{&@mul(470,641) {%mul(572,709)>#,/ from()[mul(189,623)$mul(359,331),how()>why(10,98)!do() where()*:mul(908,32)"
# y.append(begin)
# y.append(end)

print(remove)

for r in remove:
    string = string.replace(r, '')

mul = re.findall(pattern2, string)
print(mul)

totaal = []

for m in mul:
    m = m.replace('mul(', '')
    m = m.replace(')', '')
    spl = m.split(',')
    res = int(spl[0])*int(spl[1])
    totaal.append(res)

print(sum(totaal))