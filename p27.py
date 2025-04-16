def cnt( sent, cnt_word ):
    cnt = 0
    for i in sent :  # I am a Student 
       if( cnt_word == i ) :
           cnt = cnt + 1
    return cnt   
sent = input("영어문장을 입력하세요 ")
cnt_word = input("알파벳 하나를 입력하세요 ")
result = cnt( sent, cnt_word ) 
print( sent, "에 포함된 ", cnt_word, "의 개수는 ", str( result ), "개 입니다" )