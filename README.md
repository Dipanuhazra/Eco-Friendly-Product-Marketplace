<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eco-Friendly Product Marketplace</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Eco-Friendly Product Marketplace</h1>
        <nav>
            <ul>
                <li><a href="#products">Products</a></li>
                <li><a href="#certification">Certification</a></li>
                <li><a href="#delivery">Delivery Options</a></li>
                <li><a href="#reviews">User Reviews</a></li>
                <li><a href="#forum">Community Forum</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="products">
            <h2>Products</h2>
            <div class="product">
                <img src="product1.jpg" alt="Product 1">
                <h3>Product 1</h3>
                <p>Eco-friendly product description.</p>
                <p><strong>Price:</strong> $10.00</p>
                <button>Add to Cart</button>
            </div>
            <div class="product">
                <img src="product2.jpg" alt="Product 2">
                <h3>Product 2</h3>
                <p>Eco-friendly product description.</p>
                <p><strong>Price:</strong> $20.00</p>
                <button>Add to Cart</button>
            </div>
        </section>

        <section id="certification">
            <h2>Green Certification</h2>
            <p>Our products are certified by the leading eco-friendly organizations. Look for the green certification badge on our products.</p>
            <img src="certification_badge.jpg" alt="Green Certification Badge">
        </section>

        <section id="delivery">
            <h2>Eco-Friendly Delivery Options</h2>
            <p>We offer a variety of eco-friendly delivery options to minimize our carbon footprint.</p>
            <ul>
                <li>Carbon-neutral shipping</li>
                <li>Recyclable packaging</li>
                <li>Local pickup</li>
            </ul>
        </section>

        <section id="reviews">
            <h2>User Reviews</h2>
            <div class="review">
                <h3>John Doe</h3>
                <p>★★★★★</p>
                <p>Great product! Very satisfied with the eco-friendly packaging.</p>
            </div>
            <div class="review">
                <h3>Jane Smith</h3>
                <p>★★★★☆</p>
                <p>Good quality, but delivery took a bit longer than expected.</p>
            </div>
            <form>
                <h3>Leave a Review</h3>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
                <label for="rating">Rating:</label>
                <select id="rating" name="rating">
                    <option value="5">★★★★★</option>
                    <option value="4">★★★★☆</option>
                    <option value="3">★★★☆☆</option>
                    <option value="2">★★☆☆☆</option>
                    <option value="1">★☆☆☆☆</option>
                </select>
                <label for="review">Review:</label>
                <textarea id="review" name="review"></textarea>
                <button type="submit">Submit</button>
            </form>
        </section>

        <section id="forum">
            <h2>Community Forum</h2>
            <p>Join our community forum to discuss eco-friendly products and share tips on sustainable living.</p>
            <a href="forum.html">Go to Forum</a>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Eco-Friendly Product Marketplace. All rights reserved.</p>
    </footer>
</body>
</html>
