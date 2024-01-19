sanab = 1
def play(level):
    global sanab
    from random import randint, choice
    print(f'{level}-levelga xush kelibsiz')
    
 #   for i in range(2,12):
    num1 = randint(0, sanab*3)
    num2 = randint(0, sanab*3)
    sanab += 1
    amal = choice(['-', '+'])
    javob = int(input(f'{num1} {amal} {num2} = '))
    loyiha = [javob, num1, num2,   amal]
    return loyiha