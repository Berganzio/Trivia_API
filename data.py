import requests

API_parameters = {
    'amount': 20,
    'type': 'boolean',
    'category': None,
    'difficulty': None,     # easy-medium-hard, None=casual
}
categories = [
    {'num': None, 'category': 'Causal'},
    {'num': 9, 'category': 'General Knowledge'},
    {'num': 10, 'category': 'Entertainment: Books'},
    {'num': 11, 'category': 'Entertainment: Film'},
    {'num': 12, 'category': 'Entertainment: Music'},
    {'num': 13, 'category': 'Entertainment: Musicals & Theatres'},
    {'num': 14, 'category': 'Entertainment: Television'},
    {'num': 15, 'category': 'Entertainment: Video Games'},
    {'num': 16, 'category': 'Entertainment: Board Games'},
    {'num': 17, 'category': 'Science & Nature'},
    {'num': 18, 'category': 'Science: Computers'},
    {'num': 19, 'category': 'Science: Mathematics'},
    {'num': 20, 'category': 'Mythology'},
    {'num': 21, 'category': 'Sports'},
    {'num': 22, 'category': 'Geography'},
    {'num': 23, 'category': 'History'},
    {'num': 24, 'category': 'Politics'},
    {'num': 25, 'category': 'Art'},
    {'num': 26, 'category': 'Celebrities'},
    {'num': 27, 'category': 'Animals'},
    {'num': 28, 'category': 'Vehicles'},
    {'num': 29, 'category': 'Entertainment: Comics'},
    {'num': 30, 'category': 'Science: Gadgets'},
    {'num': 31, 'category': 'Entertainment: Japanese Anime & Manga'},
    {'num': 32, 'category': 'Entertainment: Cartoon & Animations'}]

response = requests.get('https://opentdb.com/api.php', params=API_parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']
