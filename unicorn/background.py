class Background():
	"""load and render background objects (ground and trees)"""
	GROUND="-"
	TREE="T"
	LEAVE="L"
	BRANCH="B"
	def __init__(self, level_file):
		with open(level_file) as f:
			lines = level_file.readlines()


