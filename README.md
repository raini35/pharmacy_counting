# pharmacy_counting
by Rainier G.

The following program runs in Python 2.7.15.

The program takes two arguments the path to the input file and the path to the output file. You can run the program using the following command:

    python ./src/main.py ./path/to/input_file ./path/to/output_file

## General
Inside /src, my program is divided up into three files w/ the following functions:
* `main.py`

* `process_file.py`
  * clean_up(line, pattern)
    * input: string, regex pattern
    * output: string
    * Uses the regex pattern to extract the parts of the current line w/ commas and double double apostrophes

  * prescriber_existence(name, drug, fileInfo)
    * input: string, string, dict
    * output: True or False
    * Checks if name of the current prescriber already exists in the drug's prescriber list.

  * process_line(line, fileInfo)
    * input: line, dict
    * output: None
    * Stores the line input into fileInfo dict by first turning the line into a list split by the commas present in the string and then uses the following schema to store the line into fileInfo:
      * key: drug
      * value: [count, total_price, {prescriber_name: True}]

  * process_file(file):
    * input: string
    * output: list
    * Opens the file input,

* `write_output.py`
  * write_output(file, header, info, sortInfo=False)
    * input: file-object, list, dict, True or False
    * output: None
    * Writes header (the first line of the input file) and info (the processed data) into file (the output file). sortInfo is set to False as default, but if sortInfo is set to True, then info will be written sorted by total price in descending order.

## Tests:
In total, I made 4 tests:
* `blank_line_test` - This test was to make sure that my program was able to recognize if the current line was just blank

* `prescriber_uniqueness` - This test was used so that I was only incrementing the drug prescriber count if the current prescriber hadn't already been logged.

Because in process_line I split the line strings into array by comma, it was necessary for my program to filter out any unnecessary commas. The following two tests made sure that my program was able to handle unnecessary commas:

* `single_comma_test` - This test covered for an input where there was a single comma inside one of the line strings. For example,

    '1000000003,Johnson,James,"CHLORPROMAZINE 5,000",1000'

* `multiple_commas_test` - This test covered for an input where there were multiple commans inside one of the line strings. For example,

    '1000000001,"Smith, MD, INC.",James,AMBIEN,100'

## Notes/Improvements
* The program in much larger data sets would be too slow. It would be better if I used software that enabled distributed storage and processing. My first thought was to utilize multi-processing, split up the files according to the number of CPUs in the computer and designate each file to a CPU to process, and then combine the results, but the cost of splitting up the files was too much. There's probably a better way of doing it, but when I implemented it, to equally split the file, I went through the entire file first to count the total amount of lines first to approximate when the limits. When I compared the two programs together, there was not much improvement.
* The regex that I programmed in only handled single cases of a 'single comma' or 'multiple commas.' If there were more than one case, it would only pick up on one of the cases instead of all. For example, with the following:

    '1000000001,"Smith, MD, INC.",James,"CHLORPROMAZINE 5,000",100'

    It would only recognize "Smith, MD" instead of both "Smith, MD " and "CHLORPROMAZINE 5,000".
* The program isn't that dynamic. I hardcoded the information to process. It would be better if the user could choose the keys and the values that are being stored in the dict.
