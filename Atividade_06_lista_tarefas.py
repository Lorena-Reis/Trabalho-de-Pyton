class ListaaFazer:
    def __init__(self):
        self.tarefas = []

    def add_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada.')

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            print(f'Tarefa "{tarefa}" removida.')
        else:
            print(f'Tarefa "{tarefa}" não encontrada.')

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            print("Lista de Tarefas:")
            for idx, tarefa in enumerate(self.tarefas, start=1):
                print(f'{idx}. {tarefa}')

def main():
    Lista_aFazer = ListaaFazer()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            task = input("Digite a tarefa a ser adicionada: ")
            Lista_aFazer.add_tarefa(task)
        elif opcao == '2':
            task = input("Digite a tarefa a ser removida: ")
            Lista_aFazer.remover_tarefa(task)
        elif opcao == '3':
            Lista_aFazer.listar_tarefas()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
