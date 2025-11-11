# Detective Quest – Tema 4
# Autor: Gabriel
# Tema: Estrutura de Dados em Python

suspeitos = {}

def adicionar_suspeito(nome, idade, cidade):
    """Adiciona um suspeito ao dicionário."""
    suspeitos[nome] = {'idade': idade, 'cidade': cidade}
    print(f"✅ Suspeito {nome} adicionado com sucesso!\n")

def buscar_suspeito(nome):
    """Busca um suspeito pelo nome."""
    if nome in suspeitos:
        info = suspeitos[nome]
        print(f"🔍 {nome} encontrado:")
        print(f"   Idade: {info['idade']}")
        print(f"   Cidade: {info['cidade']}\n")
    else:
        print("❌ Suspeito não encontrado.\n")

def listar_suspeitos():
    """Lista todos os suspeitos cadastrados."""
    if not suspeitos:
        print("⚠️ Nenhum suspeito cadastrado.\n")
    else:
        print("\n=== Lista de Suspeitos ===")
        for nome, dados in suspeitos.items():
            print(f"- {nome}: {dados['idade']} anos, {dados['cidade']}")
        print()

def remover_suspeito(nome):
    """Remove um suspeito do dicionário."""
    if nome in suspeitos:
        del suspeitos[nome]
        print(f"🗑️ Suspeito {nome} removido com sucesso!\n")
    else:
        print("❌ Suspeito não encontrado.\n")

# Demonstração de uso
if __name__ == "__main__":
    print("=== Detective Quest – Sistema de Investigação ===\n")

    adicionar_suspeito("Ana", 28, "São Paulo")
    adicionar_suspeito("Carlos", 35, "Rio de Janeiro")
    adicionar_suspeito("Beatriz", 22, "Curitiba")

    listar_suspeitos()

    buscar_suspeito("Ana")
    remover_suspeito("Carlos")

    listar_suspeitos()
