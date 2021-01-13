class Nepal:
    def capital(self):
        print("capital: KTM")

    def language(self):
        print("language: Nepali")

    def __str__(self):
        return "Nepal"


class USA:
    def capital(self):
        print("capital: Washington D.C")
    def language(self):
        print("language: English")

    def __str__(self):
        return "USA"


nepal = Nepal()
usa = USA()

for country in (nepal, usa):
    print(country)
    country.capital()
    country.language()
    print()