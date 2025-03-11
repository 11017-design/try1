def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
    
def report(data):
    names, score=zip(*data)
    average_grade = get_grade(sum(score)/ len(score))
    highest_grade = get_grade(max(score))
    lowest_grade = get_grade(min(score))
    
    grades=[get_grade(s) for s in score]
        
    grade_counts={grade: grades.count(grade) for grade in set(grades)}
    
    report_txt=f"""
    REPORT:
    
    Average Grade: {average_grade:}
    Highest Grade: {highest_grade}
    Lowest Grade: {lowest_grade}
    
    
    Grade Distribution:
        
        {grade_counts}
    """
    return report_txt


data = [("Akshay", 99), ("Bikash", 92), ("Chandan", 83), ("Diksha", 70), ("Eeshan", 52)]
print(report(data))