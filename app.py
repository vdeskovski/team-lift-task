from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

ADMIN_LIST = ["Python", "relational database", "Software engineering",
"data science", "NLP", "natural language processing"]

def find_matches(query: str):
    query_words = set(query.lower().split())
    match_results = []
    for skill in ADMIN_LIST:
        skill_words = set(skill.lower().split())
        match_score = len(query_words & skill_words) / len(skill_words)
        match_results.append({"skill_name": skill, "match_score": round(match_score,2)})
    match_results = sorted(match_results, key=lambda x: x["match_score"], reverse=True)
    return match_results

@app.post("/query")
async def submit_query(query: str = Form(...)):
    match_result = find_matches(query)
    return JSONResponse(content={"query": query, "match_results": match_result})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)