###### Princípio da segregação de Interface

Se você possui uma interface grande, quebre-a em menores e mais específicas. Não faça seu cliente ter que lidar com funções que não são necessárias.

Exemplo, se você possui uma classe(interface) Machine que possui todos esses métodos abaixo:

```python
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

```

Caso seja necessário utilizar essa interface para uma outra interface que não precisa de todos aquieles métodos por exemplo, a classe OldPrinter só necessita do método print, mas por causa da classe pai, tem que  implementar os outros métodos mesmo não os utilizando.

```python
class OldPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass # noop

    def scan(self, document):
        raise NotImplementedError('Printer cannot scan')

```

O que deveria ser feito então ?
Como explicado no início a interface deve ser quebrada em pedaços menores, no caso em vez de criar a classe Machine, vamos criar duas classes Printer e Scanner onde seus métodos são abstratos. Com isso é possível combinar as interfaces para reproduzir o comportamento desejado

```python
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

```

A combinação ficara assim:

```python
class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def fax(self, document):
        pass


```

Mas caso você ainda queira uma interface como a classe Machine, você pode criar a classe herdando das duas outras interfaces porém os métodos continuam sendo abstratos

```python
class NewMachine(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass


    @abstractmethod
    def scan(self, document):
        pass

```
	
	
[Code example](./segregacao_interface.py)