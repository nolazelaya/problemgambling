import pandas as pd
from collections import defaultdict

# Load your dataset
df = pd.read_csv('problem_gambling_posts.csv')

# Define keyword sets for each category (this is a simplified approach)
keywords = {
    'Affirmation': ['support', 'encouragement'],
    'Confessional': ['admitted', 'confessed'],
    'Day Count': ['day 10', 'monthly count'],
    'Observation': [], # This could be more complex based on contextual clues.
    'Offering Recovery Advice': ['tip:', 'strategy:', 'advice:'],
    'Progress Report': ['progress update', 'journey so far'],
    'Question': ['?', 'help me understand'],
    'Rant/Vent': [], # This could be identified by sentiment analysis.
    'Seeking Help/Advice': ['need help with:', 'advice on:'],
    'Story': []  # Stories might require a more nuanced approach, possibly involving NLP techniques for topic modeling or named entity recognition to identify personal narratives.
}

# Initialize categories dictionary (novel types can be added here)
categories = defaultdict(list)

for index, row in df.iterrows():
    text_content = row['Text']
    
    # Simple categorization based on keywords; for more complex or novel category identification consider NLP techniques like sentiment analysis (Rant/Vent), topic modeling (Story), etc.
    detected_category = 'Unknown'  # Default to unknown if no match is found
    max_keywords_matched, matched_categories = 0, []
    
    for category, keywords in keywords.items():
        keyword_matches = sum(keyword in text_content for keyword in keywords)
        
        if keyword_matches > max_keywords_matched:
            detected_category = category
            matched_categories = [category]  # Reset list when a new match is found.
            max_keywords_matched = keywords[keyword_matches]
        elif keyword_matches == max_keywords_matched and category not in matched_categories:
            matched_categories.append(category)
    
    if 'Unknown' in detected_category or len(matched_categories) > 1:
        print(f"Post at index {index} could not be categorized definitively.")
        
    categories[detected_category].append(row['Text'])

# Display the results (optional, for reviewing what was matched to each category)
for cat in categories.keys():
    print(f"\n{cat}:")
    for post in categories[cat]:
        print("-", post)