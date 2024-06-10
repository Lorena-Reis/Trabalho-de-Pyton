import tkinter as tk

class Cronometro:
    def __init__(self):
        self.rodando = False
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

        self.janela = tk.Tk()
        self.janela.title("Cronômetro")
        
        self.rotulo_tempo = tk.Label(self.janela, text="00:00:00", font=("Helvetica", 48))
        self.rotulo_tempo.pack()

        self.botao_iniciar = tk.Button(self.janela, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.pack(side=tk.LEFT)

        self.botao_parar = tk.Button(self.janela, text="Parar", command=self.parar)
        self.botao_parar.pack(side=tk.LEFT)

        self.botao_resetar = tk.Button(self.janela, text="Resetar", command=self.resetar)
        self.botao_resetar.pack(side=tk.LEFT)

        self.atualizar_tempo()
    def atualizar_tempo(self):
        if self.rodando:
            self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1            
            tempo_str = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
            self.rotulo_tempo.config(text=tempo_str)

        self.janela.after(1000, self.atualizar_tempo)
    def iniciar(self):
        if not self.rodando:
            self.rodando = True
    def parar(self):
        if self.rodando:
            self.rodando = False
    def resetar(self):
        if not self.rodando:
            self.horas = 0
            self.minutos = 0
            self.segundos = 0
            self.rotulo_tempo.config(text="00:00:00")
def principal():
    cronometro = Cronometro()
    cronometro.janela.mainloop()
if __name__ == "__main__":
    principal()
