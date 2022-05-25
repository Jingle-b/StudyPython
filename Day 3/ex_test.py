#예외처리 테스트

def add(x,y) : 
    res = x+y
    return res

def sub(x,y):
    res = x-y
    return res 

def mul(x,y) : 
    res = x*y
    return res

def div(a,b):  
    """  %%%군더더기인 처리법%%%
    #예외가 발생한 함수 자체의 예외를 처리→ 결론적으로 예외 처리를 두 번이나 하는 것!
    #예외를 처리하면 할수록 컴퓨터가 사용하는 리소스가 증가하므로, 무리를 준다. 즉, 속도 저하를 야기한다.
    try :
        res = x/y   #에러 원인
    except :
        print('예외 발생')
    """
    res = a/b   #에러 원인
    return res

def print_hello():
    print('hello')  #return이 없는 유형 = return이 생략된 유형(돌려줄 값이 없어 return의 존재가 무의미하므로 생략한 것)

print('계산기 시작')
x,y = 4,1  #개수만 맞으면 괄호 안써도 됨
print(f'더하기 {x}+{y} = {add(x,y)}')
try :   #try statement 
    print(f'나누기 {x}/{y} = {div(x,y)}')
    #print('17'+3)
    #int('4.0')
#except ZeroDivisionError as ex:  #ZeroDivisionError 처리
#    print(f'주의! 제수에 0을 넣으면 안됩니다. {ex}')  #error 메세지 출력
#except TypeError as ex : 
#    print('문자열과 수를 +연산으로 더할 수 없습니다.')
except Exception as ex :  #모든 예외에 대한 메세지를 넣음  #Exception : 모든 예외의 부모격이라 모두 포함 가능한 것
    print(f'예외가 발생했습니다.{ex}')   #뒤에 {ex}로 예외 타입 밝힘.

finally: #예외 발생 여부에 관계없이 무조건 실행함 
    print('예외가 발생하는 구간을 지났습니다.')      

print(f'빼기 {x}-{y} = {sub(x,y)}')
print(f'곱하기 {x}*{y} = {mul(x,y)}')
print('계산기 종료')