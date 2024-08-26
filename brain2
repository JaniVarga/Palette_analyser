class Brain:
    def __init__(self, file_path):
        self.file_path = file_path
        self.history = []
        self.read_process_history()
        self.system_id = 0
        self.date = ""
        self.filtered_data = []
        self.filtering_from_raw_data()
        self.pallets = []
        self.palette_in_machine()
        self.pass_part_on_pallet = {}
        self.fail_part_on_pallet = {}
        self.failure_summary = {}
        self.data_sorted_by_pallets()
        self.list_of_failures = []
        self.make_list_of_all_failures()
        self.final_summary = {}
        self.make_final_summary()
        self.data = ""
        self.print_out_summary()
        self.data_all = ""
        self.pass_rate_on_palett = {}
        self.failure_rate_on_palett = {}
        self.print_out_all_rates()



    def read_process_history(self):
        with open(self.file_path, mode="r") as history:
            self.history = history.readlines()

    def filtering_from_raw_data(self):
        camera_id = ""
        pallet_id = ""
        for row in self.history:
            raw_data = row.strip().split(":")
            if raw_data[0] == "SYSTEM ID":
                self.system_id = raw_data[1].strip()
            if raw_data[0] == "DATE":
                self.date = raw_data[1].strip().split(" ")[0]
            if raw_data[0] == "CAMERA ID":
                camera_id = raw_data[1].strip()
            if raw_data[0] == "PALLET ID":
                pallet_id = raw_data[1].strip()
            if raw_data[0] == "RESULT":
                pre_data = raw_data[1].strip()
                if "057" in pre_data:
                    result = "FAIL FT - (057) Particle Test Failed."
                    test = {
                        "cam_id": camera_id,
                        "pallet_id": pallet_id,
                        "result": result,
                    }
                    self.filtered_data.append(test)
                else:
                    result = raw_data[1].strip()
                    test = {
                        "cam_id": camera_id,
                        "pallet_id": pallet_id,
                        "result": result,
                    }
                    self.filtered_data.append(test)

    def palette_in_machine(self):
        for data in self.filtered_data:
            self.pallets.append(data["pallet_id"])
        self.pallets = list(dict.fromkeys(self.pallets))

    def data_sorted_by_pallets(self):
        quantity_ok = 0
        quantity_nok = 0
        for pal in self.pallets:
            failure_list = []
            for dat in self.filtered_data:
                if dat["pallet_id"] == pal and dat["result"] != "PASS":
                    failure_list.append(dat["result"])
                    self.failure_summary[pal] = failure_list
                else:
                    self.pass_part_on_pallet[pal] = quantity_ok
                    self.fail_part_on_pallet[pal] = quantity_nok

        for pal in self.pallets:
            for dat in self.filtered_data:
                if dat["pallet_id"] == pal and dat["result"] == "PASS":
                    self.pass_part_on_pallet[pal] += 1
                if dat["pallet_id"] == pal and dat["result"] != "PASS":
                    self.fail_part_on_pallet[pal] += 1


    def make_list_of_all_failures(self):
        for failure_lists in self.failure_summary:
            for failures in self.failure_summary[failure_lists]:
                self.list_of_failures.append(failures)

        self.list_of_failures = list(dict.fromkeys(self.list_of_failures))

    def make_final_summary(self):
        for failures in self.failure_summary:
            pallet_number = failures
            self.final_summary[pallet_number] = {}
            for pieces_of_failure in self.failure_summary[failures]:
                for compare_failure in self.list_of_failures:
                    if pieces_of_failure == compare_failure:
                        self.final_summary[pallet_number][compare_failure] = 0

        # Feltölti a fent létrehozott dictionary-t
        for fail in self.final_summary:
            for f_fail in self.final_summary[fail]:
                for l_fail in self.failure_summary[fail]:
                    if f_fail == l_fail:
                        self.final_summary[fail][f_fail] += 1


    def print_out_summary(self):
        for _dict in self.final_summary:
            failure_rate = round(
                (self.fail_part_on_pallet[_dict] / (self.pass_part_on_pallet[_dict] + self.fail_part_on_pallet[_dict])) * 100, 2)
            passing_rate = 100 - failure_rate
            #print(
              #  f"Paletta: {_dict}; Jó termék a palettán: {self.pass_part_on_pallet[_dict]} db; Hibaarány: {failure_rate}%; "
               # f"PASS%: {passing_rate}% \n")
            header = f"Paletta: {_dict} "
            self.data += f"\n {header}\n\n"
            for row in self.final_summary[_dict]:
                #print(f"{row} : {self.final_summary[_dict][row]} db")
                main = f"\t{row} : {self.final_summary[_dict][row]} db"
                self.data += f"{main}\n "
        # print("\n")

    def print_out_all_rates(self):
        for _dict in self.final_summary:
            failure_rate = round(
                (self.fail_part_on_pallet[_dict] / (self.pass_part_on_pallet[_dict] + self.fail_part_on_pallet[_dict])) * 100, 2)
            passing_rate = 100 - failure_rate
            self.failure_rate_on_palett[_dict] = failure_rate
            self.pass_rate_on_palett[_dict] = passing_rate
            # print(
             #   f"Paletta: {_dict}; Jó termék a palettán: {self.pass_part_on_pallet[_dict]} db; Hibaarány: {failure_rate}%; "
              #  f"PASS%: {passing_rate}% \n")
            header = f"Paletta: {_dict}  OK termék: {self.pass_part_on_pallet[_dict]} db  Hibaarány: {failure_rate}%  PASS%: {passing_rate}% \n"
            self.data_all += f"{header}"




