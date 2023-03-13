from pyexcel_xlsx import get_data


def xlsx_to_json(filepath, sheetName ,source_file):
    data = get_data(filepath)
    sheetName = sheetName
    new_dict = {}

    data_list = []
    # Iterate through each row and append in above list
    for i in range(0, len(data[sheetName])):
        try:
            data_list.append({
                data[sheetName][i][0]: data[sheetName][i][2]
            })
        except:
            pass
    for d in data_list:
        q = new_dict.update(d)

    # Remove the first key from the dict

    (k := next(iter(new_dict)), new_dict.pop(k))
    f = open(project_locales_path,'w+')
    f.write(new_dict)
    f.close()
    return new_dict
