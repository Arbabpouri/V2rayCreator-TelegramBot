from jdatetime import datetime as PersianTime
from config.config import Config
from modules.enums import ResponseCode
from modules.api.APIS import APIS




class Strings:

    BUY_CONFIG = "💳 به بخش خرید کانفیگ خوش آمدید , لطفا سرور مد نظر رو انتخاب کنید"
    SHOP = "💰 به بخش فروشگاه خوش آمدید, از منوی زیر انتخاب کنید"
    MY_SUBSCRIPTION = ""
    SUPPORT = "💡 جهت پیام ارتباط با ادمین لطفا روی دکمه زیرین کلیک کنید 🌀"
    GET_CUSTOM_CHARGE = "📍 مبلغ مد نظر خود را به **تومان** وارد کنید (با اعداد لاتین) 💳"
    NOT_NUMBER = "❌مقدار ارسالی شما  به صورت عددی نیست , لطفا **به صورت عدد لاتین** ارسال کنید. ❌"
    NOT_PICTURE = "🚫 مورد ارسال شده اشتباه است, لطفا فقط عکس ارسال کنید"
    WAITING = "⏳ لطفا منتظر بمانید "
    SELECT_CHARGE = "⁉ به چه روشی میخواهید حساب خود را شارژ کنید؟"
    SEND_PICTURE = "⚠ لطفا تصویر فیش واریزی"
    BACKED_TO_HOME = "👋 به منوی اصلی بازگشتید"
    SERVICES = "سروریس های شما به شرح زیر است"
    NOT_SERVICE = "شما سرویسی ندارید"
    NOT_SERVER = "server ni"
    SELECT_SERVER = "kodum"
    ERROR = "error"
    CONFIG_DOES_NOT_EXIST = "nist"
    CANCELED = "cancel shod"
    WAIT_CONFIRMATION = "Waiting for confirmation"
    DOCUMENTS_RECEIVED = "✅ مدارک ارسالی شما برای ادمین ناظر ارسال شد, تا تایید صبور باشید"
    ACC_ERROR = "Error"
    DOCUMENTS_NOT_RECEIVED = (
        "💢در ارسال مدارک شما به تیم پشتیبانی مشکلی رخ داد, لطفا مدارک خود رو برای ایدی زیر ارسال کنید تا تایید شود."
        "\n\n"
        "⭕️ پ.ن : پوزش مارا بپذیرید"
    )

    RESPONSE_API_STRINGS = {
        str(ResponseCode.USER_TYPE_ERROR): ("a"),
        str(ResponseCode.CONFIG_DOES_NOT_EXIST): ("b"),
        str(ResponseCode.SERVER_DOES_NOT_EXIST): ("c"),
        str(ResponseCode.LOW_BALANCE): ("d"),
        str(ResponseCode.SERVER_IS_FULL): ("e"),
        str(ResponseCode.ADD_NEW_CONFIG_PANEL_FAILUR): ("f"),
        str(ResponseCode.CONFIG_TYPE_NOT_FOUND): ("g"),
        str(ResponseCode.CONFIG_IS_ALREADY_ENABLE): ("ss"),
        str(ResponseCode.SERVER_DOES_NOT_EXIST): ("ssss"),
    }

    @staticmethod
    def send_evidence(price: int) -> str:
        """
        
        """
        return (
            f"➕ لطفا به شماره کارت زیر مبلغ {int(price):,} تومان واریز کنید و عکس فیش واریزی را ارسال کنید"
            "\n\n"
            f"شماره کارت : \n {Config.CARD_NUMBER}"
            "\n"
            f"بنام : {Config.CARD_HOLDER}"
        )

    @staticmethod
    def start_menu(name: str, user_id: int) -> str:
        return f"👋 سلام [{name}](tg://user?id={user_id}) عزیز به ربات خوش اومدی , از منوی زیر انتخاب کن ❤️"

    @staticmethod
    def get_user_id(user_id: int) -> str:
        return "🔹 آیدی عددی شما :  <code>{}</code>".format(user_id)

    @staticmethod
    def low_price(price: int) -> str:
        return f"❌مقدار وارد شده کم است , حداقل مقدار شارژ برای شما {int(price):,} تومان است ❌"

    @staticmethod
    def referral(user_id: int) -> str:
        return (
            "💎 لینک زیر را با دوستان خود به اشتراک بزارید و به ازای هر خرید ۱۰٪ از مبلغ خرید به کیف پول شما اضافه "
            "خواهد شد تا بتوانید محصولات داخل فروشگاه را بدون پرداخت هزینه دریافت کنید 💸"
            "\n\n"
            f"https://t.me/{Config.BOT_USERNAME}?start={user_id}"
        )

    @staticmethod
    def created_payment_link(price: int) -> str:
        return f"🏧 لینک پرداخت شما به مبلغ {int(price):,} تومان اماده شد , روی دکمه زیر کلیک کرده تا به صفحه هدایت شوید ♻️"

    @staticmethod
    def account(user_id: int) -> str:
        user_api = APIS.user_api(user_id)
        result = user_api.get_user_information

        if (not result): return "به مشکل خورد مجدد امتحان کنید"

        return (
            f"balance : {result.balance}"
            "\n"
            f"referrals: {result.referrals.__len__()}"
            "\n"
            f"user_id: {user_id}"
        ).format(user_id)

    @staticmethod
    def acc_reject(name: str, user_name: str,  user_id: int, amount: int) -> str:

        text = (
            "#درخواست_افزایش_موجودی 💳"
            "\n\n"
            f"👤 - Name : [{name}](tg://user?id={user_id})"
            "\n"
            f"👾 - User Name : {user_name}"
            "\n"
            f"🔢 - User ID : {user_id}"
            "\n"
            f"💰 - Amount : {int(amount):,}"
            "\n"
            "⏰ - Date Time : {}"
            "\n"
            f"🔑 - Status : {Strings.WAIT_CONFIRMATION}"
            "\n\n\n"
            f"@{Config.BOT_USERNAME}"
        )
        return text
    
    @staticmethod
    def end_config(user_id: int, v2ray_link: str) -> str:

        text = (
            f"کاربر با ایدی عددی `{user_id}`"
            "\n"
            "تاریخ انتقضا کانفیگ شما با لینک : "
            "\n"
            f"`{v2ray_link}`"
            "\n"
            "در حال اتمام است, اگر مایلید تمدید کنید"
            "\n\n\n"
            f"🆔 @{Config.BOT_USERNAME}"
        )

        return text

    @staticmethod
    def admin_accepted(user_id: int, admin_user_id: int, amount: int) -> str:

        text = (
            "salam"
            "acc"
            "shod"
        )

        return text

    @staticmethod
    def admin_rejected(user_id: int, admin_user_id: int, amount: int) -> str:
        text = (
            "a"
            ""
            ""
        )

        return text

    @staticmethod
    def user_accepted(amount: int) -> str:
        text = (
            "s"
            ""
            ""
        )

        return text

    @staticmethod
    def user_rejected(amount: int) -> str:
        text = (
            "c"
            ""
            ""
        )

        return text
