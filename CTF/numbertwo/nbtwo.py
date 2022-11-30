import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('wrong pass')
        return

def main():
    zfile = zipfile.ZipFile('secret.zip')
    passFile = open('password.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print('password = ' + password)
            break