import re

def clean_up(line, pattern):
    partToEdit = pattern.search(line).group(0)
    edited = partToEdit.replace(',', '').replace('"', '')

    return pattern.sub(edited, line)

def prescriber_existence(name, drug, fileInfo):
    if name in fileInfo[drug][2]:
        return True
    else:
        return False

def process_line(line, fileInfo):
    arr = line.strip().split(',')

    prescriber = arr[1].upper() + " " + arr[2].upper()
    drug = arr[3]
    price = arr[4]

    if(drug in fileInfo):
        if prescriber_existence(prescriber, drug, fileInfo) == False:
            fileInfo[drug][0] = fileInfo[drug][0] + 1
            fileInfo[drug][2][prescriber] = True

        fileInfo[drug][1] = fileInfo[drug][1] + float(price)
    else:
        fileInfo[drug] = [1, float(price), {prescriber: True}]

    return

def process_file(file):
    print('STARTED PROCESSING %s' %file)

    output = []
    fileInfo = {}
    with open(file) as fin:
        pattern = re.compile(r'"(.*)"')

        header = fin.next()

        output.append(header.strip().split(','))

        for i,line in enumerate(fin):
            if len(line) > 1:

                if pattern.search(line):
                    line = clean_up(line, pattern)

                process_line(line, fileInfo)


    fin.close()

    output.append(fileInfo)

    print('FINISHED PROCESSING %s' %file)

    return output
