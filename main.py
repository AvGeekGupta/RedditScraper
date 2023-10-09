# Libraries used

import requests
import csv
import time

# Variables

# Reddit API needs this

headers = {'User-agent': 'Mozilla/5.0'}

after = None

# Feature lists for CSV File

fieldnames = ['approved_at_utc', 'subreddit', 'selftext', 'author_fullname', 'saved', 'mod_reason_title', 'gilded',
              'clicked', 'title', 'link_flair_richtext', 'subreddit_name_prefixed', 'hidden', 'pwls',
              'link_flair_css_class', 'downs', 'thumbnail_height', 'top_awarded_type', 'hide_score', 'media_metadata',
              'name', 'quarantine', 'link_flair_text_color', 'upvote_ratio', 'author_flair_background_color', 'ups',
              'total_awards_received', 'media_embed', 'thumbnail_width', 'author_flair_template_id',
              'is_original_content', 'user_reports', 'secure_media', 'is_reddit_media_domain', 'is_meta', 'category',
              'secure_media_embed', 'link_flair_text', 'can_mod_post', 'score', 'approved_by', 'is_created_from_ads_ui',
              'author_premium', 'thumbnail', 'edited', 'author_flair_css_class', 'author_flair_richtext', 'gildings',
              'post_hint', 'content_categories', 'is_self', 'subreddit_type', 'created', 'link_flair_type', 'wls',
              'removed_by_category', 'banned_by', 'author_flair_type', 'domain', 'allow_live_comments', 'selftext_html',
              'likes', 'suggested_sort', 'banned_at_utc', 'view_count', 'archived', 'no_follow', 'is_crosspostable',
              'pinned', 'over_18', 'preview', 'all_awardings', 'awarders', 'media_only', 'link_flair_template_id',
              'can_gild', 'spoiler', 'locked', 'author_flair_text', 'treatment_tags', 'visited', 'removed_by',
              'mod_note', 'distinguished', 'subreddit_id', 'author_is_blocked', 'mod_reason_by', 'num_reports',
              'removal_reason', 'link_flair_background_color', 'id', 'is_robot_indexable', 'report_reasons', 'author',
              'discussion_type', 'num_comments', 'send_replies', 'whitelist_status', 'contest_mode', 'mod_reports',
              'author_patreon_flair', 'author_flair_text_color', 'permalink', 'parent_whitelist_status', 'stickied',
              'url', 'subreddit_subscribers', 'created_utc', 'num_crossposts', 'media', 'is_video',
              'url_overridden_by_dest', 'gallery_data', 'is_gallery', 'author_cakeday']

# Subreddit Name

subreddit = "r/developersIndia"

# No. of rows

num_rows = 0

# writes to a csv called 'data.csv' in python
with open('data.csv', 'w', newline='', encoding="utf-8") as file:
    file_writer = csv.DictWriter(file, fieldnames=fieldnames)
    file_writer.writeheader()

    for _ in range(200):  # Loop 4 times to get 100 posts, 25 each time
        subreddit_url = 'https://www.reddit.com/' + subreddit + '/.json'
        if after:
            subreddit_url += '?after=' + after
        r = requests.get(subreddit_url, headers=headers)
        data = r.json()  # Parse JSON data

        # Adds the scraped data (fieldnames) into rows in our csv
        for post in data['data']['children']:
            file_writer.writerow(post['data'])

        after = data['data']['after']

        num_rows += 25
        print(str(num_rows) + " rows written.")
        time.sleep(4)  # sleep for 2 seconds to avoid hitting Reddit's rate limit

file.close()
