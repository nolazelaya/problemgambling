import praw
import os

# Create a Reddit instance
reddit = praw.Reddit(
    client_id="IWohTodwmhJtQ3SqlKnTFA",
    client_secret="tyKe37ktwYGvtcXAjqzX2DzEJipvgg",
    user_agent="chrome:pg-app:v1.0.0 (by u/discord19)"
)

# Define the subreddit
subreddit = reddit.subreddit('problemgambling')

# Fetch all posts (can be customized to fetch a specific number of posts)
def fetch_posts(subreddit, limit=1000):
    posts = []
    for post in subreddit.new(limit=limit):  # Using `new` to fetch recent posts
        posts.append({
            'title': post.title,
            'text': post.selftext,
            'id': post.id,
            'url': post.url,
            'created_utc': post.created_utc,
            'score': post.score,
            'num_comments': post.num_comments
        })
    return posts

# Fetch the posts
posts = fetch_posts(subreddit, limit=100)

# Save posts to a file
output_file = "problem_gambling_posts.txt"

with open(output_file, 'w', encoding='utf-8') as f:
    for post in posts:
        f.write(f"Title: {post['title']}\n")
        f.write(f"Text: {post['text']}\n")
        f.write(f"URL: {post['url']}\n")
        f.write(f"Score: {post['score']}\n")
        f.write(f"Comments: {post['num_comments']}\n")
        f.write(f"Created: {post['created_utc']}\n")
        f.write("="*40 + "\n")

print(f"Fetched and saved {len(posts)} posts to {output_file}")