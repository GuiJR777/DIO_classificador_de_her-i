from hero_classifier import HeroClassifier


if __name__ == "__main__":
    hero_name = input("Qual o nome do seu herói?\n")
    hero_level = int(input("Qual o level dele? (Apenas numeros)\n"))

    hero_class = HeroClassifier(hero_level).classify()

    print(f"Seu herói de nome {hero_name} é da classe {hero_class}!")
