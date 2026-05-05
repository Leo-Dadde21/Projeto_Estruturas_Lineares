Desafio 1: Sistema de Votação para Representante
1. Qual problema o programa resolve:
O programa automatiza o processo de votação para representante de classe. Ele permite que os alunos votem repetidamente em três candidatos válidos (Ana, Bruno ou Carlos), valida as entradas para evitar votos nulos por erro de digitação, e ao final da votação (quando o usuário digita "fim"), realiza a apuração contabilizando os votos, declarando o vencedor ou indicando se houve empate.

2. Quais estruturas foram utilizadas:

Listas (list): Para armazenar o registro de todos os votos (append) e contá-los nativamente (count).
Laço de repetição (while True): Para manter o sistema rodando até que o comando de parada seja acionado.
Estruturas condicionais (if/else): Para validar se o voto pertence aos candidatos disponíveis e definir a lógica de empate/vitória.
Dicionário (dict): Para associar facilmente cada candidato ao seu número total de votos.

3. Como executar o programa:
No terminal, execute o arquivo correspondente ao desafio (ex: python desafio1.py). O sistema exibirá os candidatos e aguardará a digitação do nome do escolhido. Para encerrar e ver os resultados, digite fim.

4. Exemplo de entrada e saída:

ENTRADA:
Candidatos:
1 Ana
2 Bruno
3 Carlos
Digite o nome do candidato (fim para encerrar): 

SAIDAS:
Resultado da votação:
Ana: 2 votos
Bruno: 3 votos
Carlos: 3 votos
Houve um empate entre os candidatos.

ou

Resultado da votação:
Ana: 5 votos
Bruno: 2 votos
Carlos: 2 votos
O vencedor é: Ana



Desafio 2: Editor de Texto (Pilha - LIFO)
1. Qual problema o programa resolve:
O programa simula a funcionalidade de "Desfazer" de um editor de texto clássico. Ele resolve o problema de armazenar um histórico de palavras digitadas e garantir que, ao solicitar a reversão de uma ação, a última palavra digitada seja a primeira a ser apagada, evitando também erros caso o usuário tente desfazer algo em um texto vazio.

2. Quais estruturas foram utilizadas:

Lista atuando como Pilha (Stack): Utilizando o princípio LIFO (Last In, First Out).
Métodos de Lista: append() para inserir no topo da pilha e pop() para remover o elemento do topo.
Laço (while True) e Condicionais (if/elif/else): Para criar e gerenciar o menu interativo de opções.
Manipulação de String: O método " ".join() foi usado para transformar a lista de palavras em uma frase legível.

3. Como executar o programa:
No terminal, execute o arquivo (ex: python desafio2.py). Um menu numérico de 1 a 4 será exibido. Digite o número correspondente à ação que deseja realizar (Digitar, Desfazer, Mostrar ou Sair) e pressione Enter.

4. Exemplo de entrada e saída:

ENTRADA:
EDITOR DE TEXTO
[1] - Digitar palavra
[2] - Desfazer ultima palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção:

SAÍDAS POSSÍVEIS:
[1] - Digitar palavra
[2] - Desfazer ultima palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 1
Digite uma palavra: minha
Palavra adicionada: minha ('aqui mostra quando o usuário digitar a palavra, e mostra a palavra adicionada')

'Usuário escolheu digitar outra palavra:'
EDITOR DE TEXTO
[1] - Digitar palavra
[2] - Desfazer ultima palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 1
Digite uma palavra: terra
Palavra adicionada: terra ('aqui mostra quando o usuário digitar a palavra, e mostra a palavra adicionada')

'Usuário escolheu mostrar as palavras digitadas até agora:'
EDITOR DE TEXTO
[1] - Digitar palavra
[2] - Desfazer ultima palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 3
Texto atual: minha terra

'Usuário escolheu desfazer a ultima palavra:'
EDITOR DE TEXTO
[1] - Digitar palavra
[2] - Desfazer ultima palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 2
Palavra removida: terra



Desafio 3: Fila de Atendimento (Fila - FIFO)
1. Qual problema o programa resolve:
O programa organiza o fluxo de atendimento de uma secretaria acadêmica, garantindo justiça na ordem de espera. Ele resolve o problema de ordenação ao garantir que o primeiro aluno a retirar uma senha e entrar na fila será o primeiro a ser chamado para atendimento, incluindo tratativas para não permitir a chamada de alunos se a fila estiver vazia.

2. Quais estruturas foram utilizadas:

Lista atuando como Fila (Queue): Utilizando o princípio FIFO (First In, First Out).
Métodos de Lista: append() para adicionar alunos ao final da fila e pop(0) para remover e retornar sempre o elemento da posição zero (o primeiro da fila).
Laço e Condicionais: Para navegação segura no menu.
Função enumerate(): Utilizada para gerar a numeração visual da fila de forma automática na hora de exibi-la.

3. Como executar o programa:
No terminal, rode o arquivo (ex: python desafio3.py). Use o menu numérico para retirar senhas (adicionar nomes), chamar o próximo, visualizar quem está aguardando ou sair do sistema.

4. Exemplo de entrada e saída:

ENTRADA:
SECRETARIA ACADEMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 

'Usuário tentou retirar uma senha:'
SECRETARIA ACADEMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 1
Nome do aluno: Marco ('aqui o usuário digita o nome dele')
Marco entrou na fila de atendimento. ('aqui aparece quando o usuário digitar o nome dele')

'Usuário escolheu tentar mostrar a fila:'
SECRETARIA ACADEMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 3
Fila atual:
1° - Marco

'Usuário escolheu chamar o próximo da fila:'
SECRETARIA ACADEMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 2
Chamando aluno: Marco

'Usuário mostrar a fila após atender o aluno:'
SECRETARIA ACADEMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 3
A fila está vazia.

