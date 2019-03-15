from frcmpsp.classes.frcmpsp_instance import Instance


def main():

    # create instance
    instance = Instance()
    # instance.load_json_ts_projects(path=r"C:\Users\brachmann_r\Python Projects\FRCMPSP\log_files\ts_project_json")
    instance.load_json_ts_projects(path=r"C:\Users\brachmann_r\Python Projects\FRCMPSP\log_files\ts_project_json\2.json")
    # generate instance
    instance.generate_instance()


if __name__ == "__main__":
    main()
