import json


def find_dict2_in_dict1(dict1, dict2, simbol):
    no_in_dict1 = {}
    for k, i in dict2.items():
        if not(k in dict1):
            no_in_dict1[simbol + ' ' + k] = i
    return no_in_dict1


def item_in_dicts(dict1, dict2):
    dict_sum = {}
    for k, i in dict1.items():
        if (k in dict2):
            if i == dict2[k]:
                dict_sum['  ' + k] = i
            else:
                dict_sum['- ' + k] = i
                dict_sum['+ ' + k] = dict2[k]
    return dict_sum


def format_str_out(dictunform):
    str_form = ''
    for i, k in dictunform.items():
        str_form += f"{str(i)}: {str(k)}\n"
    return str_form


def generate_diff(file_path1, file_path2):
    getfile1 = json.load(open(file_path1))
    getfile2 = json.load(open(file_path2))
    dictdiff = find_dict2_in_dict1(getfile1, getfile2, '+')
    dictdiff.update(find_dict2_in_dict1(getfile2, getfile1, '-'))
    dictdiff.update(item_in_dicts(getfile1, getfile2))
    dictdiff = dict(sorted(dictdiff.items(), key=lambda x: x[0][1:]))
    list_dict = '{\n' + format_str_out(dictdiff) + '}'
    return list_dict