""" Лекція 17. DB in Python """

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

print(f"\n=======================| Task 1 |=======================")

#   Add models for
#           student,
#           subject and
#           student_subject
#       from previous lessons in SQLAlchemy.


Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    subjects = relationship("StudentSubject", back_populates="student")


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship("StudentSubject", back_populates="subject")


class StudentSubject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))

    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

students_data = [
    {'name': 'Bae', 'age': 18},
    {'name': 'Eddy', 'age': 21},
    {'name': 'Lily', 'age': 22},
    {'name': 'Jenny', 'age': 19}
]

subjects_data = ['English', 'Math', 'Spanish', 'Ukrainian']

student_subjects_data = [
    {'student_id': 1, 'subject_id': 1},
    {'student_id': 2, 'subject_id': 2},
    {'student_id': 3, 'subject_id': 3},
    {'student_id': 4, 'subject_id': 4},
    {'student_id': 1, 'subject_id': 3}
]

for student_info in students_data:
    session.add(Student(**student_info))

for subject_name in subjects_data:
    session.add(Subject(name=subject_name))

for student_subject_info in student_subjects_data:
    session.add(StudentSubject(**student_subject_info))

session.commit()

print(f"\n=======================| Task 2 |=======================")
#   Find all students` name
#       that visited 'English' classes.

english_students = session.query(Student) \
    .join(StudentSubject) \
    .join(Subject) \
    .filter(Subject.name == 'English') \
    .all()

for student in english_students:
    print(f" all students` name that visited 'English' classes: \n{student.name = }")
