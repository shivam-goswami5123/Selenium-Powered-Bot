from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='INR')
    bot.select_place_to_go('Jaipur')
    bot.select_dates(check_in_date='2025-02-10',
                     check_out_date='2025-02-15')
    