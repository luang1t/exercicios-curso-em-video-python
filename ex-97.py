def design_line(msg):
    print("~"*(len(msg)+3))

def escreva(msg):
    design_line(msg)
    print(" ",msg)
    design_line(msg)
    
escreva('Olá, Mundo!')    