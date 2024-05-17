class Film:
    def __init__(self, film, year, director):
        self.film = film
        self.year = year
        self.director = director

    def person(self, name, id):
        return f'Prak 5 ({name} - {id})\n-------------------ELKOM 2-------------------'


# Membuat array of object dari film favorit
film1 = Film("Avatar", 2009, "James Cameron")
film2 = Film("Avengers", 2012, "Joss Whedon")
film3 = Film("Batman", 2005, "Christian Bale")
film4 = Film("Kimetsu no Yaiba", 2019, "Haruo Sotozaki")
film5 = Film("Detective Conan", 2018, "Yuzuru Tachikawa")

# Membuat list of object film
people_list = [film1, film2, film3, film4, film5]

# Membuat objek film
person = Film('', 0, '')

# Memanggil metode person dengan parameter yang sesuai
persons = person.person('Agfan Herru Pratama Hendarsin', '064002100043')
print(persons.center(93))

# Mengakses objek dalam list
loops = 1
for film in people_list:
    print(f'Film favorit ke-{loops}:\nJudul: {film.film}\nRilis: {film.year}\nDirector: {film.director}\n=================')
    loops += 1
