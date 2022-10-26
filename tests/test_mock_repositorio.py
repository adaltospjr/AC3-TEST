from unittest.mock import Mock

import pytest
from src.livro import Blog


class ExcecaoLivroNaoEncontrado(Exception):
    pass


@pytest.fixture
def livro():
    return {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    }


# o livro será passado automaticamente como parâmetro, pois é uma fixture
def test_blog(livro: dict):
    mocker = Mock()
    mocker.return_value = livro

    livro2 = Blog.post_by_user_id(userId="1")

    assert mocker() == livro2
