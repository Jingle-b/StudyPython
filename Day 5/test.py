import os

PRJ_ROOT = os.path.dirname(os.path.abspath(__file__))  #[py 파일이 위치한 경로] : 현재 파일(__file__ :자기자신의미함)이 있는 위치
print(PRJ_ROOT)  

BASE_DIR = os.path.dirname(PRJ_ROOT)  #[프로젝트의 기반이 되는 폴더의 경로] : 이 파일의 전체 경로의 기본이 되는 경로가 어디인지
print(BASE_DIR)  

f = open('./test_console.txt', mode='w', encoding='utf-8')  #실행하면 base directory에 파일이 생성된다.(VS) 
#콤솔에서 진행하면 Day 5 폴더에 생성된다.(직접 경로로 들어가서)  ##상대경로 꼭꼭 체크!(정확한 절대경로만 쓰기에는 복잡해지고, 혼동생길수있음.)
f.write('Hello World\n')
f.close() 