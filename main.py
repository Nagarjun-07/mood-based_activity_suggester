from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/get_activities', methods=['POST'])
def get_activities():
    data = request.json
    mood = data.get('mood')
    activities = suggest_activities(mood)
    return jsonify(activities)

def suggest_activities(mood):
    activities = {
        "happy": [
            "Go for a walk", "Watch a comedy movie", "Call a friend", "Dance to your favorite song", "Cook a new recipe",
            "Have a picnic", "Play a musical instrument", "Plan a small get-together", "Do some gardening", "Take photos"
        ],
        "sad": [
            "Listen to music", "Read a book", "Meditate", "Write in a journal", "Talk to a loved one",
            "Watch a feel-good movie", "Take a long bath", "Do some gentle yoga", "Express yourself through art", "Cuddle a pet"
        ],
        "energetic": [
            "Go for a run", "Dance", "Play a sport", "Start a DIY project", "Do a workout session",
            "Go hiking", "Join a fitness class", "Go cycling", "Play an active video game", "Clean and organize your space"
        ],
        "bored": [
            "Try a new hobby", "Watch a documentary", "Learn a new skill online", "Cook a new recipe", "Read an interesting article",
            "Visit a museum or art gallery", "Explore your local area", "Play a board game", "Start a puzzle", "Write a short story"
        ],
        "stressed": [
            "Practice deep breathing", "Do yoga", "Take a bath", "Listen to calming music", "Go for a nature walk",
            "Do a guided meditation", "Try aromatherapy", "Stretch your body", "Write down what's bothering you", "Spend time in silence"
        ],
        "anxious": [
            "Practice mindfulness", "Do some light exercise", "Talk to a friend", "Listen to a podcast", "Do a creative activity like drawing or writing",
            "Try progressive muscle relaxation", "Read a book that interests you", "Drink a calming tea", "Do a breathing exercise", "Spend time with a pet"
        ],
        "relaxed": [
            "Read a book", "Watch a movie", "Take a nap", "Enjoy a hobby", "Have a leisurely walk",
            "Listen to soothing music", "Do some gentle stretching", "Spend time in nature", "Write in a gratitude journal", "Sip a warm beverage"
        ],
        "motivated": [
            "Set new goals", "Work on a project", "Learn something new", "Organize your space", "Exercise",
            "Create a vision board", "Start a blog or vlog", "Take an online course", "Plan your week ahead", "Network with like-minded people"
        ],
        "lonely": [
            "Reach out to a friend or family member", "Join an online community", "Read a book", "Listen to a podcast", "Volunteer",
            "Attend a local event or meetup", "Join a club or group", "Engage in a hobby you enjoy", "Watch a livestream or webinar", "Chat with someone online"
        ],
        "creative": [
            "Draw or paint", "Write a story or poem", "Try a DIY project", "Take photos", "Experiment with cooking",
            "Play a musical instrument", "Make a scrapbook", "Design something digitally", "Create a vision board", "Learn a new craft"
        ],
        "angry": [
            "Punch a pillow", "Go for a run", "Write down your feelings", "Practice deep breathing", "Do a high-intensity workout",
            "Listen to loud music", "Talk to someone you trust", "Draw or paint your emotions", "Spend time in a quiet place", "Take a cold shower"
        ],
        "grateful": [
            "Write in a gratitude journal", "Thank someone who's helped you", "Spend time with loved ones", "Do something kind for someone", "Reflect on positive memories",
            "Send a thank-you note", "Volunteer your time", "Create a gratitude jar", "Share your appreciation on social media", "Make a gratitude collage"
        ],
        "curious": [
            "Read a non-fiction book", "Watch educational videos", "Take an online course", "Visit a museum or science center", "Try a new hobby or activity",
            "Attend a lecture or seminar", "Explore a new place", "Ask questions and research answers", "Join a discussion group", "Experiment with science kits"
        ],
        "playful": [
            "Play a game", "Do a puzzle", "Build something with LEGO", "Have a water balloon fight", "Do a scavenger hunt",
            "Play with pets", "Do a fun craft", "Try a new sport or activity", "Watch funny videos", "Do a playful photoshoot"
        ],
        "romantic": [
            "Plan a special date night", "Write a love letter", "Cook a romantic meal", "Watch a romantic movie", "Go for a moonlit walk",
            "Create a playlist of love songs", "Dance together", "Take a couples' class", "Have a picnic under the stars", "Do something spontaneous"
        ],
        "nostalgic": [
            "Look through old photos", "Watch a movie from your childhood", "Listen to music from the past", "Visit a place that holds memories", "Reconnect with an old friend",
            "Write about your memories", "Cook a meal that reminds you of home", "Read a book you loved as a child", "Do a craft you enjoyed in the past", "Create a memory box"
        ]
    }
    return activities.get(mood, ["No activities available for this mood"])
