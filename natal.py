import time
import random
import sys
import os
from colorama import init, Fore, Style, Back

init(autoreset=True)

def configurar_janela():
    if os.name == 'nt':
        os.system("title FELIZ NATAL - ESPECIAL WHAM!")
        os.system("mode con: cols=90 lines=30")

def limpar_tela_inicial():
    os.system('cls' if os.name == 'nt' else 'clear')

def esconder_cursor():
    sys.stdout.write("\033[?25l")

def mostrar_cursor():
    sys.stdout.write("\033[?25h")

def mover_cursor_topo():
    sys.stdout.write("\033[H")

def obter_enfeite():
    cores = [Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTWHITE_EX]
    enfeites = ['o', '*', '+', '•', '¥']
    
    if random.random() < 0.15:
        return random.choice(cores) + Style.BRIGHT + random.choice(enfeites) + Style.RESET_ALL
    else:
        return Fore.GREEN + Style.DIM + '*' + Style.RESET_ALL

def animacao_natal_karaoke():
    altura_arvore = 15 
    
    dados_musica = [
        ("A face on a lover", 10),           
        ("With a fire in his heart", 12),    
        ("A man under cover", 10),           
        ("But you tore me apart...", 32),    
        ("Now I've found a real love", 7),   
        ("You'll never fool me again", 999)  
    ]
    
    indice_musica = 0
    contador_frames = 0
    
    configurar_janela()
    limpar_tela_inicial()
    esconder_cursor()

    try:
        while True:
            mover_cursor_topo()
            linhas_buffer = []

            linhas_buffer.append(Fore.RED + "\n" + " " * 5 + "Merry Christmas" + " " * 20 + "Music: LAST CHRISTMAS" + Style.RESET_ALL)
            
            linha_estrela = " " * (altura_arvore + 1) + Fore.YELLOW + Style.BRIGHT + "★" + Style.RESET_ALL
            linhas_buffer.append(linha_estrela + " " * 30)
            
            for i in range(altura_arvore):
                espacos = " " * (altura_arvore - i)
                camada_arvore = ""
                for _ in range(2 * i + 1):
                    camada_arvore += obter_enfeite()
                parte_arvore = f"{espacos}{camada_arvore}"
                
                parte_letra = ""
                if i < len(dados_musica):
                    frase_texto = dados_musica[i][0]
                    if i <= indice_musica:
                        if i == indice_musica:
                            cor_texto = Fore.WHITE + Style.BRIGHT
                            icone = "♫ "
                        else:
                            cor_texto = Fore.CYAN + Style.DIM
                            icone = "  "
                        parte_letra = f"{icone}{frase_texto}"
                
                linhas_buffer.append(f"{parte_arvore}     {Style.RESET_ALL}{cor_texto}{parte_letra}".ljust(90))

            espaco_tronco = " " * (altura_arvore + 1 - 1)
            linhas_buffer.append(f"{espaco_tronco}" + Back.BLACK + Fore.RED + "|||" + Style.RESET_ALL + " " * 50)
            linhas_buffer.append(f"{espaco_tronco}" + Back.BLACK + Fore.RED + "|||" + Style.RESET_ALL + " " * 50)
            linhas_buffer.append(Fore.GREEN + "=" * 60 + Style.RESET_ALL)
            
            print("\n".join(linhas_buffer))

            contador_frames += 1
            duracao = dados_musica[indice_musica][1]
            if contador_frames >= duracao:
                if indice_musica < len(dados_musica) - 1:
                    indice_musica += 1
                    contador_frames = 0
            
            time.sleep(0.2)

    except KeyboardInterrupt:
        mostrar_cursor()
        print("\nBoas Festas!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        caminho_arquivo = os.path.abspath(__file__)
        os.system(f'start cmd /k python "{caminho_arquivo}" modo_janela')
    else:
        animacao_natal_karaoke()