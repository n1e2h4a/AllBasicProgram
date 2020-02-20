student = {
  'phone': 'Iphone',
  'car': 'Mercedes',
  'person': 'Ambani'
}
print(student.keys() >= {'phone', 'car'})
print(student.keys() >= {'car', 'Mercedes'})
print(student.keys() >= {'person', 'Ambani'})