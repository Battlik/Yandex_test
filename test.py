import json
from typing import Any, Dict, List

def parse(response: Dict[str, Any]) -> List[str]:
    logins: List[str] = []

    # Находим people‑блок (он может быть либо в response["people"],
    # либо в response["suggest"]["people"])
    people_block = (
        response.get("people") or
        response.get("suggest", {}).get("people")
    )
    if not people_block:
        return logins

    # Внутри people могут быть:
    #  - "result"   (как в твоём примере)
    #  - "results"  (другие версии API)
    #  - "items"    (иногда)
    #  - сам people_block уже списком
    results = (
        people_block.get("result") or
        people_block.get("results") or
        people_block.get("items") or
        people_block
    )

    # Собираем логины
    if isinstance(results, list):
        for person in results:
            login = person.get("login")
            if login:
                logins.append(login)

    return logins


if __name__ == "__main__":
    # читаем test.json
    with open("test.json", encoding="utf-8") as f:
        data = json.load(f)

    print(parse(data))