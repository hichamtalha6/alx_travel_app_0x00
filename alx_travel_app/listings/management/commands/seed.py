from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Example listings
        sample_listings = [
            {"title": "Cozy Cottage", "description": "A nice cozy cottage.", "price_per_night": 75, "location": "Paris"},
            {"title": "Modern Apartment", "description": "City center apartment.", "price_per_night": 120, "location": "London"},
            {"title": "Beach House", "description": "Ocean view house.", "price_per_night": 200, "location": "Miami"},
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
