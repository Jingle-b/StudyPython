#주소록 프로그램
'''
주소록 프로그램 v1.1
작성일 2022-05-26 14:14
작성자 : santa
설명 : 파일DB를 사용한 주소록 프로그램 test 
'''

import os #운영체제 명령용 모듈

#주소록 클래스
class Contact :  #클래스 내 함수는 모두 self를 넣어줘야 한다.
    name = ''; phone_num = ''; e_mail = ''; addr = ''  #한 줄에 변수 다 나타냄(덜 복잡)
    
    #생성자(constructor) 
    def __init__(self,name,phone_num,e_mail,addr) -> None:  #init은 return을 안쓴다. ##class에만 self 존재 (함수에는 x. self는 매개변수가 아니다.)
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr
        pass

    def __str__(self) -> str:   #str은 문자열(str)을 return
        res_str = f'이름 : {self.name}\n'\
                  f'폰번호 : {self.phone_num}\n'\
                  f'이메일 : {self.e_mail}\n'\
                  f'주소 : {self.addr}\n' \
                   '=============================='
                #여러 줄 작성할 때 이렇게 표기하면 보기 좋음(하지만 get_menu쪽은 마지막에 \붙일 필요 없이도 가능)
        return res_str
    
    def isNameExist(self,name) -> bool:
        if (self.name == name):
            return True
        else :
            return False 

dir_name =  'C:/Repository/StudyPython_Kasan/Day 4/' #마지막에 /꼭 붙여줘야 한다.(폴더 하나 더 생길 수 있음..)

#파일 저장 함수
def save_contacts(contacts):
    #f = open('./Day 4/contacts.txt', mode = 'w', encoding='utf-8')  #상대경로 : 반복하는 코드를 쓰면 상대경로라서 오류가 된다.(콘솔에서 예외발생) 
    #절대경로 사용 (밖에 있음)
    global dir_name
    f = open(f'{dir_name}contact.txt', mode = 'w', encoding = 'utf-8')
    for item in contacts:
        f.write(f'{item.name}/{item.phone_num}/{item.e_mail}/{item.addr}\n') #복사해서 옮겨야 오류 안남!
    f.close()  #파일은 열면 반드시 닫아야 한다. (오픈 하면서부터 같이 작성하기)

#파일 로드 함수 
def loadContacts(contacts):
    #절대경로 사용
    global dir_name
    f = open(f'{dir_name}contact.txt', mode = 'r', encoding = 'utf-8')
    while True:  #한 줄씩 읽음 
        line = f.readline()
        if not line : break
               
        lines = line.replace('\n','').split('/')  # 탈출 문자는 전부 삭제(특히, \n, \r은 무조건 삭제!!)
        contact = Contact(lines[0], lines[1],lines[2],lines[3])
        contacts.append(contact)

    f.close()  #필수!! 파일 닫기


#화면 클리어 함수 
def clearConsole():
    command = 'clear'  #UNIX, LINUX, MACOS 
    if os.name in ('nt','dos'): #Window
        command = 'cls'
    os.system(command)

#사용자 정보 입력 
def get_Contact():
    member = None #로컬 변수 초기화   
    try : 
        (name, phone_num, e_mail, addr) = \
            input('정보 입력(이름, 폰번호, 이메일, 주소) [구분자 : slash(/)]  > ').split('/')
        member = Contact(name, phone_num, e_mail, addr)
            #변수 개수만 다 맞으면 괄호 없어도 됨.
            #print(name,phone_num,e_mail,addr)
    except Exception as ex :
        #print(f'예외 발생! : {ex}')
        print('정확하게 이름/폰번호/이메일/주소 순으로 입력해주세요.')    
        
    return member

#연락처 리스트 출력 함수
def printContacts(contacts):
    for item in contacts: #리스트 원소(Contacts 객체)
        print(item)


#연락처 삭제
def delContact(contacts, name):
    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True :
            del contacts[i]


