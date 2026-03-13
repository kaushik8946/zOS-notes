#!/usr/bin/env python3
"""
Generate 300 IMS Application Programmer Questions
Filters existing questions to focus on Application Programming topics only.
Generates two outputs: Markdown Question Bank and Consolidated JSON
"""

import json
import os

# Keywords that indicate System Programming (EXCLUDE these)
# More focused on clear system programming topics
SYSTEM_PROG_KEYWORDS = [
    'control region', 'installation', 'configure', 'configuration',
    'system tuning', 'multiprocessor cpc', 'system programming',
    'system code', 'system programmer',
    'system generation', 'sysgen', 'scaled on a multiprocessor',
    'being scaled on', 'subtask waits for system service',
    'failure in one application program must not bring down ims systems',
    'system admin', 'install ims', 'z/os system administration'
]

# Keywords that indicate Application Programming (INCLUDE these)
APP_PROG_KEYWORDS = [
    'dl/i', 'dli', 'segment', 'parent', 'child', 'hierarchy',
    'dbd', 'psb', 'pcb', 'ssa', 'get unique', 'get next',
    'insert', 'replace', 'delete', 'program', 'cobol', 'application',
    'call', 'key field', 'database access', 'navigation',
    'sequential', 'field', 'pointer', 'twin', 'database record'
]

def is_application_programming_question(question_text):
    """Determine if a question is about Application Programming"""
    q_lower = question_text.lower()
    
    # First check if it has STRICT system programming keywords (exclude)
    for keyword in SYSTEM_PROG_KEYWORDS:
        if keyword.lower() in q_lower:
            return False
    
    # If it doesn't have strict system keywords, it's likely relevant for app prog
    # IMS App Programmers need to understand the overall architecture even if 
    # some questions touch on sysplex, DBA, or subsystem concepts
    # as long as they're not about installation, configuration, or system tuning
    
    return True

def load_questions(directory):
    """Load all questions from EASY, MEDIUM, HARD JSON files"""
    all_questions = []
    
    for filename in ['EASY.json', 'MEDIUM.json', 'HARD.json']:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            questions = json.load(f)
            all_questions.extend(questions)
    
    return all_questions

def filter_app_prog_questions(questions):
    """Filter questions to keep only Application Programming ones"""
    filtered = []
    
    for q in questions:
        if is_application_programming_question(q['question']):
            filtered.append(q)
    
    return filtered

def renumber_questions(questions):
    """Renumber questions sequentially starting from 1"""
    for idx, q in enumerate(questions, start=1):
        q['questionnumber'] = idx
        # Update question tag if it exists
        if '[' in q['question'] and ']' in q['question']:
            # Remove old tag
            parts = q['question'].rsplit('[', 1)
            if len(parts) == 2:
                q['question'] = parts[0].strip()
    
    return questions

def generate_markdown_output(questions, output_file):
    """Generate Markdown Question Bank"""
    with open(output_file, 'w') as f:
        f.write("# IMS Application Programmer Questions\n\n")
        f.write("**Total Questions: {}**\n\n".format(len(questions)))
        f.write("---\n\n")
        
        for q in questions:
            # Question header
            f.write(f"### Q{q['questionnumber']}. {q['question']}\n\n")
            
            # Choice type
            f.write(f"**Type:** {q['choice_type']}\n\n")
            
            # Options
            f.write(f"**A.** {q['option_1']}\n\n")
            f.write(f"**B.** {q['option_2']}\n\n")
            f.write(f"**C.** {q['option_3']}\n\n")
            f.write(f"**D.** {q['option_4']}\n\n")
            
            # Correct answer
            answers = []
            for ans in q['correct_answer']:
                if ans == 'option_1':
                    answers.append('A')
                elif ans == 'option_2':
                    answers.append('B')
                elif ans == 'option_3':
                    answers.append('C')
                elif ans == 'option_4':
                    answers.append('D')
            
            if len(answers) > 1:
                f.write(f"**Correct Answers:** {', '.join(answers)}\n\n")
            else:
                f.write(f"**Correct Answer:** {answers[0]}\n\n")
            
            f.write("---\n\n")

def generate_json_output(questions, output_file):
    """Generate consolidated JSON file"""
    with open(output_file, 'w') as f:
        json.dump(questions, f, indent=2)

def remove_duplicates(questions):
    """Remove duplicate questions keeping the first occurrence"""
    seen_questions = set()
    unique_questions = []
    
    for q in questions:
        # Normalize question text for comparison
        question_text = q['question'].strip().lower()
        # Remove tags like [Easy-1], [Medium-2], etc.
        if '[' in question_text and ']' in question_text:
            question_text = question_text.rsplit('[', 1)[0].strip()
        
        if question_text not in seen_questions:
            seen_questions.add(question_text)
            unique_questions.append(q)
    
    return unique_questions

def main():
    # Load all questions
    print("Loading questions from IMS_DB directory...")
    # Use directory where script is located for better portability
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ims_db_dir = os.path.join(script_dir, 'IMS_DB')
    questions = load_questions(ims_db_dir if os.path.exists(ims_db_dir) else '.')
    print(f"Total questions loaded: {len(questions)}")
    
    # Filter for Application Programming questions
    print("\nFiltering for Application Programming questions...")
    app_prog_questions = filter_app_prog_questions(questions)
    print(f"Application Programming questions: {len(app_prog_questions)}")
    print(f"System Programming questions filtered out: {len(questions) - len(app_prog_questions)}")
    
    # Remove duplicates
    print("\nRemoving duplicate questions...")
    app_prog_questions = remove_duplicates(app_prog_questions)
    print(f"Unique questions after deduplication: {len(app_prog_questions)}")
    
    # Load additional questions if we have them
    additional_file = 'additional_questions.json'
    if os.path.exists(additional_file):
        print(f"\nLoading additional questions from {additional_file}...")
        with open(additional_file, 'r') as f:
            additional_questions = json.load(f)
            print(f"Additional questions loaded: {len(additional_questions)}")
            app_prog_questions.extend(additional_questions)
    
    # Take exactly 300 questions
    if len(app_prog_questions) >= 300:
        final_questions = app_prog_questions[:300]
    else:
        print(f"\nWARNING: Only {len(app_prog_questions)} total questions available.")
        print(f"Need {300 - len(app_prog_questions)} more questions to reach 300.")
        final_questions = app_prog_questions
    
    # Renumber questions
    final_questions = renumber_questions(final_questions)
    
    print(f"\nFinal question count: {len(final_questions)}")
    
    # Generate outputs
    print("\nGenerating Markdown output...")
    generate_markdown_output(final_questions, 'IMS_APP_PROG_QUESTIONS.md')
    print("✓ Created IMS_APP_PROG_QUESTIONS.md")
    
    print("\nGenerating JSON output...")
    generate_json_output(final_questions, 'IMS_APP_PROG_QUESTIONS.json')
    print("✓ Created IMS_APP_PROG_QUESTIONS.json")
    
    print("\n✓ Done!")
    print(f"\nSummary:")
    print(f"  - Total questions generated: {len(final_questions)}")
    print(f"  - Output files: IMS_APP_PROG_QUESTIONS.md, IMS_APP_PROG_QUESTIONS.json")
    print(f"  - Questions focus: IMS Application Programming")

if __name__ == '__main__':
    main()
