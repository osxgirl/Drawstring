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
        currency,
        source_experience=None,
        order_id=None,
        notes=None,
        verified_visible=False,
    ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.item_type = item_type  # "physical" or "digital"
        self.platform = platform
        self.acquisition_type = acquisition_type  # "cash", "robux", "earned"
        self.price = price
        self.currency = currency
        self.source_experience = source_experience
        self.order_id = order_id
        self.notes = notes
        self.verified_visible = verified_visible
        self.date_acquired = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return self.__dict__
