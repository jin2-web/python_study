def quiz( answer, eng ):
   if( answer == eng ):
      print("맞았습니다")
   else:
      print("틀렸습니다")   

eng_dict = {"house":"집",  "piano":"피아노",  "christmas":"크리스마스",  "friend":"친구", "bread":"빵" }

for eng in eng_dict.keys():
   answer = input(eng_dict[eng] + "의 영어 단어는? ") 
   quiz( answer, eng )
