# Soluzione-Noisy-Bits-Olicyber

La challenge ci da un'immagine "bits.bmp" e ci dice che nasconde qualcosa.

Si nota che è formato da pixel bianchi e neri in sequenza, questi dovranno essere tradotti in 1 e 0, così da formare un codice binario, trasformarlo tutto in bytes e poi inserire il tutto in un unico file, che scopriremo essere in formato ".zip".

Per prima cosa lo script apre l'immagine e inserisce nella variabile file i byte dell'immagine, questi poi vengono codificati come 0 e 1, poi la stringa di 01 viene divisa in una lista per ogni 8 elementi, trasforma tutti i codici in intero e trasforma la lista finale in un Bytearray, questo bytearrray viene poi salvato in output.zip dove all'interno troveremo la flag.
