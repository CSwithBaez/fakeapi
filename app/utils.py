from app.config import fake_data_map


def generate_fake_data(data: dict) -> dict:
    res = dict()
    if "repeat" in data:
        res = []
        limit = min(data["repeat"], 10)
        for _ in range(limit):
            res_data = dict()
            for k, v in data.items():
                if isinstance(v, dict):
                    res_data[k] = generate_fake_data(v)
                else:
                    try:
                        res_data[k] = fake_data_map[v]()
                    except KeyError:
                        pass
            res.append(res_data)

    else:
        for k, v in data.items():
            if isinstance(v, dict):
                res[k] = generate_fake_data(v)
            else:
                try:
                    res[k] = fake_data_map[v]()
                except KeyError:
                    pass
    return res