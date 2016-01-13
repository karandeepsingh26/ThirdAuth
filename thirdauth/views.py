from .forms import StatusForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
import facebook

def home(request):
	form=StatusForm(request.POST or None)
	if request.method=="POST":
		data=request.POST.get('text')
		
		graph=facebook.GraphAPI('CAAKSXRPyyz8BABFGlmnPYONBmunbtLUkF0YFB7dECZCHa4U74L2ZBzf0HmFgYPpJH1faptKwZCxhh8xZB4QJlFKEQSAdw2ML862ls7QBm9VIUnNisdOPHP5qZAQ5pYPZCYiXaJAZC4nr25CDpGZAGZCej7IL2elcZC2GRZC1U743d0UTo4y9pphPFEcWZCj7zQKUXYCq9zWZChQZAHZACHiFCP3ftAU')
		graph.put_wall_post(data, {
        
        })
		print 'done'
		return render(request,"home.html")
	else:
		context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'form':form})
		return render(request,'home.html',context)