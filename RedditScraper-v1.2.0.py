import praw
import os
import csv

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
posts = fetch_posts(subreddit, limit=1000)

# Save posts to a CSV file
output_file = "problem_gambling_posts.csv"

# Write to CSV with the required headers
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Text', 'URL', 'Score', 'Comments', 'Created']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    for post in posts:
        writer.writerow({
            'Title': post['title'],
            'Text': post['text'],
            'URL': post['url'],
            'Score': post['score'],
            'Comments': post['num_comments'],
            'Created': post['created_utc']
        })

print(f"Fetched and saved {len(posts)} posts to {output_file}")
