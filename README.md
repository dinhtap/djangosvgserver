# djangosvgserver
Simple Django server with account management, but looks a little bit ugly<br />
Run site with `python3 manage.py runserver` with default configuration at localhost:8000, or `python3 manage.py runserver YOURIP:PORT`. Access the site by localhost:8000 (or YOURIP:PORT) on your browser.
You can see some "images" on the site, logged-in users can edit their images. Image can have a tag (ex. tag1, tag2). <br />
You can log in as admin to manage images (add new images, add tags, add new users, assign images to users, manage users). Username admin, password admin <br />
There are 2 users with usernames art1 and art2, password Artart123<br />
Run fastapi server with `fastapi run api.py`, it will run at localhost:8000. 2 GET entries are localhost:8000/allimages and localhost:8000/allimages/tag to get all images and all images with given tag. A POST entry at /allimages/del to delete an image.<br />
