import pandas as pd

def get_dataframe_from_list(json_list):
    adult = [item['adult'] for item in json_list]
    original_title = [item['original_title'] for item in json_list]
    english_title = [item['title'] for item in json_list]
    original_language = [item['original_language'] for item in json_list]
    overview = [item['overview'] for item in json_list]
    popularity = [item['popularity'] for item in json_list]
    release_date = [item['release_date'] for item in json_list]
    vote_average = [item['vote_average'] for item in json_list]
    vote_count = [item['vote_count'] for item in json_list]

    return pd.DataFrame({
        'adult': adult,
        'original_title': original_title,
        'english_title': english_title,
        'original_language':original_language,
        'overview':overview,
        'popularity':popularity,
        'release_date':release_date,
        'vote_average':vote_average,
        'vote_count': vote_count
    })