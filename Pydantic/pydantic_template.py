from pydantic import BaseModel, ConfigDict, Field, model_validator, field_validator
import re

class UserRequest(BaseModel):
    user_id: str | None = Field(..., description="UUID of user.") # required because of ...
    user_request: str | None = Field(None, description="Request of user.") # not required because default set to None
    name: str # required
    last_name: str | None # required but None is also possible
    age: str | None = None # required because default set to None
    model_config = ConfigDict(extra="allow")

    # @field_validator('user_id') # on one field
    # def check_uuid(cls, v):
    #     uuid_regex = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    #     if not re.match(uuid_regex, v):
    #         raise ValueError('Invalid QR-code.')
    #     return v
    
    # @model_validator(mode="after") # several fields
    # def validate_model(self):
    #     if not self.element_id and not self.user_request :
    #         raise AttributeError('Request can not be empty.')
    #     return self
    
def main():
    request_data = {"user_id": "123", "user_request": "123", "name": "123", "last_name": None}
    new_user_request = UserRequest(**request_data)
    json_object_to_send = new_user_request.model_dump() # serialize
    print("hi")

if __name__ == "__main__":
    main()

