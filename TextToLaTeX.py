# !python3
import re

fin = open('Text.txt', 'rt')
fout = open('LaTeX.txt', 'wt')
categoryFormat = re.compile(r'\d\..+')
thingsFormat = re.compile(r'^DebugSpawn\W*“(\w+)”\W*（(.+)）')
thingsList = []
# latexFormat = r'{}& \texttt{{{}}}&'
latexFormat = r'\makebox[.5\textwidth][l]{{{}：\texttt{{{}}}}}'
for line in fin:
    categoryLine = categoryFormat.search(line)
    thingsLine = thingsFormat.search(line)
    if thingsLine:
        thingName = thingsLine.group(2)
        thingCode = thingsLine.group(1)
        thingCode = thingCode.replace('_', r'\_', 10)
        thingsList.append((thingName, thingCode))
    elif categoryLine:
        thingsOrder = sorted(thingsList, key=lambda thing: thing[1])
        thingsList = []
        num = len(thingsOrder)-2
        for i in range(0, num, 2):
            textLine = ''
            for j in range(0, 2):
                thingName, thingCode = thingsOrder[i+j]
                textLine += latexFormat.format(thingName, thingCode)
            textLine = textLine.rstrip('&')
            textLine += r'\\'
            print(textLine, file=fout)
        num = num % 2
        textLine = ''
        for i in range(0, num):
            thingName, thingCode = thingsOrder[i-num]
            textLine += latexFormat.format(thingName, thingCode)
        textLine.rstrip('&')
        textLine += '\\\\\n'
        print(textLine, file=fout)

# print(sorted(thingsList, key = lambda thing:thing[1]), file = fout)
fin.close()
fout.close()
