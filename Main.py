from random import randint
welcome_banner = """Welcome to the Random Band Name Generator! Answer the propmts to generate your random band name."""
print(welcome_banner)
lead_singer = input("Lead singer's first name:")
music_adjective = input("Adjective describing the music:")
plural_noun = input("A plural noun:")
month = input("A month of the year:")
verb= input("A verb ending in ing:")
animal= input("A plural aninimal:")
color= input("A color:")
body_part= input("A body part:")
random_number = randint(0,4)
if random_number == 0:
    band_name = (f"{lead_singer} and the {plural_noun}")
elif random_number==1:
    band_name = (f"{music_adjective} and the {month}")
else:
    band_name = (f"{lead_singer} and the {music_adjective}")
    
if random_number==2:
    band_name = (f"{music_adjective} and the {month}")
    
elif random_number==3:
    print(f"Your Random Band Name is The {band_name}")

if random_number==4:
    print(f"Your Random Band Name is The {band_name}")
