def saveUserinSession(request,user):
    request.session['name'] = user.name
    request.session['email'] = user.email
    request.session['phoneno'] = user.phone_number