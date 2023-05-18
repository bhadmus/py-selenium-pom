from resources.page_object import HomePageObject
from data_elements.element_mapper import *

test = HomePageObject()

test.launch_page()
test.mouse_over_element(HomePage.mens_tab)
test.mouse_over_element(HomePage.mens_top)
test.click_element(HomePage.mens_hoodie)
test.select_value(ShopPage.indexer, '36')
test.click_element(ShopPage.test_item)
test.click_element(ShopPage.xl_size)
test.click_element(ShopPage.orange_colour)
test.click_element(ShopPage.add_cart_button)
test.wait_for_text_presence(ShopPage.cart_icon, '1')
test.click_element(ShopPage.cart_icon)
test.click_element(ShopPage.checkout_button)
test.fill_details(PayDetails.email_field, TestData.email)
test.fill_details(PayDetails.fname_field, TestData.fname)
test.fill_details(PayDetails.lname_field, TestData.lname)
test.fill_details(PayDetails.street_field, TestData.street)
test.fill_details(PayDetails.city_field, TestData.city)
test.fill_details(PayDetails.pcode_field, TestData.zip_code)
test.select_value(PayDetails.country, "NG")
test.fill_details(PayDetails.region, TestData.state)
test.fill_details(PayDetails.phone_field, TestData.mobile_number)
test.wait_for_selection(PayDetails.ship_rate)
test.click_element(CompleteOrder.continue_button)
test.wait_for_text_presence(CompleteOrder.place_holder_for_order, TestData.holder_text)
test.execute_click_action(CompleteOrder.place_order_button)
test.wait_for_text_presence(CompleteOrder.success_message_holder, CompleteOrder.actual_success_message)
test.verify_text(CompleteOrder.success_message_holder, TestData.expected_success_message)