# SE-Individual-Project

v0.2

Welcome to the term project of Dominic Oertel for Software Engineering, Spring 2021, Towson University.

Included in this repository is the CC20 Messenger Application. It adds an extra layer of encryption that only you and the people you share your key with can access.

To start, one needs a computer with NodeJS, Python 3, and the PyCryptodome library installed. To automatically send and receive messages with another, a Discord account is required with the client installed locally. All setup instructions are provided.

The name CC20 is a shortening of 'ChaCha20', the name of the cipher algorithm to be used for en- and decryption. 

A key will be established using either a predefined default value, or the user has the option to generate their own with a partner using Diffie-Helman key establishment protocols. The application will guide the user through the process.
