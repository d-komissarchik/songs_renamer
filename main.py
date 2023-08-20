import os

DIRECTORY = r''#путь к папке


def files(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            rename(root, name)

def rename(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)  # получаем путь к старому файлу соединяя ссылку с названием файла
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)  # переименовываем, указывая старый и потом новый путь

def get_valid_name(name):
    pass



if __name__ == '__main__':
    files(DIRECTORY)