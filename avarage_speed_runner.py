#get speed values for 10 runners
runner_speeds = []
for i in range(10):
    speed = float(input(f"enter speed of runner {i+1} (km/h): "))
    runner_speeds.append(speed)
# Calculate average speed
average_speed = sum(runner_speeds) / len(runner_speeds)
#  get qualified runners
qualified_runners = []
for i, speed in enumerate(runner_speeds):
    if speed > 1.5*average_speed:
        qualified_runners.append((i+1, speed))
        # print results
        print(f" average speed :{average_speed:.2f} km/h")
        print("qualified runners :")
for runner in qualified_runners:
    print(f"Runner {runner[0]} - speed: {runner[1]:.2f} km/h")