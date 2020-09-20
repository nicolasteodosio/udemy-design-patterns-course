from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass # noop

    def scan(self, document):
        raise NotImplementedError('Printer cannot scan')


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def fax(self, document):
        pass


class NewMachine(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass


    @abstractmethod
    def scan(self, document):
        pass
