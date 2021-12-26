# https://github.com/Zokrates/ZoKrates/blob/deploy/zokrates_stdlib/tests/tests/hashes/sha256/512bitPadded.zok
import hashlib

INPUT_PREIMAGE = 2022

padded_hex_preimage = hex(INPUT_PREIMAGE).lstrip("0x").zfill(128)
padded_hex_bytes_preimage = bytes.fromhex(padded_hex_preimage)
digest = hashlib.sha256(padded_hex_bytes_preimage).hexdigest()
print(
    f"# Preimage (decoded): \n'{(int(padded_hex_bytes_preimage.hex(), 16))}'")
print(f"# SHA256 Digest: \n'{digest}'")
print(f"# Preimage (padded hex): \n{padded_hex_preimage}")
