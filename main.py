from fastapi import FastAPI
import uvicorn

app = FastAPI()


# First we make some fake data to be able to use as our "database calls"
class_pass_chance = [
    {"Participant": "a", "chance to fail the class": 0.100, "age": 18},
    {"Participant": "b", "chance to fail the class": 0.110, "age": 17},
    {"Participant": "c", "chance to fail the class": 0.411, "age": 12},
    {"Participant": "d", "chance to fail the class": 0.541, "age": 124},
    {"Participant": "e", "chance to fail the class": 0.154, "age": 15},
    {"Participant": "f", "chance to fail the class": 0.415, "age": 16},
    {"Participant": "g", "chance to fail the class": 0.141, "age": 18},
    {"Participant": "h", "chance to fail the class": 0.114, "age": 13},
    {"Participant": "i", "chance to fail the class": 0.011, "age": 124},
    {"Participant": "j", "chance to fail the class": 0.001, "age": 15},
    {"Participant": "k", "chance to fail the class": 0.123, "age": 16},
    {"Participant": "l", "chance to fail the class": 0.200, "age": 12},
    {"Participant": "m", "chance to fail the class": 1.000, "age": 19},
    {"Participant": "o", "chance to fail the class": 1.000, "age": 18},
    {"Participant": "p", "chance to fail the class": 0.932, "age": 18},
    {"Participant": "q", "chance to fail the class": 0.211, "age": 18},
    {"Participant": "r", "chance to fail the class": 0.985, "age": 17},
    {"Participant": "y", "chance to fail the class": 0.222, "age": 17},
    {"Participant": "x", "chance to fail the class": 0.865, "age": 16},
    {"Participant": "z", "chance to fail the class": 1.000, "age": 19},

]


# Here we see that order matters. Going to this path will trigger this route first rather than the next because it
# comes first
@app.get("/class_pass_chance/intro")
async def get_me():
    return {"participant": "chance to fail the class"}


# Parameters in our route definitions allow us to match multiple paths
@app.get("/class_pass_chance/{Participant}")
async def get_profile(participant_name: str):
    for participant in class_pass_chance:
        if participant["Participant"].lower() == participant_name.lower():
            return participant
    return {"msg": "User not found"}


# Here we see another way to create dynamic routes using query parameters


@app.get("/secret")
async def get_secret():
    return {"msg": "The secret is: I don't have a secret"}
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)