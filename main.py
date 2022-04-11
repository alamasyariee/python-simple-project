import os

def main():
    i = 0
    path = input('Masukkan path folder file yang ingin diubah: ')

    for filename in os.listdir(path):
        my_dest = 'img' + str(i) + '.jpg'
        my_source = path + filename
        my_dest += path

        os.rename(my_source, my_dest)
        i = i + 1

if __name__ == '__main__':
    main()