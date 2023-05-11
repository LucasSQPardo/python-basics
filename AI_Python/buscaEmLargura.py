def agenteMapa(ambiente):
    mapa = [ambiente]
    acao = mapa[ambiente]
    return acao

def buscaLargura(estados):
    estadosProx = [] #contem os estados do próximo nível
    for s in estados:
        novosNos = [ resultado(s,a) for a in acoes(s) ]
        estadosprox = estadosProx + novosNos
    if any(atingiuObj(s) for s in estadosprox):
        return solucao(estadosprox)
    return buscaLargura(estadosProx)


def buscaProfundidade(s):
    for a in acoes(s):
        sol = buscaProfundidade(resultados(s,a))
        if atingiuObj(sol):
            return sol
    return 'Error'


def buscaProfundidadeLimite(s, profundidade):
    if profundidade > limite :
        return 'Error'
    for a in acoes(s) : 
        sol = buscaProfundidadeLimite(resultado(s,a), profundidade + 1 )
        
        if atingiuObj(sol):
            return sol
    return 'Error'

def buscaProfundidadeIterativo(s):
    for it in range(maxProfundidade):
        sol = buscaProfundidadeLimite(s, it)
        if sol != 'Error' :
            return sol
    return 'Error'

def buscaGulosa(nos, heuristica):
    no = argmin(nos, heuristica) #verifica qual tem o menor valor de heuristica dentre os nos
    sl = [resultados(no, a) for a in acoes(no)]
    if any(atingiuObj(s) for s in sl):
        return filter(atingiuObj, sl)[0]
    nos = nos.remove(no) + sl

    if nos.Empty():
        return falha
    return buscaGulosa(nos, heuristica)
    
def bestFirst(nos, g, heuristica):
    no = argmin(nos, g, heuristica) #verifica qual tem o menor valor de heuristica dentre os nos
    sl = [resultados(no, a) for a in acoes(no)]
    if any(atingiuObj(s) for s in sl):
        return filter(atingiuObj, sl)[0]
    nos = nos.remove(no) + sl

    if nos.Empty():
        return falha
    return bestFirst(nos, g, heuristica)
        