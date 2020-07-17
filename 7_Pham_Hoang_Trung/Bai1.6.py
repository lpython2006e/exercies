
import random
score = 0
somay = random.randint(1,20)
while(score<5):
    print('Moi ban doan: ')
    sonhap= int(input())
    score +=1
    if sonhap < somay:
        print("So ban doan nho hon")
    elif sonhap> somay:
        print("So ban nhap lon hon")
    else:
        break

if sonhap == somay:
    print("Ban nhap dung so roi")
else:
    print("ban doan sai")
