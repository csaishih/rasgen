class Department:
	def __init__(self, code, department, faculty_code, faculty):
		self.code = code.strip()
		self.department = department.strip()
		self.faculty_code = faculty_code.strip()
		self.faculty = faculty.strip()

	def __repr__(self):
		return 'Code: ' + self.code + '\nDepartment: ' + self.department + '\nFaculty code: ' + self.faculty_code + '\nFaculty: ' + self.faculty