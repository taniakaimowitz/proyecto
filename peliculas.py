class pelicula:
    def __init__(self,nombre,duracion,descripcion,restricciones,hinicio,hfinal,salas): 
        #hinicio: hora inicio de la película, hfinal: hora a la que finaliza la película
        self.nombre= nombre
        self.duracion=duracion
        self.descripcion = descripcion
        self.restricciones = restricciones
        self.hinicio = hinicio
        self.hfinal = hfinal
        self.salas = salas


    def set_nombre(self, nombre):
            self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_descripcion(self, descripcion):
            self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion
    
    def set_duracion(self, duracion):
            self.duracion = duracion

    def get_duracion(self):
        return self.duracion

    def set_restricciones(self, restricciones):
            self.restricciones = restricciones

    def get_restricciones(self):
        return self.restricciones

    def set_hinicio(self, hinicio):
        self.hinicio = hinicio

    def get_hinicio(self):
            return self.hinicio

    def set_hfinal(self, hfinal):
        self.hfinal = hfinal

    def get_hfinal(self):
            return self.hfinal
    
    def set_salas(self, salas):
            self.hfinal = salas

    def get_salas(self):
            return self.salas

if __name__ == '__main__':
    listapelis = {}
    
    wonderwoman = pelicula('Wonder Woman',120,'Super heroe femenina salva al mundo del mal','12+',['17:00','19:15'],['19:00','21:15'],1)
    minions = pelicula('Minions',90,'Es un spin-off de "Mi Villano Favorito"','TP',['14:00','15:45','17:30'],['19:00','17:15','19:00'],2)
    spiderman = pelicula('Spiderman',110,'Jóven descubre poderes especiales de araña y se convierte en superhéroe','12+',['16:00','18:05'],['17:50','20:05'],3)
    sirenita = pelicula('La Sirenita',95,'Una sirenita que se enamora de un muchacho humano','TP',['14:00','15:50','17:35'],['15:35','17:20','19:05'],4)


    listapelis = {'wonderwoman':wonderwoman, 'minions':minions, 'spiderman':spiderman,'sirenita':sirenita}

    print(wonderwoman.get_salas())

