import math

# Função para calcular o inverso modular multiplicativo
def MMI(a, m):
    m0 = m
    x0, x1 = 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def main():
    sair = "continuar"

    while sair != "sair":
        print("""
*****************************
*         MFA / RSA         *
*****************************
| 1 - Definir chaves RSA     |
| 2 - Criptografar mensagem  |
| 3 - Descriptografar        |
| 4 - Sair                   |
*****************************
""")

        menu = int(input("O que você deseja fazer? "))

        if menu == 1:
            rsa()
        elif menu == 2:
            cod()
        elif menu == 3:
            decod()
        elif menu == 4:
            sair = "sair"
        else:
            print("Número inválido!")


def rsa():
    primook = False
    nums = []
    verifp = False
    verifq = False

    print("Insira dois valores primos P e Q")

    while not verifp:
        p = int(input("Digite P: "))
        if is_primo(p):
            verifp = True
        else:
            print("P não é primo!")

    while not verifq:
        q = int(input("Digite Q: "))
        if is_primo(q):
            verifq = True
        else:
            print("Q não é primo!")

    n = p * q
    fn = (p - 1) * (q - 1)

    print("\nPossíveis valores para chave pública (E):")
    for i in range(2, fn):
        if mdc(i, fn) == 1:
            nums.append(i)

    print(nums)

    while not primook:
        e = int(input("\nDigite um valor para E da lista: "))
        if e in nums:
            primook = True
        else:
            print("Valor inválido, escolha da lista.")

    d = MMI(e, fn)

    print("\nChaves Geradas:")
    print(f"Chave Pública  -> (N = {n}, E = {e})")
    print(f"Chave Privada  -> (P = {p}, Q = {q}, D = {d})\n")


def cod():
    n = int(input("Digite N: "))
    e = int(input("Digite E: "))
    mensagem = input("Digite a mensagem para criptografar: ")

    precod = [ord(c) for c in mensagem]
    mensagem_final = ""

    for num in precod:
        bloco = (num ** e) % n
        mensagem_final += str(bloco) + " "

    print("\nMensagem criptografada:")
    print(mensagem_final.strip(), "\n")


def decod():
    p = int(input("Digite P: "))
    q = int(input("Digite Q: "))
    d = int(input("Digite D: "))

    n = p * q

    cript = input("Digite a mensagem criptografada:\n").split()
    mensagem_ok = ""

    for bloco in cript:
        num = int(bloco)
        dec = (num ** d) % n
        mensagem_ok += chr(dec)

    print("\nMensagem descriptografada:")
    print(mensagem_ok, "\n")


# Função auxiliar: verificação de número primo
def is_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


# Função auxiliar: máximo divisor comum
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


main()
