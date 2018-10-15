i: int=1
Antonyms = dict();
while i<2:
    inputWord = input("What is your word : ")
    if Antonyms.get(inputWord) != None:
        print(Antonyms[inputWord])
    else:
        YorN = input("I don't know the antonym of " + inputWord + " if you know and want to help me enter Y else enter N:")
        if YorN == str("Y"):
            inputAntonym = input("Enter the antonym of " + inputWord + " :")
            Antonyms[inputWord] = inputAntonym
            Antonyms[inputAntonym] = inputWord
