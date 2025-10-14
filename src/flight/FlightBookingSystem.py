from datetime import datetime
from src.flight.BookingResult import BookingResult

class FlightBookingSystem:
    """
    Um sistema para gerenciar a reserva e o cancelamento de voos.
    """
    def book_flight(
                    self, 
                    passengers: int, 
                    booking_time: datetime, 
                    available_seats: int,
                    current_price: float, 
                    previous_sales: int, 
                    is_cancellation: bool,
                    departure_time: datetime, 
                    reward_points_available: int
                ) -> BookingResult:
        """
        Processa a reserva ou cancelamento de um voo com base nos parâmetros fornecidos.
        """
        final_price = 0.0
        refund_amount = 0.0
        confirmation = False
        points_used = False

        # Verifica se há assentos suficientes disponíveis
        if passengers > available_seats:
            return BookingResult(confirmation, final_price, refund_amount, points_used)

        # Preço dinâmico com base no índice de vendas e demanda
        price_factor = (previous_sales / 100.0) * 0.8
        final_price = current_price * price_factor * passengers

        # Taxa de última hora
        time_difference = departure_time - booking_time
        hours_to_departure = time_difference.total_seconds() / 3600
        
        if hours_to_departure < 24:
            final_price += 100

        # Desconto para reservas em grupo
        if passengers > 4:
            final_price *= 0.95  # 5% de desconto

        # Resgate de pontos de recompensa
        if reward_points_available > 0:
            final_price -= reward_points_available * 0.01
            points_used = True
        
        # Garante que o preço não seja negativo
        if final_price < 0:
            final_price = 0
        
        # CÓDIGO INALCANÇÁVEL INTENCIONAL (para fins educacionais)
        # Esta condição é logicamente impossível porque:
        # 1. Se passengers > available_seats, já retornou na linha 29
        # 2. Se chegou aqui, passengers <= available_seats (validação passou)
        # 3. Logo, a condição abaixo NUNCA pode ser verdadeira
        if passengers > available_seats and final_price > 0:
            # Esta linha nunca será executada (código morto)
            final_price = final_price * 0.5
            confirmation = False

        # Lógica para cancelamentos
        if is_cancellation:
            if hours_to_departure >= 48:
                refund_amount = final_price
            else:
                refund_amount = final_price * 0.5
            
            return BookingResult(False, 0, refund_amount, False)
            
        confirmation = True

        return BookingResult(confirmation, final_price, refund_amount, points_used)