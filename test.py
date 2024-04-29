import unittest
from main import Student

class StudentTest(unittest.TestCase):

    def test_walk(self):
        student = Student('Anna')
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, f"Дистанции не равны {student.distance} != 500")

    def test_run(self):
        student = Student('Mike')
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, f"Дистанции не равны {student.distance} != 1000")

    def test_run_vs_walk(self):
        running_student = Student("Bob")
        walking_student = Student("Mary")
        for _ in range(10):
            running_student.run()
            walking_student.walk()
        self.assertGreater(running_student.distance, walking_student.distance,
    f"{running_student.name} должен преодолеть дистанцию больше, чем {walking_student.name}")

    if __name__ == '__main__':
        unittest.main()