from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from suppoter import kv
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.picker import MDThemePicker
import webbrowser
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image


class ImageButton(ButtonBehavior, Image):
    pass


class Mechsem1screen(Screen):
    pass


class Mechsem2screen(Screen):
    pass


class FirebaseLoginScreen(Screen):
    pass


class Mechsem3screen(Screen):
    pass


class Mechsem4screen(Screen):
    pass


class Mechsem5screen(Screen):
    pass


class Mechsem6screen(Screen):
    pass


class Mechsem7screen(Screen):
    pass


class Mechsem8screen(Screen):
    pass


class Ecesem1screen(Screen):
    pass


class Ecesem2screen(Screen):
    pass


class Ecesem3screen(Screen):
    pass


class Ecesem4screen(Screen):
    pass


class Ecesem5screen(Screen):
    pass


class Ecesem6screen(Screen):
    pass


class Ecesem7screen(Screen):
    pass


class Ecesem8screen(Screen):
    pass


class Itsem1screen(Screen):
    pass


class Itsem2screen(Screen):
    pass


class Itsem3screen(Screen):
    pass


class Itsem4screen(Screen):
    pass


class Itsem5screen(Screen):
    pass


class Itsem6screen(Screen):
    pass


class Itsem7screen(Screen):
    pass


class Itsem8screen(Screen):
    pass


class Csesem1screen(Screen):
    pass


class Csesem2screen(Screen):
    pass


class Csesem3screen(Screen):
    pass


class Csesem4screen(Screen):
    pass


class Csesem5screen(Screen):
    pass


class Csesem6screen(Screen):
    pass


class Csesem7screen(Screen):
    pass


class Csesem8screen(Screen):
    pass


class Csescreen(Screen):
    pass


class Itscreen(Screen):
    pass


class Ecescreen(Screen):
    pass


class Mechscreen(Screen):
    pass


class Infoscreen(Screen):
    pass


class Contactscreen(Screen):
    pass


class Aboutscreen(Screen):
    pass


class Mainscreen(Screen):
    pass


class Secondscreen(Screen):
    pass


class windowmanager(ScreenManager):
    pass


Window.size = (300, 500)


