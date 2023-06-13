from typing import Type, Tuple, Union
from authentication.models import User
from company.models import Company
from pizza.models import Pizza
from address.models import Address
from order.models import Order


class OrderUtils:
    def __init__(self, request) -> None:
        self.user: Type[User] = User
        self.company: Type[Company] = Company
        self.pizza: Type[Pizza] = Pizza
        self.address: Type[Address] = Address
        self.order: Type[Order] = Order
        self.request = request
        self.size = request.data["size"]
        self.quantity = request.data["quantity"]
        self.total_price = request.data["total_price"]
        self.status = request.data["status"]


    def filter_models(self):
        missing_models = {}
        try:
            user = self.user.objects.get(id=self.request.data["user_id"])
        except self.user.DoesNotExist:
            missing_models["user"] = self.request.data["user_id"]
        
        try:
            company = self.company.objects.get(id=self.request.data["company_id"])
        except self.company.DoesNotExist:
            missing_models["company"] = self.request.data["company_id"]
        
        pizza_ids = self.request.data.get("pizza_ids", [])
        pizzas = self.pizza.objects.filter(id__in=pizza_ids)
        if len(pizzas) != len(pizza_ids):
            missing_pizza_ids = set(pizza_ids) - set(pizzas.values_list("id", flat=True))
            missing_models["pizza"] = list(missing_pizza_ids)
        
        try:
            address = self.address.objects.get(id=self.request.data["delivery_address_id"])
        except self.address.DoesNotExist:
            missing_models["delivery_address"] = self.request.data["delivery_address_id"]
        
        if missing_models:
            return missing_models
        
        return user, company, pizzas, address


    def get_relation_objects(self) -> Union[Tuple[User, Company, Pizza, Address], bool]:
        relation_objects = self.filter_models()

        if relation_objects:
            user = self.user.objects.get(id=self.request.data["user_id"])
            company = self.company.objects.get(id=self.request.data["company_id"])
            pizzas = self.pizza.objects.filter(id__in=self.request.data["pizzas_ids"])
            address = self.address.objects.get(id=self.request.data["delivery_address_id"])
            return user, company, pizzas, address
        return False


    def create_order(self):
        relation_objects = self.get_relation_objects()
        if isinstance(relation_objects, dict):
            missing_models = []
            for model, model_id in relation_objects.items():
                missing_models.append(f"{model} (ID: {model_id})")
            return False, missing_models

        user, company, pizzas, address = relation_objects  

        try:
            order = self.order.objects.create(
                customer=user,
                company=company,
                delivery_address=address,
                size=self.size,
                quantity=self.quantity,
                total_price=self.total_price,
                status=self.status
            )
            order.pizzas.set(pizzas)  
            return True, order
        except Exception as e:

            return False, str(e)