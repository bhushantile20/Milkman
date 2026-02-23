#  Milkman API - README
 Quick Start:
bash
pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser  # milkman/milkman123
python manage.py runserver
# 5 APIs
text
GET/POST /api/users/          # Milkman admins
GET/POST /api/categories/     # Cow/Buffalo/Ghee  
GET/POST /api/products/       # 0.5L/1L/2L packets
GET/POST /api/customers/      # Customers + Telegram
GET/POST /api/subscriptions/  # Daily/Monthly subs

# Admin
text
http://127.0.0.1:8000/admin/
milkman / milkman123
 # Test Flow
POST category: {"name": "cow_milk"}

POST product: {"category":1,"packet_size":"one_litre","price":45}

POST customer: {"phone":"9876543210","address":"Pune"}

POST subscription: {"customer":1,"product":1,"start_date":"2026-03-01"}
| Endpoint            | Description                  | Methods                                 |
| ------------------- | ---------------------------- | --------------------------------------- |
| /api/users/         | Milkman admins/managers      | GET, POST, PUT, DELETE                  |
| /api/categories/    | Cow Milk, Buffalo Milk, Ghee | GET, POST, PATCH /active/, /deactivate/ |
| /api/products/      | 0.5L, 1L, 2L packets         | GET, POST, /available/, /by_category/   |
| /api/customers/     | End customers + Telegram IDs | GET, POST, /telegram_customers/         |
| /api/subscriptions/ | Subscriptions + /types/      | GET, POST, /pending/, /confirm_payment/ |

<img width="1919" height="985" alt="image" src="https://github.com/user-attachments/assets/182523f0-3df0-436f-9841-bd6ff5eb8a5a" />
<img width="1894" height="908" alt="image" src="https://github.com/user-attachments/assets/382ab559-3081-4fd2-aa09-b0009890d606" />
<img width="1919" height="919" alt="image" src="https://github.com/user-attachments/assets/7e39994d-3450-40fa-94df-a1fe98ed3e0c" />
<img width="1919" height="911" alt="image" src="https://github.com/user-attachments/assets/ac57c5c5-48a4-4794-959b-e7eefcb8e075" />
<img width="1918" height="919" alt="image" src="https://github.com/user-attachments/assets/97d26b9d-a259-4671-a5b9-27600da1ce05" />
<img width="1919" height="919" alt="image" src="https://github.com/user-attachments/assets/ec9f8fd6-ede8-497a-b282-24f7910f7733" />
<img width="1918" height="920" alt="image" src="https://github.com/user-attachments/assets/6a33bf55-c2a8-4fea-b8c6-f3d4e4880b1f" />







