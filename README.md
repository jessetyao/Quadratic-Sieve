# A python implementation of the Quadratic Sieve algorithm 
In the realm of cryptography and number theory, the ability to factorize integers, especially large ones, plays an enormous role. In this project, I implemented the Quadratic Sieve algoritm focused on the RSA scheme.

* The [Quadratic Sieve](https://en.wikipedia.org/wiki/Quadratic_sieve) is designed to factor very large numbers to break the famous [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) scheme
* My algorithm uses [Tonelli-shanks algorithm](https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm), [Dixon's factorization method](https://en.wikipedia.org/wiki/Dixon%27s_factorization_method), [Fermat's factorization method](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) and many more theorems that are too long to list.
* I also used [A Fast Algorithm for Gaussian Elimination over GF (2)](https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf) by ÇETIN K. KOÇ AND SARATH N. ARACHCHIGE from the University of Houston




### Important Notes
* This was specifically designed to break the RSA scheme which means numbers are normally meant to be the product of very large prime numbers
* My code can factor a 52-bit integer in under 5 minutes. Anything bigger and you might have to wait a while
* basicRSA.py just sents up a basic RSA scheme and proves I can figure out the encoded message
* My function structure was inspired by [alexbers](https://github.com/alexbers), but everything else was implemented differently




## Thank You
  
