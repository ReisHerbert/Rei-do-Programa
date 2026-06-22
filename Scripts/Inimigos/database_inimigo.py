
import pygame 

VELOCIDADE = {
    "baixa" : 100,
    "media" : 200,
    "alta" : 300, 
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
