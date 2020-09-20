###### Princípio do aberto/fechado

Sua classe deve ser fechada para modificação e aberta para extensão
Exemplo, imagine que existe uma classe de produto:
	
```python
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name
```

E agora o gerente de produto queira adicionar a funcionalidade de filtrar os produtos por cor, então lembrando do princípio de responsabilidade única, criamos uma classe de para filtrar os produtos e criamos o método de filtrar por cor:
	
```python 
class ProductFilter:

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p
```

Agora é necessária a funcionalidade de filtrar por tamanho:

```python
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

```

E agora a de tamanho e cor:
	
```python
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p
```

Agora imagina que é possível filtrar por 10 coisas diferentes com **ANDs** e **ORs**, isso claramente não é escalável.

Então para demonstrar o princípio do aberto/fechado, vamos utilizar o Enterprise Pattern chamado Specification.
Criaremos duas classes bases que serão sobrescritas:

```python
class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass
```

Então ao invés de adicionar mais métodos para o ProductFilter, podemos faze-lo herdar dessas classes bases para realizar o filtro. Como queremos realizar um filtro por cor e tamanho, primeiramente criamos as especificações para eles, herdando da classe base Specification:

```python
class ColorSpecification(Specification):

    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):

    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

```

E agora a classe de Filter pode utilizas essas especificações para realizar a filtragem:

```python
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

```
		
Você pode-se perguntar o porque de herdar de filter pra fazer essa validação se poderíamos realizar na classe base, nesse caso mantendo o princípio de aberto-fechado no nosso caso items é uma lista agora imagina se item fosse um json, assim teríamos que modificar a classe base para trabalhar com json e desse jeito só é necessário herdar e criar o necessário para esse novo tipo de dado.

Então para mostrar o uso dos dois tipos de filtro que criamos, vamos primeiro criar os produtos:

```python
if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

```

Pra fazer o filtro com o ProductFilter seria assim:

```python
pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is green')
```

Já utilizando as classes bases primeiramente criamos a especificação e passamos para o BetterFilter:

```python
bf = BetterFilter()
print('Green products (new):')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f' - {p.name} is green')
```

Assim é possível ver que um respeita o princípio do aberto/fechado e o outro não.

[Code example](./aberto_fechado.py)

