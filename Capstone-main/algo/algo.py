#import pull_sql_data

def check_threshold(box_data, room_thresholds, algo_threshold, weights):
    """
    Check if the data from the weather box satisfies the threshold condition
    with respect to the specified minimum and maximum thresholds.

    Args:
    - box_data (dict): Dictionary containing data from the weather box.
    - room_thresholds (dict): Dictionary containing min/max thresholds for each data value.
    - algo_threshold (int): Integer representing the +- threshold
    - weights (dict): Dictionary containing weights for each data value.

    Returns:
    - int: 1 if condition is met, otherwise 0.
    """
    total_weighted_difference = 0

    # Iterate over each data value in the box_data dictionary
    for key, value in box_data.items():
        if key in room_thresholds:
            min_threshold, max_threshold = room_thresholds[key]
            weight = weights.get(key, 1.0)

            # Check if the value is outside the specified threshold range
            if value < min_threshold:
                weighted_difference = (min_threshold - value) * weight
            elif value > max_threshold:
                weighted_difference = (value - max_threshold) * weight
            else:
                weighted_difference = 0

            # Accumulate the weighted differences
            total_weighted_difference += weighted_difference

    # Check if the total weighted difference satisfies the threshold condition
    if total_weighted_difference >= algo_threshold:
        return 1
    else:
        return 0


def main():
    # Assuming you have obtained data from the weather API and the weather box
    '''
    weather = WeatherInfo('Norman', 'US', '67527409760b0484db2e2c1951850f0a')

    api_data = weather.get_weather_data()
    '''

    box_data = {
        "room_temperature": 22,  # Assuming the temperature in the room is 22C
        "humidity": 45  # Assuming the humidity in the room is 45%
        # Add more data from the weather box as needed
    }

    # Define thresholds for each variable (min, max)
    room_thresholds = {
        "room_temperature": (21, 24),  # Threshold for temperature (21C to 24C)
        "humidity": (40, 60)  # Threshold for humidity (40% to 60%)
        # Add more thresholds as needed
    }

    # Define weights for each variable
    weights = {
        "room_temperature": 1.0,  # Weight for temperature comparison
        "humidity": 0.8  # Weight for humidity comparison
        # Add more weights as needed
    }

    # Set the threshold based on your preference
    algo_threshold = 1.0  # Adjust as needed

    # Check if the condition is met
    result = check_threshold(box_data, room_thresholds, algo_threshold, weights)
    if result == 1:
        print("Open the window!")  # If the condition is met
    else:
        print("Close the window!")  # If the condition is not met

if __name__ == '__main__':
    main()