from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)

def get_hundred_days_end_date():
    print(str(start_100days + timedelta(days = 100)))
    return str(start_100days + timedelta(days = 100))


def get_days_between_pb_start_first_joint_pycon():
    print((pycon_date - pybites_founded).days)
    return (pycon_date - pybites_founded).days

get_hundred_days_end_date()
get_days_between_pb_start_first_joint_pycon()
