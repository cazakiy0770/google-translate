
import pyttsx3
import random
from math import*

pyttsx3.speak("Salom    sen     men     bilan    gaplashishni    hoxlaysaanmi    ha    yoki     yoqq")
a=input("Salom men bilan gaplashishni hoxlaysanmi hayoki yo'q;")
if a=="ha":
    pyttsx3.speak("menga nima deb ism quyasan;")
    q=input("menga nima deb ism quyasan;")
    pyttsx3.speak(f"Mening ismim {q}")
    print(f"Mening ismim {q}")
    pyttsx3.speak("Sening isming nima:")
    w=input("Sening isming nima:")
    pyttsx3.speak(f"Tanishganimga xursandman {w}")
    print(f"Tanishganimga xursandman {w}")
  
    while True:
      pyttsx3.speak(f"Sen bilan nima qilamiz men zirikib ketyapman")
      print(f"Sen bilan nima qilamiz men zirikib ketyapman")
      pyttsx3.speak("Xoxlasang matematika bilan shug'ullanamizma")
      print("Xoxlasang matematika bilan shug'ullanamizma")
      pyttsx3.speak("Yoki qiziqarli test utkizamizma")
      print("Yoki qiziqarli test utkizamizma")
      pyttsx3.speak("Agar matematika bilan shugullanadigan bolsag mati yaki test utkizmoqchi bolsak test deb yozing")
      print("Agar matematika bilan shugullanadigan bolsag mate yaki test utkizmoqchi bolsak test deb yozing")
      e=input(f">>>")
      if e=="test":

          while True:
           
              if e=="test":
                pyttsx3.speak("Bu test orrqali  sezning sevging iz necha foiz ekaninni billib olasiz")
                print("Bu test orqalisezning sevgingiz necha foiz ekanini bilib olasiz")
                pyttsx3.speak("O'gilbolamisiz(1) yoki qizbola(0) tanlang birordasini")
                print("O'gilbolamisiz(1) yoki qizbola(0) tannlang birordasini")
                pyttsx3.speak("jav obingiz")
                javob1=int(input("javobingiz;"))
                if javob1==1:
                  pyttsx3.speak("sevgan qizingizni ismini yozing;")
                  g=input("sevgan qizingizni ismini yozing;")
                else: 
                  pyttsx3.speak("yigitingizni ismini yozing;")
                  g=input("yigitingizni ismini yozing;")
              def fi_02():
                  hisab = len(g) + len(g)
                  if hisab > 10:
                    y=40
                    x=100
                  else:
                    y=20
                    x=100
                  qwert = random.randint(y, x)
                  if qwert < 50:
                    pyttsx3.speak(f"{qwert}% sevarkan. {w} seni {se02} sevmaykan")
                    print(f"{qwert}% sevarkan. {w} seni {se02} sevmaykan")
                  elif 70>qwert>50:
                    pyttsx3.speak(f"{qwert}% sevarkan. {w} sen {se02}dan pul undiradigan darajada u seni sevmaykan ")
                    print(f"{qwert}% sevarkan. {w} sen {se02}dan pul undiradigan darajada u seni sevmaykan ")
                  elif 70 < qwert < 90:
                    pyttsx3.speak(f"{qwert}% sevarkan. {w} seni {se02} o'lib quguday sevadi, o'zini osib quyguday sevadi. Xuddi toshbaqa tuxumini yxshi kurganday sevadi ")
                    print(f"{qwert}% sevarkan. {w} seni {se02} o'lib quguday sevadi, o'zini osib quyguday sevadi. Xuddi toshbaqa tuxumini yxshi kurganday sevadi ")

                
                  else:
                    pyttsx3.speak("Bu hammasi hazil edi u seni bir teyingayan olmaydi latta")
                    print("Bu hammasi hazil edi u seni bir teyingayan olmaydi latta")
                  fi_02()
              break
        
          
      elif e=="mate":
          pyttsx3.speak('kankuliyator yoki kvadrat tenglamalardan bittasini tanlang')
          print('kankuliyator yoki kvadrat tenglamalardan bittasini tanlang')
          pyttsx3.speak('tendlama yoki hisob ')
          assa = input('tendlama yoki hisob ')
  
          if assa == "hisob" :
           # pyttsx3.speak('sonlar ustida amallar bajaruvchi dastur')
            print('sonlar ustida amallar bajaruvchi dastur')
           # pyttsx3.speak('dasturni boshidan boshlan uchun zz deb yozing')
            print('dasturni boshidan boshlan uchun zz deb yozing')

            while True:
              pyttsx3.speak('a=')
              a = int(input('a='))
              pyttsx3.speak('b=')
              b = int(input('b='))
              q=input('+/-/*/div/**:')
              if q=='+':
                c=a+b          
              elif q=='-':
                c=a-b            
              elif q=='*':
                 c=a*b              
              elif q=='div':
                 c=a/b             
              elif q=='**': 
                 c=a**b              
              else:
                  a='zz'              
                  break
              print(f"javobi=c")
   #           break
            
          else:
 #         from math import*
            pyttsx3.speak('son kirit a =')
            a = int(input('son kirit a ='))
            pyttsx3.speak('son kirit b =')
            b = int(input('son kirit b ='))
            pyttsx3.speak('son kirit c =')
            c = int(input('son kirit c ='))
          
            D = (b**2)-4*a*c
            if D > 0:
              x1=(-b+sqrt(D))/2*a
              x2=(-b-sqrt(D))/2*a
              print(x1, x2)
            elif D == 0:
               x = -b/2*a
               print(x)
            else:
               pyttsx3.speak('yechim yuq')
               print('yechim yuq')
            
      












        







      #     pyttsx3.speak(a)