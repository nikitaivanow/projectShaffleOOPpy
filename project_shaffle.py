from random import shuffle
class GroupRandom:


	study = []

	def __init__(self):
		self.pupils = 20
		self.absent = []
		self.teams = 3
		self.ready_commands = []


	def get_pupils(self):
		pupils = int(input('Введите количество студентов :'))
		if pupils in range(1,40):
			self.pupils = pupils
		else:
			print('Неверное число')

	def list_study(self):
		for study in range(1, self.pupils+1):
			self.study.append(study)
		return self.study


	def get_absent(self):
		who_is_absent = input('Введите номера не участвующих студентов через пробел:')
		self.absent = [int(i) for i in who_is_absent.split()]
		return self.absent



	def hard_workers_list(self):
		self.study = [int(x) for x in self.study if x not in self.absent]
		return self.study


	def shaffle_list(self):
		shuffle(self.study)
		return self.study

	def get_number_of_teams(self):
		self.teams = int(input('Введите количество команд:'))
		return self.teams

	def divide_teams(self):
		list_len = len(self.study)
		if self.teams > list_len:
			raise IndexError(f'Number of parts({self.teams}) is greater than len of input_list({list_len})')

		def_part_len = list_len//self.teams
		size_tail = list_len%self.teams

		result_sizez = [ def_part_len + (1 if i < size_tail else 0) for i in range(0, self.teams) ]
		self.ready_commands = []

		start = 0
		for size in result_sizez:
			self.ready_commands.append(self.study[start:start + size])
			start += size

		return self.ready_commands



	def show_commands(self):
		print(self.ready_commands)


	def run(self):
		self.get_pupils()
		self.list_study()
		self.get_absent()
		self.hard_workers_list()
		self.shaffle_list()
		self.get_number_of_teams()
		self.divide_teams()
		self.show_commands()











































