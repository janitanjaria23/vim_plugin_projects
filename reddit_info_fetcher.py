# coding=utf-8
import vim, urllib2
# we need json for parsing the response
import json

TIMEOUT = 20
URL = "http://reddit.com/.json"

try:
    # Get the posts and parse the json response
    response = urllib2.urlopen(URL, None, TIMEOUT).read()
    json_response = json.loads(response)

    posts = json_response.get("data", "").get("children", "")

    del vim.current.buffer[:]

    vim.current.buffer[0] = 80*"-"

    for post in posts:
        # we get the post details
        post_data = post.get("data", {})
        up = post_data.get("ups", 0)
        down = post_data.get("downs", 0)
        title = post_data.get("title", "NO TITLE").encode("utf-8")
        score = post_data.get("score", 0)
        permalink = post_data.get("permalink").encode("utf-8")
        url = post_data.get("url").encode("utf-8")
        comments = post_data.get("num_comments")

        if len(vim.current.buffer) < 25:
            # And here we append line by line to the buffer.
            # First the upvotes
            vim.current.buffer.append("↑ %s"%up)
            # Then the title and the url
            vim.current.buffer.append("    %s [%s]"%(title, url,))
            # Then the downvotes and number of comments
            vim.current.buffer.append("↓ %s    | comments: %s [%s]"%(down, comments, permalink,))
            vim.current.buffer.append(80*"-")

except Exception, e:
    print e
