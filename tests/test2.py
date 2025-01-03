import requests
import json
import os

OPENROUTER_API_KEY = os.getenv('API_KEY')

def get_completion(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        completion = response.json()
        return completion.get('choices')[0].get('message').get('content')
    else:
        return f"Error: {response.status_code} - {response.text}"

def analyze_job_description(job_description):
    prompt = f"You are a career coach with 10 years of experience refining resumes for applicants. Analyze the following job description in detail;\n{job_description}"
    print(prompt)
    analysis = get_completion(prompt)
    print(analysis)

def extract_keywords(job_description):
    # Set up the prompt for extracting keywords
    prompt = "Find all essential keywords, including subjects, topics, functions and etc., in this job description."
    
    # Combine prompts with job description for context
    context_prompt = f"You are a career coach with 10 years of experience refining resumes for applicants. Analyze the following job description in detail;\n{job_description}"
    
    # First make context
    get_completion(context_prompt)
    
    # Then extract keywords
    keywords_response = get_completion(prompt)
    
    # Convert response to JSON format
    keywords_list = keywords_response.split(', ')  # Assuming the response is comma-separated
    with open('keywords.json', 'w') as file:
        json.dump(keywords_list, file)

# Example usage
job_description = """# **Equipment Planner**

- Full Time
- 1.00
- 800-1600
- Saturday, Statutory, Sunday
- Facilities Management
- 60575

mail_outline

Get future jobs matching this search

**Login**or**Register**

**Salary**

The salary range for this position is CAD $45.46 - $65.35 / hour

**Job Summary**

Fraser Health continues to be recognized as one of BC's Top Employers, are you someone who is passionate about making a difference in the lives of others?

Fraser Health is responsible for the delivery of hospital and community-based health services to over 1.9 million people in 20 diverse communities from Burnaby to Fraser Canyon on the traditional territories of the Coast Salish and Nlaka’pamux Nations. Our team of nearly 45,000 staff, medical staff and volunteers is dedicated to serving our patients, families and communities to deliver on our vision: Better health, best in health care.

We currently have an exciting **Full Time** opportunity for an **Equipment Planner** to join our team at **Central City Office in Surrey, BC.**

**Take the next step and apply so we can continue the conversation with you.**

Come work with dedicated health care providers who are enthusiastic and committed to provide quality healthcare to our clients/patients/residents.

Curious to learn what it’s like to work here? Like us on Facebook (@fraserhealthcareers), follow us on Twitter & Instagram (@FHCareer), or connect with us on LinkedIn (fraserhealthcareers) for first-hand employee insights.

**Detailed Overview**

**Supporting the Vision, Values, Purpose and Commitments of Fraser Health including service delivery that is centered around patients/clients/residents and families:**

Responsible for developing, reviewing and coordinating clinical equipment needs throughout the planning process including the development of specifications details and inventory assessment of all clinical equipment requirements for various projects at Fraser Health (FH); works with a project planning team to establish, review and incorporate equipment lists into the planning and implementation phase of capital projects; assists with the developing the equipment budget and the installation of clinical equipment; maintains a project equipment database for FH.

**Responsibilities**

1. Works with the project planning teams to develop strategies and processes to manage and minimize FH contractual and technical risk associated with budget planning, design integration, equipment specifications, selection and installation of all project related equipment; develops strategies and processes for collecting, tracking, reviewing and maintaining all clinical equipment data.
2. Establishes a process with the user group of a capital project for the development and review of the equipment list that responds to a desired and documented operational plan; prepares business cases around equipment budget planning and forecasting including project requirements.
3. Conducts research to ensure evidence-based information is provided throughout the project planning processes to identify and resolve critical path issues and to develop appropriate means to resolve these path issues.
4. Develops project schedules and ensures activities and cost targets are adhered to by working with user groups to complete assigned to target dates; identifies and report equipment and equipment-related problems or deviations from the approved plan; prepared justification reports as needed to accompany any requested equipment changes
5. Consults with Clinical and Facilities Planners in establishing and reviewing clinical equipment lists ensuring that appropriate specifications are established and design reflects user requirements and needs; prepares equipment lists and associated budget and funding source; develops a procurement strategy including organizing equipment based on dollar value in consultation with the Procurement Department; confirms that adequate funding is in place.
6. Works with the other team members to ensure that facility design accommodates equipment space and functional requirements including utilization needs; reviews proposed equipment lists and facility plans with user groups to ensure architectural, electrical and/or plumbing plan support such equipment; performs site inspections to ensure proper dimensional specifications and services have been provided for equipment installations.
7. Works with external consultants to identify specific manufacturers and equipment models to ensure established standard, user needs and safety protocols are maintains during equipment selection, installation and user training; integrates existing equipment inventory into room standards and tailors equipment requirements to the specific department requirements.
8. Manages risks and issues related to equipment to ensure project integrity, escalating issues as appropriate; prepares status reports at project milestones that reflect progress, budget, risks and issues.
9. Maintains an up-to-date knowledge base of medical equipment, clinical products and technological advances by reviewing literature, attending product forms and networking with suppliers and vendors.
10. Participates in equipment planning meetings and/or committees as it relates to budgeting, evidence-based practice, asset management and equipment forecasting, as requested.

**Qualifications**

**Education and Experience**

A level of education, training and experience equivalent to a Bachelor’s degree in Biomedical Engineering, clinical engineering, biomedical technology, or health technology, supplemented with five (5) to seven (7) years’ recent, related experience with complex medical equipment.

**Competencies**

Demonstrates the leadership practices of the Fraser Health Leadership Framework of Clear, Caring and Courageous and creates the conditions for people to succeed.

**Professional/Technical Capabilities:**

- Demonstrated ability to work effectively both independently and in collaboration/consultation with others
- Comprehensive knowledge of health care delivery systems
- Knowledge of project management principles and methodologies
- Strong analytical, critical thinking and evaluation skills
- Ability to develop and maintain rapport with others
- Ability to organize and prioritize work in a dynamic environment with changing priorities
- Ability to persuade and provide leadership and guidance to others
- Ability to operate related equipment including related software applications
- Physical ability to perform the duties of the position.

**About Fraser Health**

Fraser Health is the heart of health care for over two million people in Metro Vancouver and the Fraser Valley in British Columbia, Canada, on the traditional, ancestral and unceded lands of the Coast Salish and Nlaka’pamux Nations and is home to 32 First Nations within the Fraser Salish region.

People - those we care for and those who care for them - are at the heart of everything we do. Our hospital and community-based services are delivered by a team of 48,000+ staff, medical staff and volunteers.

We are committed to planetary health and value diversity in the work force. We strive to maintain an environment of respect, caring and trust. Fraser Health’s hiring practices aspire to ensure all individuals are treated in an inclusive, equitable and culturally safe manner.

**Together, we are the heart of health care.**

[Instagram](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.instagram.com%2Ffhcareer%2F&data=05%7C02%7Cmaria.obaid%40fraserhealth.ca%7C1cc8f5d65a264236927808dcb3292aaa%7C31f660a5192a4db392baca424f1b259e%7C0%7C0%7C638582236583664636%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=c1CKMe2R5ZqrvuHFiCazAnZfFr7X9uErxg9EfkuSuRQ%3D&reserved=0) | [Facebook](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.facebook.com%2Ffraserhealthcareers&data=05%7C02%7Cmaria.obaid%40fraserhealth.ca%7C1cc8f5d65a264236927808dcb3292aaa%7C31f660a5192a4db392baca424f1b259e%7C0%7C0%7C638582236583682404%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=GqiBjABl7mLvt2ZbBliub5iYJh%2FUBuB5MHMvmwDs9mY%3D&reserved=0) | [LinkedIn](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Ffraser-health-authority&data=05%7C02%7Cmaria.obaid%40fraserhealth.ca%7C1cc8f5d65a264236927808dcb3292aaa%7C31f660a5192a4db392baca424f1b259e%7C0%7C0%7C638582236583696389%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=yJdYv1M3d9g15Kiy495cr5fYJ65MhsnIbJNveXpCIN8%3D&reserved=0) | [X](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftwitter.com%2FFHcareer&data=05%7C02%7Cmaria.obaid%40fraserhealth.ca%7C1cc8f5d65a264236927808dcb3292aaa%7C31f660a5192a4db392baca424f1b259e%7C0%7C0%7C638582236583708968%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=Z%2FBZhLGLhrOS9MMiBRctpAo1bQ6HGpWjFPhSDwMHN6Y%3D&reserved=0) | [Indeed](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fca.indeed.com%2Fcmp%2FFraser-Health-49d6cb26&data=05%7C02%7Cmaria.obaid%40fraserhealth.ca%7C1cc8f5d65a264236927808dcb3292aaa%7C31f660a5192a4db392baca424f1b259e%7C0%7C0%7C638582236583720661%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=wZx6TFXhd3ha2jRfm4PU1ywVxCjHkE%2BatZkVIE03pi8%3D&reserved=0) | [Glassdoor](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.glassdoor.ca%2FOverview%2FWorking-at-Fraser-Health-EI_IE248782.11%2C24.htm&data=05%7C02%7Cmaria.obaid%40fraserhealth.ca%7C1cc8f5d65a264236927808dcb3292aaa%7C31f660a5192a4db392baca424f1b259e%7C0%7C0%7C638582236583731142%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=mfXf2bxLRPdqK7u%2B9t3n40bXiCKDMLzALu4rzxv4Og8%3D&reserved=0)

Follow our Careers social channels to learn about our culture and values, hear directly from some of your future colleagues, stay updated on exciting opportunities and get valuable career tips from our recruiters."""
analyze_job_description(job_description)  # Initialize context
# extract_keywords(job_description)  # Extract and save keywords