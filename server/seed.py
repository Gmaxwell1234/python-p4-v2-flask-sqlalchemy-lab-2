from models import db, Customer, Item, Review
from app import app

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create sample customers
    customer1 = Customer(name="Tal Yuri")
    customer2 = Customer(name="Jane Smith")
    customer3 = Customer(name="Bob Johnson")

    # Create sample items
    item1 = Item(name="Laptop Backpack", price=49.99)
    item2 = Item(name="Insulated Coffee Mug", price=9.99)
    item3 = Item(name="Wireless Earbuds", price=79.99)

    # Add and commit customers and items
    db.session.add_all([customer1, customer2, customer3, item1, item2, item3])
    db.session.commit()

    # Create reviews
    review1 = Review(comment="Great backpack!", customer_id=customer1.id, item_id=item1.id)
    review2 = Review(comment="Keeps coffee hot for hours", customer_id=customer1.id, item_id=item2.id)
    review3 = Review(comment="Best earbuds I've owned", customer_id=customer2.id, item_id=item3.id)
    review4 = Review(comment="Mug broke after 2 weeks", customer_id=customer3.id, item_id=item2.id)

    # Add and commit reviews
    db.session.add_all([review1, review2, review3, review4])
    db.session.commit()

    print("Database seeded successfully!")