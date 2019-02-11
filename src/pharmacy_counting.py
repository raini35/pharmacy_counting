import time
import re
import sys

start_time = time.time()

def clean_up(line, pattern):
    partToEdit = pattern.search(line).group(0)
    edited = partToEdit.replace(',', '').replace('"', '')

    return pattern.sub(edited, line)

def processFile(file):
    print('STARTED PROCESSING %s' %file)

    output = []
    fileInfo = {}
    with open(file) as fin:
        pattern = re.compile(r'"(.*)"')

        header = fin.next()
        output.append(header.strip().split(','))


        for i,line in enumerate(fin):
            original = line

            if pattern.search(line):
                line = clean_up(line, pattern)

            arr = line.strip().split(',')

            drug = arr[3]
            price = arr[4]

            if(drug in fileInfo):
                fileInfo[drug][0] = fileInfo[drug][0] + 1
                fileInfo[drug][1] = fileInfo[drug][1] + float(price)
            else:
                fileInfo[drug] = [1, float(price)]
    fin.close()

    output.append(fileInfo)

    print('FINISHED PROCESSING %s' %file)

    return output

def writeOutput(file, header, info, sortInfo):
    file.write("%s,%s,%s\n" %(header[3], 'num_prescriber','total_cost'))

    if sortInfo:
        for item in sorted(info.items(), key=lambda x: x[1][1], reverse=True):
            drug = item[0]
            patientCount = item[1][0]
            totalPrice = item[1][1]
            file.write("%s,%d,%.0f\n" %(drug, patientCount, totalPrice))
    else:
        for drug in info.keys():
            patientCount = info[drug][0]
            totalPrice = info[drug][1]
            file.write("%s,%d,%.0f\n" %(drug, patientCount, totalPrice))

    return

if __name__ == "__main__":
    # filename = 'de_cc_data.txt'
    filename = sys.argv[1]


    output = processFile(filename)

    header = output[0]
    info = output[1]

    # outputFile = open('./output/top_cost_drug.txt', 'w+')
    outputFile = open(sys.argv[2], 'w+')

    writeOutput(outputFile, header, info, True)

    outputFile.close()

    print("--- %s seconds ---" % (time.time() - start_time))
