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
    # Making it a timedelta to support mathematical operations
    make_time = current_time + timedelta()

    if SCHEDULE:
        # Added 60 seconds to account for serving time
        latest_scheduled_time = SCHEDULE[-1][0] + timedelta(seconds=60)

        time_diff = latest_scheduled_time - current_time

        if current_time > latest_scheduled_time:
            SCHEDULE.append((latest_scheduled_time, 'Take a break'))
        else:
            make_time += time_diff

    SCHEDULE.append((make_time, 'Make sandwich'))
    SCHEDULE.append((make_time + timedelta(seconds=150), 'Serve sandwich'))

    return SCHEDULE
