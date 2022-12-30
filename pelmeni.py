class eda:

    def __init__(self):
        self._dostupnost = None
        self._cena = None
        self._popul = None

    def set_dostupnost(self, dostupnost):
        self._dostupnost = dostupnost

    def get_dostupnost(self):
        return self._dostupnost

    def set_cena(self, cena):
        self._cena = cena

    def get_cena(self):
        return self._cena

    def set_popul(self, popul):
        self._popul = popul

    def get_popul(self):
        return self._popul

    def info(self):
        print("Доступность по России:", self._dostupnost, "\nЦена за кг:", self._cena, "\nПопулярность по моему мнению:", self._popul)


class pelmeni(eda):

    def __init__(self):

        super().__init__()
        self.__vid = None
        self.__prikol = None
        self.__istochnik = None

    def set_vid(self, vid):
        self.__vid = vid

    def get_vid(self):
        return self.__vid
        
    def set_prikol(self, prikol):
        self.__prikol = prikol

    def get_prikol(self):
        return self.__prikol

    def set_istochnik(self, istochnik):
        self.__istochnik = istochnik

    def get_istochnik(self):
        return self.__istochnik

    def info(self):
        super().info()
        print("Кто ты, воин?: ", self.__vid, "\nПриколный?: ", self.__prikol, "\nОткуда появился: ", self.__istochnik)

hinkali = pelmeni()
hinkali.set_vid("Хинкали")
hinkali.set_dostupnost("8 из 10")
hinkali.set_cena(480)
hinkali.set_popul("Не все в России о них знают")
hinkali.set_prikol("Да")
hinkali.set_istochnik("Грузия")
hinkali.info()
print("\n")

obich = pelmeni()
obich.set_vid("Обычные пельмени")
obich.set_dostupnost("10 из 10")
obich.set_cena(230)
obich.set_popul("Coupe")
obich.set_prikol("Нет")
obich.set_istochnik("Россия")
obich.info()
print("\n")

author = pelmeni()
author.set_vid("Каракал")
author.set_dostupnost("1 из 10")
author.set_cena("Бесценно")
author.set_popul("Его знают не только в России")
author.set_prikol("ДА!")
author.set_istochnik("Украина")
author.info()
print("\n")

jar = pelmeni()
jar.set_vid("Жареные пельмени")
jar.set_dostupnost("7 из 10")
jar.set_cena("Покупай обычные и жарь")
jar.set_popul("Их узнают из тысячи")
jar.set_prikol("Да")
jar.set_istochnik("Планета Земля")
jar.info()
print("\n")

par = pelmeni()
par.set_vid("Беляш")
par.set_dostupnost("10 из 10")
par.set_cena(138)
par.set_popul("Средняя")
par.set_prikol("Ужасный")
par.set_istochnik("Северные азиаты")
par.info()
print("\n")
