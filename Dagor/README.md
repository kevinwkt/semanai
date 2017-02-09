# Dagor

Dagor es un _framework_ de Python para programar juegos de estrategia. Fue diseñado y desarrollado por Ariel Ortiz Ramírez exprofesamente para el reto de la semana-i 2016 titulado **“Introducción a la inteligencia artificial orientada al diseño y programación de juegos de estrategia”**, en el Tecnológico de Monterrey, Campus Estado de México.

El código de Dagor está escrito para poder funcionar tanto para Python 2.7.x como para Python 3.x. Hay una constante simbólica al inicio del archivo `dagor.py` llamada `SOLO_PYTHON27`. Si dicha constante es igual a `True`, el programa arroja una excepción al intentar correrlo en una versión distinta a Python 2.7.x. Esta funcionalidad garantiza que todos los códigos que implementen jugadores para el _framework_ utilicen una misma versión del lenguaje. Se seleccionó la versión 2.7 ya que ésta es la utilizada por otra plataforma usada durante la semana-i: [omegaUp](https://omegaup.com).

Dagor es una implementación del patrón de diseño conocido como [método de la plantilla](https://es.wikipedia.org/wiki/Template_Method_(patr%C3%B3n_de_dise%C3%B1o)) (_Template Method_). Muchas de las ideas de este _framework_ fueron tomadas del sitio [Gamesman](https://people.eecs.berkeley.edu/~ddgarcia/teaching/CS3Gamesman/) elaborado por Dan Garcia de UC Berkeley. Los juegos actualmente soportados por Dagor corresponden esencialmente a los siguientes del sitio de Gamesman:

| Juego en Dagor | Nombre en Gamesman |
|------------|----------------|
| Destino-10 (D10) | [1,2,...,10](https://people.eecs.berkeley.edu/~ddgarcia/teaching/CS3Gamesman/games/1210.html) |
| SuperGato | [Tomorrow's Tic-Tac-Toe](https://people.eecs.berkeley.edu/~ddgarcia/teaching/CS3Gamesman/games/tttt.html) |
| Orugas | [Surround](https://people.eecs.berkeley.edu/~ddgarcia/teaching/CS3Gamesman/games/surround.html)|

La palabra _Dagor_ significa “batalla” en el idioma [sindarin](https://es.wikipedia.org/wiki/Sindarin) (conocido también como élfico gris), creado por el escritor británico J. R. R. Tolkien.

