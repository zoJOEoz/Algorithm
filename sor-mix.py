import random

class CckSort(object):
	def __init__(self,data=None):
		self.tree = data
	def tex(self):
		is_sort=True
		while is_sort:
			is_sort=False
			for i in range(len(self.tree)-1):
				if self.tree[i]>self.tree[i+1]:
					self.tree[i],self.tree[i+1]=self.tree[i+1],self.tree[i]
					is_sort=True
			if not is_sort:
				break
			for y in range(len(self.tree)-1):
				s=len(self.tree)-1-y
				if self.tree[s]<self.tree[s-1]:
					self.tree[s],self.tree[s-1]=self.tree[s-1],self.tree[s]
					is_sort=True
		print(self.tree)
	def select_sort(self):
		for i in range(len(self.tree)):
			index=i
			print(i)
			for y in range(i+1,len(self.tree)):
				print(' ',y)
				#xx=		
				if self.tree[index]>self.tree[y]:
					print(self.tree[index],self.tree[y])
					index=y
			if index==i:
				pass
			else:
				self.tree[i],self.tree[index]=self.tree[index],self.tree[i]
				
		print(self.tree)
	
	def quick_sort_use(self,data):
		if len(data)<=1:
			return data
		else:
			left=[]
			right=[]
			center=[]
			centerVal=random.choice(data)
			for i in data:
				if i==centerVal:
					center.append(centerVal)
				elif i<centerVal:
					left.append(i)
				else:
					right.append(i)
			return self.quick_sort_use(left)+center+self.quick_sort_use(right)


	def quick_sort(self):
		print(self.quick_sort_use(self.tree))


	def merge(self,left,right):
		#print(left,right)
		output=[]
		while left and right:
			if left[0]<=right[0]:
				output.append(left.pop(0))
			else:
				output.append(right.pop(0))
		if left:
			output+=left
		if right:
			output+=right
		return output
		
			

	def merge_sort(self,data):
		if len(data)<=1:
			return data
		left=[]
		right=[]
		size=len(data)//2
		left=data[:size]
		right=data[size:]
		left=self.merge_sort(left)
		right=self.merge_sort(right)
		return self.merge(left,right)

	def merge_start(self):
		return self.merge_sort(self.tree)
class searchpoint(CckSort):
	def sequential_search(slef,data):
		lis=super().merge_start()
		for i in range(len(lis)):
			if lis[i]==data:
				return 'I find!!I find!!'
		return "sorry sir,no find"
	def binary_search(self,data):
		lis=super().merge_start()
		print(lis)
		low=0
		high=len(lis)-1
		size=(low+high)//2
		time=0
		while True:
			time+=1
			if data==lis[size]:
				return 'find',time
				break
			elif data>lis[size]:
				print("y")
				low=size+1
				print(size)
			else:
				print('n')
				high=size-1
				print(size)
			size=(low+high)//2
			#if size==1:
				#break
			if low>high:
				return 'no find',time
				
		
data=[6,1,5,7,3,43,2,4,8,9,11,23,56,76]

#print(obj.tree)
#obj.tex()
#obj.select_sort()

#CckSort(data)
#c=kquick_sort_use(data)
#print(c)
#obj.quick_sort()
ssc=searchpoint(data)
print(ssc.binary_search(43))

#print(ssc.tree)
#ssc.merge_start()
#print(ssc.sequential_search(11))
