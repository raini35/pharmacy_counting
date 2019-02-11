import time
import sys

from write_output import write_output
from  process_file import process_file

start_time = time.time()

if __name__ == "__main__":
    # filename = 'de_cc_data.txt'
    filename = sys.argv[1]

    output = process_file(filename)

    header = output[0]
    info = output[1]


    # outputFile = open('./output/top_cost_drug.txt', 'w+')
    outputFile = open(sys.argv[2], 'w+')

    sortInfo = True

    write_output(outputFile, header, info, sortInfo)

    outputFile.close()

    print("--- %s seconds ---" % (time.time() - start_time))
