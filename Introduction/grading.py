score = input("Enter Score between 0 and 1: ")
try :
    conv_score = float(score)
    if conv_score > 1 :
        print('Score invalid')
    elif conv_score < 0 :
        print('Score invalid')
    elif conv_score >= 0.9 :
        print('A')
    elif conv_score >= 0.8 :
        print('B')
    elif conv_score >= 0.7 :
        print('C')
    elif conv_score >= 0.6 :
        print('D')
    elif  conv_score < 0.6 :
        print('F')
except :
    print('Score not entered properly')
