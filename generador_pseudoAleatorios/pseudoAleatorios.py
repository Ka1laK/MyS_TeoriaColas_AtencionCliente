import pandas as pd

class GeneradorPseudoAleatorio:
    def __init__(self, seed, multip, mod):
        self.seed = seed
        self.multip = multip
        self.mod = mod
        self.periodo = -1

    def siguiente(self):
        self.seed = (self.multip * self.seed) % self.mod
        return self.seed / self.mod

    def obtener_periodo(self):
        if self.periodo != -1:
            return self.periodo
        periodo = 0
        numeros = set()
        while True:
            aleatorio = self.siguiente()
            if aleatorio in numeros:
                break
            periodo += 1
            numeros.add(aleatorio)
        self.periodo = periodo
        return periodo

seed = 134339
multip = 6259309
mod = 1073741821
generador = GeneradorPseudoAleatorio(seed, multip, mod)


randoms = [generador.siguiente() for _ in range(10000)]

df = pd.DataFrame(randoms, columns=['Nros PseudoAleatorios'])

df.to_excel('generador_pseudoAleatorios/nros_PseudoAleatorios.xlsx', index=False)