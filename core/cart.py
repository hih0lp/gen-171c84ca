# Корзина не требуется для MVP, но оставлю заглушку для совместимости с context_processors
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})
        self.cart = cart
    
    def __len__(self):
        return 0