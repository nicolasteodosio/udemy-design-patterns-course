###### Princípio da responsabilidade única

Se você tem uma classe, essa classe tem que ter uma função única e NÃO pegar responsabilidade dos outros.
- Por exemplo uma classe Diário, onde é salvo informações nele:
```python
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)
```

- Podemos acabar adicionando funcionalidades que tem relação com a classe, mas não deveriam fazer parte dela, Ex: Adicionar funções de salvar e carregar um arquivo do Diário, garantindo assim a persistência:

```python
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()
    
    def load(self, filename):
        pass
    
    def load_from_web(self, uri):
        pass
```

Ao criar a classe esse tipo de funcionalidade fazem sentido existir para um Diário, porém agora essa classe tem duas responsabilidades:
* Criar as entradas no diário
* Salvar/Carregar (Persistir) as informações do diário
Ao pensar numa aplicação completa, pode-se considerar que irão existir outros tipos de entradas que não apenas a do Diário, que vão querer salvar e carregar de lugares diferentes, fazendo com que essa funcionalidade tenha que ser modificada pra essas outras situações, imagina que agora é necessário checar a  permissão de salvar o arquivo em determinada pasta, seria necessário modificar todas as classes que possuem o método save e fazer a checagem necessária.
Então o que se pode fazer é separar essa responsabilidade a mais para outra classe, Ex:

```python
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

```

Logo o que podemos retirar disso é que não é bom sobrecarregar os objetos da sua classe com muitas responsabilidades, que pode gerar um anti-pattern de God Object, quando uma classe fica com muitas responsabilidades e normalmente muita grande.


[Code example](./responsabilidade_unica.py)