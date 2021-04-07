NB_BITS = 32
NB_REGISTERS = 10
DEFAULT_VALUES = [0xfffe0001,
                  0xfffd0002,
                  0xfffb0004,
                  0xfff70008,
                  0xffef0010,
                  0xffdf0020,
                  0xffbf0040,
                  0xff7f0080,
                  0xfeff0100,
                  0xfdff0200,
]
params = {
    "default_values": DEFAULT_VALUES,
    "obs_names": ["r{}".format(i) for i in range(NB_REGISTERS)],
    "to_test": [True for i in range(NB_REGISTERS)],
    "reboot_name": "reboot",
    "log_name": "log",
    "log_separator": ";",
    "log_flag_begin": "FlagBegin",
    "log_flag_end": "FlagEnd",
    "nb_bits": NB_BITS,
    "reboot_name": "reboot",
    "coordinates_name": ["x_pos", "y_pos"],
    "carto_resolution": [7303, 6407],
}
