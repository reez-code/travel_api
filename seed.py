# seed.py
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import City, Hotel, TransportOption, TransportMean, TransportRoute

# --- 1. Clear existing data ---
def clear_data(db: Session):
    db.query(TransportMean).delete()
    db.query(City).delete()
    db.query(TransportOption).delete()
    db.query(TransportRoute).delete()
    db.query(Hotel).delete()
    db.commit()
    print("Cleared existing data.")


# --- 2. Seed sample data (real-time data goes here) ---
def seed_data(db: Session):
    # Example: Seed transport means
    means = [
        TransportMean(name="Air"),
        TransportMean(name="Water"),
        TransportMean(name="Land"),
    ]
    db.add_all(means)
    db.commit()
    print("Seeded transport means.")

    cities = [
        City(name="Nairobi", country="Kenya", region="Nairobi", latitude=-1.286389, longitude=36.820030, description="Capital city of Kenya."),
        City(name="Mombasa", country="Kenya", region="Coast", latitude=-4.054280, longitude=39.690430, description="Coastal city in Kenya."),
        City(name="Kisumu", country="Kenya", region="Nyanza", latitude=-0.103090, longitude=34.756062, description="City on the shores of Lake Victoria."),
       ]
    db.add_all(cities)
    db.commit()
    print("Seeded cities.")

    # Add more seeding below here as needed...
    transport_options = [
        TransportOption(name="Kenya Airways", means_id=1, website_url="https://www.kenya-airways.com/"),
        TransportOption(name="Jambo Jet", means_id=1, website_url="https://www.jambojet.com/"),
        TransportOption(name="Standard Gauge Railway (SGR)", means_id=3, website_url="https://metickets.krc.co.ke/"),
        TransportOption(name="Modern Coast", means_id=3, website_url="https://www.modern.co.ke/"),
        TransportOption(name="Easy Coach", means_id=3, website_url="https://easycoachkenya.com/"),
    ]
    db.add_all(transport_options)
    db.commit()
    print("Seeded transport options.")

    transport_routes = [
    # Nairobi ⇄ Mombasa
    TransportRoute(transport_option_id=1, origin_city_id=1, destination_city_id=2, duration="1 hour",
                   price_estimate="Economy: From KES 12,500 - 21,000 | Business: From KES 21,950 - 25,800",
                   schedule_info="Daily flights available"),
    TransportRoute(transport_option_id=1, origin_city_id=2, destination_city_id=1, duration="1 hour",
                   price_estimate="Economy: From KES 12,500 - 21,000 | Business: From KES 21,950 - 25,800",
                   schedule_info="Daily flights available"),
    TransportRoute(transport_option_id=2, origin_city_id=1, destination_city_id=2, duration="1 hour 15 minutes",
                   price_estimate="Economy: From KES 11,000 - 18,000 | Business: From KES 20,000 - 24,500",
                   schedule_info="Multiple departures daily"),
    TransportRoute(transport_option_id=2, origin_city_id=2, destination_city_id=1, duration="1 hour 15 minutes",
                   price_estimate="Economy: From KES 11,000 - 18,000 | Business: From KES 20,000 - 24,500",
                   schedule_info="Multiple departures daily"),

    # Nairobi ⇄ Kisumu (Easy Coach)
    TransportRoute(transport_option_id=5, origin_city_id=1, destination_city_id=3, duration="8 hours",
                   price_estimate="KES 1,000",
                   schedule_info="Daily departures at 7:00 AM and 10:00 AM"),
    TransportRoute(transport_option_id=5, origin_city_id=3, destination_city_id=1, duration="8 hours",
                   price_estimate="From KES 1,000",
                   schedule_info="Daily departures at 7:00 AM and 10:00 AM"),

    # Mombasa ⇄ Kisumu(Easy Coach)
    TransportRoute(transport_option_id=5, origin_city_id=2, destination_city_id=3, duration="12 hours",
                   price_estimate="KES 2,500",
                   schedule_info="Daily departures at 7:00 AM and 10:00 AM"),
    TransportRoute(transport_option_id=5, origin_city_id=3, destination_city_id=2, duration="12 hours",
                   price_estimate="From KES 2,500",
                   schedule_info="Daily departures at 7:00 AM and 10:00 AM"),
    
    # Nairobi ⇄ Mombasa (Modern Coast)
    TransportRoute(transport_option_id=4, origin_city_id=1, destination_city_id=2, duration="8 hours",
                   price_estimate="Economy: KES 1000 | Luxury: KES 3,000",
                   schedule_info="Daily departures at 7:00 AM and 10:00 AM"),
    TransportRoute(transport_option_id=4, origin_city_id=2, destination_city_id=1, duration="8 hours",
                   price_estimate="Economy: From KES 1000 | Luxury: From KES 3,000",
                   schedule_info="Daily departures at 7:00 AM and 10:00 AM"),
   
    # Nairobi ⇄ Mombasa (SGR)
    TransportRoute(transport_option_id=3, origin_city_id=1, destination_city_id=2, duration="6 hours",
                   price_estimate="Economy Class: KSH 1,500 | First Class: KSH 4,500",
                   schedule_info="Daily departures at 8:00 AM and 2:00 PM"),
    TransportRoute(transport_option_id=3, origin_city_id=2, destination_city_id=1, duration="6 hours",
                   price_estimate="Economy Class: KSH 1,500 | First Class: KSH 4,500",
                   schedule_info="Daily departures at 8:00 AM and 2:00 PM"),

    # Nairobi ⇄ Kisumu
    TransportRoute(transport_option_id=1, origin_city_id=1, destination_city_id=3, duration="1 hour",
                   price_estimate="Economy: From KES 10,000 - 18,000 | Business: From KES 20,000 - 24,000",
                   schedule_info="Daily flights available"),
    TransportRoute(transport_option_id=1, origin_city_id=3, destination_city_id=1, duration="1 hour",
                   price_estimate="Economy: From KES 10,000 - 18,000 | Business: From KES 20,000 - 24,000",
                   schedule_info="Daily flights available"),
    TransportRoute(transport_option_id=2, origin_city_id=1, destination_city_id=3, duration="1 hour",
                   price_estimate="Economy: From KES 8,500 - 11,000 | Business: From KES 15,000 - 20,000",
                   schedule_info="Daily flights available"),
    TransportRoute(transport_option_id=2, origin_city_id=3, destination_city_id=1, duration="1 hour",
                   price_estimate="Economy: From KES 8,500 - 11,000 | Business: From KES 15,000 - 20,000",
                   schedule_info="Daily flights available"),


    # Mombasa ⇄ Kisumu 
    TransportRoute(transport_option_id=1, origin_city_id=2, destination_city_id=3, duration="4 hours",
                   price_estimate="Economy: From KES 21,000 - 24,000 | Business: From KES 27,000 - 30,000",
                   schedule_info="3 times a week"),
    TransportRoute(transport_option_id=1, origin_city_id=3, destination_city_id=2, duration="4 hours",
                   price_estimate="Economy: From KES 17,000 - 24,000 | Business: From KES 27,000 - 30,000",
                   schedule_info="3 times a week"),
    TransportRoute(transport_option_id=2, origin_city_id=2, destination_city_id=3, duration="4 hours",
                   price_estimate="Economy: From KES 17,000 - 24,000 | Business: From KES 27,000 - 30,000",
                   schedule_info="3 times a week"),
    TransportRoute(transport_option_id=2, origin_city_id=3, destination_city_id=2, duration="4 hours",
                   price_estimate="Economy: From KES 17,000 - 24,000 | Business: From KES 27,000 - 30,000",
                   schedule_info="3 times a week"),
]
    db.add_all(transport_routes)
    db.commit()
    print("Seeded realistic routes.")

    hotels = [
  # Nairobi Hotels
    Hotel(
        name="The Norfolk Hotel", city_id=1, address="Harry Thuku Rd", rating=4.5,
        website_url="https://www.fairmont.com/en/hotels/nairobi/fairmont-the-norfolk.html?wiz_medium=cpc&wiz_source=google&wiz_campaign=22804080214&gad_campaignid=22804080214",
        latitude="-1.281389", longitude="36.816667", price_per_night="KES 15,000",
        description="Historic luxury hotel in central Nairobi with colonial charm."
    ),
    Hotel(
        name="Villa Rosa Kempinski", city_id=1, address="Chiromo Road", rating=4.8,
        website_url="https://www.kempinski.com/en/hotel-villa-rosa/overview",
        latitude="-1.270000", longitude="36.812000", price_per_night="KES 22,000",
        description="Upscale hotel offering world-class services and fine dining."
    ),
    Hotel(
        name="Sarova Stanley", city_id=1, address="Kimathi Street", rating=4.6,
        website_url="https://www.sarovahotels.com/stanley-nairobi/",
        latitude="-1.283333", longitude="36.816667", price_per_night="KES 14,000",
        description="Classic Nairobi hotel known for elegance and service."
    ),

    # Mombasa Hotels
    Hotel(
        name="Serena Beach Resort", city_id=2, address="Shanzu Beach", rating=4.7,
        website_url="https://www.serenahotels.com/serena-beach",
        latitude="-3.986000", longitude="39.728000", price_per_night="KES 18,000",
        description="Beachfront resort offering serene getaways and luxury."
    ),
    Hotel(
        name="Voyager Beach Resort", city_id=2, address="Mount Kenya Road", rating=4.5,
        website_url="https://www.voyagerbeachresort.com",
        latitude="-4.020000", longitude="39.689000", price_per_night="KES 16,500",
        description="All-inclusive beach resort with ocean views and entertainment."
    ),
    Hotel(
        name="PrideInn Paradise Beach", city_id=2, address="Shanzu, Mombasa", rating=4.4,
        website_url="https://www.prideinnhotels.com/hotels-in-mombasa/prideinn-paradise/",
        latitude="-3.933000", longitude="39.728000", price_per_night="KES 14,500",
        description="Family-friendly resort with water park and sea view rooms."
    ),

    # Kisumu Hotels
    Hotel(
        name="Sovereign Hotel", city_id=3, address="Aput Lane, Milimani", rating=4.3,
        website_url="https://sovereignhotel.co.ke/#/",
        latitude="-0.096500", longitude="34.759500", price_per_night="KES 11,000",
        description="Boutique hotel in Kisumu's Milimani area with lake views."
    ),
    Hotel(
        name="Acacia Premier Hotel", city_id=3, address="Achieng' Oneko Rd", rating=4.6,
        website_url="https://www.acaciapremier.com",
        latitude="-0.101389", longitude="34.759000", price_per_night="KES 13,000",
        description="Modern luxury hotel with a rooftop lounge and conference center."
    ),
    Hotel(
        name="Imperial Express", city_id=3, address="Oginga Odinga Street", rating=4.0,
        website_url="https://imperialexpress.com/",
        latitude="-0.102000", longitude="34.755000", price_per_night="KES 9,000",
        description="Affordable hotel in Kisumu CBD ideal for business travelers."
    ),
]
    db.add_all(hotels)
    db.commit()
    print("Seeded hotels.")

    print("Done seeding all data.")


# --- 3. Run seeder ---
if __name__ == "__main__":
    db = SessionLocal()
    try:
        clear_data(db)
        seed_data(db)
    finally:
        db.close()
