from app.models import Booking, Bike

def book_bike(request, bike, check_in, check_out):
    booking = Booking.objects.create(
        user = request.user,
        bike= bike,
        check_in = check_in,
        check_out = check_out
    )
    booking.save()
    return booking