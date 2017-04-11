import requests

class Lazy:
    # Creates and returns a client instance. Configured to work on a specific server.
    # Params:
    # host: The host this Lazy client will use. Example: https://lazy.herokuapp.com
    def __init__(self, host="https://lazy.herokuapp.com"):
        self.host = host

    def __create_url__(self, url):
        return self.host + url

    # Adds a given phrase to the category and trains the server.
    # Path: /learn
    # Params:
    # *phrase: string of characters representing a meaningful phrase.
    # *category: a string representing the category to put the phrase in.
    def learn(self, phrase, category):
        if not isinstance(phrase, str) and not isinstance(category, str):
            raise ValueError("Phrase and category must be strings!")
        elif phrase and category:
            parameters = {'phrase': phrase, 'category': category}
            learn_url = self.__create_url__('/learn')
            response = requests.post(learn_url, parameters)
            return response.json()
        else:
            raise ValueError("Phrase and category can not be empty!")

    # Forgets a given phrase which is present in the given category.
    # Path: /forget
    # Params:
    # *phrase: string of characters representing a phrase which is present in the server.
    # *category: a string representing the category to remove the phrase from.
    def forget(self, phrase, category):
        if not isinstance(phrase, str) and not isinstance(category, str):
            raise ValueError("Phrase and category must be strings!")
        elif phrase and category:
            parameters = {'phrase': phrase, 'category': category}
            forget_url = self.__create_url__('/forget')
            response = requests.post(forget_url, parameters)
            return response.json()
        else:
            raise ValueError("Phrase and category can not be empty!")

    # Adds a response to the given category
    # Path: /response
    # Params:
    # *category: a string representing the category to add a response to.
    # *response: string of characters to put as response to a category.
    def add_response(self, category, response):
        if not isinstance(category, str) and not isinstance(response, str):
            raise ValueError("Phrase and category must be strings!")
        elif category and response:
            parameters = {'response': response, 'category': category}
            add_response_url = self.__create_url__('/response')
            response = requests.post(add_response_url, parameters)
            return response.json()
        else:
            raise ValueError("Category and response can not be empty!")

    # Adds a actions to the given category
    # Path: /actions
    # Params:
    # *category: a string representing the category to add a actions to.
    # *actions: string of characters to put as actions to a category.
    def add_action(self, category, actions):
        if not isinstance(category, str) and not isinstance(actions, str):
            raise ValueError("Phrase and category must be strings!")
        elif category and actions:
            parameters = {'actions': actions, 'category': category}
            add_actions_url = self.__create_url__('/actions')
            actions = requests.post(add_actions_url, parameters)
            return response.json()
        else:
            raise ValueError("Category and actions can not be empty!")

    # Analyzes and returns a random response for the given phrase.
    # Path: /query
    # Method: POST
    # Params:
    # *phrase: string of characters representing a meaningful phrase.
    def query(self, phrase):
        if not isinstance(phrase, str):
            raise ValueError("Phrase must be strings!")
        elif phrase:
            parameters = {'phrase': phrase}
            query_url = self.__create_url__('/query')
            response = requests.post(query_url, parameters)
            return response.json()
        else:
            raise ValueError("Phrase can not be empty!")

    # Gets responses for a specific category.
    # Path: /responses/<category>
    # Method: GET
    def get_responses(self, category):
        if not isinstance(category, str):
            raise ValueError("Category must be strings!")
        elif category:
            responses_url = self.__create_url__('/responses/') + category
            response = requests.get(responses_url)
            return response.json()
        else:
            raise ValueError("Category can not be empty!")

    # Returns all the trained categories from the server.
    # Path: /categories
    # Method: GET
    def get_categories(self):
        categories_url = self.__create_url__('/categories')
        response = requests.get(categories_url)
        return response.json()

    # Instructs the server to save the trained data.
    # Path: /save
    # Method: GET
    def save(self):
        save_url = self.__create_url__('/save')
        response = requests.get(save_url)
        return response.json()

    # Instructs the server to load the trained data.
    # Path: /load
    # Method: GET
    def load(self):
        load_url = self.__create_url__('/load')
        response = requests.get(load_url)
        return response.json()
