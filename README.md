### PIZZA API


Project for Impacta Digital Product


### Authentication

# Post api/register/
```
Json
{
  "name": "John Due",
  "cpf": "1234567890",
  "email": "test@testmail.com",
  "password": "123456",
  "phone": "123456789",
	"address": {
		"city": "Taubaté",
		"state": "SP",
		"postal_code": "234555"
	}
}

Response Http 201

{
  "id": 1,
  "name": "John Due",
  "cpf": "1234567890",
  "email": "test@testmail.com",
  "phone": "123456789",
  "address": {
    "id": 1,
    "city": "Taubaté",
    "state": "SP",
    "postal_code": "234555",
    "additional_instructions": null
  }
}

```

# Post api/login/
```
Json
{
  "email": "test@testmail.com",
  "password": "123456"
}

Response Http 200

{
  "token": "43784a8d97dfbf73f25a8f248541ddd085660f50"
}

```

### Company

# Post api/company/
```
Json
{
	"name": "Pizza hut",
	"cnpj": "1234256",
	"address": {
		"street_address": "rua",
		"city": "São Paulo",
    "state": "SP",
    "postal_code": "20450100"
	},
	"contact_number": "11 50552020",
	"email": "pizza@hut.com",
	"description": "Best pizza in the world.",
	"pizzas": [
		{
			"flavor": "calabresa"
		}
	]
}

Response Http 201

{
  "id": 1,
  "name": "Pizza hut",
  "cnpj": "1234256",
  "address": {
    "id": 2,
    "city": "São Paulo",
    "state": "SP",
    "street_address": "Rua",
    "postal_code": "20450100",
    "additional_instructions": null
  },
  "contact_number": "11 50552020",
  "email": "pizza@hut.com",
  "description": "Best pizza in the world.",
  "pizzas": [
    {
      "id": 1,
      "flavor": "calabresa",
      "second_flavor": null,
      "is_two_flavors": false
    }
  ]
}

```

# Get api/company/?<param>&<query>&<user_id>
```
Token required

params = 'id','name', 'cnpj', 'address', 'contact_number', 'email', 'description', 'pizzas'

Json

Response Http 200
[
  {
    "id": 1,
    "name": "Pizza hut",
    "cnpj": "1234256",
    "address": {
      "id": 2,
      "city": "São Paulo",
      "state": "SP",
      "street_address": "Rua",
      "postal_code": "20450100",
      "additional_instructions": null
    },
    "contact_number": "11 50552020",
    "email": "pizza@hut.com",
    "description": "Best pizza in the world.",
    "pizzas": [
      {
        "id": 1,
        "flavor": "calabresa",
        "second_flavor": null,
        "is_two_flavors": false
      }
    ]
  }
]

```

# DELETE api/company/<int:company_id>/<int:user_id>/
```
Token required


Response Http 204


```


### Order

# Post api/order/
```
Json
{
  "user_id": 1,
  "company_id": 1,
  "pizzas_ids":[1],
  "size": "medium",
  "quantity": 1,
  "delivery_address_id": 1,
  "total_price": 50.45,
  "status": "ordered"
}
Response Http 201

{
  "customer": {
    "id": 1,
    "name": "John Due",
    "cpf": "1234567890",
    "email": "test@testmail.com",
    "phone": "123456789",
    "address": {
      "id": 1,
      "city": "Taubaté",
      "state": "SP",
      "postal_code": "234555",
      "additional_instructions": null
    }
  },
  "company": {
    "id": 1,
    "name": "Pizza hut",
    "cnpj": "1234256",
    "address": {
      "id": 2,
      "city": "São Paulo",
      "state": "SP",
      "street_address": "Rua",
      "postal_code": "20450100",
      "additional_instructions": null
    },
    "contact_number": "11 50552020",
    "email": "pizza@hut.com",
    "description": "Best pizza in the world.",
    "pizzas": [
      {
        "id": 1,
        "flavor": "calabresa",
        "second_flavor": null,
        "is_two_flavors": false
      }
    ]
  },
  "pizzas": [
    {
      "id": 1,
      "flavor": "calabresa",
      "second_flavor": null,
      "is_two_flavors": false
    }
  ],
  "delivery_address": {
    "id": 1,
    "city": "Taubaté",
    "state": "SP",
    "postal_code": "234555",
    "additional_instructions": null
  }
}

```

