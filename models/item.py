import uuid
from datetime import datetime


class FashionItem:
    def __init__(
        self,
        name,
        item_type,
        platform,
        acquisition_type,
        price,
        currency_name,
        currency_type,
        usd_equivalent=None,
        source_experience=None,
        order_id=None,
        notes=None,
        verified_visible=True,
    ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.item_type = item_type  # physical / digital
        self.platform = platform
        self.acquisition_type = acquisition_type  # cash / robux / earned

        self.price = price
        self.currency_name = currency_name  # Robux / Pink Cash / Coins / USD
        self.currency_type = currency_type  # premium / soft / fiat
        self.usd_equivalent = usd_equivalent

        self.source_experience = source_experience
        self.order_id = order_id
        self.notes = notes

        self.verified_visible = verified_visible
        self.missing_flag = not verified_visible

        self.date_acquired = datetime.now().strftime("%Y-%m-%d")
        self.last_verified = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return self.__dict__