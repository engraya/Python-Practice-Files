class Professionals:

    def __init__(self, name, country, age, job):
        self.name = name
        self.country = country
        self.age = age
        self.job = job

ahmad = Professionals('ahmad', 'nigeria', 23, 'engineer')
abubakar = Professionals('abubakar', 'ghana', 27, 'teacher')
umar= Professionals('umar', 'nigeria', 21, 'doctor')
usman = Professionals('usman', 'burkina faso', 25, 'lawyer')
ali = Professionals('ali', 'egypt', 29, 'programmer')
    

print(ahmad.age)
print(ahmad.name)