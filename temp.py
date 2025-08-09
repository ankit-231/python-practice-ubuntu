def temp():
    drone_attributes = [
        {
            "name": "battery_capacity",
            "display_name": "Battery Capacity",
            "data_type": "float",
            "description": "Battery Capacity",
        },
        {
            "name": "motor_range",
            "display_name": "Motor Range",
            "data_type": "float",
            "description": "Motor Range for drone",
        },
        {
            "name": "dimension",
            "display_name": "Dimension",
            "data_type": "float",
            "description": "Dimension of the product",
        },
        {
            "name": "length",
            "display_name": "Length",
            "data_type": "float",
            "description": "Length of the product",
        },
        {
            "name": "weight",
            "display_name": "Weight",
            "data_type": "float",
            "description": "Total weight of the drone in kilograms",
        },
        {
            "name": "flight_time",
            "display_name": "Flight Time",
            "data_type": "float",
            "description": "Maximum flight time of the drone in minutes",
        },
        {
            "name": "max_speed",
            "display_name": "Max Speed",
            "data_type": "float",
            "description": "Maximum speed the drone can achieve in km/h",
        },
        {
            "name": "max_altitude",
            "display_name": "Max Altitude",
            "data_type": "float",
            "description": "Maximum altitude the drone can reach in meters",
        },
        {
            "name": "gps_enabled",
            "display_name": "GPS Enabled",
            "data_type": "boolean",
            "description": "Indicates whether the drone has GPS functionality",
        },
        {
            "name": "camera_resolution",
            "display_name": "Camera Resolution",
            "data_type": "string",
            "description": "Resolution of the drone camera (e.g., 4K, 1080p)",
        },
        {
            "name": "camera_fov",
            "display_name": "Camera FOV",
            "data_type": "float",
            "description": "Field of view of the camera in degrees",
        },
        {
            "name": "transmission_range",
            "display_name": "Transmission Range",
            "data_type": "float",
            "description": "Maximum control or video transmission range in kilometers",
        },
        {
            "name": "obstacle_avoidance",
            "display_name": "Obstacle Avoidance",
            "data_type": "boolean",
            "description": "Whether the drone supports automatic obstacle avoidance",
        },
        {
            "name": "wind_resistance",
            "display_name": "Wind Resistance",
            "data_type": "string",
            "description": "Wind resistance level or maximum safe wind speed (e.g., Level 5 or 10 m/s)",
        },
        {
            "name": "charging_time",
            "display_name": "Charging Time",
            "data_type": "float",
            "description": "Time taken to fully charge the drone battery in hours",
        },
        {
            "name": "control_type",
            "display_name": "Control Type",
            "data_type": "string",
            "description": "Type of controller used (e.g., remote controller, smartphone)",
        },
        {
            "name": "has_return_to_home",
            "display_name": "Has Return to Home",
            "data_type": "boolean",
            "description": "Whether the drone has a return-to-home (RTH) feature",
        },
        {
            "name": "dual_gps",
            "display_name": "Dual GPS",
            "data_type": "boolean",
            "description": "Whether the drone supports both GPS and GLONASS",
        },
        {
            "name": "noise_level",
            "display_name": "Noise Level",
            "data_type": "float",
            "description": "Noise level produced by the drone during operation in dB",
        },
    ]

    battery_attributes = [
        {
            "name": "voltage",
            "display_name": "Voltage",
            "data_type": "float",
            "description": "Voltage of the battery in volts",
        },
        {
            "name": "cell_count",
            "display_name": "Cell Count",
            "data_type": "integer",
            "description": "Number of cells in the battery",
        },
        {
            "name": "configuration",
            "display_name": "Configuration",
            "data_type": "string",
            "description": "Configuration of the battery like 4S1P",
        },
        {
            "name": "battery_type",
            "display_name": "Battery Type",
            "data_type": "string",
            "description": "Type of battery such as LiPo, Li-ion, NiMH",
        },
        {
            "name": "discharge_rate",
            "display_name": "Discharge Rate",
            "data_type": "float",
            "description": "Battery discharge rate in C rating",
        },
    ]

    propeller_attributes = [
        {
            "name": "diameter",
            "display_name": "Diameter",
            "data_type": "float",
            "description": "Diameter of the propeller in inches",
        },
        {
            "name": "pitch",
            "display_name": "Pitch",
            "data_type": "float",
            "description": "Pitch of the propeller in inches",
        },
        {
            "name": "material",
            "display_name": "Material",
            "data_type": "string",
            "description": "Material used in propeller construction such as carbon fiber or plastic",
        },
        {
            "name": "blade_count",
            "display_name": "Blade Count",
            "data_type": "integer",
            "description": "Number of blades in the propeller",
        },
        {
            "name": "rotation_direction",
            "display_name": "Rotation Direction",
            "data_type": "string",
            "description": "Rotation direction of the propeller (CW or CCW)",
        },
    ]

    all_attributes = drone_attributes + battery_attributes + propeller_attributes
    print(len(all_attributes))


if __name__ == "__main__":
    temp()
