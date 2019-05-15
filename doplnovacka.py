"""
Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty připravit texty, 
které se časem naučí nazpaměť (jedná se o právní předpisy). Proto jim připravuje 
stále stejný text, ve kterém vynechá nejprve každé 5. slovo, později každé 4. slovo atd.
až se text naučí zpaměti. Výstupem bude nový soubor. Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý 
znak se má zaměnit.

1) Rozdelit string --> seznam
	oddelovac mezera
2) Prochazet prvky seznamu
	= kdyz: to bude 5.(10., 15., atd.) slovo, tak: 

	slovoUpraveno = len(slovo) * '_'

	nebo

	cyklus prochazi znaky slova, slovoUpraveno += '_'

	vysledek.append(slovoUpraveno)

	= else: vysledek.append(prvekSeznamu)

3) vyseledek --> string --> soubor

Rozbor 
načíst soubor
splitnout slova podle mezery do seznamu
procházet jednotlivá slova seznamu
když se jedná o x-té slovo:
procházet písmenka a:
písmenko nahradit pomlčkou
vynechat interpunkci
upravené slovo přidat do seznamu
jinak:
původní slovo přidat do seznamu
seznam spojit pomocí mezery do řetězce, řetězec uložit do nového souboru
"""


def nahrazeni_slova(soubor_nebo_text, kolikate_slovo_nahradit):
	
	try:
		# Otevreni souboru, nacteni obsahu do promene text
		f = open(soubor_nebo_text, 'r')
		text = f.read()
		
		# Zavreni souboru (f.closed je spatne -- vraci jestli je soubor otevreny nebo ne)
		f.close()

	except FileNotFoundError: 
		# Kdyz se nejedna o soubor, beru vstuni parametr jako text
		text = soubor_nebo_text

	# Nahrazeni novych radku za mrizku s mezerou
	text = text.replace("\n", "# ")

	# print(text)
	
	# Rozdeleni textu na jednotlive casti podle oddepovace "mezera"
	seznam = text.split(" ")

	# print(seznam)

	vysledek = []
	interpunkce = ".,?!-;\""

	for i in range(0, len(seznam)):
		slovo = seznam[i]
		slovoUpraveno = ""

		if ((i + 1) % kolikate_slovo_nahradit == 0):
			# Pokud je poradi aktualniho slova rovno nasobku parametru "kolikate_slovo_nahradit"

			# Projdi vsechny pismena v danem slove
			for znak in slovo:

				if znak not in interpunkce:
					# Pokud znak neni interpunkce, nahrad hvezdickou

					slovoUpraveno += "*"
				else:
					# Jinak ponech nezmeneny znak
					slovoUpraveno += znak

			vysledek.append(slovoUpraveno)
		else:
			# Poradi slova neni nasobkem "kolikate_slovo_nahradit"
			vysledek.append(slovo)

	s = " ".join(vysledek)
	s = s.replace("#", "\n")

	# Vytiskni vysledek
	print(s)


soubor = input("Zadej nazev souboru, ktery se ma nacist nebo text: ")
cislo = int(input("Zadej cele cislo - kolikate slovo textu se ma zamenit: "))

nahrazeni_slova(soubor, kolikate_slovo_nahradit=cislo)
