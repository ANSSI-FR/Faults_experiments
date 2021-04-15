NB_BITS = 64
NB_REGISTERS = 14
DEFAULT_VALUES = [((1 << (63-i)) + (1 << i)) for i in range(NB_REGISTERS)]

OBS_NAMES = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
TO_TEST = [False, True, False, False, False, False, True, True, True, False, True, True, True, True]

params = {
    "obs_names": OBS_NAMES,
    "default_values": DEFAULT_VALUES,
    "to_test": TO_TEST,
    "power_name": "injector_P",
    "delay_name": "injector_D",
    "done_name": "plan_done",
    "fault_name": "fault",
    "reboot_name": "reboot",
    "log_name": "log",
    "log_separator": ":",
    "log_flag_begin": "FlagBegin",
    "log_flag_end": "FlagEnd",
    "data_format": "0x{:016x}",
    "nb_bits": NB_BITS,
    "executed_instructions": [],
    "coordinates_name": ["plan_ygrid", "plan_xgrid"],
    "stage_coordinates": ["stage_y", "stage_x"],
}
