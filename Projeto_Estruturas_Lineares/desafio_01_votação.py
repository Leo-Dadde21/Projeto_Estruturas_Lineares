import os
os.system('cls')

votos = []

candidatos_validos = ["Ana", "Bruno", "Carlos"]

while True:
    print("Candidatos:")
    print("1. Ana")
    print("2. Bruno")
    print("3. Carlos")
    
    voto = input("Digite o nome do candidato (fim para encerrar): ").strip()

    if voto.lower() == "fim":
        break

    if voto.capitalize() in candidatos_validos:
        votos.append(voto.capitalize())
    else:
        print("\nVoto inválido. Tente novamente.")
        input("\nPressione Enter para continuar...")
        print("\n" * 2)
        continue

v_ana = votos.count("Ana")
v_bruno = votos.count("Bruno")
v_carlos = votos.count("Carlos")

print("\nResultado da votação:")
print(f"Ana: {v_ana} votos")
print(f"Bruno: {v_bruno} votos")
print(f"Carlos: {v_carlos} votos")

votos_por_candidato = {"Ana": v_ana, "Bruno": v_bruno, "Carlos": v_carlos}
maior_quantidade = max(votos_por_candidato.values())

vencedores = []
for candidato, total in votos_por_candidato.items():
    if total == maior_quantidade:
        vencedores.append(candidato)

if len(vencedores) > 1:
    print("Houve um empate entre os candidatos.")
else:
    print(f"O vencedor é: {vencedores[0]}")