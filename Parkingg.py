rates = {
    "two-wheeler": 20,
    "four-wheeler": 50,
    "heavy vehicle": 100,
}


def get_fee(v_type, hours):
    return rates[v_type.strip().lower()] * hours