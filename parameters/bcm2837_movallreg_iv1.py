NB_REGISTERS = 10

DEFAULT_VALUES = [((1 << (31-i)) + (1 << i)) for i in range(NB_REGISTERS)]

params = {
    "obs_names": ["r{}".format(i) for i in range(NB_REGISTERS)],
    "default_values": DEFAULT_VALUES,
    "to_test": [True for i in range(NB_REGISTERS)],
    "power_name": "injector_P",
    "delay_name": "injector_D",
    "done_name": "plan_done",
    "fault_name": "fault",
    "reboot_name": "reboot",
    "log_name": "log",
    "log_separator": ";",
    "log_flag_begin": "FlagBegin",
    "log_flag_end": "FlagEnd",
    "data_format": "0x{:08x}",
    "nb_bits": 32,
    "coordinates_name": ["plan_ygrid", "plan_xgrid"],
    "stage_coordinates": ["stage_y", "stage_x"],
}