# Get api/order/?<param>&<query>&<user_id>
```
param = 'id', 'customer', 'company', 'pizzas', 'delivery_address', 'status'


Token required
Response Http 201
[
  {
    "customer": {
      "id": 1,
      "name": "John Due",
      "cpf": "1234567890",
      "email": "test@testmail.com",
      "phone": "123456789",
      "address": {
        "id": 1,
        "city": "Taubaté",
        "state": "SP",
        "postal_code": "234555",
        "additional_instructions": null
      }
    },
    "company": {
      "id": 1,
      "name": "Pizza hut",
      "cnpj": "1234256",
      "address": {
        "id": 2,
        "city": "São Paulo",
        "state": "SP",
        "street_address": "rua",
        "postal_code": "20450100",
        "additional_instructions": null
      },
      "contact_number": "11 50552020",
      "email": "pizza@hut.com",
      "description": "Best pizza in the world.",
      "pizzas": [
        {
          "id": 1,
          "flavor": "calabresa",
          "second_flavor": null,
          "is_two_flavors": false
        }
      ]
    },
    "pizzas": [
      {
        "id": 1,
        "flavor": "calabresa",
        "second_flavor": null,
        "is_two_flavors": false
      }
    ],
    "delivery_address": {
      "id": 1,
      "city": "Taubaté",
      "state": "SP",
      "postal_code": "234555",
      "additional_instructions": null
    }
  }
]


```

# DELETE api/order/<int:order_id>/<int:user_id>/
```
Token required


Response Http 204


```


### Review

# Post api/review/
```
Json
{
  "user_id": 1,
  "rating": 5,
  "review_text": "Pizza is always good.",
  "company_id": 1
}
Response Http 201

{
  "id": 1,
  "rating": 5,
  "review_text": "Pizza is always good.",
  "timestamp": "2023-06-13T19:34:30.664821Z",
  "customer": {
    "id": 1,
    "name": "John Due",
    "cpf": "1234567890",
    "email": "test@testmail.com",
    "phone": "123456789",
    "address": {
      "id": 1,
      "city": "Taubaté",
      "state": "SP",
      "postal_code": "234555",
      "additional_instructions": null
    }
  },
  "company": {
    "id": 1,
    "name": "Pizza hut",
    "cnpj": "1234256",
    "address": {
      "id": 2,
      "city": "São Paulo",
      "state": "SP",
      "postal_code": "20450100",
      "additional_instructions": null
    },
    "contact_number": "11 50552020",
    "email": "pizza@hut.com",
    "description": "Best pizza in the world.",
    "pizzas": [
      {
        "id": 1,
        "flavor": "calabresa",
        "second_flavor": null,
        "is_two_flavors": false
      }
    ]
  }
}

```


# Get api/review/?<param>&<query>&<user_id>
```
Json

Token Required

param = "id","customer", "rating" ,"company"

Response Http 200

[
  {
    "id": 1,
    "rating": 5,
    "review_text": "Pizza is always good.",
    "timestamp": "2023-06-13T19:34:30.664821Z",
    "customer": {
      "id": 1,
      "name": "John Due",
      "cpf": "1234567890",
      "email": "test@testmail.com",
      "phone": "123456789",
      "address": {
        "id": 1,
        "city": "Taubaté",
        "state": "SP",
        "postal_code": "234555",
        "street_address": "",
        "additional_instructions": null
      }
    },
    "company": {
      "id": 1,
      "name": "Pizza hut",
      "cnpj": "1234256",
      "address": {
        "id": 2,
        "city": "São Paulo",
        "state": "SP",
        "postal_code": "20450100",
        "street_address": "rua",
        "additional_instructions": null
      },
      "contact_number": "11 50552020",
      "email": "pizza@hut.com",
      "description": "Best pizza in the world.",
      "pizzas": [
        {
          "id": 1,
          "flavor": "calabresa",
          "second_flavor": null,
          "is_two_flavors": false
        }
      ]
    }
  }
]
```

# DELETE api/review/<int:review_id>/<int:user_id>/
```
Token required


Response Http 204


```