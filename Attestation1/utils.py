def print_dict(one_dict):
    if type(one_dict) == dict:
        print('****************************************')
        for item in one_dict:
            print(f'{item}: {one_dict.get(item)}')
        print('****************************************')
    else:
        for element in one_dict:
            print('****************************************')
            for unit in element:
                print(f'{unit}: {element.get(unit)}')
            print('****************************************')
