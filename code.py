import web

render = web.template.render('templates/')
urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self, smiley):
        result={} # let's define an empty dictionary which will store the returned results
        # Match the smiley from the emoticon.txt file and store the results in the dictionary
        for line in open('emoticon.txt'):
            if smiley in line:
                key,value=line.split('\t')
		if key==smiley: # to get an exact match
                    result[key]=value
        return render.index(result) # send the result to the template index

if __name__ == "__main__": 
    app.run()
