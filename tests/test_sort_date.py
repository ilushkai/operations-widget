import pytest

date = [
    {'name': 'Item 1', 'date': '2022-02-29'},
    {'name': 'Item 2', 'date': '2023-03-27'},
    {'name': 'Item 3', 'date': '2021-09-28'}
]


def test_sort_date():
    global date
    sorted_date = sorted(date, key=lambda x: x['date'], reverse=True)
    assert sorted_date == [{'name': 'Item 2', 'date': '2023-03-27'},
                           {'name': 'Item 1', 'date': '2022-02-29'},
                           {'name': 'Item 3', 'date': '2021-09-28'}]


if __name__ == "__main__":
    pytest.main()
