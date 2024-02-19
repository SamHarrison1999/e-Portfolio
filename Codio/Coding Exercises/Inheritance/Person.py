class Person:
    count = 0

    """Represents a generic Person."""

    def __init__(self, first, last, weight, height, age=0, gender=''):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        self.this_age = age
        self.this_gender = gender
        self.bmi = ''
        Person.count = Person.count + 1

    @classmethod
    def print_count(cls, ):
        return cls.count


class Adult(Person):
    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / self.height_in_inches ** 2

        print('BMI number is: ' + str(bmi_tmp))

        if bmi_tmp < 18:
            self.bmi = 'Underweight'
        elif 18 < bmi_tmp < 25:
            self.bmi = 'Normal'
        elif 25 < bmi_tmp < 30:
            self.bmi = 'Overweight'
        elif bmi_tmp > 30:
            self.bmi = 'Obese'
        return self.bmi


class Child(Person):

    def get_male_bmi(self, age, bmi_temp):
        bmi_class = ''
        if 2 < self.this_age < 9:
            if bmi_temp < 14:
                bmi_class = 'Underweight'
            elif 14 < bmi_temp < 17:
                bmi_class = 'Normal'
            elif 17 < bmi_temp < 20:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'

        elif 9 < self.this_age < 16:
            if bmi_temp < 17:
                bmi_class = 'Underweight'
            elif 17 < bmi_temp < 23:
                bmi_class = 'Normal'
            elif 23 < bmi_temp < 25:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'

        elif self.this_age >= 16:
            if bmi_temp < 19:
                bmi_class = 'Underweight'
            elif 19 < bmi_temp < 23:
                bmi_class = 'Normal'
            elif 23 < bmi_temp < 25:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'

        return bmi_class

    def get_female_bmi(age, bmi_temp):

        return 'Not implemented'

    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / self.height_in_inches ** 2
        if self.this_gender == 'M':
            self.bmi = self.get_male_bmi(self.this_age, bmi_tmp)
        elif self.this_gender == 'F':
            self.bmi = self.get_female_bmi(self.this_age, bmi_tmp)
        return self.bmi


class Teacher(Adult):

    def __init__(self, teacher_type):
        self.teacher_type = teacher_type
        bmi_risk_factor = 0
        if teacher_type == 'kindergarten':
            bmi_risk_factor = 1
        elif teacher_type == 'secondary':
            bmi_risk_factor = 2
        elif teacher_type == 'higher ed':
            bmi_risk_factor = 3
        self.bmi_risk_factor = bmi_risk_factor


if __name__ == '__main__':
    a1 = Adult('Tom', 'Thumb', 150, 62)
    c1 = Child('Mark', 'Smith', 98, 48, 15, 'M')

    print(a1.first_name)
    print(a1.calc_bmi())

    print(c1.first_name)
    print(c1.calc_bmi())
