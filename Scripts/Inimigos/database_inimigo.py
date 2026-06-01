
import pygame 

VELOCIDADE = {
    "baixa" : 50,
    "media" : 80,
    "alta" : 120, 
}

INIMIGO_DB = {
    #1 fase
    "inimigo1_1F": {
        "velocidade": VELOCIDADE["baixa"],
        "sprite": None, 
        "tipo": "terrestre"
    },

    "inimigo2_1F": {
        "velocidade": VELOCIDADE["baixa"],
        "sprite": None, 
        "tipo": "voador"
    }
}