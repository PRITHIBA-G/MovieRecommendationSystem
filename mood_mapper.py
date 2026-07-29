def mood_to_genre(mood):

    mapping = {
        "Happy": "Comedy",
        "Sad": "Drama",
        "Stressed": "Animation",
        "Excited": "Action",
        "Bored": "Adventure"
    }

    return mapping.get(mood, "Comedy")