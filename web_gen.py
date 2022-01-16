import re, os

# Configuration
markdown_directory = "markdown"
output_directory = "output"
template_html_path = "template/template.html"
website_url = "https://leakbang.github.io"

# Global Vairables
text: str
html_title: str

def main():
	for i in os.listdir(markdown_directory):
		name, extension = os.path.splitext(i)
		convert(i, name)



# Converter
def convert(markdown_file: str, name: str):
	global text, html_title
	with open(markdown_directory + "/" + markdown_file) as file:
		text = file.read()

	process_heading()
	process_emphasis()
	process_links()
	process_line_breaks()

	with open(template_html_path) as file:
		html_content = file.read()
	html_content = html_content.replace("{{title}}", html_title)
	html_content = html_content.replace("{{content}}", text)
	with open('%s/%s.html' % (output_directory, name), 'w') as output:
		output.write(html_content)

def process_heading():
	global text, html_title
	pattern = re.compile(r"^(#{1,6})\s*(.*?)\s*$", re.M)

	for index, i in enumerate(re.finditer(pattern, text)):
		heading_type = len(i.group(1))
		html_heading = "<h%s>" % heading_type + i.group(2) + "</h%s>" % heading_type

		# Set title
		if index == 0 and heading_type == 1:
			html_title = i.group(2)

		text = re.sub(pattern, html_heading, text, 1)

def process_emphasis():
	global text
	pattern = re.compile(r"([*|_|~]{1,2})(.*)\1", re.M)

	emphasis: str = ""
	style: str = ""

	for i in re.finditer(pattern, text):
		tag = i.group(1)
		if tag == "*":
			emphasis = "i"
		elif tag == "_":
			emphasis = "i"
		elif tag == "~":
			emphasis = "span"
			style = "style='text-decoration: line-through;'"
		elif tag == "**":
			emphasis = "b"

		html_emphasis = "<%s %s>" % (emphasis, style) + i.group(2) + "</%s>" % emphasis
		text = re.sub(pattern, html_emphasis, text, 1)

def process_links():
	global text, website_url

	text = text.replace("{{url}}", website_url)

	pattern = re.compile(r"\[(.*?)\]\((.*?)\)", re.M)

	for i in re.finditer(pattern, text):
		link_text = i.group(1)
		link_url = i.group(2)
		html_url = "<a href ='%s'>" % link_url + link_text + "</a>"
		text = re.sub(pattern, html_url, text, 1)

def process_line_breaks():
	global text
	pattern = re.compile(r"\n", re.M)

	for i in re.finditer(pattern, text):
		text = re.sub(pattern, "<br>", text, 1)


if __name__ == "__main__":
	main()
