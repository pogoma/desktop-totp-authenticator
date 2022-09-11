import hmac
import time
from base64 import b32decode
from struct import pack, unpack


class Totp:
    def __init__(self, key: str, time_step: int = 30, digits: int = 6, digest: str = 'sha1'):
        self.__digits: int = digits
        self.__digest: str = digest
        self.__decoded_key: bytes = b32decode(key.upper() + '=' * ((8 - len(key)) % 8))
        self.__time_step: int = time_step

    def __hmac_otp(self, counter) -> str:
        counter: bytes = pack('>Q', counter)
        digest: bytes = hmac.new(self.__decoded_key, counter, self.__digest).digest()
        offset = digest[-1] & 0x0f
        result = unpack('>L', digest[offset:offset + 4])[0] & 0x7fffffff
        return str(result)[-self.__digits:].zfill(self.__digits)

    def totp(self) -> str:
        current_counter: int = int(time.time() / self.__time_step)
        return self.__hmac_otp(current_counter)