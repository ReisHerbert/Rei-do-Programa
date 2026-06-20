
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
        "animacao_frames": [
            "Assets/Inimigos/Prefabs2.png",
            "Assets/Inimigos/Prefabs3.png"
        ], 
        "tipo": "terrestre"
    },

    "inimigo2_1F": {
        "velocidade": VELOCIDADE["baixa"],
        "animacao_frames": [
            "Assets/Inimigos/Prefabs4.png",
            "Assets/Inimigos/Prefabs5.png"
        ], 
        "tipo": "voador"
    }
}

print( INIMIGO_DB["inimigo1_1F"])