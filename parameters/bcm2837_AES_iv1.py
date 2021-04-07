NB_REGISTERS = 1

DEFAULT_VALUES = [0x69c4e0d86a7b0430d8cdb78070b4c55a]

params = {
    "obs_names": ["c"],
    "default_values": DEFAULT_VALUES,
    "to_test": [True],
    "power_name": "injector_P",
    "delay_name": "injector_D",
    "done_name": "plan_done",
    "fault_name": "fault",
    "reboot_name": "reboot",
    "log_name": "log",
    "log_separator": ";",
    "log_flag_begin": "FlagBegin",
    "log_flag_end": "FlagEnd",
    "data_format": "0x{:032x}",
    "nb_bits": 128,
    "result_base": 16,
    "coordinates_name": ["plan_ygrid", "plan_xgrid"],
    "stage_coordinates": ["stage_y", "stage_x"]
}
