import random
from django.utils import timezone

def generate_otp(length=6):
   otp_int = random.randint(0,10**length-1)
   otp_str = str(otp_int).zfill(length)
   return otp_str


def send_otp_via_sms(phone_number,otp):
    print(f"[DEBUG] sending OTP {otp} to {phone_number}")
