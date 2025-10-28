#============================ Advanced Authentication and POST/PUT/DELETE/ Requests
#===End Project: Habit Tracker APP using Pixela
#API Rwquest Types:
    #==========GET: requests.get()
    #==========POST: request.post()
    #==========PUT: requests.put()
    #==========DELETE: requests.delete()

#STEP 1: Create a user account
def create_pixela_account():
    import requests
    pixela_url = 'https://pixe.la/v1/users'
    params = {
        "token": 'f7Qy8Wc1LZp0rA9mB2NxhE4TdvJkF3uVYSqR7oC6GzPMwHnKXtjD5beLUaQ0sI9y',
        "username": 'extender',
        "agreeTermsOfService":'yes',
        "notMinor":'yes'
    }

    response = requests.post(url=pixela_url, json=params)
    print (response.text)
# create_pixela_account()

#STEP 2: Create a graph definition
def create_graph():
    import requests
    USERNAME = 'extender'
    TOKEN = 'f7Qy8Wc1LZp0rA9mB2NxhE4TdvJkF3uVYSqR7oC6GzPMwHnKXtjD5beLUaQ0sI9y'



    graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs"
    param = {
        "id":'graph1',
        "name":'My Coding Graph',
        'unit': 'time',
        "type":'float',
        "timezone":'America/Chicago',
        "color":'sora'
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=graph_url, json=param, headers=headers)
    print (response.text)
# create_graph()

#STEP 3: POST VALUE TO THE GRAPH
def post_a_pixel():
    import requests
    USERNAME = 'extender'
    TOKEN = 'f7Qy8Wc1LZp0rA9mB2NxhE4TdvJkF3uVYSqR7oC6GzPMwHnKXtjD5beLUaQ0sI9y'
    GRAPHID = 'graph1'
    add_to_graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
    param = {
        "date":'20250127',
        "quantity":'1.0'
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=add_to_graph_url, json=param, headers=headers)
    print(response)
    print (response.text)
post_a_pixel()











