import re
import datetime


def find_by_date(file_path, date_begin, date_end):

    return_list = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            try:
                occurence = re.search(r"\[[^\]]+.", line)
                if occurence:
                    date_as_str = occurence.group()[1:-7]
                    date = datetime.datetime.strptime(date_as_str, '%d/%b/%Y:%H:%M:%S')

                    if date_begin <= date <= date_end:
                        return_list.append(line)
                    elif date > date_end:
                        break
            except Exception as e:
                print(f'An error occured while parsing line {i} ("{line}"): {e}')

    return return_list



if __name__ == '__main__':
    print(find_by_date('access_log_Jul95',
                       datetime.datetime(1995, 7, 1, 0, 10),
                       datetime.datetime(1995, 7, 1, 0, 20)))

