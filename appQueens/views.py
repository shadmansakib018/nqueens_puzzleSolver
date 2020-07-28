from django.shortcuts import render

# Create your views here.
import random

def fitness_func(a):
  fv=0
  for i in range(len(a)):
    j=i+1
    while(j<len(a)):
      if((a[i]!=a[j])and(a[j]!=a[i]+(j-i))and(a[j]!=a[i]-(j-i))):
        fv=fv+2
      j=j+1
  return (fv/2)

def random_chromosome(nq):
	return [ random.randint(1, nq) for i in range(nq) ]

def cross_over(a1,a2,nq):
  n=random.randint(1, (nq-1))
  arr1=a1[0:n]+a2[n:nq]
  arr2=a2[0:n]+a1[n:nq]
  return arr1,arr2

def mutation(a1,nq):
  n=random.randint(1,nq)
  i=random.randint(0,(nq-1))
  a1[i]=n
  return a1

def compute(population,max_fit):
  sol=[]
  for i in range(len(population)):
    x=fitness_func(population[i])
    if(x==max_fit):
      flag=True
      sol=population[i]
      break
  return sol
def selection(population):
  i=random.randint(0,(len(population)-1))
  return population[i]
  #---------------------------------------------------------------------------
def index(request):
	return render(request, 'appQueens/index.html')

def preview(request):
	if request.method == "POST":
		num = request.POST["quantity"]
		solution=[]
		nq=int(num)
		max_fit=(nq*(nq-1))/2
		population = [random_chromosome(nq) for i in range(40)]

		flag=False
		#solution=compute(population,max_fit)

		while(flag!=True):
		  l1=selection(population)
		  l2=selection(population)

		  l3,l4=cross_over(l1,l2,nq)
		  ff1=fitness_func(l3)
		  ff2=fitness_func(l4)
		  if(ff1==max_fit):
		    solution=l3
		    flag=True
		    break
		  if(ff2==max_fit):
		    solution=l4
		    flag=True
		    break
		  if(ff1> max_fit*(3/4)):
		  	population.append(l3)
		  if(ff2> max_fit*(3/4)):
		  	population.append(l4)
		  #l3=mutation(l3,nq)
		  #l4=mutation(l4,nq)
		  
		  
		  
	

		return render(request, 'appQueens/preview.html', {
			"numrange" : (range(int(num))),
			"num" : int(num),
			"solution" : decreasebyone(solution)
			})
def decreasebyone(arr):
	newarr=[]
	for i in arr:
		newarr.append(i-1)
	return newarr
