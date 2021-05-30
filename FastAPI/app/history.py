
history = list()

async def fetch_all_histories():
    return history

async def update_history(input):
    try:
        history.append(input)
        return True
    except:
        return False
