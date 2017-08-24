"""Python Script to extract specific rows from a .csv file based on a lookup string in a given column.

Information:
    maintained by:  Omer Barel
    mail:           barelomer@gmail.com
    website:        http://jungopro.com

Example:
    python3 CSV_Report.py -o /Users/User/Desktop/Original.csv -t /Users/User/Desktop/output.csv -l 123456789 -c 2
"""
import csv
import argparse

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-o', '--origin', dest='original_csv_file_path', 
                        metavar='original_csv_file_path', 
                        type=str,
                        help='Path to the original .CSV containing the data (including full path with filename)',
                        required=True)
    parser.add_argument('-t', '--target', dest='target_csv_file_path', 
                        metavar='target_csv_file_path', 
                        type=str,
                        help='Path to save the output .CSV file (including full path with filename)',
                        required=True)
    parser.add_argument('-l', '--lookup', dest='lookup_value', 
                        metavar='lookup_value', 
                        type=str,
                        help='String to look in a column. Rows with the string in the column will be saved to the output .CSV file',
                        required=True)
    parser.add_argument('-c', '--column', dest='lookup_column', 
                        metavar='lookup_column', 
                        type=int,
                        help='The column in which to search the lookup string. Must be a number (please note! - first column number is 0)',
                        required=True)
    args = parser.parse_args()

    target_csv = open(args.target_csv_file_path,'w')
    target_csv_iterator = csv.writer(target_csv, dialect='excel')

    with open(args.original_csv_file_path) as csv_file:
        original_csv_iterator = csv.reader(csv_file, delimiter=',')
        for row in original_csv_iterator:
            if str(args.lookup_value) in row[args.lookup_column]:
                target_csv_iterator.writerow(row)

    target_csv.close()


if __name__ == '__main__':
    main()
