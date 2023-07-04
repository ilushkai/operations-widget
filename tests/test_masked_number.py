import pytest

number = 'card 1234123412341234'


def test_masked_namber():
    parts = number.split()
    sender_name = ''.join(parts[:-1])
    card_number = parts[-1]
    formatted_number = " ".join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
    formatted_number = formatted_number[:7] + "** **** " + formatted_number[-4:]
    masked_format = f'{sender_name} {formatted_number}'

    assert masked_format == 'card 1234 12** **** 1234'


if __name__ == '__main__':
    pytest.main()