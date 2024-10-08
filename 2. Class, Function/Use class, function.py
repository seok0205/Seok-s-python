class Person:   #Person 클래스 선언.
    def __init__(self, age, name, gender):  #생성자 메서드이고 age, name, gender을 매개변수로 함.
        while 1:    #유효성 검사. 입력된 변수가 male, female 둘중의 하나가 아니라면 반복해서 재입력.
            if gender != 'male' and gender != 'female':
                print("incorrect. write 'male' or 'female'.")
                gender = input("gender: ")
            elif gender == 'male' or gender == 'female':
                break
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):  #self 인수를 받기 때문에, 객체 생성 시 입력된 매개변수와 공유.
        print(f"name: {self.name}, gender: {self.gender}")
        print(f"age: {self.age}")
        
    def greet(self):    #나이가 19세 이상이라면 성인, 아니라면 미성년자에 어울리는 문장 출력.
        if int(self.age) > 19:
            print(f"Hi, {self.name}! You're adult!")
        else:
            print(f"Hi, {self.name}! Where are your parents?")

s_age = input("age: ")  #나이,이름,성별 입력.
s_name = input("name: ")
s_gender = input("gender: ")

someone = Person(s_age, s_name, s_gender)   #입력 받은 정보로 클래스 객체 생성.

someone.display()   #someone객체의 기능 실행.
someone.greet()