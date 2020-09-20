###### Princípio da substituição de Liskov

Se é uma classe filha (sub-classe), então qualquer método/objeto da classe pai pode ser substituído
pelo da classe filha e continuar correta

No case se eu tenho uma classe Calculator que calcula uma soma de dois inteiros,
 caso eu crie uma classe DividerCalculator que também faz uma operação com dois inteiros, 
 mas no caso uma divisão, ele sim funciona porém, não existe divisão por zero logo é esperado um erro.
Então a classe filha NÃO consegue herdar da classe pai sem modificação e continuar correta

```python
class Calculator:
    def calculate(self, a, b): # returns a number
        return a * b

class DividerCalculator(Calculator):
    def calculate(self, a, b): # returns a number or raises an Error
        return a / b

calculation_results = [
    Calculator().calculate(3, 4),
    Calculator().calculate(5, 7),
    DividerCalculator().calculate(3, 4),
    DividerCalculator().calculate(5, 0) # 0 will cause an Error
]

print(calculation_results)

```

[Code example](./liskov.py)