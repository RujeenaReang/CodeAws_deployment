from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Resume Skill API")


class ResumeRequest(BaseModel):
    text: str


SKILLS = [
    "Python",
    "FastAPI",
    "LangChain",
    "LangGraph",
    "AWS",
    "SQL",
    "Docker",
    "Git",
    "Machine Learning",
    "Generative AI",
]


@app.get("/")
def health_check():
    return {"status": "running"}


@app.post("/analyze")
def analyze_resume(request: ResumeRequest):

    text = request.text.lower()

    found_skills = [
        skill for skill in SKILLS
        if skill.lower() in text
    ]
 
    return {
        "skills": found_skills,
        "skill_count": len(found_skills)
    }