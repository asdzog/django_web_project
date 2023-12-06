from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        categories = [
            {
                "category_name": "Laptops",
                "category_description": "Portable computers"
                },
            {
                "category_name": "Smartphones",
                "category_description": "Mobile cellphones"
                },
            {
                "category_name": "Smart-TVs",
                "category_description": "Televisions with internal OS"
                },
            {
                "category_name": "Sound systems",
                "category_description": "Speakers, headphones and others"
                },
            {
                "category_name": "Keyboards and manipulators",
                "category_description": "Keyboards, mouses, trackballs and other controllers"
                }
        ]
        categories_to_insert = []
        for category in categories:
            categories_to_insert.append(
                Category(**category)
            )

        # очистка базы данных перед заполнением
        Category.objects.all().delete()

        # заполнеие базы данных сформированными данными
        Category.objects.bulk_create(categories_to_insert)

        products = [
            {
                "product_name": "HP Pavilion 15-bv151sr",
                "product_description": "without OS",
                "preview_icon": "",
                "category": categories_to_insert[0],
                "price": 56000.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            },
            {
                "product_name": "MSI Katana G76",
                "product_description": "Gaming laptop",
                "preview_icon": "",
                "category": categories_to_insert[0],
                "price": 115000.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            },
            {
                "product_name": "JBL Partybox 710",
                "product_description": "1.0, 800 W, Bluetooth",
                "preview_icon": "",
                "category": categories_to_insert[3],
                "price": 96000.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            },
            {
                "product_name": "LG XBOOM CK43",
                "product_description": "2.0, 300 W, wireless remote, Bluetooth",
                "preview_icon": "",
                "category": categories_to_insert[3],
                "price": 16000.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            },
            {
                "product_name": "Samsung Galaxy S23 FE",
                "product_description": "8x2.8 GHZ, 8 Gb, 2 SIM",
                "preview_icon": "",
                "category": categories_to_insert[1],
                "price": 73000.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            },
            {
                "product_name": "HUAWEI P60 Pro",
                "product_description": "8x3.2 GHz, 12 Gb, 2 SIM",
                "preview_icon": "",
                "category": categories_to_insert[1],
                "price": 81999.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            },
            {
                "product_name": "LG 32LM576BPLD",
                "product_description": "TVset 32\" (80 cm) LED black",
                "preview_icon": "",
                "category": categories_to_insert[1],
                "price": 23000.0,
                "data_created": "2023-12-05",
                "data_modified": "2023-12-05"
            }
        ]

        products_to_insert = []
        for product in products:
            products_to_insert.append(
                Product(**product)
            )

        # очистка таблицы с товарами перед заполнением
        Product.objects.all().delete()

        # заполнеие таблицы с товарами сформированными данными
        Product.objects.bulk_create(products_to_insert)
