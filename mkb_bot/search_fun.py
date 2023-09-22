from MKB_dict import ALL


def search_mkb(message: str) -> str:
    """
    поиск диагнозов в словаре по коду МКБ
    возвращает строку с результатом поиска с тэгами
    """
    # создаем список с кодировкой МКБ
    if len(message) == 3:
        A = list(f"<b><u>{key_1}</u></b>" for key_1, values_1 in ALL.items()
                 if message.upper() in key_1.upper())
        # создаем список с текстом
        B = list(f"<i>{val[0]} - {val[1]}</i>" for key_1, values_1 in ALL.items()
                 for val in values_1.items() if message.upper() in key_1.upper())
        MKB = "\n".join(A + B)
        if len(A + B) == 0:
            return "***несуществующий код МКБ***"
        else:
            return MKB
    elif len(message) == 5:
        A = list(f"<b><u>{key_1}</u></b>" for key_1, values_1 in ALL.items()
                 if message[:3].upper() in key_1.upper())
        # создаем список с текстом
        B = list(f"{key_2} - {val}" for key_1, values_1 in ALL.items()
                 for key_2, val in values_1.items() if message.upper() in key_2.upper())
        MKB = "\n".join(A + B)
        if len(A + B) == 0:
            return "***несуществующий код МКБ***"
        else:
            return MKB


def searh_text(message: str) -> str:
    """
    поиск диагнозов в словаре по тексту
    возвращает строку с результатом поиска с тэгами
    """
    TEXT = []
    # создаем список с кодировкой МКБ
    x = sorted(list(set(f"{key_1}" for key_1, values_1 in ALL.items() for key_2 in values_1.items() if
                        message.upper() in key_2[1].upper())))


    y = sorted(list(set(key_1 for key_1, values_1 in ALL.items() if message.upper() in key_1.upper())))
    A = sorted(list(set(x + y)))
    # создаем список с текстом
    B = list(f"{key_2[0]} - {key_2[1]}" for key_1, values_1 in ALL.items() for key_2 in values_1.items() if
             message.upper() in key_2[1].upper())
    text = sorted(A + B)
    # создаем окончательный список

    for i in text:
        if "." not in i[:5]:
            TEXT.append(f"{i}")
        else:
            TEXT.append(f"{i}")
    text_fin = "\n".join(TEXT)
    return text_fin