class RMKEGURU(MDApp):
    def build(self):
        k = Builder.load_string(kv)
        return k

    def clg(self):
        webbrowser.open('https://www.rmkec.ac.in/')

    def web(self):
        webbrowser.open('https://www.facebook.com/rmkec.ac.in')

    def bro(self):
        webbrowser.open('https://www.instagram.com/rmkec1234/')

    def wb(self):
        webbrowser.open('https://www.linkedin.com/company/rmkec-institution/')

    def show_popup(self):
        toast("RMK Contact Details.")

    def show(self):
        toast("Click The Logo.")

    def shho(self):
        toast("Select Your Department.")

    def shoo(self):
        toast("App Makers.")

    def sub(self):
        toast("Select Subject.")

    def avali(self):
        toast("Available Soon.")

    def naren(self):
        ok = MDRectangleFlatButton(text='Ok', on_press=self.close_naren)
        self.narendra = MDDialog(title="P.Narendra kumar", text="Branch:CSE    Mail:pall18225.cs@rmkec.ac.in "
                                                                "     Batch:2018-2022",
                                 size_hint=[0.7, 0.7], auto_dismiss=False, buttons=[ok])
        self.narendra.open()

    def close_naren(self, obj):
        self.narendra.dismiss()

    def sumanth(self):
        ok = MDRectangleFlatButton(text='Ok', on_press=self.close_sumanth)
        self.sumanthsai = MDDialog(title="T.Sai Sumanth", text="Branch:CSE    Mail:tond18322.cs@rmkec.ac.in "
                                                               "     Batch:2018-2022",
                                   size_hint=[0.7, 0.7], auto_dismiss=False, buttons=[ok])
        self.sumanthsai.open()

    def close_sumanth(self, obj):
        self.sumanthsai.dismiss()

    def siva(self):
        ok = MDRectangleFlatButton(text='Ok', on_press=self.close_siva)
        self.saisiva = MDDialog(title="V.Sai Siva", text="Branch:CSE    Mail:vema18329.cs@rmkec.ac.in "
                                                         "     Batch:2018-2022",
                                size_hint=[0.7, 0.7], auto_dismiss=False, buttons=[ok])
        self.saisiva.open()

    def close_siva(self, obj):
        self.saisiva.dismiss()

    def show_dai(self):
        ok = MDRectangleFlatButton(text='Ok', on_press=self.close_dialog)
        self.my_dai = MDDialog(title="Contact Mail", text="principal@rmkec.ac.in / rmkec@vsnl.com",
                               size_hint=[0.7, 0.7], auto_dismiss=False, buttons=[ok])
        self.my_dai.open()

    def close_dialog(self, obj):
        self.my_dai.dismiss()

    def show_da(self):
        ok = MDRectangleFlatButton(text='Ok', on_press=self.close_dial)
        self.my_da = MDDialog(title="Contact Number", text="044 - 3330 3330",
                              size_hint=[0.7, 0.7], auto_dismiss=False, buttons=[ok])
        self.my_da.open()

    def close_dial(self, obj):
        self.my_da.dismiss()

    def show_dia(self):
        ok = MDRectangleFlatButton(text='Ok', on_press=self.close_dialo)
        self.my_dia = MDDialog(title="Contact Mail",
                               text="RSM Nagar,Kavaraipettai,Gummidipoondi Taluk,Tiruvallur District,Tamil Nadu,Pin:601 206",
                               size_hint=[0.8, 0.8], auto_dismiss=False, buttons=[ok])
        self.my_dia.open()

    def close_dialo(self, obj):
        self.my_dia.dismiss()

    def change(self):
        self.root.current = 'second'

    def change_screen(self):
        self.root.current = 'cse'

    def change_s(self):
        self.root.current = 'it'

    def change_se(self):
        self.root.current = 'ece'

    def change_sce(self):
        self.root.current = 'mech'

    def goto(self):
        self.root.current = 'second'

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def eceMA8352all(self):
        webbrowser.open('https://drive.google.com/file/d/1zq3aWiholkbAKs2uP31u26tgOCfRK_OM/view')

    def eceEC8393all(self):
        webbrowser.open('https://drive.google.com/file/d/15B4iRi-qiU9wizHPHczMYOdT_MFLB8QR/view')

    def eceEC8351all(self):
        webbrowser.open('https://drive.google.com/file/d/1Gu9pq2E0gkzONGzGlqoxm9Su3iMw6rTP/view')

    def eceEC8352all(self):
        webbrowser.open('https://drive.google.com/file/d/1MNMek23kpSbCgtSVTTfTt8Ho75o9UIkr/view')

    def eceEC8392all(self):
        webbrowser.open('https://drive.google.com/file/d/1mszyrAKjglXIvuOoM4hgTXIA5dySSUCC/view')

    def eceEC8391all(self):
        webbrowser.open('https://drive.google.com/file/d/1PQJUWPIgmhiHvTR5tPG-klqCsppwSsAk/view')

    def eceEC8452all(self):
        webbrowser.open('https://drive.google.com/file/d/16-U5fDM2EgHf8AgmNP48-oQzzPmkhM6u/view')

    def eceEC8453all(self):
        webbrowser.open('https://drive.google.com/file/d/161iijqWvVDjdSqEnOOs47fBPZ-Rp9sZ3/view')

    def eceGE8291all(self):
        webbrowser.open('https://drive.google.com/file/d/1beIuB5wdSuIr0hYMnW8BZMlNcunBR7_G/view')

    def eceEC8491all(self):
        webbrowser.open('https://drive.google.com/file/d/18XlOsM9mYB1J49BFkegw6QSgF1JXbOwB/view?usp=sharing')

    def eceEC8451all(self):
        webbrowser.open('https://drive.google.com/file/d/1OUPn00zW0MUKQOLBPrQUZE6P2VLDYGnh/view?usp=sharing')

    def eceEC8501all(self):
        webbrowser.open('https://drive.google.com/file/d/1DsdB9uw2PVJYOZiSytnSLZl3HTJXEie-/view')

    def eceEC8553all(self):
        webbrowser.open('https://drive.google.com/file/d/13Eqp45rIQGvdUsHxM2VEVVqeBjhYTlQG/view')

    def eceEC8552all(self):
        webbrowser.open('https://drive.google.com/file/d/1ErSoEotuHSdACl4aBxXVLaK129-BIDYR/view')

    def eceEC8551all(self):
        webbrowser.open('https://drive.google.com/file/d/1KZIpZd-QeDTQnf7XuY6yQ0_rWBCYT0rg/view')

    def eceEC8073u1(self):
        webbrowser.open('https://drive.google.com/file/d/15s7YeGA3XvHWUCQ1Uaq2ui9L3nLqMLfH/view')

    def eceEC8073u2(self):
        webbrowser.open('https://drive.google.com/file/d/1w7_6uzFXkUA0ph3UGuiTbnuQefTQqBw7/view')

    def eceEC8073u3(self):
        webbrowser.open('https://drive.google.com/file/d/1uwOsZN9THT_0iMTEcuSAR-NNwf32vyKD/view')

    def eceEC8073u4(self):
        webbrowser.open('https://drive.google.com/file/d/1V-cVSaEEFwIgjlAU-coA2nm-Zp85bRmL/view')

    def eceEC8073u5(self):
        webbrowser.open('')

    def eceOMD551u1(self):
        webbrowser.open('https://drive.google.com/file/d/1siAVmHOoDH1Y2m8W04HE3pRiIe3LmqQh/view')

    def eceOMD551u2(self):
        webbrowser.open('https://drive.google.com/file/d/1Fg5k1nrWCJYBjOpifwvDGAnP9J6JtIqW/view')

    def eceOMD551u3(self):
        webbrowser.open('https://drive.google.com/file/d/1iJm2p_YbEAF_FE7lvDZKynXNkFUSD71Q/view')

    def eceOMD551u4(self):
        webbrowser.open('https://drive.google.com/file/d/11q_gTwq_sB8M17wpoT-AJS3y2grB_mQ3/view')

    def eceOMD551u5(self):
        webbrowser.open('')

    def eceEC8691all(self):
        webbrowser.open('https://drive.google.com/file/d/1F8czWMz818sVmr_FocphmmpWzvkgw7wa/view')

    def eceEC8095all(self):
        webbrowser.open('https://drive.google.com/file/d/1w5WC9zBFO2UCalakuagVTfTV62bBG92a/view')

    def eceEC8652all(self):
        webbrowser.open('https://drive.google.com/file/d/1CDZjfFashe4kRWEPHfXEaRxQCYGEIYvq/view')

    def eceMG8591all(self):
        webbrowser.open('https://drive.google.com/file/d/1oqnoTiUwsJJ_FeBU2nqfRHyGCw23vWyt/view')

    def eceEC8651all(self):
        webbrowser.open('https://drive.google.com/file/d/1N2jVOLzrE25YHDjCTKxHPpK5yAs67-9S/view?usp=sharing')

    def eceEC8002all(self):
        webbrowser.open('https://drive.google.com/file/d/1pat1Rn3QDc5CL6pRYKb7yRQOAEpTnV3Y/view')

    def eceEC8701u1(self):
        webbrowser.open('https://drive.google.com/file/d/1_8hj3fvEAsjwizFLkXmdvGs7U7UNgX6_/view')

    def eceEC8701u2(self):
        webbrowser.open('https://drive.google.com/file/d/1E8ZJRIeCmark8kij_mb0s-swxpWB9UxU/view')

    def eceEC8701u3(self):
        webbrowser.open('https://drive.google.com/file/d/17Ow8k9hvieJer8NiWJl63QHJne4P1rSk/view')

    def eceEC8701u4(self):
        webbrowser.open('https://drive.google.com/file/d/1krUi1gG2M5diawjGZV5-oTQn7ieKGoZK/view')

    def eceEC8701u5(self):
        webbrowser.open('')

    def eceEC8751u1(self):
        webbrowser.open('https://drive.google.com/file/d/1t7_-bQYI73A5emCv8s724tYvG9WU8Utf/view')

    def eceEC8751u2(self):
        webbrowser.open('https://drive.google.com/file/d/14xE-x6innf3oGbT2WIrv4uZjkkZXP3vk/view')

    def eceEC8751u3(self):
        webbrowser.open('https://drive.google.com/file/d/1uca2i8OEdrACZrpTjS1EBr0t-HxrgfT1/view')

    def eceEC8751u4(self):
        webbrowser.open('https://drive.google.com/file/d/1OFU6KbitlgJJdSpXWLv3dRhJAt_oP7XB/view')

    def eceEC8751u5(self):
        webbrowser.open('')

    def eceEC8791u1(self):
        webbrowser.open('https://drive.google.com/file/d/1Ou2cgyG5vZKKsdq8cZPuBdIQCdqSLQLw/view')

    def eceEC8791u2(self):
        webbrowser.open('https://drive.google.com/file/d/1WODma3Iw-xFM4P47IqE0znlWm894mY-l/view')

    def eceEC8791u3(self):
        webbrowser.open('https://drive.google.com/file/d/1s444RZLHjdicLqLvKU2uwYgd2DwlI2jx/view')

    def eceEC8791u4(self):
        webbrowser.open('https://drive.google.com/file/d/1kJu5MYkdhg37Wpbeh0Wo-3rH2bgG1ajP/view')

    def eceEC8791u5(self):
        webbrowser.open('')

    def eceEC8702u1(self):
        webbrowser.open('https://drive.google.com/file/d/1KSiRHJLiqu_Bg8SoCBEbfurl92zk_y3d/view')

    def eceEC8702u2(self):
        webbrowser.open('https://drive.google.com/file/d/15PjR8pjsrRTTxKAc2co1imhwDkf8VGko/view')

    def eceEC8702u3(self):
        webbrowser.open('https://drive.google.com/file/d/1z7d8lyyouRN2xRfzSRK77j6P0hKKSgFS/view')

    def eceEC8702u4(self):
        webbrowser.open('https://drive.google.com/file/d/1I6xB_E8oeqCRUJ_LBHDE9dInhbjtrb0d/view')

    def eceEC8702u5(self):
        webbrowser.open('')

    def eceEC8071u1(self):
        webbrowser.open('https://drive.google.com/file/d/1NVDwMo5Sye4yz86JqsL7BoBv4Qn1xK3Q/view')

    def eceEC8071u2(self):
        webbrowser.open('https://drive.google.com/file/d/1UKiRQmEzOoHXFNQxB2RskVE0QxGTDnTO/view')

    def eceEC8071u3(self):
        webbrowser.open('https://drive.google.com/file/d/1LJC_2ww8j9I-6fzktQKDwh5kCYr4nYEN/view')

    def eceEC8071u4(self):
        webbrowser.open('https://drive.google.com/file/d/13Dd8iWWuXv1C0mVLSs8XGYTfG55WoFIf/view')

    def eceEC8071u5(self):
        webbrowser.open('')

    def eceOIC751u1(self):
        webbrowser.open('https://drive.google.com/file/d/1kHh607FFs0GvWLW7aeha0Rn5x6YrVb--/view')

    def eceOIC751u2(self):
        webbrowser.open('https://drive.google.com/file/d/1sfDe0Q4TBYWZl81QjKGCZnhKrjapeQmw/view')

    def eceOIC751u3(self):
        webbrowser.open('https://drive.google.com/file/d/1guRt03R3UZMP4yglILlEEzshj50UnBv5/view')

    def eceOIC751u4(self):
        webbrowser.open('https://drive.google.com/file/d/1FS803l6nJqwsmgkzcjwp5Lff9IPUBhAB/view')

    def eceOIC751u5(self):
        webbrowser.open('')

    def ecePH8253u1(self):
        webbrowser.open('https://drive.google.com/file/d/1I8oNMD_y3-JEW2mCdnrpLu07gBylZeND/view?usp=sharing')

    def ecePH8253u2(self):
        webbrowser.open('https://drive.google.com/file/d/1rpnADsK9B6N7iwTgP55RhkbKABU0_hPX/view?usp=sharing')

    def ecePH8253u3(self):
        webbrowser.open('https://drive.google.com/file/d/130-pxdrhzYDvfzXar-Hrn4tqhfPk0fsY/view?usp=sharing')

    def ecePH8253u4(self):
        webbrowser.open('https://drive.google.com/file/d/1B0YfqRbzGFPECX1sfXCcJWtFeEVo39Es/view?usp=sharing')

    def ecePH8253u5(self):
        webbrowser.open('https://drive.google.com/file/d/1h8HHhDP-uzFP019oN95wbSuTpnvOIYrY/view?usp=sharing')

    def itcs8351u1(self):
        webbrowser.open('https://drive.google.com/file/d/15Mi_02b3e2aphJ63r0lVBVP7xcdZcKJP/view?usp=sharing')

    def itcs8351u2(self):
        webbrowser.open('https://drive.google.com/file/d/1tJtOPDKI1PpBmyTrjAu7KNGGqoXLlrs0/view')

    def itcs8351u3(self):
        webbrowser.open('https://drive.google.com/file/d/1Wll0gxbexb1ZSghASxJYFzliiqYHIWMw/view?usp=sharing')

    def itcs8351u4(self):
        webbrowser.open('https://drive.google.com/drive/folders/15i641QR_Ej-9MaKDwh-g6jOrAULEuHij')

    def itcs8351u5(self):
        webbrowser.open('https://drive.google.com/file/d/18u5HGWlaYdqIFRj8f2d9USSVKqu96oJV/view?usp=sharing')

    def itcs8392u1(self):
        webbrowser.open('https://drive.google.com/file/d/1YBZJY5JWyMsbqznSStcfZH8L4e6_p1qx/view')

    def itcs8392u2(self):
        webbrowser.open('https://drive.google.com/file/d/19fTKLOsFIbQv5Gvl1oD4E8Uu1XmgBO-6/view')

    def itcs8392u3(self):
        webbrowser.open('https://drive.google.com/file/d/1UXmp6vKz2OwUlSItFGm-vd9JaSYUuS2h/view')

    def itcs8392u4(self):
        webbrowser.open('https://drive.google.com/file/d/16xim22n5QwUBctCZWORPB8hHs10mmaI5/view')

    def itcs8392u5(self):
        webbrowser.open('https://drive.google.com/file/d/1HvIOnGZ600utqO1rUnyheW0_ugJJ9f4e/view?usp=sharing')

    def itcs8391(self):
        webbrowser.open('https://drive.google.com/file/d/14nXxUOaBER0q_cRjRX7xgCygGfadXMKQ/view')

    def itec8394u1(self):
        webbrowser.open('https://drive.google.com/drive/folders/1VJeE8JEk-efsTLCH7UCJJVA7bjFcuPEv')

    def itec8394u2(self):
        webbrowser.open('https://drive.google.com/drive/folders/1KN2iGybUw99YTju5X9fjDeE7Yp5L0N_P')

    def itec8394u3(self):
        webbrowser.open('https://drive.google.com/file/d/1SutRObi8Gq57RYLGRz97eltpCYZnc4EV/view')

    def itec8394u4(self):
        webbrowser.open('https://drive.google.com/file/d/1S6YprpkaiIFweKHelXBixtnsnBpZ-RBg/view')

    def itec8394u5(self):
        webbrowser.open('https://drive.google.com/file/d/1i_IKEpg0jMFyLbmWuKXSRNtCl8FG2fsq/view?usp=sharing')

    def itcs8491u1(self):
        webbrowser.open('https://drive.google.com/file/d/114ZZwIDUQeBHzurx24lkqcCrIQR05mnM/view?usp=sharing')

    def itcs8491u2(self):
        webbrowser.open('https://drive.google.com/file/d/1JFEkpbtpUWyB0WFZ8DaElTCNGzKDiuQR/view?usp=sharing')

    def itcs8491u3(self):
        webbrowser.open('https://drive.google.com/file/d/12ivGF_jJha6ZbViosIl4fTRPRNBeZ07k/view?usp=sharing')

    def itcs8491u4(self):
        webbrowser.open('https://drive.google.com/file/d/1fYMesQd23CP108h2KCepH-Tu69sqRp9g/view?usp=sharing')

    def itcs8491u5(self):
        webbrowser.open('https://drive.google.com/file/d/1qn4YVm3E9mA6hHPSGSrA7AaEBcLGQuRS/view?usp=sharing')

    def itma8391(self):
        webbrowser.open('https://drive.google.com/file/d/0B3b1HiYMjnXlcVRnUGtUV1VsRnFtSWh5d2xKVWlUdzN4QnRJ/view')

    def itcs8492(self):
        webbrowser.open('https://drive.google.com/file/d/1xN6yZn_p4xLX29_4E6ckl0yj3i4STF5a/view')

    def itcs8493(self):
        webbrowser.open('https://drive.google.com/file/d/1Ky9a68OoEUMIHcz2CgxFxA0qn7aziJeK/view')

    def itcs8451(self):
        webbrowser.open('https://drive.google.com/file/d/1Ykj3UvimabSS5pJmHVQkOn2ZVwTNbq6E/view')

    def itcs8591u1(self):
        webbrowser.open('https://drive.google.com/file/d/1sEgoXYj1IHcLgQ1FLvEUCm2NuNFFjrbx/view')

    def itcs8591u2(self):
        webbrowser.open('https://drive.google.com/file/d/1alezxbRlg5193ZTzAnNPOFUtei9Q-1k-/view')

    def itcs8591u3(self):
        webbrowser.open('https://drive.google.com/file/d/1hPoIIxuQQuRRrZsw0sLmlQ6rP5B54HA3/view?usp=sharing')

    def itcs8591u4(self):
        webbrowser.open('https://drive.google.com/file/d/1k6BBZ0uoWI4uG7g3GtoU95vDfN8zSRcJ/view?usp=sharing')

    def itcs8591u5(self):
        webbrowser.open('https://drive.google.com/file/d/11Ua3xIKNT5brFW-jsuwrP-GLkiyvNo2F/view?usp=sharing')

    def itec8691u1(self):
        webbrowser.open('https://drive.google.com/file/d/1YauAP-XQpFB4_OvJigiTMTOHZuOS0yNz/view')

    def itec8691u2(self):
        webbrowser.open('https://drive.google.com/file/d/1a174M4aEyw_adVvndt1rmxo3IItQ4sSI/view')

    def itec8691u3(self):
        webbrowser.open('https://drive.google.com/file/d/14VnpF9cT-enGJ01hfEuUTuaD_5JCjZ58/view')

    def itec8691u4(self):
        webbrowser.open('https://drive.google.com/file/d/1_EZ_X2A7qywxaL3u6ps9mixKqtRkYHfL/view')

    def itec8691u5(self):
        webbrowser.open('https://drive.google.com/file/d/1YgQPHUUvyMAVT1qY8UAE7KGeb3Ut4aPQ/view?usp=sharing')

    def itit8501(self):
        webbrowser.open('https://drive.google.com/file/d/14xtYZZaGhVa_qzOnhqw9syiyXTUUTOi_/view')

    def itma8551u1(self):
        webbrowser.open('https://drive.google.com/file/d/1zvmOIIpYAm-RFq6NHnmdssiwz2MKn5ww/view?usp=sharing')

    def itma8551u2(self):
        webbrowser.open('https://drive.google.com/file/d/1acWpr907g1XhDSF2be1jMlsxC7AXNf1l/view?usp=sharing')

    def itma8551u3(self):
        webbrowser.open('https://drive.google.com/file/d/1LWy_QZGBVKlDh4fpKc455ArbfCZCKgWh/view?usp=sharing')

    def itma8551u4(self):
        webbrowser.open('https://drive.google.com/file/d/1m4pfNoMDbiok7yo7oe3RCNfYK43lVWa2/view?usp=sharing')

    def itma8551u5(self):
        webbrowser.open('https://drive.google.com/file/d/1oqX1jdMwfuV7b3NHy2e_deHDJzkhTmJO/view?usp=sharing')

    def itoce551u1(self):
        webbrowser.open('https://drive.google.com/file/d/1okhfnf0HTaeUuKUKB78xmz8QIMYWGPCP/view')

    def itoce551u12(self):
        webbrowser.open('https://drive.google.com/file/d/1KHPi8oAb_QDSVIbswyNmVsFwzTsBBhla/view')

    def itoce551u3(self):
        webbrowser.open('https://drive.google.com/drive/folders/1rb9aq6t_CqwMqM9OWzbO43zqAQgtXiDx')

    def itoce551u4(self):
        webbrowser.open('https://drive.google.com/drive/folders/16Ic4VfIP_jWzA5QAToxJEYb1AuO4DQ2I')

    def itoce551u5(self):
        webbrowser.open('')

    def itcs8494u1(self):
        webbrowser.open('https://drive.google.com/file/d/1sfvhti03eSsHHlyQWuzMl5EUt4y637nG/view?usp=sharing')

    def itcs8494u2(self):
        webbrowser.open('https://drive.google.com/file/d/15h7q9ImBiGAXdSD66fKv9rem70ERScHr/view?usp=sharing')

    def itcs8494u3(self):
        webbrowser.open('https://drive.google.com/file/d/1H7dG1aiXMkOJ-3SoIC_dGDn9vLLD0q2q/view?usp=sharing')

    def itcs8494u4(self):
        webbrowser.open('https://drive.google.com/file/d/1ev2MZyutzVuhb9DpuEwXaBKZnKwp3Il5/view?usp=sharing')

    def itcs8494u5(self):
        webbrowser.open('https://drive.google.com/file/d/1yD7NGH2aCdSZqOHP2BODeiO_YmFu_Fw5/view?usp=sharing')

    def itcs8592u1(self):
        webbrowser.open('https://drive.google.com/file/d/1eKX7QNWMsAvHVYXUPeVt20slZhoOAOJ2/view?usp=sharing')

    def itcs8592u2(self):
        webbrowser.open('https://drive.google.com/file/d/1QfXXvbv5IiCdX6JWcvlVcWzCvX2pFJqf/view?usp=sharing')

    def itcs8592u3(self):
        webbrowser.open('https://drive.google.com/file/d/1YWyzwy7guKXSxnA8iuDhqH8gpgckIs4c/view?usp=sharing')

    def itcs8592u4(self):
        webbrowser.open('https://drive.google.com/file/d/17ruU_r6kGqufoF14H9LC7JOrNmZ7yB-w/view?usp=sharing')

    def itcs8592u5(self):
        webbrowser.open('https://drive.google.com/file/d/1nppDau4seudwc-eEp4UxzxhHHPQksZi-/view?usp=sharing')

    def itcs8091u1(self):
        webbrowser.open('https://drive.google.com/file/d/1L7HFt2CPg2tfgdo9xwDGTdGLOLTk8JXe/view?usp=sharing')

    def itcs8091u2(self):
        webbrowser.open('https://drive.google.com/file/d/1bUALgPAcPVTcJ7DRcHCCM95CekVVJYGo/view?usp=sharing')

    def itcs8091u3(self):
        webbrowser.open('https://drive.google.com/file/d/1XlhhWF8XrPmp9RtHieVqwAR3vLiQ_LUq/view?usp=sharing')

    def itcs8091u4(self):
        webbrowser.open('https://drive.google.com/file/d/1soTJeVxSr12SJ90OZtqM9IXVj-gYpoB_/view?usp=sharing')

    def itcs8091u5(self):
        webbrowser.open('https://drive.google.com/file/d/1ebA-uDMhgik3lDinENEcl3lwEK_H2_tb/view?usp=sharing')

    def itit8601u1(self):
        webbrowser.open(
            'https://drive.google.com/file/d/0B3b1HiYMjnXld0JBSnkzZkNSNmxCeGt5SXFSZkcxam1lYWo4/view?usp=sharing')

    def itit8601u2(self):
        webbrowser.open('https://drive.google.com/file/d/1uPXDbY6Yi6al6-kcU4RVE2emGtZcz1E4/view?usp=sharing')

    def itit8601u3(self):
        webbrowser.open('https://drive.google.com/file/d/1sHyut61JfTAwxk2spFep8ooToN15At4V/view?usp=sharing')

    def itit8601u4(self):
        webbrowser.open('https://drive.google.com/file/d/1oanA2Q_k0BGuGQJCYwxZP_4GuRfl6yVA/view?usp=sharing')

    def itit8601u5(self):
        webbrowser.open(
            'https://docs.google.com/document/d/1Brlj72LcUjQ2OXzvip6ik9S5MY2ZmRWoxFa0eLVCOcA/edit?usp=sharing')

    def itit8076u1(self):
        webbrowser.open('https://drive.google.com/file/d/10uLlfsMDBjXWHogxYDbhuZMsQoIfrsTH/view?usp=sharing')

    def itit8076u2(self):
        webbrowser.open('https://drive.google.com/file/d/1-w4wUHppRmVFqAGLuKwa3andpapVqWTL/view?usp=sharing')

    def itit8076u3(self):
        webbrowser.open('https://drive.google.com/file/d/18IEz7ZrLr0lUhVZmzJo0EWGBsJSltgOs/view?usp=sharing')

    def itit8076u4(self):
        webbrowser.open('https://drive.google.com/file/d/1yLT4KGIdOMwl8OOgdHNDJjqZZU-P26Un/view?usp=sharing')

    def itit8076u5(self):
        webbrowser.open('https://drive.google.com/file/d/1V7rUAgxudZl4_WE-UG7VUhbw30LkMd6D/view?usp=sharing')

    def itcs8092u1(self):
        webbrowser.open('https://drive.google.com/file/d/1e3fpiSISYBxAcwmKqaOK26T5E-m8uCxJ/view?usp=sharing')

    def itcs8092u2(self):
        webbrowser.open(
            'https://docs.google.com/document/d/1ALeWNdRsfnxndUR6NDU_1sNQEwXtxRmZ9W-PDVwbkvE/edit?usp=sharing')

    def itcs8092u3(self):
        webbrowser.open('https://drive.google.com/file/d/1euFYW8CagsIBFhMEHqLPo_CkT-oK_bbx/view?usp=sharing')

    def itcs8092u4(self):
        webbrowser.open('https://drive.google.com/file/d/1XveiiG30Oz_y1jztzcFhyexA6lBIkTPj/view?usp=sharing')

    def itcs8092u5(self):
        webbrowser.open('https://drive.google.com/file/d/1ytmBioLfVPZXiBZdiidrMdSx8OJW6kMV/view?usp=sharing')

    def itit8602u1(self):
        webbrowser.open('https://drive.google.com/file/d/1skfuZTZlFCf0ddI-05jkUTqxANvaO5sk/view?usp=sharing')

    def itit8602u2(self):
        webbrowser.open('https://drive.google.com/file/d/1isf92VSrD1qQwY4hD9OIdUsPSUoKBrfQ/view?usp=sharing')

    def itit8602u3(self):
        webbrowser.open('https://drive.google.com/file/d/1HzoGOb-LRWMq9lnICz9CY_QVhYIRHTPM/view?usp=sharing')

    def itit8602u4(self):
        webbrowser.open('https://drive.google.com/file/d/18WqY8Br7c79bX858a1K4Q4jJx6xa9BFc/view?usp=sharing')

    def itit8602u5(self):
        webbrowser.open('https://drive.google.com/file/d/1NtdSY5r1Hy2WsLJis_lhG1Tw6ag6o-l2/view?usp=sharing')

    def itcs8791(self):
        webbrowser.open('https://drive.google.com/file/d/1XU-pTCVFcIPWtoBLcJmcyO3FaTe_sDOK/view?usp=sharing')

    def itmg8591u1(self):
        webbrowser.open('https://drive.google.com/file/d/156niWMopuIqeqGGYAQtA03Fxqgc_gH9C/view?usp=sharing')

    def itmg8591u2(self):
        webbrowser.open('https://drive.google.com/file/d/1epCJ6fL2HUppPZsIjLJS26jlRVginELS/view?usp=sharing')

    def itmg8591u3(self):
        webbrowser.open('https://drive.google.com/file/d/1zY6WTZNKUt_jVpmqH2ayngmpvchnHmKr/view?usp=sharing')

    def itmg8591u4(self):
        webbrowser.open('https://drive.google.com/file/d/18TGteeKgZSTy9S4JRdVycEPG53OLaWzm/view?usp=sharing')

    def itmg8591u5(self):
        webbrowser.open('')

    def itcs8792u1(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1VcJo7j8KROLHfXHamlBYB5ZFGIE6ZVmi')

    def itcs8792u2(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1PHIQNcnZjbL7kGCDT-c7cKjBDVxJBnxW')

    def itcs8792u3(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1qWVkoYlagO5_tiqy15v3ef02o0-Gz5lB')

    def itcs8792u4(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1_ncqY9_7NMowFDKKYeQS9AXMrqqivlXy')

    def itcs8792u5(self):
        webbrowser.open('https://drive.google.com/file/d/1ulW-PMKMUJ1n_xRVEOO93rF3tKj5G0rP/view?usp=sharing')

    def itcs8079u1(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/18JJzRsrRwkp6TpbOLKyAhoeEaAYjFxsC')

    def itcs8079u2(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1RBT8O_z62fObJO26YbUPaOcBjnPGhAJH')

    def itcs8079u3(self):
        webbrowser.open('https://drive.google.com/file/d/1hyzWXiua7q78L-7D9slOSQKHZTnOwLzp/view')

    def itcs8079u4(self):
        webbrowser.open('https://drive.google.com/file/d/1peZ0YMWrZmtH5w0IKmWLhri3GqVgaJ0D/view')

    def itcs8079u5(self):
        webbrowser.open('')

    def itge8077u1(self):
        webbrowser.open('https://drive.google.com/file/d/1hQaYsm_BtvNencSowJWafFF9X3vh7q5o/view')

    def itge8077u2(self):
        webbrowser.open('https://drive.google.com/file/d/1nh_3_V_bxtCifNzgdxyRX23jfq3e8GZk/view')

    def itge8077u3(self):
        webbrowser.open('https://drive.google.com/file/d/10yLulA3Ks4QxevU4RPe50fhUnF8aGMnF/view?usp=sharing')

    def itge8077u4(self):
        webbrowser.open('https://drive.google.com/file/d/1bMCsJD2ahc9GCRgytKllXxl_upUYKUc3/view?usp=sharing')

    def itge8077u5(self):
        webbrowser.open('')

    def itome752u1(self):
        webbrowser.open('https://drive.google.com/file/d/1-BA0lsOE-A6JPSZrnyB3KmmDb_xGes0x/view?usp=sharing')

    def itome752u2(self):
        webbrowser.open('https://drive.google.com/file/d/1m8DZCuwsz7OmUrHZgYhOiRRiSwvWRAsp/view?usp=sharing')

    def itome752u3(self):
        webbrowser.open('https://drive.google.com/file/d/1Pm2PA1MLVxLDmVhhD2h6utRQnE8qOUAv/view?usp=sharing')

    def itome752u4(self):
        webbrowser.open('https://drive.google.com/file/d/1ha4EX9cb09uVz2YgvnEr5BWQvrpUrLcI/view?usp=sharing')

    def itome752u5(self):
        webbrowser.open('')

    def cseMA8351u1(self):
        webbrowser.open('https://drive.google.com/file/d/12rj-qJfdsNEFre9QkqDhCmThBXh0LlYb/view?usp=sharing')

    def cseMA8351u2(self):
        webbrowser.open('https://drive.google.com/file/d/1EmeRQtguQdaSpaPaygLiDhPFpnId1pnm/view?usp=sharing')

    def cseMA8351u3(self):
        webbrowser.open('https://drive.google.com/file/d/1ODsLrA-0rAOALs6tRRBcjSlgtPjEtmNO/view?usp=sharing')

    def cseMA8351u4(self):
        webbrowser.open('https://drive.google.com/file/d/1coj_cX67frpPEpwHqwz3e-stPjN6RRFo/view?usp=sharing')

    def cseMA8351u5(self):
        webbrowser.open('https://drive.google.com/file/d/12rxA8mnB0_5E8VRui1_c68G7MaLh2cIU/view?usp=sharing')

    def cseCS8351u1(self):
        webbrowser.open('https://drive.google.com/file/d/1w2N7fgJuN0dV0WqrksG_4EGS4XGL2Fns/view?usp=sharing')

    def cseCS8351u2(self):
        webbrowser.open('https://drive.google.com/file/d/1unUaT7eNn9j-0eMTE2Ilwv2kZQweXqnN/view?usp=sharing')

    def cseCS8351u3(self):
        webbrowser.open('https://drive.google.com/file/d/1rfOaD65d6XEDCRlquCOre0G04tgnEFbN/view?usp=sharing')

    def cseCS8351u4(self):
        webbrowser.open('https://drive.google.com/file/d/1_vQHksT9z3bnbJT56bU0186hH0YwywwN/view?usp=sharing')

    def cseCS8351u5(self):
        webbrowser.open('https://drive.google.com/file/d/1QJY0Bf69KCcv0htn6-CLca79okjCOLUk/view?usp=sharing')

    def cseCS8391u1(self):
        webbrowser.open('https://drive.google.com/file/d/1YK6lUc8yTv_7GI4qbwH_n3lk_Qj5yTN9/view?usp=sharing')

    def cseCS8391u2(self):
        webbrowser.open('https://drive.google.com/file/d/13niEDUxxpVlYm9gMrQWWwpPqgsJ9hFeJ/view?usp=sharing')

    def cseCS8391u3(self):
        webbrowser.open('https://drive.google.com/file/d/1KtTOBiHVI3vj4yLB8acGl_s8QmG4kzkR/view?usp=sharing')

    def cseCS8391u4(self):
        webbrowser.open('https://drive.google.com/file/d/1FbrIEjhf3aWmNjgJ-o17CJx0bctW5qGW/view?usp=sharing')

    def cseCS8391u5(self):
        webbrowser.open('https://drive.google.com/file/d/1DPCWD1Krf0l4qbZW_4Hi6M26YuGm5ezO/view?usp=sharing')

    def cseCS8392u1(self):
        webbrowser.open('https://drive.google.com/file/d/1YEasrd74TnxqLrq1i-692FXgfEHAPzK-/view?usp=sharing')

    def cseCS8392u2(self):
        webbrowser.open('https://drive.google.com/file/d/1gPGglHShDbNYp4rC1ulgG5j8b7Ed1k3P/view?usp=sharing')

    def cseCS8392u3(self):
        webbrowser.open('https://drive.google.com/file/d/1lunlUlDt961H0r08yW45BdgUR1aipw77/view?usp=sharing')

    def cseCS8392u4(self):
        webbrowser.open('https://drive.google.com/file/d/1tn3Ly_T6QJtUUUuOUZQGBuCxD6Z_71jt/view?usp=sharing')

    def cseCS8392u5(self):
        webbrowser.open('https://drive.google.com/file/d/1bL5cW19Ni2YmqvRFe79rSL9AKVFLlFL1/view?usp=sharing')

    def cseEC8395u1(self):
        webbrowser.open('https://drive.google.com/file/d/1C5V_kp9qSFqB1DZAh7EXbsql1tj4j8Lh/view?usp=sharing')

    def cseEC8395u2(self):
        webbrowser.open('https://drive.google.com/file/d/1e9n-d5CZvn9E2JfXpSLsYaxArPxL6jSn/view?usp=sharing')

    def cseEC8395u3(self):
        webbrowser.open('https://drive.google.com/file/d/1tDoMky3XpjuRsMUfPaLMlliGxH4jXMyE/view?usp=sharing')

    def cseEC8395u4(self):
        webbrowser.open('https://drive.google.com/file/d/1SjS9S5sON5SXppdhdGK9emkdh1FfVYyn/view?usp=sharing')

    def cseEC8395u5(self):
        webbrowser.open('https://drive.google.com/file/d/1EYT-GRz7D28hvXZYEIxE8Z5FPftnXVRD/view?usp=sharing')

    def cseMA8402u1(self):
        webbrowser.open('https://drive.google.com/file/d/1Jj3xNkCOH3sLhvGDne-vZM86XN8GWfvg/view?usp=sharing')

    def cseMA8402u2(self):
        webbrowser.open('https://drive.google.com/file/d/1WgaNxYnHlpRSr09RtJ5j5pdSlABLgC0L/view?usp=sharing')

    def cseMA8402u3(self):
        webbrowser.open('https://drive.google.com/file/d/1gLKdXFP7QXd3sYZIV5TJb3zGd_2TypVY/view?usp=sharing')

    def cseMA8402u4(self):
        webbrowser.open('https://drive.google.com/file/d/1OtMmvnZkXsytrkI8bgNMIWaUgHg3X2e7/view?usp=sharing')

    def cseMA8402u5(self):
        webbrowser.open('https://drive.google.com/file/d/1xVkbRRQFOc0SJ5j1CxK3V-ygaa8E0q_1/view?usp=sharing')

    def cseCS8491u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1UqKiXiWngC5O8eix-tU97W8qoR0_DsBn/view?usp=sharing')

    def cseCS8492u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1WRWMX5Q1IcRmnjD0azZ6q6dUnv5SYN1u/view?usp=sharing')

    def cseCS8451u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1Ykj3UvimabSS5pJmHVQkOn2ZVwTNbq6E/view?usp=sharing')

    def cseCS8493u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1Ky9a68OoEUMIHcz2CgxFxA0qn7aziJeK/view?usp=sharing')

    def cseCS8494u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1Usb6AMoqyUS7DSWvm5dMLsQnAWKg6Pio/view?usp=sharing')

    def cseMA8551u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1GXFidhKq7LBNr7DcTy4BKugjDuuXgzWq/view?usp=sharing')

    def cseCS8591u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1fORxENospDogF8DCgs6UVY44A73SDIsL/view')

    def cseEC8691u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1vBs_5vH5xUhvc4jXDThnC5eOhg-XvUsw/view')

    def cseCS6503u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1YHiyA-1MxbNUssMnE9N-u4Uej3i1JnOD/view?usp=sharing')

    def cseCS8592u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/19Gc36qBshJIXtL077QkBy2BeiD56M9V7/view')

    def cseOCE552u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/0B34Kafesp7UnczhreTR3UFJRc244NHpQRHM1ZXpZQktxYkhV/view')

    def cseCS8651u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1pvF4QZcUZEcv3ajL51sjPgWGANoynzS9/view')

    def cseCS8691u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/16_LmCKVxqXLfZQulDdp0plDecksOWOgC/view?usp=sharing')

    def cseCS8601u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1NtJOB_M6p0vl-SPGumJgt2l7zpQeIkl4/view')

    def cseCS8602u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1ROEve4jIYE0XHOEYBXxHbb3onog2n6it/view?usp=sharing')

    def cseCS8603u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1wiV1ZvvSlvXrtX_xazkZbN9K32ZzVWWs/view?usp=sharing')

    def cseIT8076u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1j4_9T9nuUseBT1bkO80R8JOA2x0o43yw/view')

    def cseMG8591u1(self):
        webbrowser.open('https://drive.google.com/file/d/1c07m6h_vr0V-nafIhC1e589PQZ1IDyFw/view?usp=sharing')

    def cseMG8591u2(self):
        webbrowser.open('https://drive.google.com/file/d/1Unz1neyO8BuiKq6-Y_U2edxvrrg11mGR/view?usp=sharing')

    def cseMG8591u3(self):
        webbrowser.open('https://drive.google.com/file/d/1PXYlwJmWoaQBVzCCQzcT495YZBknAa8Y/view?usp=sharing')

    def cseMG8591u4(self):
        webbrowser.open('https://drive.google.com/file/d/1yrGNx8v8foA8jMKyHXikkWVK2db4hHfv/view?usp=sharing')

    def cseMG8591u5(self):
        webbrowser.open('https://drive.google.com/file/d/1_iTKoeJxJj6pq7SRMzO5wOCMz978pQnz/view?usp=sharing')

    def eceEC8252u1(self):
        webbrowser.open('https://drive.google.com/file/d/1imJ0XtvMmhciJBES88VyQJUhSSL6ODNo/view?usp=sharing')

    def eceEC8252u2(self):
        webbrowser.open('https://drive.google.com/file/d/1_js-Lz5EKDLGC7rYzb5KbvUk8SPuz526/view?usp=sharing')

    def eceEC8252u3(self):
        webbrowser.open('https://drive.google.com/file/d/1J4c2Mj1MojquwsdrMzJrLQxII77MYRXa/view?usp=sharing')

    def eceEC8252u4(self):
        webbrowser.open('https://drive.google.com/file/d/10ttvZgJ5_QM6iKUyEb5vOROKfJ2dFJin/view?usp=sharing')

    def eceEC8252u5(self):
        webbrowser.open('https://drive.google.com/file/d/12aPSzQPiGq5imjLKeHvIbIFH6QBAVKbe/view?usp=sharing')

    def eceEC8251all(self):
        webbrowser.open('https://drive.google.com/file/d/113LfDrIVEEaRyJWYuLUO-uPHmr7g1wVX/view?usp=sharing')

    def eceBE8254u1(self):
        webbrowser.open('https://drive.google.com/file/d/1xyTXc5YCWMvPkTg5ZHwvkxfFiQsiCV4L/view?usp=sharing')

    def eceBE8254u2(self):
        webbrowser.open('https://drive.google.com/file/d/1x0KAcm2X-no9EjR5Bvs2EqNvi8Ws7sUY/view?usp=sharing')

    def eceBE8254u3(self):
        webbrowser.open('https://drive.google.com/file/d/1DGCTxCkZTbOW5UOMqHho3DeaqhDyL3E0/view?usp=sharing')

    def eceBE8254u4(self):
        webbrowser.open('https://drive.google.com/file/d/1imKSP2__M3U4lmYKzF52QhDjGHzQeiE9/view?usp=sharing')

    def eceBE8254u5(self):
        webbrowser.open('https://drive.google.com/file/d/1wFxwHSL2cn-y_TxQLSVJiDygp0Y-d5KZ/view?usp=sharing')

    def mME8391u1(self):
        webbrowser.open('https://drive.google.com/file/d/1rkIxPuFJs1cRQAv_bxV5QzcU_Hnl9lJA/view')

    def mME8391u2(self):
        webbrowser.open('https://drive.google.com/file/d/1U9Z4aOFbxTSI0y3g_doLOvkotTehg0N0/view')

    def mME8391u3(self):
        webbrowser.open('https://drive.google.com/file/d/1aVc6G39JB4yezCbID0pMW3kO1bCg4ggq/view')

    def mME8391u4(self):
        webbrowser.open('https://drive.google.com/file/d/1G4F3G976CemNODlBNznpoOsRYx4-e17M/view')

    def mME8391u5(self):
        webbrowser.open('https://drive.google.com/file/d/1MUZoYCEHIdhx7Yg_Kg9ap2SaV8SEGO_O/view?usp=sharing')

    def mEE8353u1(self):
        webbrowser.open('https://drive.google.com/file/d/18qtXmU2p8ZNJ73FmSVOiiSBPubHe_HxK/view')

    def mEE8353u2(self):
        webbrowser.open('https://drive.google.com/file/d/1CQ4IpXeHk14_Uskqz9L6VK1I3a_AI4oD/view')

    def mEE8353u3(self):
        webbrowser.open('https://drive.google.com/file/d/1PNfVJ0X4-z2ROOLEMdDWsAIFZcKxkEJK/view')

    def mEE8353u4(self):
        webbrowser.open('https://drive.google.com/file/d/1JDdQyK-AyYtCIOucLl8DSCUdSFtF5ZZK/view')

    def mEE8353u5(self):
        webbrowser.open('https://drive.google.com/file/d/1DyAkh0lWjDrE_YzyA-JoF8ffMF1vaNl6/view?usp=sharing')

    def mCE8394u1(self):
        webbrowser.open('https://drive.google.com/file/d/1Ag3lDx3qPoLZZmmcXpTDGL1iuiBtFeFB/view')

    def mCE8394u2(self):
        webbrowser.open('https://drive.google.com/file/d/1wwCMElwOoPcMkVtCEihgxO3EviPOjILi/view')

    def mCE8394u3(self):
        webbrowser.open('https://drive.google.com/file/d/1MqKVNG7AAJIOGBxNN8oLsmO8xifuyveE/view')

    def mCE8394u4(self):
        webbrowser.open('https://drive.google.com/file/d/10opkUpmLAzhS3UDjJWMTem60zrfxCN_D/view')

    def mCE8394u5(self):
        webbrowser.open('https://drive.google.com/file/d/1eQu-jeVFTWQMpquxFM2kr9lc-XLZ55Bd/view?usp=sharing')

    def mME8351u1(self):
        webbrowser.open('https://drive.google.com/file/d/1BOl3jrMJ2qWLBNxsw0iuOlXWsadVjIuo/view')

    def mME8351u2(self):
        webbrowser.open('https://drive.google.com/file/d/1xXqsMcjC2Nwn5cs-XNzsHZv0SglH40MV/view')

    def mME8351u3(self):
        webbrowser.open('https://drive.google.com/file/d/1MBvvcf55e1_BHFfOWTs2Vyqp0Kvtczlg/view')

    def mME8351u4(self):
        webbrowser.open('https://drive.google.com/file/d/1NMwA0g1wNMtt5PdIY7WQQvq6uD_TgWqN/view')

    def mME8351u5(self):
        webbrowser.open('https://drive.google.com/file/d/1g-mKrX6sACaDtJWYW0-bRKJUg_ULZ8Bk/view?usp=sharing')

    def mMA8353u1(self):
        webbrowser.open('https://drive.google.com/file/d/1nnnc1xhgw0STIPa4p0hkMn69HUYu843Y/view')

    def mMA8353u2(self):
        webbrowser.open('https://drive.google.com/file/d/1teN-HOmiEe_39zZ_C5bd7VZ4xrhAqXe8/view')

    def mMA8353u3(self):
        webbrowser.open('https://drive.google.com/file/d/1fakmFS3M363iTPvD-rO0MRAPftGAmAgL/view')

    def mMA8353u4(self):
        webbrowser.open('https://drive.google.com/file/d/13Jr3eH5jqomdxAv4_V0qQ2kXwyc1m9ax/view')

    def mMA8353u5(self):
        webbrowser.open('https://drive.google.com/file/d/1L4aG5R0nJd2eWo23ugH02Ai4_IcncsRN/view?usp=sharing')

    def shma8151(self):
        webbrowser.open("https://drive.google.com/file/d/1BMGAcFMjlRix-YjuZb8dQi7X5tVKT2P6/view?usp=sharing")

    def shcy8151(self):
        webbrowser.open("https://drive.google.com/file/d/1Tsh2186tHkVklezVrveVj-uTy406gc-_/view?usp=sharing")

    def shge8151(self):
        webbrowser.open("https://drive.google.com/file/d/1JPUdJvJX_ah_npKqFi4029TaU3kK1Lsq/view?usp=sharing")

    def shph8151(self):
        webbrowser.open("https://drive.google.com/file/d/1um-IhJinxiVMD61bXC3q8mDZ4xQYjZya/view?usp=sharing")

    def shhs8151(self):
        webbrowser.open("https://drive.google.com/file/d/1LGd6zI1wBvchfJ7eHs-wVW5HiOEPSNRc/view?usp=sharing")

    def shge8152(self):
        webbrowser.open("https://drive.google.com/file/d/1k-pUuIGN-iJYbppZLhTZhKtfiey49YJR/view?usp=sharing")

    def mME8491u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1oPp-EiSF6M7p2HaGnK0WrmqOB7Y5n6gw/view?usp=sharing')

    def mME8492u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/17HRCy578T39KfSMZvTPqxU5KSLOiIJqw/view?usp=sharing')

    def mMA8452u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1yAxqYFzGPKQhKcq8tgJaxpOiA4yvD_m-/view?usp=sharing')

    def mME8493u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/1xTzHLCjs8Z5t542ROmn5NFPdht_AZWBc/view?usp=sharing')

    def mME8451u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/10Cecdazd2ZUveIxPCsMETTmjeB8U5g_A/view?usp=sharing')

    def mCE8395u1to5(self):
        webbrowser.open('https://drive.google.com/file/d/12eTgWH7YfBx14cimNCOK5IkOeSXgb5Up/view?usp=sharing')

    def mme8691(self):
        webbrowser.open('https://drive.google.com/file/d/1xhrLAKdG80LcVGmD4ulsr1QMa7MxP-Oh/view?usp=sharing')

    def mme8694(self):
        webbrowser.open('https://drive.google.com/file/d/1nYWqwLyVvtGCi5JBa50ofI29eGnYKl7D/view?usp=sharing')

    def mme8091(self):
        webbrowser.open('https://drive.google.com/file/d/1T0wUWg2y5_oomwZNs0Q4QqLcCFRzyCUy/view?usp=sharing')

    def mme8692(self):
        webbrowser.open("https://drive.google.com/file/d/1V-YlVGg7LaGK-oEjbEu9UPI6mJvqdRwu/view?usp=sharing")

    def mme8651(self):
        webbrowser.open("https://drive.google.com/file/d/1V5PDDB_5L0gPCO67JpbJwge8MM_dctor/view?usp=sharing")

    def mme8693(self):
        webbrowser.open('https://drive.google.com/file/d/1WmjbUlGAkHztJCYP3ZzELgSFRVdRACxb/view?usp=sharing')

    def mme8501u1(self):
        webbrowser.open('https://drive.google.com/file/d/13V9PvdhlD7RNxAsIT4EGpcit5uwR_Dt0/view?usp=sharing')

    def mme8501u2(self):
        webbrowser.open('https://drive.google.com/file/d/1W_xAv6rqKxIHklv3-oJTHj6egKMOP3se/view?usp=sharing')

    def mme8501u3(self):
        webbrowser.open('https://drive.google.com/file/d/1RnvMX4dAvqfTuNIupLC4LBBVV204_vmq/view?usp=sharing')

    def mme8501u4(self):
        webbrowser.open('https://drive.google.com/file/d/1TKLuVw-LZcxn_bd4CzuVkHehzfY4nLEo/view?usp=sharing')

    def mme8501u5(self):
        webbrowser.open('https://drive.google.com/file/d/1Par5brlPtASLpnNGwI5e28HR1YSTDaCx/view?usp=sharing')

    def mme8593u1(self):
        webbrowser.open('https://drive.google.com/file/d/1wvqPNHkAkWEv27yNrMu6T7rsC5Zn7dFK/view?usp=sharing')

    def mme8593u2(self):
        webbrowser.open('https://drive.google.com/file/d/166D9KOuAHmU7Q1FUy5uI-hqq4JMxRank/view?usp=sharing')

    def mme8593u3(self):
        webbrowser.open('https://drive.google.com/file/d/11eUEFPrsIZ4hUtUcf6P-9Qy2x0vQgjYa/view?usp=sharing')

    def mme8593u4(self):
        webbrowser.open('https://drive.google.com/file/d/1ELdTTZSMjePWar-P51xwNKz_upVztrAU/view?usp=sharing')

    def mme8593u5(self):
        webbrowser.open('https://drive.google.com/file/d/1yV_H-qBt_OO5EycWMBjk1nxxGZSaWeVK/view?usp=sharing')

    def mme8594u1(self):
        webbrowser.open('https://drive.google.com/file/d/1Hhvl05hj55fNjKCa3yDrpZGZJkf0AxDb/view')

    def mme8594u2(self):
        webbrowser.open('https://drive.google.com/file/d/1L836yKepMXvQgEV8txiyopaNATpWeQub/view')

    def mme8594u3(self):
        webbrowser.open('https://drive.google.com/file/d/11jmQXHuPBkJkZrd22rs0xT8-Jkq9pWPt/view')

    def mme8594u4(self):
        webbrowser.open('https://drive.google.com/file/d/1rIPfBBWkZ1fuQKwWFKkmYE8x11KFPUIk/view')

    def mme8594u5(self):
        webbrowser.open('https://drive.google.com/file/d/1llihvCll6NULUTKkvHswkuALbTpMlLOQ/view?usp=sharing')

    def mme8595u1(self):
        webbrowser.open('https://drive.google.com/file/d/15azSt1gUNH0gVtnjw_WRaYM4R8PMvWZc/view?usp=sharing')

    def mme8595u2(self):
        webbrowser.open('https://drive.google.com/file/d/1RQC8LFaZ-Om38ronHP1XHnt0dFo_tSYK/view?usp=sharing')

    def mme8595u3(self):
        webbrowser.open('https://drive.google.com/file/d/1bz8sRotWu3NQWIAWcHlowQAJeVPBgbxg/view?usp=sharing')

    def mme8595u4(self):
        webbrowser.open('https://drive.google.com/file/d/1M2gV-ys33njepZkbTB1yDxpyLRNlUOwg/view?usp=sharing')

    def mme8595u5(self):
        webbrowser.open('https://drive.google.com/file/d/1Y2xDaM0TOfr0U92wvmtUOs1nAbxLhsGZ/view?usp=sharing')

    def momf551u1(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1CP7fDEnv52LV9hehfN5Fy16jfkEueJcI')

    def momf551u2(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1iYz5sxmNUCIYwk7oFVhN3gMb5-KiAIvc')

    def momf551u3(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1hwzz1riOb1ZkjmsYI4ASc3O2Ko1C44hn')

    def momf551u4(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1W24dwBIEdjDu5ahwQGmsNav1CwVcNCiv')

    def momf551u5(self):
        webbrowser.open('')

    def moml751u1(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1ugXf5ygygnPhLK26uD0K6Nkp6_36T_Wl')

    def moml751u2(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1Zv_DhyfD0Z6vEkpOtkUn8RBZEfCQbZ8F')

    def moml751u3(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1Gc4DCeYSCkwA70kHSoD4vPjsWBjxnqb1')

    def moml751u4(self):
        webbrowser.open('https://drive.google.com/drive/u/1/folders/1YxUkANBqn3CiQ0b3axCY10M0BEowGdsb')

    def moml751u5(self):
        webbrowser.open('')

    def mme8097u1(self):
        webbrowser.open('https://drive.google.com/file/d/1HP3V5_Vwhf0tkGVBZF5QjcZjM25VlqLN/view?usp=sharing')

    def mme8097u2(self):
        webbrowser.open('https://drive.google.com/file/d/1DRWQNQBgf2RzLSqVcTSvsEPig_jtqmxK/view?usp=sharing')

    def mme8097u3(self):
        webbrowser.open('https://drive.google.com/file/u/1/d/1Xltvlkzz7BUg19UY67XaiPyzpHVwqilZ/view?usp=sharing')

    def mme8097u4(self):
        webbrowser.open('https://drive.google.com/file/u/1/d/1sN-QxQ4-Yta-SiDlyjfK2f3s5zjqj-ft/view?usp=sharing')

    def mme8097u5(self):
        webbrowser.open('')

    def shhs8251(self):
        webbrowser.open("https://drive.google.com/file/d/1kJgnSa0cZAHeBUfCqNreNsnv7teDGWK2/view?usp=sharing")

    def shma8251(self):
        webbrowser.open("https://drive.google.com/file/d/1uV0oK5MPo1YCIR-bU55p_tc1op3MOk8s/view?usp=sharing")

    def shph8252u1(self):
        webbrowser.open("https://drive.google.com/file/d/1Pvex3B70RaNN6MOmCxOO1Zo6EpyUHhJz/view?usp=sharing")

    def shph8252u2(self):
        webbrowser.open("https://drive.google.com/file/d/1pAWuhIUZavsUdEtn9Adr76X9ctCHA7EH/view?usp=sharing")

    def shph8252u3(self):
        webbrowser.open("https://drive.google.com/file/d/1Lle4LmOWvn9J5G5Qmg0dQxwVFvmb5b8i/view?usp=sharing")

    def shph8252u4(self):
        webbrowser.open("https://drive.google.com/file/d/1gs78vO2siLKb0yCC9VkW9FtiLylKexmz/view?usp=sharing")

    def shph8252u5(self):
        webbrowser.open("https://drive.google.com/file/d/15wzfjCsfSfNx6QdbUMZlZBGLS-qy0k7M/view?usp=sharing")

    def shge8291(self):
        webbrowser.open("https://drive.google.com/file/d/1Y-4txcASfWJ9dG9tExYF05oK6D0wGT8t/view?usp=sharing")

    def shcs8251(self):
        webbrowser.open("https://drive.google.com/file/d/1pkAj4AxGEmtuq5MS_VAOgWX6_ti5rQfw/view?usp=sharing")

    def shbe8255u1(self):
        webbrowser.open("https://drive.google.com/file/d/1WYq4i4kPm7nKMA7tFIlWW3lWrmekKrf4/view?usp=sharing")

    def shbe8255u2(self):
        webbrowser.open("https://drive.google.com/file/d/1JP8uPAHlsgy7V_u1-8CyJPrmjPr6xs6f/view?usp=sharing")

    def shbe8255u3(self):
        webbrowser.open("https://drive.google.com/file/d/1ByLuNtyl68ULqQZJSKUwg7XotIKqWdA6/view?usp=sharing")

    def shbe8255u4(self):
        webbrowser.open("https://drive.google.com/file/d/1gwrQLh6IJYrMlK0d3FReSmUauN1RDqVM/view?usp=sharing")

    def shbe8255u5(self):
        webbrowser.open("https://drive.google.com/file/d/1Ds8ExtcGjUBZ-PGzxqahMHYAEfwfcOow/view?usp=sharing")


RMKEGURU().run()
