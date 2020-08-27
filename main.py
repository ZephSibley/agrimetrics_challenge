from fastapi import FastAPI

app = FastAPI()

SCHEDULE = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/order")
async def order():
    from datetime import datetime, timedelta
    current_time = datetime.now()
    make_time = current_time

    if SCHEDULE:
        latest_scheduled_time = SCHEDULE[-1][0]
        if current_time < latest_scheduled_time:
            # The latest entry is always 'Take a break'
            SCHEDULE.pop()
            time_diff = latest_scheduled_time - current_time
            make_time += time_diff

    SCHEDULE.append((make_time, 'Make sandwich'))
    SCHEDULE.append((make_time + timedelta(seconds=150), 'Serve sandwich'))
    SCHEDULE.append((make_time + timedelta(seconds=210), 'Take a break'))

    return {"message": "OK"}


@app.get("/schedule")
async def schedule():
    return {"schedule": SCHEDULE}
