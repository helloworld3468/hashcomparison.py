while True:

    import hashlib

    hasher1=hashlib.md5()
    file1=input('insert file1 name:')
    afile1=open(file1,'rb')
    buf1=afile1.read()
    hasher1.update(buf1)
    print('file1 md5 hash:',str(hasher1.hexdigest()))
    print(' ')

    hasher2=hashlib.md5()
    file2=input('insert file2 name:')
    afile2=open(file2,'rb')
    buf2=afile2.read()
    b=hasher2.update(buf2)
    print('file1 md5 hash:',str(hasher2.hexdigest()))
    print(' ')
    
    if str(hasher1.hexdigest())==str(hasher2.hexdigest()):
        print('Same file')
        break
    else:
         print('A different file')
         print(' ')
         print(' ')
