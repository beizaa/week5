streak1 = """
                 ____
                |    |
                |    O                  5 HAKKINIZ KALDI!!!
                |
                |
               ---                          """
streak2 = """
                 ____
                |    |
                |    O                  4 HAKKINIZ KALDI!!!
                |    |
                |
               ---                            """
streak3 = """
                 ____
                |    |
                |    O                  3 HAKKINIZ KALDI!!!
                |   /|
                |
               ---                            """
streak4 = """
                 ____
                |    |
                |    O                 2 HAKKINIZ KALDI!!!
                |   /|\\
                |   
               ---                            """

streak5 = """
                 ____
                |    |
                |    O
                |   /|\\                 SON SANSINIZ !!!
                |   /
               ---                            """
streak6 = """
                 ____
                |    |
                |    O
                |   /|\\               OYUNU KAYBETTINIZ!!!
                |   / \\
               ---                            """
ss = []
ss.extend([streak1, streak2, streak3, streak4, streak5, streak6])
guess = []
word = "weltschmerz"
a = 1
trials = 1
print(""" Hang man game!""")
while a == 1:
    word2 = ""
    letter = input("letter: ")
    guess.append(letter)
    if len(letter) > 1 or letter.isalpha() == False or letter.islower() == False:
        print('Please enter a lower letter')
    elif letter not in word:
        trials += 1
    if trials == 1:
        print(ss[0])
    if trials == 2:
        print(ss[1])
    if trials == 3:
        print(ss[2])
    if trials == 4:
        print(ss[3])
    if trials == 5:
        print(ss[4])
    if trials == 6:
        print(ss[5])
        break
    for letter in word:
        if letter in guess:
            word2  += letter
        else:
            word2 += " - "
    if word2 == word:
        print("Kelimemiz:", word2, "\nKAZANDINIZ, TEBRIKLER!!!")

        break

    print(word2)

 # for ile kisa yapmaya calistim ama olmadi
 # streak1 = """
 #                  ____
 #                 |    |
 #                 |    O                  5 HAKKINIZ KALDI!!!
 #                 |
 #                 |
#                ---                          """
# streak2 = """
#                  ____
#                 |    |
#                 |    O                  4 HAKKINIZ KALDI!!!
#                 |    |
#                 |
#                ---                            """
# streak3 = """
#                  ____
#                 |    |
#                 |    O                  3 HAKKINIZ KALDI!!!
#                 |   /|
#                 |
#                ---                            """
# streak4 = """
#                  ____
#                 |    |
#                 |    O                 2 HAKKINIZ KALDI!!!
#                 |   /|\\
#                 |
#                ---                            """
#
# streak5 = """
#                  ____
#                 |    |
#                 |    O
#                 |   /|\\                 SON SANSINIZ !!!
#                 |   /
#                ---                            """
# streak6 = """
#                  ____
#                 |    |
#                 |    O
#                 |   /|\\               OYUNU KAYBETTINIZ!!!
#                 |   / \\
#                ---                            """
# ss = []
# ss.extend([streak1, streak2, streak3, streak4, streak5, streak6])
# guess = []
# word = "weltschmerz"
# a = 1
# trials = 1
# print(""" Hang man game!""")
# # while a == 1:
# kelime2 = ""
# letter = input("letter: ")
# guess.append(letter)
# # for i in range(6):
# #     if letter not in word:
# #         trials += 1
# #         print(ss[i])
# # input()

##########################################################################
#Odev2

print("""SAYI TAHMIN OYUNU
Rakamlari 0 olmayan ve birbirlerinden farkli 
 4 basamakli bir sayi giriniz.'
Cikis icin q """)


sayi = '6789'
sayi = list(sayi)
sayac = 0

while True:
    insideandrightplace = 0
    insidebutwrongplace = 0
    sayac += 1
    guess = list(input('Enter your guess:   '))

    for i in guess:
        if i in sayi and guess.index(i) == sayi.index(i):
            insideandrightplace += 1
        elif i in sayi:
            insidebutwrongplace -= 1
    if sayi == guess:
        print("Congrats! You guessed right!")
        break

    print(insideandrightplace, insidebutwrongplace)

