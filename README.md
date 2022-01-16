# web-gen
A Simple and efficient Static website generator written in python.

![Screenshot](https://i.imgur.com/VN8mZ8a.png)

## Features

- A simple markdown to html converter. 

Current supported markdown conversions:
- Headings
- Emphasized text(bold, italics, strikethrough)
- Links

## Usage

Demos are included.

1) Open `web_gen.py` and set the variables listed in the configuration section.  
> Note: You could use any html file as template. The script replaces `{{content}}` with the markdown content.   
The script also sets the first H1 Heading as the title. For that to function, be sure to set the html title as `{{title}}`.  
Using `{{url}}` in your markdown files replaces it with the url defined in the configuration section.  

2) Run the script with `python3 web_gen.py`.
3) The generated html files can be found in the designated folder.
