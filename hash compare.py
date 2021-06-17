#파일명: 31126한병윤
#프로젝트 제목: 특정 파일의 해시값 비교 프로그램

while True:

    import hashlib

    hasher1=hashlib.md5()
    file1=input('1번 파일명을 입력:')
    afile1=open(file1,'rb')
    buf1=afile1.read()
    a=hasher1.update(buf1)
    print('1번 파일의 md5 해시값:',str(hasher1.hexdigest()))
    print(' ')

    hasher2=hashlib.md5()
    file2=input('2번 파일명을 입력:')
    afile2=open(file2,'rb')
    buf2=afile2.read()
    b=hasher2.update(buf2)
    print('2번 파일의 md5 해시값:',str(hasher2.hexdigest()))
    print(' ')
    
    if str(hasher1.hexdigest())==str(hasher2.hexdigest()):
        print('동일')
        break
    else:
         print('다름')
