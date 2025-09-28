import pytest

def test_count_posts_per_user():
    posts = [
        {"userId": 1, "id": 1},
        {"userId": 2, "id": 2},
        {"userId": 1, "id": 3},
    ]
    from transform import aggregate_posts
    result = aggregate_posts(posts)
    assert result[1] == 2
    assert result[2] == 1
