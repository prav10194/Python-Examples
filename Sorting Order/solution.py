import re

class Sorting:
    def __init__(self, jobs):
        self.jobs = jobs
    
    def sortJobs(self):
        
        # regex for splitting job - alpha and numeric and storing it in list
        updatedJobs = []
        for job in self.jobs:
            print(job[0])
            if job[0].isalpha(): 
                result = re.search(r"([a-zA-Z]*)([0-9]*)", job)
                updatedJobs.append(list(result.groups()))
            else:
                result = re.search(r"([0-9]*)([a-zA-Z]*)", job)
                temp = list(result.groups())
                temp.reverse()
                temp[0] += "*"
                updatedJobs.append(temp)
        
        # logic for sorting those arrays
        
        updatedJobs = sorted(updatedJobs, key=lambda x:x[0])
        updatedJobs = sorted(updatedJobs, key=lambda x:x[1])
        
        # logic for reversing jobs 
        
        for job in updatedJobs:
            if job[0][-1] == "*":
                job[0] = job[0].split("*")[0]
                job.reverse()
        
        # joining all jobs
        
        for index, job in enumerate(updatedJobs):
            updatedJobs[index] = ''.join(job)
        
        return updatedJobs
    
    
    
jobs = ['4004A', '5005B', 'A2002', 'B3003']    
s = Sorting(jobs)  
print(s.sortJobs())
