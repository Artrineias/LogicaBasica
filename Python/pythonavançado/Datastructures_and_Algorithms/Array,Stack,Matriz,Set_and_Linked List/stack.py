# Para Type annotation
from typing import List

# Pilha de livros com type annotation
stack_of_books: List[str] = []  # {1}

# Adicionando livros no topo da pilha
stack_of_books.append('Livro 1')  # {2}
stack_of_books.append('Livro 2')  # {2}
stack_of_books.append('Livro 3')  # {2}

# Laço for
for book in stack_of_books[::-1]:
    # Faça o que preferir com o Livro
    print(book)