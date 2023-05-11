## Jogo Pedra-Papel-Tesoura

# S0, estado inicial:
s=[]

# Player
player = [("jogador1", "jogador2")]

# Ações
acoes=[("Pedra","Pedra"), ("Pedra", "Papel"), ("Pedra", "Tesoura") ("Papel", "Pedra"),("Papel","Papel"), ("Papel","Tesoura"), ("Tesoura","Pedra"), ("Tesoura","Papel"), ("Tesoura", "Tesoura") ]

# Resultado
def resultado(i,s):
    s.append(acoes[i])
    return s

# Terminal
def terminal(s):
    return len(s) != 0

# Utilidade
def utilidade(s):
    a1, a2 = s[0] #a1,a2 são as ações do jogador 1 e 2, respectivamente
    if a1==a2 : return(0,0)
    elif a1 == "Pedra":
        return ( (-1,1) if a2  == "Papel" else (1,-1) )
    elif a1 == "Tesoura":
        return( (-1,1) if a2 == "Pedra" else (1,-1) )
    elif a1 == "Papel":
        return( (-1,1) if a2 == "Tesoura" else (1,-1) )
    


