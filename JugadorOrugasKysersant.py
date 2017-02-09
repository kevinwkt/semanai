class JugadorOrugasKysersant(JugadorOrugas):
    distancias=[[],[]]
    def evalua(self, posicion):
        '''#Busca cabeza enemigo
        tab = posicion[1]
        for ren in range(self.juego.renglones):
            for c in range(self.juego.columnas):
                if tab[ren][c] == self.contrario.simbolo:
                    xEne = ren
                    yEne = c
                if tab[ren][c] == self.simbolo:
                    xNos = ren
                    yNos = c
        lon = int(((xNos-xEne)*2 + (yNos-xNos)2)*0.5)
        if lon< 3:
            return 1E999 - lon

        puntaje = 0
        t = posicion[1]
        s = self.simbolo
        rens = self.juego.renglones
        cols = self.juego.columnas
        for r in range(rens):
            for c in range(cols):

                if t[r][c] == s:

                    # Verificar localidad de arriba
                    if r > 0:
                        if t[r - 1][c] == s:
                            puntaje += 10
                        elif t[r - 1][c] == ' ':
                            puntaje += 1

                    # Verificar localid de abajo
                    if r < rens - 1:
                        if t[r + 1][c] == s:
                            puntaje += 10
                        elif t[r + 1][c] == ' ':
                            puntaje += 1

                    # Verificar localidad de la izquierda
                    if c > 0:
                        if t[r][c - 1] == s:
                            puntaje += 10
                        elif t[r][c - 1] == ' ':
                            puntaje += 1

                    # Verificar localidad de la derecha
                    if c < cols - 1:
                        if t[r][c + 1] == s:
                            puntaje += 10
                        elif t[r][c + 1] == ' ':
                            puntaje += 1
        return puntaje'''
        tablero = posicion[1]
        #Llena distancias y b

        self.distancias = [[['*' for c in range(self.juego.columnas)] for r in range(self.juego.renglones)] for k in range(2)]

        #Busca la cabeza nuestra y la contraria e inicializar distancias
        for r in range(self.juego.renglones):
            for c in range(self.juego.columnas):
                if tablero[r][c] == self.simbolo:
                    rCabNuestra = r
                    cCabNuestra = c

                elif tablero[r][c] == self.contrario.simbolo:
                    rCabOtro = r
                    cCabOtro = c

        self.buscarDistancias(rCabNuestra, cCabNuestra, 0, tablero) #Busca las distancias de nosotros
        self.buscarDistancias(rCabOtro, cCabOtro, 1, tablero) #Busca las distancias de ellos

        tonto = 0
        genio = 0

        for r in range(self.juego.renglones):
            for c in range(self.juego.columnas):
                if self.distancias[0][r][c] > self.distancias[1][r][c]:
                    tonto+=1
                elif self.distancias[0][r][c] < self.distancias[1][r][c]:
                    genio+=1

        return genio-tonto


    def buscarDistancias(self, rCab, cCab, jugador, tablero):
        queue = deque()
        queue.append((rCab, cCab, 0))

        while len(queue)>0:
            (r, c, distancia)=queue.popleft()

            # Checar arriba
            if r > 0:
                i = r - 1
            else:
                i = self.juego.renglones - 1
            j = c

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1

            # Checar derecha
            if c < (self.juego.columnas - 1):
                j = c + 1
            else:
                j = 0
            i = r

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1

            # Checar abajo
            if r < (self.juego.renglones - 1):
                i = r + 1
            else:
                i = 0
            j = c

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1

            # Checar izquierda
            if c > 0:
                j = c - 1
            else:
                j = self.juego.columnas - 1
            i = r

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1



    def heuristica(self, posicion, depth, alpha, beta):
        localAlpha= alpha

        if self.triunfo(posicion) is not None :
            return -1E999

        if depth==0:
            return self.evalua(posicion)

        posibles = self.posiciones_siguientes(posicion)

        max = -1E9999

        for p in posibles:
            h = -self.heuristica(posicion, depth - 1, -beta, -localAlpha)

            if h>max:
                max = h

            if max>=beta:
                break;
            if max>localAlpha:
                localAlpha=max

        return max

        '''t = posicion[1]
        s = self.simbolo
        rens = self.juego.renglones
        cols = self.juego.columnas
        for r in range(rens):
            for c in range(cols):

                if t[r][c] == s:

                    # Verificar localidad de arriba
                    if r > 0:
                        if t[r - 1][c] == s:
                            puntaje += 10
                        elif t[r - 1][c] == ' ':
                            puntaje += 1

                    # Verificar localid de abajo
                    if r < rens - 1:
                        if t[r + 1][c] == s:
                            puntaje += 10
                        elif t[r + 1][c] == ' ':
                            puntaje += 1

                    # Verificar localidad de la izquierda
                    if c > 0:
                        if t[r][c - 1] == s:
                            puntaje += 10
                        elif t[r][c - 1] == ' ':
                            puntaje += 1

                    # Verificar localidad de la derecha
                    if c < cols - 1:
                        if t[r][c + 1] == s:
                            puntaje += 10
                        elif t[r][c + 1] == ' ':
                            puntaje += 1'''

    def tira(self, posicion):
        '''Busca el mejor tiro entre todos los posibles.'''
        posibles = self.posiciones_siguientes(posicion)

        mejorPuntaje = -1E999
        mejorOpcion = choice(posibles)
        for p in posibles:
            puntaje = self.heuristica(p, 6, -1E999, 1E999)
            if puntaje > mejorPuntaje:
                mejorPuntaje = puntaje
                mejorOpcion = p

        return mejorOpcion