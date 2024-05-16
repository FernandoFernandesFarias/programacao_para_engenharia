def registraFuncionario(nome, salario=9000):
    print(f"Nome do funcionário: {nome}")
    print(f"Salário do funcionário: {salario}")

def main():
  nome = input("Digite o nome do funcionário: ")
  salario = float(input("Digite o salário do funcionário: ") or "9000")
  registraFuncionario(nome, salario)

main()