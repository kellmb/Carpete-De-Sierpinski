import tkinter as tk

class CarpeteSierpinski:
    #inicialização da janela
    def __init__(self, mestre):
        self.mestre = mestre
        self.mestre.title("Carpete de Sierpinski")
        self.canvas = tk.Canvas(self.mestre, width=600, height=600, bg="white")
        self.canvas.pack()
        self.nivel = 0
        self.desenhar_carpete_sierpinski(0, 0, 600, self.nivel)
        # evento pra detectar a tecla enter
        self.mestre.bind("<Return>", self.proximo_nivel)
        print("Pressione Enter para avançar o nível do fractal")

        # evento pra detectar a roda do mouse
        self.canvas.bind("<MouseWheel>", self.zoom)

        self.scale = 1.0
        self.orig_x = 300
        self.orig_y = 300


    def desenhar_carpete_sierpinski(self, x, y, tamanho, nivel):
        # caso base
        if tamanho < 1:
            return

        if nivel == 0:
            self.canvas.create_rectangle(x, y, x + tamanho, y + tamanho, fill="purple")
            self.canvas.create_rectangle(x + tamanho / 3, y + tamanho / 3, x + 2 * tamanho / 3, y + 2 * tamanho / 3, fill="white")
        else:
            # divide em 9 partes e chama função em 9 delas recursivamente
            novo_tamanho = tamanho / 3
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        # preenche o do meio com a cor branca
                        self.canvas.create_rectangle(x + novo_tamanho, y + novo_tamanho, x + 2 * novo_tamanho, y + 2 * novo_tamanho, fill="white")
                    else:
                        #chamada recursiva
                        self.desenhar_carpete_sierpinski(x + i * novo_tamanho, y + j * novo_tamanho, novo_tamanho, nivel - 1)

    def proximo_nivel(self, event):
        self.nivel += 1
        self.canvas.delete("all")
        self.desenhar_carpete_sierpinski(0, 0, 600, self.nivel)
        print(f"Nível {self.nivel} - Pressione Enter para avançar para o próximo nível")
    
    def zoom(self, event):
        # Determinar o fator de zoom
        factor = 1.1 if event.delta > 0 else 0.9

        # Obter a posição atual do mouse
        mouse_x = self.canvas.canvasx(event.x)
        mouse_y = self.canvas.canvasy(event.y)

        # Aplicar o zoom na posição do mouse
        self.canvas.scale("all", mouse_x, mouse_y, factor, factor)

        # Atualizar a área de scroll
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = CarpeteSierpinski(root)
    root.mainloop()
