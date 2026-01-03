class Cart():
    def __init__(self,request):

        self.session=request.session

        # Returning user - obtain his/her existing session

        cart=self.session.get('session_key')

        # New user - generate a session key

        if 'session_key' not in request.session:
            cart=self.session['session_key']={"fav_num":13}
        
        self.cart=cart
