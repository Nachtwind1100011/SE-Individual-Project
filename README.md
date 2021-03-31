# SE-Individual-Project

V0.1

This will be the term project of Dominic Oertel for Software Engineering, Spring 2021, Towson University.

Included in this repository is the CC20 Translator Application. It will include a GUI inspired by that of Google Translate.

To start, one simply needs Python 3 installed and the PyCryptodome library. Input text will be entered into one box, output text will be displayed in the other. Output can also optionally be printed to a file. There will be two modes of operation, encryption; taking keyboard input from the user and displaying ciphertext. Decryption; taking ciphertext pasted from the user or from a file and translated into readable plaintext.

The name CC20 is a shortening of 'ChaCha20', the name of the cipher algorithm to be used for en- and decryption. 

A key will be established using either a predefined default value, or the user has the option to generate their own with a partner using Diffie-Helman key establishment protocols. The application will guide the user through the process.