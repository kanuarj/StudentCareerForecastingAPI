def cgpa_calculator(data_json):
    student_type = data_json['student_type']
    sem = data_json['current_sem']
    current_cgpa = data_json['current_cgpa']
    target_cgpa = data_json['target_cgpa']

    current_cgpa = float(current_cgpa)
    target_cgpa = float(target_cgpa)

    if student_type == 'regular':
        recovery = 8 - int(sem)
        needed_cgpa = target_cgpa - current_cgpa
        coverage = needed_cgpa * int(sem)
        distribution = coverage / recovery
        required = target_cgpa + distribution
        if required > 10.0:
            required = 10.0
        required = str(required)
        recovery = str(recovery)
        return required, recovery

    elif student_type == 'diploma':
        sem = sem - 2
        recovery = 6 - int(sem)
        needed_cgpa = target_cgpa - current_cgpa
        coverage = needed_cgpa * int(sem)
        distribution = coverage / recovery
        required = target_cgpa + distribution
        if required > 10.0:
            required = 10.0
        required = str(required)
        recovery = str(recovery)
        return required, recovery