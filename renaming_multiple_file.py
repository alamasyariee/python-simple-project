import os

def main():
    i = 1
    path = input('Masukkan path folder file yang ingin diubah: ')

    

    for filename in os.listdir(path):
        arr_path = path.split('/')

        my_dest = arr_path[len(arr_path) - 2] + "-" + str(i) + '.pdf'
        my_source = path + filename
        my_dest = path + my_dest

        os.rename(my_source, my_dest)
        i = i + 1

if __name__ == '__main__':
    main()