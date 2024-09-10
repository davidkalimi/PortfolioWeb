from flask import Flask, render_template
import os

app = Flask(__name__)

resume_data = {
    "name": "David Kalimi",
    "title": "Data Analyst, Ex-8200, Data Science Engineering Student",
    "contact_info": {
        "location": "Ashdod, Israel",
        "phone": "052-4300492",
        "email": "davidkalimyy@gmail.com",
        "linkedin": "https://www.linkedin.com/in/david-kalimi-65751a222"
    },
    "profile": "Experienced data analyst with a background in Unit 8200. Driven and ambitious, I thrive on learning and tackling new challenges to enhance my abilities. Enthusiast of AI and mathematics.",
    "employment": [
        {
            "title": "Data Science Engineering Student",
            "company": "BGU University",
            "duration": "Jan 2024 – Present",
            "details": ["Studying advanced concepts in data science and engineering."]
        },
        {
            "title": "Digital Marketing Specialist and Brand Owner",
            "company": "Self-employed",
            "duration": "Jul 2023 — Nov 2023",
            "details": [
                "Managed Shopify online stores, elevating sales and customer engagement.",
                "Built partnerships to streamline operations and led marketing campaigns using Canva.",
                "Leveraged AI tools like ChatGPT, Claude, and Google Gemini for advanced marketing strategies.",
                "Skilled in TikTok and Instagram Ads with a comprehensive grasp of advertising tactics.",
                "Developed GPT applications in ChatGPT for business operations and AI solutions."
            ]
        },
        {
            "title": "Data Analyst, 8200",
            "company": "Israel Defense Forces",
            "duration": "Jul 2022 — Aug 2023",
            "details": [
                "Delivered real-time and daily intelligence reports.",
                "Worked with SQL, Excel, Tableau, and internal systems.",
                "Specialized in computing networks and built user-friendly Tableau dashboards.",
                "Consulted and promoted long-term projects.",
                "Tested, developed, and tutored new intelligence analysts."
            ]
        },
        {
            "title": "Intelligence Analyst, 8200",
            "company": "Israel Defense Forces",
            "duration": "Jan 2022 — Mar 2022",
            "details": [
                "Built flexible, user-friendly Tableau dashboards using SQL, Excel, and internal systems.",
                "Analyzed large, complex data sets for business strategy and implementation."
            ]
        },
        {
            "title": "Data Analyst & BI Developer",
            "company": "Bank Leumi",
            "duration": "Dec 2020 — Dec 2021",
            "details": [
                "Developed Backend BI with Python and SQL working with DWH and Big Data (Hadoop) environments.",
                "Built and maintained Tableau/Power BI dashboards.",
                "Collaborated with bank managers, contributing to decision-making processes.",
                "Strong experience with SQL, Excel, Power BI, Tableau, Python, and SAS."
            ]
        },
        {
            "title": "Intelligence & Data Analyst Team Leader, 8200",
            "company": "Israel Defense Forces",
            "duration": "Nov 2019 — Dec 2020",
            "details": [
                "Managed a team of 17 analysts, overseeing intelligence collection plans and shifts.",
                "Executed strategic intelligence projects and team development under intense work conditions.",
                "Collaborated with AI tool developers to streamline HR operations, revolutionizing work concepts.",
                "Led data collection and ML/DL projects, optimizing team processes and achieving significant efficiency improvements."
            ]
        }
    ],
    "education": [
        {
            "institution": "BGU University",
            "degree": "Data Science Engineering",
            "duration": "Jan 2024 – Present"
        },
        {
            "institution": "Mekif-vav Highschool, Ashdod",
            "degree": "High School Diploma",
            "duration": "Sep 2012 — Jun 2018",
            "details": [
                "Physics: 5 Units",
                "Computer Science: 10 Units",
                "English: 5 Units",
                "Math: 5 Units"
            ]
        }
    ],
    "skills": [
        "Data Analysis", "SQL", "Python", "Excel", "Tableau", "Power BI", "SAS",
        "Big Data (Hadoop)", "Machine Learning", "Deep Learning", "Digital Marketing",
        "AI Tools", "Team Leadership"
    ],
    "languages": [
        {"name": "Hebrew", "proficiency": "Native"},
        {"name": "Persian", "proficiency": "Native"},
        {"name": "English", "proficiency": "Highly proficient"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', resume=resume_data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)