import pytest
from viewing_party.party import *


def test_get_watched_avg_rating_calculates_watched_average_rating():
    # Arrange
    janes_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Fantasy",
                "rating": 4.8
            },
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            },
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.56666666664)

@pytest.mark.skip()
def test_get_watched_avg_rating_returns_zero_for_empty_list():
    # Arrange
    janes_data = {
        "watched": [
        ]
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)


def test_get_most_watched_genre_returns_most_frequent_genre_from_list():
    # Arrange
    janes_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Fantasy"
            },
            {
                "title": "Title B",
                "genre": "Intrigue"
            },
            {
                "title": "Title C",
                "genre": "Intrigue"
            },
            {
                "title": "Title D",
                "genre": "Fantasy"
            },
            {
                "title": "Title E",
                "genre": "Intrigue"
            },
        ]
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Intrigue"

def test_get_most_watched_genre_returns_most_frequent_genre_from_list_even_when_alphabetically_smaller():
    # Arrange
    janes_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Fantasy"
            },
            {
                "title": "Title B",
                "genre": "Action"
            },
            {
                "title": "Title C",
                "genre": "Action"
            },
            {
                "title": "Title D",
                "genre": "Fantasy"
            },
            {
                "title": "Title E",
                "genre": "Action"
            },
        ]
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Action"

def test_get_most_watched_genre_returns_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre is None
