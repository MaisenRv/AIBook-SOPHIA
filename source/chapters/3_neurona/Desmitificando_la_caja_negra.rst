
=====================================================
Desmitificando la caja negra
=====================================================

Vamos a empezar por algo que ya sabemos, que una red neuronal es una "caja negra", y que además de alguna manera misteriosa le entregamos información, pasa por nuestra "caja negra" y como resultado nos da una respuesta coherente y lógica simulando "inteligencia".

.. container:: only-light

   .. tikz:: La caja negra de la red neuronal
      :align: center

      \activarPaletaClara
      \input{caja_negra.tex}


.. container:: only-dark

   .. tikz:: La caja negra de la red neuronal
      :align: center

      \activarPaletaOscura
      \input{caja_negra.tex}

Esta forma de ver el problema, aunque es muy simple, es una manera muy acertada de cómo funciona en este caso nuestra primera pieza de Lego, y si me permiten podemos empezar a definir nuestro problema de una forma un poco más rigurosa, lo primero de todo es saber que nuestro dibujito de la "caja negra" tiene relación con algo llamado "funciones" en matemáticas.

De una forma muy sencilla, y por supuesto sin entrar mucho a detalles formales de la matemática, vamos a decir que una "función" es una máquina que transforma una entrada (cualquiera) y saca una salida (también cualquiera) que depende de la entrada, en otras palabras, entra un "elemento" a la máquina, la máquina "modifica" dicho elemento, y sale un nuevo elemento que es resultado de la modificación del primero, esto ultimo es muy importante, porque si se cambia la entrada tambien se cambia la salida.

La representación de una función en matemáticas es muy simple: elegimos una letra (generalmente en minúscula), la cual representa el nombre de dicha máquina, y utilizamos "(" y ")" para describir qué entrada tiene nuestra "caja negra". El nombre más común es la letra :math:`f` seguido de :math:`(x)`, donde :math:`x` representa la entrada (cualquiera que sea). Además, representamos la salida como otra letra diferente, la más común es :math:`y`, la cual vamos a igualar a toda nuestra máquina, como se observa en :eq:`primera_funcion`.

.. math::
   :label: primera_funcion

   {\huge f(x) = y}

Vamos a recapitular: nuestra primera pieza de Lego se va a llamar "función", la cual es una máquina a la que se le pasa una entrada (llamada en este caso :math:`x`) y como resultado genera una salida (en este caso :math:`y`). Además, esta pieza de Lego es exactamente igual al primer dibujito de nuestra caja negra que representa una red neuronal.

.. container:: only-light

   .. tikz:: La caja negra como una funcion
      :align: center

      \activarPaletaClara
      \input{caja_negra_definida.tex}


.. container:: only-dark

   .. tikz:: La caja negra como una funcion
      :align: center

      \activarPaletaOscura
      \input{caja_negra_definida.tex}

Otra cosa importante es que una sola función puede estar compuesta por más funciones, como se observa en la ecuación :eq:`suma_funciones`.
Esta forma de escribir nos dice que una función (cualquiera) llamada :math:`h(x)` más otra función (cualquiera) llamada :math:`g(x)` es igual a la función :math:`f(x)`. Nótese que cuando escribimos :math:`g(x)` o :math:`h(x)`, solo es un nombre y no nos dice qué hace exactamente. En otras palabras, la suma de dos "cajas negras" ( :math:`g(x)` y :math:`h(x)` ) me da como resultado otra "caja negra" ( :math:`f(x)` ).

.. math::
   :label: suma_funciones

   {\huge f(x) = h(x) + g(x)}


Finalmente, tenemos el último elemento importante para comprender el interior de nuestra red neuronal: una operación llamada composición. Se puede ver de dos formas distintas:

1. **Perspectiva de proceso:** Si tenemos una función llamada :math:`s(x)` y otra llamada :math:`g(x)`, la composición consiste en que la salida de la primera función se convierte en la entrada de la segunda.
2. **Perspectiva matemática:** Teniendo las mismas dos funciones, la composición es utilizar la primera función directamente como la entrada de la segunda. En otras palabras, tomamos la función :math:`g(x)` y reemplazamos su entrada :math:`x` por la función :math:`s(x)`, obteniendo :math:`g(s(x))`.

Matematicamente hablando esta operacion se escribe de esta forma :eq:`composicion_funciones`:

.. math::
   :label: composicion_funciones

   {\huge (g \circ s)(x) = g(s(x))}

Okey, pero vamos con algo más interesante: el contenido de nuestra red neuronal "caja negra". Tal vez ya pudieron intuir que efectivamente dentro de la red neuronal existen más funciones (máquinas), a las cuales las vamos a llamar "capas" (o en inglés *layers*), y estas están relacionadas o, mejor dicho, se les aplica la operación de composición entre ellas. Cabe aclarar que la forma de disponer nuestras capas define un tipo de arquitectura.

   Entiéndase **arquitectura** como la forma de organizar nuestros bloques de Lego y cómo estos interactúan; si se ordenan o interactúan de forma diferente, se dice que cambió la arquitectura.

En este caso, esta arquitectura en particular se llama de **capas densas** (*dense layers*), la cual es la más fundamental y por la que vamos a empezar a explicar. Con esta información, ya podemos empezar a visualizar cómo podría estar representada gráficamente dentro de nuestra "caja negra".


.. container:: only-light

   .. tikz:: La caja negra con capas
      :align: center

      \activarPaletaClara
      \input{caja_con_capas.tex}


.. container:: only-dark

   .. tikz:: La caja negra con capas
      :align: center

      \activarPaletaOscura
      \input{caja_con_capas.tex}
