from flask import Flask
from utils import get_all, get_by_pk, get_by_skill, load_candidates

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
