from django.shortcuts import render

from django.http import HttpResponse
# Create your classes here.
class Dog: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Moose', 'Mut', 'Lovable & Carefree', 5),
  Dog('Rocco', 'Mut', 'Introverted & Stubborn', 5),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Doggies</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', {'dogs': dogs})
