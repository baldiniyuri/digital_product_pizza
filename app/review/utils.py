from typing import Type, Tuple, Union, Dict
from authentication.models import User
from company.models import Company
from review.models import Review


class ReviewUtils:
    def __init__(self, request) -> None:
        self.user = User
        self.company = Company
        self.review = Review
        self.request = request
        self.review_text = request.data["review_text"]
        self.rating = request.data["rating"]
            

    def filter_models(self) -> Union[Dict[str, Union[int, str]], Tuple[User, Company]]:
        missing_models = {}
        try:
            user = self.user.objects.get(id=self.request.data["user_id"])
        except self.user.DoesNotExist:
            missing_models["user"] = self.request.data["user_id"]
        
        try:
            company = self.company.objects.get(id=self.request.data["company_id"])
        except self.company.DoesNotExist:
            missing_models["company"] = self.request.data["company_id"]

        if missing_models:
            return missing_models
        
        return user, company
    

    def get_relation_objects(self) -> Union[Tuple[User, Company], bool]:
        relation_objects = self.filter_models()

        if relation_objects:
            user = self.user.objects.get(id=self.request.data["user_id"])
            company = self.company.objects.get(id=self.request.data["company_id"])
            return user, company
        return False
    

    def create_review(self) -> Tuple[bool, Union[Review, str]]:
        relation_objects = self.get_relation_objects()

        if isinstance(relation_objects, dict):
            missing_models = []
            for model, model_id in relation_objects.items():
                missing_models.append(f"{model} (ID: {model_id})")
            return False, missing_models

        user, company  = relation_objects  

        try:
            review = self.review.objects.create(
                customer=user,
                company=company,
                review_text = self.review_text,
                rating = self.rating

            )
        
            return True, review
        except Exception as e:

            return False, str(e)