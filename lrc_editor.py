import sys
from os import path
import re
from datetime import datetime, timedelta
from collections import OrderedDict


class LrcEditor(object):
    def __init__(self):
        print("into lrc editor")

    def adjust_lrc_time(self, lrc_file_path, adj_time_ms):
        time_tag_str = r"\[\d\d:\d\d.\d\d\]"
        time_match_str = r"\[\d\d:\d\d.\d\d].*"
        adj_time_lrc = []

        lrc_content = self.read_file(lrc_file_path)
        for line_content in lrc_content:
            # print(line_content)
            time_match = re.match(time_match_str, line_content)
            if time_match:
                all_time_list = self.get_all_match_list_from_str(time_tag_str, line_content)
                for time_tag in list(OrderedDict.fromkeys(all_time_list)):
                    adj_time_tag = self.time_tag_adjust(time_tag, adj_time_ms)
                    # print(adj_time_tag)
                    line_content = line_content.replace(time_tag, adj_time_tag)

            adj_time_lrc.append(line_content)

        with open(lrc_file_path, 'w', encoding='utf8') as f:
            for line in adj_time_lrc:
                f.write(line)

    @staticmethod
    def time_tag_adjust(time_tag, adj_time_ms):
        time_tag_format = '%M:%S.%f'

        time_tag_loc = time_tag
        time_tag_loc = time_tag_loc.replace("[", "")
        time_tag_loc = time_tag_loc.replace("]", "")

        adj_time_ms_h = timedelta(milliseconds=int(adj_time_ms))
        # print(adj_time_ms_h)

        time_tag_time_h = datetime.strptime(time_tag_loc, time_tag_format)
        # print(time_tag_time_h)
        adjed_time_h = time_tag_time_h + adj_time_ms_h

        if adjed_time_h.year <= 1899:
            adjed_time_str = "[00:00.00]"
        else:
            adjed_time_str = "["+adjed_time_h.time().strftime(time_tag_format)[:-4]+"]"
        return adjed_time_str

    @staticmethod
    def get_all_match_list_from_str(match_str, content_str):
        match_re = "(" + match_str + "?)" + ".*"
        content = content_str
        match_list = []

        while True:
            matched_re = re.search(match_re, content)
            if matched_re:
                matched_str = matched_re.group(1)
                content = content.replace(matched_str, "")
                match_list.append(matched_str)
            else:
                break

        return match_list

    @staticmethod
    def read_file(file_path):
        format_list = ['utf8', 'utf-8-sig', 'utf16', None, 'big5', 'gbk', 'gb2312']
        for file_format in format_list:
            try:
                with open(file_path, 'r', encoding=file_format) as file:
                    content = file.readlines()

                # print('find correct format {} in ini file: {}'.format(file_format, self.ini_full_path))
                return content
            except Exception as e:
                print('checking {} format: {}'.format(file_path, file_format))
                str(e)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please input lrc file path and adjust time by million seconds")
        sys.exit()

    lrc_path = sys.argv[1]
    adj_time = sys.argv[2]
    if path.exists(lrc_path):
        lrc_editor = LrcEditor()
        lrc_editor.adjust_lrc_time(lrc_path, adj_time)
    else:
        print("file {} not found!".format(lrc_path))
