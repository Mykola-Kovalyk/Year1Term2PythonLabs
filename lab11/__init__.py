import re
import datetime
import zipfile


def find_by_date(archive_path, file_path, date_begin, date_end):

    return_list = []

    with zipfile.ZipFile(archive_path, 'r') as archive:
        with archive.open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i].decode()
                try:
                    if re.search('NASA', line):
                        occurence = re.search(r"\[[^\]]+.", line)
                        if occurence:
                            date_as_str = occurence.group()[1:-7]
                            date = datetime.datetime.strptime(date_as_str, '%d/%b/%Y:%H:%M:%S')

                            if date_begin <= date <= date_end:
                                return_list.append(line)
                            elif date > date_end:
                                break
                except Exception as e:
                    print(f'An error occurred while parsing line {i} ("{line}"): {e}')

    return return_list



if __name__ == '__main__':

    count = len(find_by_date('access_log_Jul95.zip',
                             'access_log_Jul95',
                       datetime.datetime(1995, 7, 1, 0, 7),
                       datetime.datetime(1995, 7, 1, 2, 21)))

    print(f"There's {count} occurrences found.")

