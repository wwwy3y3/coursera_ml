import numpy as np
# iteration
	# if find mistake go in else optimal
	# update w
	
class Pla(object):
	"""pla"""
	def __init__(self, filename):
		self.datas= np.loadtxt(filename)
		# add threshold in datas, w0=0, x0=1
		
		# init first line, by adding the first dot
		# self.w= 

	def train(self):
		upt, self.w= self.updateW()
		while upt:
			pass
			# not optimal



	def updateW(self):
		for dot in self.datas:
			if not self.w(dot) == self.result(dot):
				pass
				# find a mistake, update w
				# return (True, )
		return (False, self.w)


	def result(self, dot):
		pass

if __name__ == '__main__':
	pla= Pla('hw1_15_train.dat')
	print pla.datas.size