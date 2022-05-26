#파일 테스트
'''
#절대경로로 파일 생성
f = open('C:/Repository/StudyPython_Kasan/Day 4/sample2.log',mode = 'w',\
        encoding = 'utf-8')
f.write('테스트, 테스트!!')
'''

#상대경로로 파일 생성  : 경로를 알고 있을 때, 코드를 짧게 작성하기 위함 (헷갈릴 수 있음!!)
#f = open('./sample2.log',mode = 'w',encoding = 'utf-8')  #바깥 파일에 생성
f = open('./Day 4/sample3.log',mode = 'w',encoding = 'utf-8')  #Day 4 폴더에 생성
f.close()
print('로그파일 생성완료')