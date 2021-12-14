import json


def get_post():
    with open("data/data.json", encoding="utf-8") as file:
        posts = json.load(file)

    for i in range(len(posts)):
        pk = posts[i]["pk"]
        content = posts[i]['content']
        posts[i]["len_comments"] = len(return_comments(pk))
        posts[i]["content"] = content_tag(content)
    return posts


def return_post(data, pk):
    for post in data:
        if post["pk"] == pk:
            return post


def return_comments(post_id):
    all_comments = []
    with open("data/comments.json", encoding="utf-8") as file:
        comments = json.load(file)
    for com in comments:
        if com.get("post_id") == post_id:
            all_comments.append(com)
    return all_comments


def return_user(data, name):
    for user in data:
        user["cnt_comment"] = 0
        pk = user["pk"]
        comments = return_comments(pk)
        for com in comments:
            if user["pk"] == com["post_id"]:
                user["cnt_comment"] += 1
        if user["poster_name"] == name:

            return user


def get_tags(content):
    with open("data/data.json", encoding="utf-8") as file:
        posts = json.load(file)
    cont_tag = []
    for post in posts:
        if f'#{content}' in post["content"]:
            cont_tag.append(post)
            cont = post["content"]
            pk = post["pk"]
            post["len_comments"] = len(return_comments(pk))
            post["content"] = content_tag(cont)

    return cont_tag



def content_tag(content):
    words = content.split(" ")
    words_tag = []

    for word in words:
        if word[0] == "#":
            tag = word.replace("#", "")
            words_tag.append(f"<a href=/tag/{tag}>{word}</a>")
        else:
            words_tag.append(word)
    return " ".join(words_tag)


def search_post(s):
    with open("data/data.json", encoding="utf-8") as file:
        posts = json.load(file)

    content = []

    for post in posts:
        post["cnt_comment"] = 0
        pk = post["pk"]
        comments = return_comments(pk)
        for com in comments:
            if post["pk"] == com["post_id"]:
                post["cnt_comment"] +=1
        if s in post["content"]:
            content.append(post)

    return content


def add_comments( post):
    with open("data/comments.json", encoding="utf-8") as file:
        data = json.load(file)
    data.append(post)
    with open("data/comments.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)

print(len(search_post("не")))