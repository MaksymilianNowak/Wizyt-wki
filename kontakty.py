print("Wizytówki")
class BaseContact:
    pass
my_character=BaseContact()
type(my_character)
print(my_character)
class BaseContact:
    def __init__(self):
        pass
class BaseContact:
    def __init__(self,name,surname,number,mail):
        self.name=name
        self.surname=surname
        self.number=number
        self.mail=mail
class BusinessContact(BaseContact):
    def __init__(self,position,company,work_number):
        self.position=position
        self.company=company
        self.work_number=work_number
Jacek_Król=BaseContact(name="Jacek",surname="Król",number=+485114372,mail="JacekKrol@armyspy.com")
Jacek_Król1=BusinessContact(position="Kierownik ds.edukacji i szkoleń",company="Handy City",work_number=+485114373)
Danuta_Górska=BaseContact(name="Danuta",surname="Górska",number=+485162396,mail="DanutaGorska@rhyta.com")
Danuta_Górska1=BusinessContact(position="Administrator bazy danych komputera",company="Planiści Liberty Wealth",work_number=+485162395)
Amadej_Adamczyk=BaseContact(name="Amadej",surname="Adamczyk",number=+485168588,mail="AmadejAdamczyk@dayrep.com")
Amadej_Adamczyk1=BusinessContact(position="Technik fiskalny",company="Parada butów",work_number=+485168589)
Adrianna_Czarnecka=BaseContact(name="Adrianna",surname="Czarnecka",number=+485115162,mail="AdriannaCzarnecka@armyspy.com")
Adrianna_Czarnecka1=BusinessContact(position="Programista C++",company="Targ Coffeys",work_number=+485125174)
print(Jacek_Król.name,Jacek_Król.surname,Jacek_Król.number,Jacek_Król.mail)