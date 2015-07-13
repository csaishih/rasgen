class Course:
	def __init__(self, link, code, title, credits, campus, dept, year, semester, semester_code, faculty, courselvl, description, prereq, coreq, exclusion, breadth, flags):
		self.link =  link.strip()
		self.code = code.strip()
		self.title = title.strip()
		self.credits = credits.strip()
		self.campus = campus.strip()
		self.dept = dept.strip()
		self.year = year.strip()
		self.semester = semester.strip()
		self.semester_code = semester_code.strip()
		self.faculty = faculty.strip()
		self.courselvl = courselvl.strip()
		self.description = description.strip()
		self.prereq = prereq.strip()
		self.coreq = coreq.strip()
		self.exclusion = exclusion.strip()
		self.breadth = breadth.strip()
		self.flags = flags


	def __repr__(self):
		return '\nLink: ' + self.link + '\nCode: ' + self.code + '\nTitle: ' + self.title + '\nCredits: ' + self.credits + '\nCampus: ' + self.campus +  '\nDepartment: ' + self.dept + '\nYear: ' + self.year + '\nSemester: ' + self.semester + '\nSemester code: ' + self.semester_code + '\nFaculty: ' + self.faculty + '\nCourse level: ' + self.courselvl + '\nDescription: ' + self.description + '\nPre-requisites: ' + self.prereq + '\nCo-requisites' + self.coreq + '\nExclusion: ' + self.exclusion + '\nBreadth: ' + self.breadth + '\nFlags: ' + str(self.flags)