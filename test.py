import pygame

def main():
    # Inicialize o pygame
    pygame.init()

    # Defina as dimensões da janela
    largura_tela, altura_tela = 800, 600  # Substitua por suas próprias dimensões

    # Carregue sua imagem de mapa
    mapa = pygame.image.load("assets\maps\map_1.png")

    # Redimensione a imagem para se ajustar à janela
    mapa = pygame.transform.scale(mapa, (largura_tela, altura_tela))

    # Crie uma janela com as dimensões especificadas
    screen = pygame.display.set_mode((largura_tela, altura_tela))

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pressione a tecla ESC para sair
                    running = False

        # Desenhe a imagem de mapa na tela
        screen.blit(mapa, (0, 0))

        # Atualize a tela
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()