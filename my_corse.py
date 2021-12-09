from flask import Flask, render_template, request, abort
from functions import read_json, return_post, return_comments, return_user, add_comments
app = Flask("my_project")

POST_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"
BOOKMARKS_PATH = "data/bookmarks.json"


@app.route("/")
def all_post():
    data = read_json(POST_PATH)
    return render_template("index.html", data=data)


@app.route("/post/<postid>", methods=["GET", "POST"])
def post_views(postid):
    data = return_post(read_json(POST_PATH), int(postid))
    comments = return_comments(read_json(COMMENTS_PATH), int(postid))
    if request.method == "GET":
        return render_template("post.html", data=data, comments=comments, count=len(comments))

    name = request.form.get("commenter_name")
    comments = request.form.get("comment")
    if not name or not comments:
        abort(400, "ERROR")

    comments_add = {
        "post_id": int(postid),
        "commenter_name": name,
        "comment": comments,
        "pk": int(postid)
    }
    add_comments(COMMENTS_PATH, comments_add)
    return render_template("post.html", data=data, comments=comments, count=len(comments))






@app.route("/search")
def search_page():
    return render_template("search.html")

@app.route("/user-feed/<username>")
def user_page(username):
    post = return_user(read_json(POST_PATH), username)
    return render_template("user-feed.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)