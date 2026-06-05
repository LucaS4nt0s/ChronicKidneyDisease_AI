def ler_arff(caminho_arquivo):
    atributos = []
    dados = []
    lendo_dados = False

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            
            if not linha or linha.startswith('%'):
                continue

            if linha.upper().startswith('@ATTRIBUTE'):
                partes = linha.split()
                if partes[1].startswith("'") and partes[1].endswith("'"):
                    partes[1] = partes[1][1:-1]
                nome_atributo = partes[1]
                atributos.append(nome_atributo)
            
            elif linha.upper().startswith('@DATA'):
                lendo_dados = True

            elif lendo_dados:
                valores = [valor.strip() for valor in linha.split(',')]
                dados.append(valores)

    return atributos, dados

def main():
    caminho = './base_de_dados/chronic_kidney_disease.arff'

    try:
        atributos, dados = ler_arff(caminho)

        print("ATRIBUTOS LIDOS:")
        print(atributos)

        print("\nPRIMEIROS 5 DADOS LIDOS:")
        for i in range(min(5, len(dados))):
            print(dados[i])

        print(f"\nTotal de atributos: {len(atributos)}")
        print(f"Total de dados: {len(dados)}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")

if __name__ == "__main__":
    main() 