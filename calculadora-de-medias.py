qnt_a = int(input('Quantos alunos?: '))
#quantidade de alunos que quer calcular.

for a in range(qnt_a):
#laço de repetição de acordo com a quantidade de alunos.

    nome = input('Nome do aluno(a): ')
    #nome dos alunos.
    qnt_n = int(input('Quantas notas?: '))
    #quantidade de notas qu esse aluno tem.

    soma = 0
    #soma é as notas dos alunos somadas, definida aqui inicialmente em 0.

    for i in range(qnt_n): #laço de repetição, que vai pedir cada nota do aluno.
        nota = float(input('Nota: '))#cada nota do aluno.
        soma += nota #resultado de cada nota somada.

    media = soma / qnt_n 
    #aqui ele vai pegar a soma e dividir pela quantidade de notas, tendo assim a média do aluno.

    print(nome, media) #aqui ele vai exibir o nome e a nota média de cada aluno.

    if media >= 6:
        print('Aprovado!') #se a média for maior ou igual a 6, ele receberá o aprovado.
    else:
        print('Reprovado!') #se a média for menor do que 6, ele será reporvado.