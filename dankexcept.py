 # dankexcept module

from time import time

def test(obj_type: str, obj_name) -> None:
    print(f"Testing object {obj_name}\nType: {obj_type}\n");
    obj_obj = obj_name()
    obj_obj.set_year();
    
    return(0);

class Logger:
    secInFourY = (86400 * 365 * 3) + (86400 * 366);
    year = 1970
    day = 1
    month = 1

    def __init__(self) -> None:
        self.today = round(time())
    
    def set_year(self) -> int:
        y_cnt = 0;
        sec_rem = self.today;
        tot_sec = 0;
        print(f"y{y_cnt} r{sec_rem} t{tot_sec}")
        while tot_sec < self.today:
            tot_sec = tot_sec + self.secInFourY
            y_cnt = y_cnt + 4
            sec_rem = sec_rem - self.secInFourY
            print(f"y{y_cnt} r{sec_rem} t{tot_sec}")

        print(f"y_cnt: {y_cnt}");
        print(f"sec_rem: {sec_rem}");
        print(f"tot_sec: {tot_sec}");




def handle_exception(fatal: bool, func_name: str, msg: str) -> int:

    return(0);

if __name__ == '__main__':
    print("##############################");
    print("### dankexcept run as main ###");
    print("##############################\n");
    test("class", Logger)
