import random
from random import choice, randint, sample

num_players = 50 #Nombre de jugadors que s'han apuntat.

min_player_followed = 15 #Mínim de jugadors que segueix cada user a instagram
max_player_followed = 30 #Màxim de jugadors que segueix cada user a instagram


def participants_file_creator():  # Creem el fitxer amb els participants
    file_participants = open("../material/participants_insta.txt", "w")
    for participants in range(num_players):
        file_participants.write(username_generator() + "\n")
    file_participants.close()


def follows_file_creator():  # A partir del fitxer dels participants, generem les relacions de mutuals
    file_mutuals = open("../material/follows.txt", "w")
    file_participants = open("../material/participants_insta.txt", "r")

    # Creo una llista amb els jugadors participants
    lines = file_participants.read().splitlines()
    players_list = []
    for player in lines:
        players_list.append(player)

    # Per a cada participant, crear la llista de followeds
    for user in lines:
        file_mutuals.write(user + ": ")
        # Creo llista amb els followeds
        followeds = random.sample(players_list, random.randint(min_player_followed, max_player_followed))
        # print(followeds)
        # print(user[:4])
        for element in followeds:
            # if element != user and user[:4] == element[:4]: #Condició per a que no es segueixi a ell mateix i per a que segueixi a gent de la seva carrera
            if element != user:  # Condició per a que no es segueixi a ell mateix
                file_mutuals.write(element + " ")
        file_mutuals.write("\n")
    file_mutuals.close()
    file_participants.close()


def username_generator():  # Funció per a crear usernames amb la sintaxi @name_birthday
    file_names = open("../material/names.txt", "r")
    line = file_names.read().splitlines()
    carrera = ["CAF", "GEI", "GEA", "ADE", "PSI", "SOC", "HIS", "TSO", "DAD", "DRE"]
    username = "@" + choice(carrera) + choice(line) + "_" + str(random.randint(1, 28)) + str(
        random.randint(1, 12)) + str(random.randint(1990, 2005))
    file_names.close()
    return username


participants_file_creator()
follows_file_creator()
