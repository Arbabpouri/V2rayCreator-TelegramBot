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
    WAITING = "⏳ لطفا منتظر بمانید "
    SELECT_CHARGE = "⁉ به چه روشی میخواهید حساب خود را شارژ کنید؟"
    SEND_PICTURE = "⚠ لطفا تصویر فیش واریزی"
    DOCUMENTS_RECEIVED = "✅ مدارک ارسالی شما برای ادمین ناظر ارسال شد, تا تایید صبور باشید"
    BACKED_TO_HOME = "👋 به منوی اصلی بازگشتید"
    SERVICES = "سروریس های شما به شرح زیر است"
    NOT_SERVICE = "شما سرویسی ندارید"
    NOT_SERVER = ""
    SELECT_SERVER = ""
    ERROR = ""
    CONFIG_DOES_NOT_EXIST = ""

    RESPONSE_API_STRINGS = {
        str(ResponseCode.USER_TYPE_ERROR): (""),
        str(ResponseCode.CONFIG_DOES_NOT_EXIST): (""),
        str(ResponseCode.SERVER_DOES_NOT_EXIST): (""),
        str(ResponseCode.LOW_BALANCE): (""),
        str(ResponseCode.SERVER_IS_FULL): (""),
        str(ResponseCode.ADD_NEW_CONFIG_PANEL_FAILUR): (""),
        str(ResponseCode.CONFIG_TYPE_NOT_FOUND): (""),
    }


    @staticmethod
    def documents_status(uuid: str, price: int, status: bool) -> str:
        """
        
        """

        if status:
            return "💢 کاربر گرامی"
        else:
            return ""

    @staticmethod
    def send_evidence(price: int) -> str:
        """
        
        """
        return (
            f"➕ لطفا به شماره کارت زیر مبلغ {price} تومان واریز کنید و عکس فیش واریزی را ارسال کنید"
            f"شماره کارت : \n {Config.CARD_NUMBER}"
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
        user_api = APIS.user_api(int(user_id))
        result = user_api.get_user_information
        if (not result):
            
            return "به مشکل خورد مجدد امتحان کنید"

        return (
            f"balance : {result.balance}"
            "\n\n"
            f"user_id: {user_id}"
        ).format(user_id)
