def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position,Company,URL\n")

    for job in jobs:
                 # get() 메서드를 사용하여 기본값을 설정
        position = job.get('position', 'No position')
        company = job.get('company', 'No company')
        link = job.get('link', 'No link')
        file.write(f"{position}, {company}, {link}\n")
    file.close()