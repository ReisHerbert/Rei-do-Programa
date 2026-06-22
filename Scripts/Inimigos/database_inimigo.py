
import pygame 

VELOCIDADE = {
    "baixa" : 70,
    "media" : 100,
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
    },

    "inimigo1_2F": {
        "velocidade": VELOCIDADE["baixa"],
        "animacao_frames": [
            "Assets/Inimigos/Sprite-0002.png",
            "Assets/Inimigos/Sprite-0003.png"
        ], 
        "tipo": "terrestre"
    },

    "inimigo2_2F": {
        "velocidade": VELOCIDADE["media"],
        "animacao_frames": [
            "Assets/Inimigos/Sprite-0004.png",
            "Assets/Inimigos/Sprite-0005.png"
        ], 
        "tipo": "terrestre"
    }
}
