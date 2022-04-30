from timeit import default_timer as timer


def measure_time(func):
	""" Декоратор для отслеживания времени работы функции """
	def inner(*args, **kwargs):
		start = timer()
		func(*args, **kwargs)
		end = timer()
		print(f'Function {func.__name__} took {end-start} for execution')
	return inner
