import os
os.system('cls')

pilha_texto = []

while True:
    print("\nEDITOR DE TEXTO")
    print("[1] - Digitar palavra")
    print("[2] - Desfazer ultima palavra")
    print("[3] - Mostrar texto")
    print("[4] - Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        palavra = input("Digite uma palavra: ")
        pilha_texto.append(palavra)
        print(f"Palavra adicionada: {palavra}")
        
    elif opcao == '2':
        if len(pilha_texto) > 0:
            palavra_removida = pilha_texto.pop()
            print(f"Palavra removida: {palavra_removida}")
        else:
            print("Aviso: O texto já está vazio. Não há nada para desfazer.")
            
    elif opcao == '3':
        texto_atual = " ".join(pilha_texto)
        print(f"Texto atual: {texto_atual}")
        
    elif opcao == '4':
        print("Saindo do editor...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")