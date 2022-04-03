import argparse
import os
import re
from datetime import date
from textwrap import dedent

'''
# generate kata file from given sample
python3.8 generate_kata.py --file_out split_the_bill
'''

t = date.today().strftime('%d.%m.%Y')

kata_text = dedent(f'''
            \'\'\'
            train_date: {t}\n\
            kata link: https://www.codewars.com/kata/5641275f07335295f10000d0/\n\
            points: 7 kyu\n\
            type: OOP\n\
            -------------\n\
            DESCRIPTION:\n\
            -------------\n\
            TRANSLATION:\n\
            -------------\n\
            ===TRAINED====\n\
            -------------\n\
            \'\'\'\n\
            \n\
            import codewars_test as test\n\
            ''')

print(kata_text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_out', dest='file_out', required=True)

    args = parser.parse_args()
    file_out = args.file_out

    print(file_out)
    dir_list = os.listdir(".")
    max_num = 0
    for f in dir_list:
        if m := re.search(r'(\d+)\_', f):
            curr_num = int(m.group(1))
            max_num = curr_num if curr_num > max_num else max_num
    file_out_name = f'{max_num + 1}_{file_out}.py'
    print(f'{file_out_name=}')

    f = open(file_out_name, "w")
    f.write(f"{kata_text}")
    f.close()


if __name__ == '__main__':
    main()