from flask import Flask
from os import path as os_path
from json import load as json_load


# Функция загружает данные кандидатов из файла в список
def load_candidates(file_name):
    """
    Загружает данные кандидатов из файла в список
    """
    json = []
    if os_path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file:
            json = json_load(file)

    return json


# Функция возвращает полный список кандидатов
def get_all(candidates_list):
    """
    Возвращает полный список кандидатов
    """
    answer = "<pre>\n"
    for candidate in candidates_list:
        answer += f"  Имя кандидата - {candidate['name']}\n" \
                  f"  Позиция кандидата - {candidate['position']}\n" \
                  f"  Навыки: {candidate['skills']}\n\n"
    answer = answer[:-1] + "</pre>"

    return answer


# Функция возвращает кандидата по pk
def get_by_pk(candidates_list, pk):
    """
    Возвращает кандидата по pk
    """
    answer = ""
    for candidate in candidates_list:
        if candidate['pk'] == pk:
            answer += f"<img src = \"{candidate['picture']}\">\n\n" \
                      f"<pre>\n" \
                      f"  Имя кандидата - {candidate['name']}\n" \
                      f"  Позиция кандидата - {candidate['position']}\n" \
                      f"  Навыки: {candidate['skills']}\n" \
                      f"</pre>"

    return answer


# Функция возвращает кандидатов по навыку
def get_by_skill(candidates_list, skill_name):
    """
    Возвращает кандидатов по навыку
    """
    answer = ""
    for candidate in candidates_list:
        if skill_name.strip().lower() in candidate['skills'].strip().lower().split(", "):
            answer += f"  Имя кандидата - {candidate['name']}\n" \
                      f"  Позиция кандидата - {candidate['position']}\n" \
                      f"  Навыки: {candidate['skills']}\n\n"
    if len(answer) > 0:
        answer = "<pre>\n" + answer[:-2] + "\n</pre>"

    return answer


def main():
    candidates_list = load_candidates("candidates.json")

    app = Flask(__name__)

    @app.route("/")
    def page_index():
        return get_all(candidates_list)

    @app.route("/candidates/<int:pk>")
    def page_pk(pk):
        return get_by_pk(candidates_list, pk)

    @app.route("/skills/<skill>")
    def page_skill(skill):
        return get_by_skill(candidates_list, skill)

    app.run(host='127.0.0.1', port=80)


if __name__ == '__main__':
    main()
