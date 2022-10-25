import pytest
from unittest.mock import Mock
from src.livro import Blog

class ExcecaoLivroNaoEncontrado(Exception):
    pass

@pytest.fixture
def livro():
    post = [{'userId': 1, 
    'id': 1, 
    'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
    'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
    }]


def test_blog(livro):
    livroRepositorio = Mock()
    livroRepositorio.obter_livro.return_value = livro
    resultado = livroRepositorio.post_by_user_id('1')

    assert resultado['id'] == livro[1]['id']
