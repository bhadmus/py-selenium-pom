class HomePage:
    """
        This stores element on the homepage
    """
    url = 'https://magento.softwaretestingboard.com/'
    mens_tab = '[href="https://magento.softwaretestingboard.com/men.html"]'
    mens_top = '[href="https://magento.softwaretestingboard.com/men/tops-men.html"]'
    mens_hoodie = '[href="https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html"]'


class ShopPage:
    """
        This stores element on the product page
    """
    indexer = 'div:nth-of-type(4) > .field.limiter > .control > select#limiter'
    test_item = 'li:nth-of-type(13) > .product-item-info'
    xl_size = 'div[role="listbox"] > div:nth-of-type(5)'
    orange_colour = '.color.swatch-attribute > div[role="listbox"] > div:nth-of-type(3)'
    add_cart_button = 'button#product-addtocart-button'
    cart_icon = '.action.showcart > .counter.qty'
    checkout_button = 'button#top-cart-btn-checkout'


class PayDetails:
    email_field = 'fieldset  div > div > input[name="username"]'
    fname_field = 'input[name="firstname"]'
    lname_field = 'input[name="lastname"]'
    street_field = 'input[name="street[0]"]'
    city_field = 'input[name="city"]'
    pcode_field = 'input[name="postcode"]'
    country = 'select[name="country_id"]'
    region = 'input[name="region"]'
    phone_field = 'input[name="telephone"]'
    ship_rate = 'input[value="flatrate_flatrate"]'


class CompleteOrder:
    continue_button = 'button[data-role="opc-continue"]'
    place_order_button = '[class="action primary checkout"]'
    place_holder_for_order = '.payment-method-content >div > div > button[type="submit"]'
    success_message_holder = 'h1 > span'
    actual_success_message = 'Thank you for your purchase!'


class TestData:
    email = 'bhadmus_test@yopmail.com'
    fname = 'Eva'
    lname = 'Mendez'
    street = '3 Walter Carrington Street'
    city = 'Victoria Island'
    zip_code = '23401'
    state = 'Lagos'
    mobile_number = '+2345011111111'
    holder_text = 'Place Order'
    expected_success_message = 'Thank you for your purchase!'
