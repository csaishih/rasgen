class Department:
	def __init__(self, code, department, faculty_code, faculty):
		self.code = code
		self.department = department
		self.faculty_code = faculty_code
		self.faculty = faculty

	def __repr__(self):
		return 'Code: ' + self.code + '\nDepartment: ' + self.department + '\nFaculty code: ' + self.faculty_code + '\nFaculty: ' + self.faculty