class Fractie:
    def init(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, fraction):
        numitor_comun = self.numitor * fraction.numitor
        numarator_unu = self.numarator * fraction.numitor
        numarator_doi = fraction.numarator * self.numitor
        numarator_nou = numarator_unu + numarator_doi
        return f"{numarator_nou}/{numitor_comun}"

    def __sub__(self, fraction):
        numitor_comun = self.numitor * fraction.numitor
        numarator_unu = self.numarator * fraction.numitor
        numarator_doi = fraction.numarator * self.numitor
        numarator_nou = numarator_unu - numarator_doi
        return f"{numarator_nou}/{numitor_comun}"

    def inverse(self):
        return f"{self.numitor}/{self.numarator}"
