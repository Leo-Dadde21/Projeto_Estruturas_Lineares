import os
os.system('cls')

fila_atendimento = []

while True:
    print("\nSECRETARIA ACADEMICA")
    print("[1] - Retirar senha")
    print("[2] - Chamar próximo aluno")
    print("[3] - Mostrar fila")
    print("[4] - Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        nome = input("Nome do aluno: ")
        fila_atendimento.append(nome)
        print(f"{nome} entrou na fila de atendimento.")
        
    elif opcao == '2':
        if len(fila_atendimento) > 0:
            aluno_chamado = fila_atendimento.pop(0)
            print(f"Chamando aluno: {aluno_chamado}")
        else:
            print("A fila está vazia. Não há alunos aguardando atendimento.")
            
    elif opcao == '3':
        if len(fila_atendimento) > 0:
            print("Fila atual:")
            for i, aluno in enumerate(fila_atendimento, start=1):
                print(f"{i}° - {aluno}")
        else:
            print("A fila está vazia.")
            
    elif opcao == '4':
        print("Encerrando o sistema de atendimento...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")