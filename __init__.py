
import platform
import subprocess
import os

class StandbyButton:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "STANDBY": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "standby_now"
    OUTPUT_NODE = True
    CATEGORY = "System"

    def standby_now(self, confirm=False):
        if not confirm:
            print("Standby nicht bestätigt.")
            return ()

        system = platform.system()
        try:
            if system == "Windows":
                subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"], shell=True)
            elif system == "Linux":
                subprocess.run(["systemctl", "suspend"])
            elif system == "Darwin":
                subprocess.run(["pmset", "sleepnow"])
            else:
                raise Exception("Nicht unterstütztes Betriebssystem.")
        except Exception as e:
            print(f"Fehler beim Standby: {e}")
        return ()

    @classmethod
    def IS_PREVIEW(cls):
        return True

    def preview(self, **kwargs):
        image_path = os.path.join(os.path.dirname(__file__), "standby.png")
        if os.path.exists(image_path):
            return {"image": image_path}
        else:
            return {}

NODE_CLASS_MAPPINGS = {
    "StandbyButton": StandbyButton
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StandbyButton": " Standbybutton ⏾ ⇐ press"
}
