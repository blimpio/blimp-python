# blimp-python #
This library allows you to interact with the Blimp API using Python. You can find more information 
about Blimp's Public API documentation at [http://dev.getblimp.com/](http://dev.getblimp.com/).
If you have any problems or requests please contact [support](mailto:support@getblimp.com?subject=Blimp API Python library).

Inspired by Mike Lewis' [Python Foursquare v2 library](https://github.com/mLewisLogic/foursquare).

## License ##
Licensed under the MIT License.

## Install ##

Using Github:

```
git clone git@github.com:getblimp/blimp-python.git
```

Using pip:

```
pip install blimp
```

Using easy_install:

```
easy_install blimp
````

## Pre-Usage ##

Before we begin using the library you need to signup to [Blimp](http://app.getblimp.com/) and generate a new API Key if you don't have one in your [settings](https://app.getblimp.com/user/settings/api/) as well as an Application ID and Secret in your [applications](https://app.getblimp.com/user/settings/api/developers/).

## Usage ##

```python
import blimp

api = blimp.Client('username', 'api_key', 'app_id', 'app_secret')

# get all companies that I'm part of
companies = api.company()

# get one company by id
company = api.company(1)

# get all projects for one company
projects = api.project(params={'company': 1})

# get count of total projects
total_projects = projects['meta']['total_count']

# Loop through all projects and print their name
for project in projects['objects']:
    print project['name']

# Get all goals for a project
goals = api.goal(params={'project': 1})

# Get all tasks for a goal
tasks = api.task(params={'goal': 1})

# Get all comments for a task
comments = api.comment(params={'content_type': 'todo', 'object_pk': 1})

# Get schema for all available endpoints
print api.company.schema()
print api.project.schema()
print api.goal.schema()
print api.task.schema()
print api.comment.schema()
print api.file.schema()

# All available methods per endpoint
# api.task.get()
# api.task.get(task_id)
# api.task.post(data)
# api.task.put(task_id, data)
# api.task.delete(task_id)
# api.task.schema()
```
### Example response of all companies I'm part of ###
```JSON
{
    "meta": {
        "limit": 20,
        "next": null,
        "offset": 0,
        "previous": null,
        "total_count": 1
    },
    "objects": [
        {
            "company_users": [
                {
                    "accepted_invitation": true,
                    "date_created": "2012-11-01T00:00:00",
                    "date_modified": "2012-11-27T02:22:09.817265",
                    "id": 38,
                    "is_active": true,
                    "role": "admin",
                    "user": "/api/v2/user/3/"
                },
                {
                    "accepted_invitation": true,
                    "date_created": "2012-11-01T00:00:00",
                    "date_modified": "2012-11-27T02:22:09.705959",
                    "id": 37,
                    "is_active": true,
                    "role": "admin",
                    "user": "/api/v2/user/2/"
                },
                {
                    "accepted_invitation": true,
                    "date_created": "2012-11-01T00:00:00",
                    "date_modified": "2012-11-27T02:22:09.380851",
                    "id": 39,
                    "is_active": true,
                    "role": "owner",
                    "user": "/api/v2/user/1/"
                }
            ],
            "date_created": "2012-11-01T00:00:00",
            "date_modified": "2012-12-21T21:57:09.965247",
            "id": 1,
            "image_url": "",
            "name": "Blimp",
            "resource_uri": "/api/v2/company/1/",
            "slug": "blimp",
            "used_projects": 0,
            "used_storage": "4929882"
        }
    ]
}
```

## Improvements
What else would you like this library to do? Let me know. Feel free to send pull requests for any improvements you make.

### Todo
* Tests
