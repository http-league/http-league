from django.shortcuts import render


from datetime import datetime


# Setting dates to dynamically output year in footer and double timestamp
today = datetime.today()
year = datetime.now().year

# Create your views here.
page_titles = [
    'Cup', 'Introduction',
    'Build tools',
    'About',
    'Team'
]

'''
--------------
Main URLs
--------------
'''


def index(request):
    return render(request, 'design/home.html', {'title': f'{page_titles[0]} · The design system for HTTP League', 'year': year, 'pages': page_titles})


def docs(request):
    return render(request, 'docs/index.html', {'title': f'{page_titles[1]} · Cup', 'year': year})


def build_tools(request):
    return render(request, 'docs/build_tools.html', {'title': f'{page_titles[2]} · Cup', 'year': year})


'''
--------------
Component URLs
--------------
'''


def components(request, slug):
    if slug:
        return render(request, 'docs/components/detail.html', {'title': slug})
    else:
        return render(request, 'docs/components/detail.html', {'title': 'No slug'})


'''
--------------
Utilities URLs
--------------
'''


def utilities(request, slug):
    if slug:
        return render(request, 'docs/utilities/detail.html', {'title': slug})
    else:
        return render(request, 'docs/utilities/detail.html', {'title': 'No slug'})


'''
--------------
About URLs
--------------
'''


def about(request):
    return render(request, 'about/index.html', {'title': f'{page_titles[3]} · Cup', 'year': year})


def about_team(request):
    return render(request, 'about/team.html', {'title': f'{page_titles[4]} · Cup', 'year': year})
