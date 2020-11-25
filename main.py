"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    M = float(input("Quantos metros quadrados serão pintados ?\n"))
    L = 18 
    G = 3.6
    LS = 80
    GS = 25
    Li = (M / 6) * 1.1
    LAT = math.ceil(Li / L) 
    GAL= math.ceil(Li / G)
    LATS = LAT * LS
    GALS = GAL * GS 
    LAT_M = math.floor(Li / L)
    LAT_MS= LAT_M * LS
    LiF = Li - LAT_M * 18
    GAL_M = math.ceil(LiF  / G)
    GAL_MS = GAL_M * GS
    SM = GAL_MS + LAT_MS
    print (f"O valor gasto comprando apenas latas é de {LATS}.\nSerão necessárias {LAT} latas.\nO valor gasto comprando apenas galões é de {GALS}.\nSerão necessários {GAL}  galões.\nO valor gasto comprando de forma que gere a menor quantidade de desperdício é de {SM}\nSerão necessárias {LAT_M} latas e {GAL_M} galões.")


if __name__ == '__main__':
    main()
