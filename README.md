# gIMG - Get Images
#### Video Demo: https://www.youtube.com/watch?v=P43cZeqGJ40
#### Description:
It's a simple web app to download all images form any page or link. It has been created using Python Flask framework. For web crawling the requests and bs4 (beautifusoup) library is used. The crawler method returns json response for ajax call from the frontend. Used bootstrap css framework for design with jquery and sweet alert 2.
Sweet alert is used to show nay kind of message the response contains.
It makes easy for anyone to get all the images at once if they want all the images form a single link. If manually they
would wanted to download all the images they had to use open image of save link multiple times.

## How It Works
- The app.py file contains all the backend functionality.
    - The index method returns the home page.
    - The craw method takes website link as input from form data. Here requests library is used for getting the website data as text.
    - Then the Beautiful Soup pareses the html and gives the ability to search for `img` tag.
    - Then some website loads image after the page loads, so they use `data-src` with jQuery,
    - They don't have `src` in `img` tag, then we check if the `data-src` is available and take that as link
    - If the link doen't contain website in it, because of relative path, then append the website in the link.
    - Then we get list of `img` tag, then parsing the img tag we can have the image link.
    - Then the image links list is returned through json response.
    - The data is shown when the reponse `status` is `True`
    - If there is any kind of issue the `try` `except` will handle it, and the app won't crash.
    - Here is had only one issue for crashing, and handled it with `except`, broad exception is likely to be discouraged.
    - When the response is given, then `ajax` `done` will take the response as `res` and process the data.
    - In `res` json object, there will be a `status` filed that will ensure if the image links are given from the crawler.
    - If `status` is `False` then an alert will be shown with Sweet alert plugin.
    - Else the images will be loaded with a box and a download button.
    - Then the image data will be shown, with an animation which have 200 miliseconds duration.
- There is a app.js file in static folder for all the javascript work in the project.
- The index.html is in the templates folder. I needed only one template file because it's a simple one page app.

## Technology used:
- Python
- Flask
- requests
- Beautiful Soup
- HTML
- Bootstra
- Javascript
- jQuery
- Sweet Alert


## Whan can be improved?

> Actually there is a lot to improve

- Giving a optionality to download all the images in zip file.
- Downloading all the images from the website.
- Giving options wich file format to download.
- Checking file size.
- Limiting file size.
- Email files at once.
