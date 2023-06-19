from jdatetime import datetime as PersianTime
from config.config import Config
from modules.enums import ResponseCode
from modules.api.APIS import APIS


class Strings:

    BUY_CONFIG = "💳 به بخش خرید کانفیگ خوش آمدید , لطفا سرور مد نظر رو انتخاب کنید"
    SHOP = "💰 به بخش فروشگاه خوش آمدید, از منوی زیر انتخاب کنید"
    SUPPORT = "💡 جهت پیام ارتباط با ادمین لطفا روی دکمه زیرین کلیک کنید 🌀"
    GET_CUSTOM_CHARGE = "📍 مبلغ مد نظر خود را به **تومان** وارد کنید (با اعداد لاتین) 💳"
    NOT_NUMBER = "❌مقدار ارسالی شما  به صورت عددی نیست , لطفا **به صورت عدد لاتین** ارسال کنید. ❌"
    NOT_PICTURE = "🚫 مورد ارسال شده اشتباه است, لطفا فقط عکس ارسال کنید"
    WAITING = "⏳ لطفا منتظر بمانید "
    SELECT_CHARGE = "⁉ به چه روشی میخواهید حساب خود را شارژ کنید؟"
    SEND_PICTURE = "⚠ لطفا تصویر فیش واریزی"
    BACKED_TO_HOME = "👋 به منوی اصلی بازگشتید"
    SERVICES = "💢 سرویس های شما به شرح زیر است 👇"
    NOT_SERVICE = "❌ شما سرویسی برای نمایش ندارید ❌"
    NOT_SERVER = "❌ سروری برای نمایش وجود ندارد ❌"
    SELECT_SERVER = "🔹 از لیست زیر سرور مد نظر خود را انتخاب کنید ⁉️"
    NO_PURCHASE = "❌ این سرویس برای بازاریاب ها غیرفعال است ❌"
    FINAL_APPROVAL = "📍 از خرید خود مطمئن هستید ⁉️"
    ERROR = "🚫 مشکلی پیش آمد , لطفا مجددا تست کنید ❤️"
    CANCELED = "🔴 عملیات کنسل شد "
    WAIT_CONFIRMATION = "در انتظار تایید "
    PAID = "با موفقیت پرداخت شد ✅"
    UNPAIN = "پرداخت نشده ❌"
    DOCUMENTS_RECEIVED = "✅ مدارک ارسالی شما برای ادمین ناظر ارسال شد, تا تایید صبور باشید"
    ACC_ERROR = "🔺 مشکلی پیش آمد "
    DOCUMENTS_NOT_RECEIVED = (
        "💢در ارسال مدارک شما به تیم پشتیبانی مشکلی رخ داد, لطفا مدارک خود رو برای ایدی زیر ارسال کنید تا تایید شود."
        "\n\n"
        "⭕️ پ.ن : پوزش مارا بپذیرید"
    )

    RESPONSE_API_STRINGS = {
        str(ResponseCode.USER_TYPE_ERROR): "💢 مشکلی پیش آمد, درجه شما برای انجام این کار مناسب نیست",
        str(ResponseCode.CONFIG_DOES_NOT_EXIST): ("❌ این کانفیگ وجود ندارد "),
        str(ResponseCode.SERVER_DOES_NOT_EXIST): ("❌ این سرور وجود ندارد "),
        str(ResponseCode.LOW_BALANCE): ("💳 موجودی شما کم است"),
        str(ResponseCode.SERVER_IS_FULL): ("💸 ظرفیت سرور تکمیل شده است"),
        str(ResponseCode.ADD_NEW_CONFIG_PANEL_FAILUR): ("❌ مشکلی پیش آمد, مجدد تست کنید, در صورت کسر وجه از شما مدارک را به پشتیبانی ارسال کنید ."),
        str(ResponseCode.CONFIG_TYPE_NOT_FOUND): ("❌ این کانفیگ وجود ندارد, مجدد تست کنید "),
        str(ResponseCode.CONFIG_IS_ALREADY_ENABLE): ("⏳ سرور شما درحال حاضر فعال است"),
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
    def account(name: str, user_id: int) -> str:
        user_api = APIS.user_api(user_id)
        result = user_api.get_user_information

        if (not result): return Strings.ERROR

        time = t = PersianTime.today().strftime("%Y-%m-%d")

        return (
            "📊 - وضعیت حساب شما به شرح زیر است :\n\n"
            f"✍ نام شما : `{name}`\n"
            f"🔢 ایدی عددی شما : {user_id}\n" 
            f"🤑 موجودی شما : {result.balance} تومان\n"
            f"⛓ تعداد زیرمجموعه : {len(result.referrals)}\n"
            f"📅 تاریخ امروز : {time}\n\n"
            f"🆔 {Config.BOT_USERNAME}"
        )
    
    @staticmethod
    def acc_reject(name: str, user_name: str,  user_id: int, amount: int) -> str:

        time = PersianTime.today().strftime("%Y-%m-%d")
        text = (
            "#درخواست_افزایش_موجودی 💳\n\n"
            f"👤 - Name : [{name}](tg://user?id={user_id})\n"
            f"👾 - User Name : {f'@{user_name}' if (not user_name is None) else 'ندارد'}\n"
            f"🔢 - User ID : {user_id}\n"
            f"💰 - Amount : {int(amount):,}\n"
            f"⏰ - Date Time : {time}\n"
            f"🔑 - Status : {Strings.WAIT_CONFIRMATION}\n\n\n"
            f"@{Config.BOT_USERNAME}"
        )
        return text
    
    @staticmethod
    def end_config(user_id: int, v2ray_link: str) -> str:

        text = (
            f"💢 کاربر با آیدی عددی `{user_id}` تاریخ انتقضا کانفیگ با لینک :\n\n"
            f"`{v2ray_link}`\n\n"
            "در حال پایان است, میتوانید از بخش سرویس های من سرویس خود را تمدید کنید\n\n\n"
            f"🆔 @{Config.BOT_USERNAME}"
        )

        return text

    @staticmethod
    def admin_accepted(user_id: int, admin_user_id: int, amount: int) -> str:

        time = PersianTime.today().strftime("%Y-%m-%d")
        text = f"✅ فیش کاربر : {user_id} توسط ادمین با آیدی عددی {admin_user_id} به مبلغ {amount} در تاریخ {time} قبول شد ."

        return text

    @staticmethod
    def admin_rejected(user_id: int, admin_user_id: int, amount: int) -> str:

        time = PersianTime.today().strftime("%Y-%m-%d")
        text = f"❌ فیش کاربر : {user_id} توسط ادمین با آیدی عددی {admin_user_id} به مبلغ {amount} در تاریخ {time} رد شد ."

        return text

    @staticmethod
    def user_accepted(amount: int) -> str:
        text = (
            "🔺 فیش ارسالی شما توسط ادمین پذیرفته شد\n"
            f"💳 موجودی شما {int(amount):,} تومان افزایش یافت"
        )

        return text

    @staticmethod
    def user_rejected(amount: int) -> str:

        text = f"🔺 فیش ارسالی شما به مبلغ {int(amount):,} تومان توسط ادمین رد شد."
        return text

    @staticmethod
    def error_text(error_id: int) -> str:
        """_summary_

        Args:
            error_id (int): _description_

        Returns:
            str: _description_
        """
        response_error = Strings.RESPONSE_API_STRINGS
        if (str(error_id) in response_error.keys()):
            
            return response_error[str(error_id)]
        
        return Strings.ERROR

    @staticmethod
    def your_config(config_link: str) -> str:

        """_summary_

        Returns:
            _type_: _description_
        """

        text = (
            "🔹 لینک کانفیگ شما : \n\n"
            f"`{config_link}`"
        )

        return text

    @staticmethod
    def online_payment_link(config_name: str, price: int) -> str:

        text = f"🔶 خرید کانفیگ `{config_name}` با قیمت `{price}` تومان "
        return text
