class Kiosk: 
    def __init__(self):
         
        self.menu = ["아메리카노", "카페라떼", "카푸치노"]
        self.price = [3000, 3500, 4000]

    # 메뉴 출력 메서드
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i + 1, self.menu[i], ' : ', self.price[i], '원')

    # 주문 메서드
    def menu_select(self):
        print()  # 줄 바꿈
        n = 0
        while n < 1 or n > len(self.menu):
            n = int(input("음료 번호를 입력하세요 : "))  # 음료 번호 입력

            # 메뉴판에 있는 음료 번호일 때
            if 1 <= n <= len(self.menu):
                self.price_sum = self.price[n-1]  # 선택 음료의 가격
        
            # 메뉴판에 없는 번호일 때
            else:  
                print("없는 메뉴입니다. 다시 주문해 주세요.")

        # 음료 온도 물어보기
        t = 0  # 기본값을 넣어주고
        while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
            t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            # 문제 2-3. 음료의 온도에 따라 temp 변수를 "HOT" 또는 "ICE"로 지정하세요.   
            if t == 1:
                self.temp = "HOT"
            elif t == 2:
                self.temp = "ICE"
            else:    
                print("1과 2 중 하나를 입력하세요.\n")

        
        print('주문 음료:', self.temp, self.menu[n-1], ' : ', self.price_sum, '원')  # 온도 속성을 추가한 주문 결과 출력

# 예시 사용법
kiosk = Kiosk()
kiosk.menu_print()
kiosk.menu_select()