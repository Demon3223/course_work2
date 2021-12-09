import json

def read_json(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def return_post(data, pk):
    for post in data:
        if post["pk"] == pk:
            return post


def return_comments(data, pk):
    all_comments = []
    for post in data:
        if post["post_id"] == pk:
            all_comments.append(post)
    return all_comments


def return_user(data, name):
    for user in data:
        if user["poster_name"] == name:
            return user


def add_comments(filename, post):
    data = read_json(filename)
    data.append(post)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)

