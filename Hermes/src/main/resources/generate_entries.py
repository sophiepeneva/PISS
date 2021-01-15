import json



def generate_json_entry(id, hour, minute, stationId, bus_num, people_count, off, on):
    json_dict = {
        "id": id,
        "timestamp": f"2021-01-14T{hour}:{minute}:00Z",
        "stationId": stationId,
        "peopleCountCurrent": people_count,
        "peopleGettingOffTheBus": off,
        "peopleGettingOnTheBus": on,
        "number": bus_num
    }

    return json_dict

def main():
    stations   = (i for i in range(60))
    people_in  = (i for i in [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    people_out = (i for i in [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    total_people_count = 0

    print('[')
    id = 1
    for hour in range(10):
        for minute in range(6):
            current_people_out = next(people_out)*10
            current_people_in = next(people_in)*10
            total_people_count += current_people_in - current_people_out
            print(json.dumps(generate_json_entry(id, hour, minute * 10, next(stations), 73, total_people_count, current_people_out, current_people_in)), ',')
    print(']')


if __name__ == "__main__":
    main()