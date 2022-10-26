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
        "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto",
    }


def test_blog(livro: dict):
    mocker = Mock()
    mocker.return_value = livro

    mocker(Blog.post_by_user_id, userId="1")
