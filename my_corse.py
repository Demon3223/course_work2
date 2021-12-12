from flask import Flask, render_template, request, abort
from functions import get_post, return_post, return_comments, return_user, add_comments, search_post
app = Flask("my_project")


@app.route("/")
def all_post():
    data = get_post()
    return render_template("index.html", data=data)


@app.route("/post/<postid>")
def post_views_all(postid):
    data = return_post(get_post(), int(postid))
    comments = return_comments(int(postid))
    return render_template("post.html", data=data, comments=comments)


@app.route("/post/<postid>", methods=["POST"])
def post_views(postid):
    name = request.form.get("commenter_name")
    comment = request.form.get("comment")
    if not name or not comment:
        abort(400, "ERROR")
    comments_add = {
        "post_id": int(postid),
        "commenter_name": name,
        "comment": comment,
        "pk": int(postid)
    }
    add_comments(comments_add)
    data = return_post(get_post(), int(postid))
    comments = return_comments(int(postid))
    return render_template("post.html", data=data, comments=comments, count=len(comments))


@app.route("/search")
def search_page():
    s = request.args.get("s")
    if not s:
        return render_template("search.html")
    posts = search_post(s)
    cnt = len(search_post(s))
    return render_template("search.html", posts=posts, cnt=cnt)

@app.route("/user-feed/<username>")
def user_page(username):
    post = return_user(get_post(), username)

    return render_template("user-feed.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)