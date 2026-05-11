import sys
import time
import os
 
# Histórico de fotos tiradas na sessão

historico = []

# UTILITÁRIOS

def carregar_sistema(acao):
    """Animação de carregamento no terminal."""
    for _ in range(3):
        for pontos in range(4):
            sys.stdout.write(f"\r{acao}{'.' * pontos}   ")
            sys.stdout.flush()
            time.sleep(0.4)
    print("\nConcluído!\n")
 
 
def entrada_inteira(mensagem, minimo, maximo):
    """
    Lê um inteiro do usuário com validação.
    Fica pedindo até receber um valor válido dentro do intervalo.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"  ⚠ Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("  ⚠ Entrada inválida. Digite apenas números.")
 
 
def registrar_foto(modo, configuracoes):
    """Salva o registro da foto no histórico da sessão."""
    historico.append({
        "modo": modo,
        "config": configuracoes,
        "hora": time.strftime("%H:%M:%S")
    })


# MODOS DA CÂMERA

def auto():
    """
    Modo automático: a câmera escolhe o melhor ISO e velocidade
    com base na condição de luz informada pelo usuário.
    """
    print("=" * 35)
    print("       MODO AUTOMÁTICO")
    print("=" * 35)
    print("Informe a condição de luz atual:")
    print("  1 - Ambiente claro (sol, área aberta)")
    print("  2 - Ambiente médio (nublado, sombra)")
    print("  3 - Ambiente escuro (noite, interior)")
 
    luz = entrada_inteira("Sua escolha: ", 1, 3)
 
    # Regra de negócio: ajuste automático por condição de luz
    if luz == 1:
        iso = 100
        velocidade = "1/1000s"
        abertura = "f/8"
    elif luz == 2:
        iso = 400
        velocidade = "1/250s"
        abertura = "f/4"
    else:
        iso = 1600
        velocidade = "1/60s"
        abertura = "f/2"
 
    config = f"ISO {iso} | Velocidade {velocidade} | Abertura {abertura}"
    print(f"\n Configuração automática aplicada:\n  {config}")
    registrar_foto("Automático", config)
    return "Modo automático configurado"
 
 
def pets():
    """
    Modo pets: velocidade alta para capturar movimento.
    Botão sonoro opcional para chamar a atenção do animal.
    """
    print("=" * 35)
    print("         MODO PETS")
    print("=" * 35)
 
    # Regra de negócio: velocidade alta para congelar movimento
    iso = 800
    velocidade = "1/500s"
    abertura = "f/3.5"
    config = f"ISO {iso} | Velocidade {velocidade} | Abertura {abertura}"
    print(f" Configurações para pets aplicadas:\n  {config}")
 
    # Funcionalidade extra: botão sonoro
    usar_botao = input("\nUsar botão sonoro para chamar o pet? (s/n): ").strip().lower()
    if usar_botao == "s":
        carregar_sistema("Chamando pet")
        print(" Botão sonoro acionado!")
    else:
        print("Botão sonoro não utilizado.")
 
    registrar_foto("Pets", config)
    return "Modo pets configurado"
 
 
def retrato():
    """
    Modo retrato: fundo desfocado (bokeh).
    Usuário escolhe a distância do sujeito para ajuste fino.
    """
    print("=" * 35)
    print("        MODO RETRATO")
    print("=" * 35)
    print("Qual a distância aproximada do sujeito?")
    print("  1 - Próximo   (até 1 metro)")
    print("  2 - Médio     (1 a 3 metros)")
    print("  3 - Distante  (mais de 3 metros)")
 
    dist = entrada_inteira("Sua escolha: ", 1, 3)
 
    # Regra de negócio: quanto mais próximo, mais aberta a abertura
    if dist == 1:
        abertura = "f/1.8"
        foco = "foco bem próximo"
    elif dist == 2:
        abertura = "f/2.8"
        foco = "foco médio"
    else:
        abertura = "f/4"
        foco = "foco distante"
 
    iso = 200
    velocidade = "1/200s"
    config = f"ISO {iso} | Velocidade {velocidade} | Abertura {abertura} | {foco}"
    print(f"\n Configurações de retrato aplicadas:\n  {config}")
    registrar_foto("Retrato", config)
    return "Modo retrato configurado"
 
 
def paisagens():
    """
    Modo paisagens: máxima nitidez, abertura fechada.
    Usuário informa se há movimento (água, folhas) para ajuste.
    """
    print("=" * 35)
    print("       MODO PAISAGENS")
    print("=" * 35)
 
    # Regra de negócio: abertura fechada para profundidade de campo total
    abertura = "f/11"
    iso = 100
 
    movimento = input("Há elementos em movimento na cena? (s/n): ").strip().lower()
    if movimento == "s":
        velocidade = "1/500s"
        obs = "velocidade alta para congelar movimento"
    else:
        velocidade = "1/125s"
        obs = "velocidade padrão para paisagem estática"
 
    config = f"ISO {iso} | Velocidade {velocidade} | Abertura {abertura} | {obs}"
    print(f"\n Configurações de paisagem aplicadas:\n  {config}")
    registrar_foto("Paisagens", config)
    return "Modo paisagens configurado"
 
 
def manual():
    """
    Modo manual: usuário define ISO e velocidade livremente.
    A câmera valida se os valores estão dentro do suportado.
    """
    print("=" * 35)
    print("        MODO MANUAL")
    print("=" * 35)
    print("Configure os parâmetros manualmente.\n")
 
    # Regra de negócio: ISO entre 100 e 6400, velocidade entre 1 e 4000
    iso = entrada_inteira("ISO (100 a 6400): ", 100, 6400)
    velocidade = entrada_inteira("Velocidade do obturador em 1/Xs — digite X (1 a 4000): ", 1, 4000)
 
    abertura_opcoes = ["f/1.8", "f/2.8", "f/4", "f/5.6", "f/8", "f/11"]
    print("\nEscolha a abertura:")
    for i, op in enumerate(abertura_opcoes, 1):
        print(f"  {i} - {op}")
 
    idx = entrada_inteira("Sua escolha: ", 1, len(abertura_opcoes))
    abertura = abertura_opcoes[idx - 1]
 
    config = f"ISO {iso} | Velocidade 1/{velocidade}s | Abertura {abertura}"
    print(f"\n Configurações manuais aplicadas:\n  {config}")
    registrar_foto("Manual", config)
    return "Modo manual configurado"
 
 
def ver_historico():
    """Exibe todas as fotos registradas na sessão atual."""
    print("=" * 35)
    print("      HISTÓRICO DA SESSÃO")
    print("=" * 35)
 
    if not historico:
        print("Nenhuma foto registrada ainda.")
    else:
        for i, foto in enumerate(historico, 1):
            print(f"\n  Foto {i}:")
            print(f"    Modo   : {foto['modo']}")
            print(f"    Config : {foto['config']}")
            print(f"    Hora   : {foto['hora']}")
    print()
 


# MENU PRINCIPAL

def menu():
    opcoes = {
        1: ("Automático",  auto),
        2: ("Pets",        pets),
        3: ("Retrato",     retrato),
        4: ("Paisagens",   paisagens),
        5: ("Manual",      manual),
        6: ("Histórico",   ver_historico),
        7: ("Sair",        None),
    }
 
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 35)
        print("         CÂMERA — MODOS")
        print("=" * 35)
        for num, (nome, _) in opcoes.items():
            print(f"  {num} - {nome}")
        print("=" * 35)
 
        func_num = entrada_inteira("Escolha uma opção: ", 1, 7)
 
        if func_num == 7:
            os.system("cls" if os.name == "nt" else "clear")
            carregar_sistema("Encerrando câmera")
            print("Até logo!")
            break
 
        os.system("cls" if os.name == "nt" else "clear")
        carregar_sistema("Carregando modo")
 
        nome_modo, funcao = opcoes[func_num]
        resultado = funcao()
 
        if resultado:
            print(f"\n {resultado} — pronto para fotografar.")
 
        input("\nPressione ENTER para voltar ao menu...")

# PONTO DE ENTRADA

if __name__ == "__main__":
    menu()


