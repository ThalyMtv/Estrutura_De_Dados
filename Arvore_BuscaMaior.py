class no_arvore:
    def __init__(self, val):
        self.esq = None
        self.info = val
        self.dir = None


def Insere(Raiz, No):
    if Raiz == None:
        Raiz = No
    else:
        if (Raiz.info < No.info):
            if Raiz.dir == None:
                Raiz.dir = No
            else:
                Insere(Raiz.dir, No)
        else:
            if Raiz.esq == None:
                Raiz.esq = No
            else:
                Insere(Raiz.esq, No)


def Pre_Order(Raiz):
    if Raiz != None:
        print(Raiz.info, " ", end='')
        Pre_Order(Raiz.esq)
        Pre_Order(Raiz.dir)


def In_Order(Raiz):
    if Raiz != None:
        In_Order(Raiz.esq)
        print(Raiz.info, " ", end='')
        In_Order(Raiz.dir)


def Pos_Order(Raiz):
    if Raiz != None:
        Pos_Order(Raiz.esq)
        Pos_Order(Raiz.dir)
        print(Raiz.info, " ", end='')


def Busca(Raiz, val):
    if Raiz == None:
        return None
    else:
        if Raiz.info == val:
            return Raiz
        else:
            if (Raiz.info > val):
                return Busca(Raiz.esq, val)
            else:
                return Busca(Raiz.dir, val)


def BuscaMaior(r):
    if r.esq == None and r.dir == None:
        return r
    else:
        if r.dir == None:
            return r
        else:
            return BuscaMaior(r.dir)


def Buscar_Pai(Raiz, r):
    if (Raiz.esq == r or Raiz.dir == r):
        return Raiz
    else:
        if (r.info > Raiz.info):
            return Buscar_Pai(Raiz.dir, r)
        else:
            return Buscar_Pai(Raiz.esq, r)


def Remove(Raiz, val):
    r = Busca(Raiz, val)
    if r.esq == None and r.dir == None:
        p = Buscar_Pai(Raiz, r)
        if r.info > p.info:
            p.dir = None
        else:
            p.esq = None
    elif r.esq == None or r.dir == None:
        p = Buscar_Pai(Raiz, r)
        if r.esq == None:
            if r.info > p.info:
                p.dir = r.dir
            else:
                p.esq = r.dir
        else:
            p.esq = r.esq
    else:
        if r.esq is not None and r.dir is not None:
            p = BuscaMaior(r.esq)
            rNovo = p.info
            pai = Buscar_Pai(Raiz, p)

            if pai.info < p.info:
                pai.dir = p.esq
            else:
                pai.esq = p.esq

            r.info = rNovo



Raiz = None
while True:
    print("\n1 - Inserir valores")
    print("2 - Percursos")
    print("3 - Buscar Valor")
    print("4 - Buscar o Pai")
    print("5 - Remover um No")
    print("6 - Maior nó à esquerda do valor")

    '''
    1o. caso o nó r é folha
        buscar o pai de r
        trocar o lado esq ou dir do pai para None

    2o. caso o nó r possui apenas um filho
        buscar o pai de r
        trocar o lado esq ou dir do pai com o filho de r

    3o. caso o nó r possui 2 filhos
        buscar em p o maior no do lado esquerdo de r
        trocar o r.info por p.info
        buscar o pai de p
        trocar o lado esq ou dir do pai com o filho esq. de p

    '''

    print("0 - Sair do Programa")

    op = int(input("\nDigite a opcao: "))

    if op == 0:
        break
    elif op == 1:
        val = int(input("Digite o valor a inserir: "))
        No = no_arvore(val)
        if Raiz == None:
            Raiz = No
        else:
            Insere(Raiz, No)

    elif op == 2:
        print("\nPRE:")
        Pre_Order(Raiz)
        print("\nIN:")
        In_Order(Raiz)
        print("\nPOS:")
        Pos_Order(Raiz)

    elif op == 3:
        val = int(input("Digite o valor a buscar: "))
        r = Busca(Raiz, val)

        if r == None:
            print("\nValor nao existe na árvore!")
        else:
            print("\nValor = ", r.info)

    elif op == 4:
        val = int(input("Digite o valor a buscar: "))
        r = Busca(Raiz, val)

        if r == None:
            print("\nValor nao existe na árvore!")
        else:
            if (r == Raiz):
                print("\nA raiz nao tem pai!")
            else:
                pai = Buscar_Pai(Raiz, r)
                print("\n O pai do ", r.info, " = ", pai.info)

    elif op == 5:
        val = int(input("Digite o valor a remover: "))
        r = Busca(Raiz, val)
        if r is None:
            print("\nValor nao existe na árvore!")
        else:
            if r == Raiz:
                print("\nA raiz nao pode ser removida!")
            else:
                Remove(Raiz, val)
                print("\nNúmero removido com sucesso!")

    elif op == 6:
        val = int(input("Digite o valor a buscar: "))
        r = Busca(Raiz, val)
        if r.esq is not None:
            p = BuscaMaior(r.esq)
            print("O maior número encontrado à esquerda do nó ", r.info, " é ", p.info)
        else:
            print("Não foi encontrado um número maior à esquerda do nó ", r.info)




