from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = "Crea 500 productos de prueba usando bulk_create"

    def handle(self, *args, **options):
        productos = []
        for i in range(1, 501):
            productos.append(
                Product(
                    title=f"Producto {i}",
                    price=round(10 + (i * 0.5), 2),
                    description=f"Descripción del producto {i}",
                    seller=f"Vendedor {((i - 1) % 10) + 1}",
                    color=["Rojo", "Azul", "Negro", "Blanco", "Verde"][i % 5],
                    product_dimensions=f"{10 + (i % 50)}x{5 + (i % 30)}x{2 + (i % 20)} cm",
                )
            )

        Product.objects.bulk_create(productos)
        self.stdout.write(self.style.SUCCESS("✅ Se crearon 500 productos de prueba."))
