
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
