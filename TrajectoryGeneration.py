import re
from datetime import datetime

def extract_career_trajectory(resume_text):
    trajectory = []
    jobs=[]
    di=[]
    gh={}
    mon={
        "Jan":'a',
        "Feb":'b',
        "Mar":'c',
        "Apr":'d',
        "May":'e',
        "Jun":'f',
        "Jul":'g',"Aug":'h',"Sep":'i',"Oct":'j',"Nov":'k',"Dec":'l'
    }
    lines = resume_text.split("\n")
    current_job = None
    i=0
    for line in lines:
        date_matches = re.findall(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|June|July|August|September|October|November|December)[a-z]* (?:19|20)\d{2}\b', line, re.IGNORECASE)
        if date_matches:
            dates = [datetime.strptime(date, "%b %Y") for date in date_matches]
            m=dates[0].strftime('%b')
            if current_job:
                trajectory.append((current_job, dates[0].strftime('%b %Y'), dates[-1].strftime('%b %Y')))
            current_job = line.strip()
            if i>0:
                jobs.append(lines[i-1])
                y=f"{dates[0].strftime('%Y')}{mon.get(m)}"
                di.append([y,lines[i-1]])
                gh[lines[i-1]]=dates[0].strftime('%b %Y')+"  "+ dates[-1].strftime('%b %Y')
        i+=1
    if current_job:
        trajectory.append((current_job, "Present"))
    return trajectory,jobs,di,gh

def career_trajectory(input_file):
    file = input_file
    with open(file, 'r') as f:
        resume_text = f.read()
        career_trajectory,jobs,di,gh = extract_career_trajectory(resume_text)
        di=sorted(di)
        print("Career Trajectory:")
        for x in di:
            print(gh[x[1]],x[1])
        print()
    return gh, di