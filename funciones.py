def promedio_temperatura(t):
  for i in range (len(t)):
     for j in range (len(t[i])):
        suma = 0
        for k in (t[i][j]):
         suma += k["temp"]
        promedio = int(suma / len(t[i][j]))
        print(f"para la ciudad {i+1} de la semana {j+1} el promedio es {promedio} grados aproximadamente")

t = [
    [##Quito
        [##Semana 1
            {'dia':'lunes', 'temp':30},
            {'dia':'martes','temp':20},
            {'dia':'miercoles','temp':15},
            {'dia':'jueves','temp':25},
            {'dia':'viernes','temp':26},
            {'dia':'sábado','temp':18},
            {'dia':'domingo','temp':20}

        ],
        [ ##Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 21}
        ],
        [##Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [##Cuenca
         [##Semana 1
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 20}
        ],
        [##Semana 2
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 20}
        ],
        [##Semana 3
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 20}
        ],
        [##Semana 4
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 20}
        ]


    ],
    [##Guayaquil
        [##Semana 1
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 20}
        ],
        [##Semana 2
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 20}
        ],
        [##Semana 3
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 53},
            {"day": "Domingo", "temp": 20}
        ],
        [##Semana 4
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 60}
        ],


    ]

]
promedio_temperatura(t)








