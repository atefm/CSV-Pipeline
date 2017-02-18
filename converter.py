import json

def format_as_json(data):
    return (json.dumps([object.__dict__ for object in data]))


def format_as_html(data):
	formatted = "<table>"
	if (len(data) > 0):
		object = data[0]
		for key, value in object.__dict__.iteritems():
			formatted += "<th>" + key + "</th>"
		
		for object in data:
			formatted += "<tr>"
			for key, value in object.__dict__.iteritems():
				formatted += "<td>" + str(value) + "</td>"
			formatted += "</tr>"
	formatted += "</table>"	
	return formatted

supported_format_method = {
    'json': format_as_json,
    'html': format_as_html,
}