#연락처 검색 220526 16:14 신규 추가
def searchContact(contacts, name):
    isFind = False

    for i, item in contacts:
        print('------------------------------')
        print(f'{name}님의 연락처 검색 정보입니다.')
        print('------------------------------')
        if item.isNameExist(name) == True :
            isFind == True          
            print('f{item}')
            break
        else :
            print(f'{name}님의 연락처 정보가 없습니다.')
            break

#연락처 수정
def editContact(contacts, name):
    contact = None #수정할 연락처를 담을 변수
    index = -1  #찾은 리스트의 인덱스
    isFind = False

    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True :
            isFind = True
            contact = item 
            index = i 
            break
    
    if isFind == False:
        print('검색 정보가 없습니다.')
    else : 
        #pass # Contact 객체를 보여주고 수정할 값을 입력받기
        print(f'{name}님의 연락처 검색 정보입니다.')
        print(f'{contact.name}/{contact.phone_num}/{contact.e_mail}/{contact.addr}')

        try : 
            #수정할 폰 번호/이메일/주소 입력(키(이름)은 바꾸면 안됨!)
            (phone_num,e_mail,addr ) =\
                input('정보입력(폰번호, 이메일,주소) [구분자 : /]').split('/')
            member = Contact(contact.name,phone_num,e_mail,addr)

            contacts[index] = member #이전값을 새 연락처로 변경 
        except Exception as ex:
            print('정확하게 폰번호/이메일.주소 순으로 입력해주세요.')



#메뉴 출력
def get_menu():  
    str_menu = ('주소록 프로그램 v1.1\n'  #마지막에 \붙일 필요 없는 표기법(소괄호로 wrapping)
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 검색\n'      #22.05.26. 16:09 검색기능 추가 
                '4. 연락처 수정\n'      
                '5. 연락처 삭제\n'
                '6. 프로그램 종료\n'
                )
    print(str_menu)
    menu = input('메뉴 선택 > ')
    try :
        menu = int(menu)
    except : 
        menu = 0
    return menu

#기본 실행 함수
def run(): #일반 함수
    contacts = []  #리스트 변수 (빈 리스트 변수 초기화)
    try : 
        loadContacts(contacts)  
    except Exception as ex:
        print('로딩할 데이터가 없습니다.')
    
    clearConsole()

    while True: #메뉴를 선택하게 하기 위해, 무한루프를 생성한다.
        sel_menu = get_menu()
        if sel_menu == 1:  #연락처 추가
            clearConsole()
            member = get_Contact()
            if (member != None):
                contacts.append(member)
            #contacts.append(member)  #연락처 리스트에 새 연락처 추가
            input('\n계속하려면 아무 키나 누르세요')  #input할 때까지 화면 안넘어감
            clearConsole()
        elif sel_menu == 2: #연락처 출력
            clearConsole()
            print('------------------------------')
            print(f'총 {len(contacts)}건입니다.')
            print('------------------------------')
            printContacts(contacts)
            input('\n계속하려면 아무 키나 누르세요')
            clearConsole()
        elif sel_menu == 3: #연락처 검색
             clearConsole()
             name = input('검색할 이름을 입력해주십시오. > ')
             searchContact(contacts, name)
             input('\n계속하려면 아무 키나 누르세요')
             clearConsole()
        elif sel_menu == 4 : #연락처 수정
            clearConsole()
            name = input('수정할 이름을 입력해주십시오. > ')
            editContact(contacts, name)
            input('\n계속하려면 아무 키나 누르세요')
            clearConsole()

        elif sel_menu == 5: #연락처 삭제
            clearConsole()
            name = input('삭제할 이름을 입력해주십시오. > ')
            delContact(contacts, name)
            input('\n계속하려면 아무 키나 누르세요')
            clearConsole()
        elif sel_menu == 6:  #프로그램 종료를 입력할 때가지 루프한다.
            save_contacts(contacts)  #파일DB에 저장
            break
        else: 
            clearConsole()

if __name__ == '__main__':  #EntryPoint(프로그램 시작점)  
    print('\n프로그램 시작\n')  #프로그램이 시작됨(프로그램의 시작을 지정하는 코드) 
    try : 
        run()
    except KeyboardInterrupt as ex : 
        print('비정상 종료!')

print('프로그램 종료')
