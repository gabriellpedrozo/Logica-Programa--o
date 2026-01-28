import random

# Símbolos do caça-níquel
simbolos = ["🍒", "🍋", "⭐", "🔔", "💎"]

def girar():
    return [
        random.choice(simbolos),
        random.choice(simbolos),
        random.choice(simbolos)
    ]

def verificar(resultado):
    if resultado[0] == resultado[1] == resultado[2]:
        print("🎉 VAMOO PORRA!")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2]:
        print("🙂 Quase! gasta mais ae.")
    else:
        print("😢 sem sorte papae.")

# Loop principal
while True:
    input("\nPressione ENTER para girar...")
    
    resultado = girar()
    print(" | ".join(resultado))
    
    verificar(resultado)

    jogar = input("Quer jogar novamente? (s/n): ").lower()
    if jogar != "s":
        print("Obrigado por jogar!")
        break
