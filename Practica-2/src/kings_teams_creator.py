import matplotlib.pyplot as plt
import networkx as nx
import random

teams_graph = nx.Graph()


# Crea els diferents equips
def teams_creator():
    global teams_graph
    with open("../material/follows.txt") as users_follows:
        for line in users_follows:
            user = line[:line.find(':')]
            followeds = line[line.find(' ') + 1:].split()  # fiquem els seguits de users en una llista
            make_edges(user, followeds)
    users_follows.close()

    teams = list(team for team in nx.connected_components(teams_graph) if len(team) >= 5)
    show_teams(teams)
    draw(teams)


# Crea les arestes entre els nodes
def make_edges(user, followeds):
    global teams_graph
    teams_graph.add_node(user)
    degree = user[1:4]

    for followed in followeds:
        if not teams_graph.has_node(followed):
            teams_graph.add_node(followed)
        followed_degree = followed[1:4]
        if degree == followed_degree and not teams_graph.has_edge(user, followed):
            teams_graph.add_edge(user, followed)


# Mostra els equips creats
def show_teams(teams):
    id = 0
    for team in teams:
        print(f"Equip número {id}: {team}")
        id += 1


# Dibuixa el graf amb els equips
def draw(teams):
    global teams_graph
    color_dict = {}

    for team in teams:
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        for node in team:
            color_dict[node] = color
    nx.set_node_attributes(teams_graph, color_dict, 'color')

    colors = [teams_graph.nodes[node].get('color', 'black') for node in teams_graph.nodes()]
    display = nx.spring_layout(teams_graph, k=0.2)
    nx.draw(teams_graph, pos=display, node_color=colors, node_size=20, alpha=0.8)
    plt.figure(figsize=(100, 100))
    plt.show()


teams_creator()
