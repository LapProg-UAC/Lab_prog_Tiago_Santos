from lp_somatorios import lista_somas

def main() -> None:
    n: int = int(input("Inteiro (>= 0) -> "))
    # testa erro (n = -1); termina para n < -1
    while n >= -1:
        try:
            print("Somatórios", lista_somas(n))
        except ValueError as ve:
            print(ve)
        n: int = int(input("Inteiro (>= 0) -> "))
    print(f"Terminou: n ={n} (<-1)")

main()
