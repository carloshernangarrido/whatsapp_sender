
import pyautogui as pg
from datetime import datetime as dt, timedelta
import phonenumbers
import myexceptions as ex


def e164(tel_number):
    try:
        parsed_number = phonenumbers.parse(tel_number, "AR")
        formated_tel_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    except Exception:
        print(ex.E1)
        print(tel_number)
        return -1
    return formated_tel_number


def wait_seconds(s):
    now_s = dt.now()
    while dt.now() < now_s+timedelta(seconds=s):
        pass


def close_tab():
    pg.keyDown('ctrl')
    pg.press('f4')
    pg.keyUp('ctrl')