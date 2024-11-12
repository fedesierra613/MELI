from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.utils import is_mutant
from app.database import redis_client

app = FastAPI()

class DNABody(BaseModel):
    dna: list[str]

@app.post("/mutant/")
async def check_mutant(dna_body: DNABody):
    dna_str = ",".join(dna_body.dna)
    cached_result = redis_client.get(dna_str)
    
    if cached_result is not None:
        is_mutant_result = cached_result == "1"
    else:
        try:
            is_mutant_result = is_mutant(dna_body.dna)
            
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    if is_mutant_result:
        redis_client.incr("count_mutant_dna")
        return {"status": "Mutant detected"}
    else:
        redis_client.incr("count_human_dna")
        raise HTTPException(status_code=403, detail="Not a mutant")


@app.get("/stats")
async def get_stats():
    mutant_count = int(redis_client.get("count_mutant_dna") or 0)
    human_count = int(redis_client.get("count_human_dna") or 0)
    ratio = round(mutant_count / (human_count or 1), 2)
    return {
        "count_mutant_dna": mutant_count,
        "count_human_dna": human_count,
        "ratio": ratio
    }
