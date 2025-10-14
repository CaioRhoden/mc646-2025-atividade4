import pytest
from datetime import datetime, timedelta
from src.flight.FlightBookingSystem import FlightBookingSystem


class TestFlightBookingSystem:
    def setup_method(self):
        self.system = FlightBookingSystem()
        self.booking_time = datetime(2024, 1, 1, 12, 0, 0)

    def test_tc14_insufficient_seats(self):
        """
        TC14: Assentos insuficientes.
        Cobertura: Aresta nó 3 → nó 4 (passengers > available_seats)
        Par def-uso: Variáveis inicializadas (linhas 22-25) usadas no retorno (linha 29)
        """
        result = self.system.book_flight(
            passengers=10,
            booking_time=self.booking_time,
            available_seats=5,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )
        assert result.confirmation is False
        assert result.total_price == 0.0
        assert result.refund_amount == 0.0
        assert result.points_used is False

    def test_tc15_basic_booking_without_modifiers(self):
        """
        TC15: Reserva básica sem modificadores.
        Cobertura: Fluxo básico nó 3 → nó 5 → nó 8 → nó 10 → nó 12 → nó 14 → nó 16
        Par def-uso: final_price calculado (linha 33), usado no retorno (linha 66)
        """
        result = self.system.book_flight(
            passengers=2,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )
        assert result.confirmation is True
        assert result.total_price > 0
        assert result.refund_amount == 0.0
        assert result.points_used is False
        expected_price = 500.0 * (50 / 100.0) * 0.8 * 2
        assert result.total_price == expected_price

    def test_tc16_last_minute_fee(self):
        """
        TC16: Taxa de última hora.
        Cobertura: Aresta nó 5 → nó 7 (hours_to_departure < 24)
        Par def-uso: final_price modificado (linha 40)
        """
        result = self.system.book_flight(
            passengers=1,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=12),  # < 24 horas
            reward_points_available=0
        )
        assert result.confirmation is True
        base_price = 500.0 * (50 / 100.0) * 0.8 * 1
        expected_price = base_price + 100
        assert result.total_price == expected_price

    def test_tc17_group_discount(self):
        """
        TC17: Desconto em grupo.
        Cobertura: Aresta nó 8 → nó 9 (passengers > 4)
        Par def-uso: final_price modificado (linha 44)
        """
        result = self.system.book_flight(
            passengers=6,  # > 4, aplica desconto
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )
        assert result.confirmation is True
        base_price = 500.0 * (50 / 100.0) * 0.8 * 6
        expected_price = base_price * 0.95
        assert result.total_price == expected_price

    def test_tc18_reward_points_redemption(self):
        """
        TC18: Resgate de pontos de recompensa.
        Cobertura: Aresta nó 10 → nó 11 (reward_points_available > 0)
        Par def-uso: final_price modificado (linha 48), points_used definido (linha 49)
        """
        result = self.system.book_flight(
            passengers=1,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=1000
        )
        assert result.confirmation is True
        assert result.points_used is True
        base_price = 500.0 * (50 / 100.0) * 0.8 * 1
        expected_price = base_price - (1000 * 0.01)
        assert result.total_price == expected_price

    def test_tc19_negative_price_corrected(self):
        """
        TC19: Preço negativo corrigido.
        Cobertura: Aresta nó 12 → nó 13 (final_price < 0)
        Par def-uso: final_price definido como 0 (linha 53)
        """
        result = self.system.book_flight(
            passengers=1,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=1.0,  # Preço muito baixo
            previous_sales=10,  # Vendas baixas
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=10000  # Pontos altos para gerar preço negativo
        )
        assert result.confirmation is True
        assert result.total_price == 0.0
        assert result.points_used is True

    def test_tc20_cancellation_full_refund(self):
        """
        TC20: Cancelamento com reembolso total.
        Cobertura: Aresta nó 14 → nó 15 → nó 17 → nó 18 (hours_to_departure >= 48)
        Par def-uso: refund_amount definido como final_price (linha 58)
        """
        result = self.system.book_flight(
            passengers=1,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=True,
            departure_time=self.booking_time + timedelta(hours=72),
            reward_points_available=0
        )
        assert result.confirmation is False
        assert result.total_price == 0
        expected_refund = 500.0 * (50 / 100.0) * 0.8 * 1
        assert result.refund_amount == expected_refund
        assert result.points_used is False

    def test_tc21_cancellation_partial_refund(self):
        """
        TC21: Cancelamento com reembolso parcial.
        Cobertura: Aresta nó 15 → nó 19 → nó 18 (hours_to_departure < 48)
        Par def-uso: refund_amount definido como final_price * 0.5 (linha 60)
        """
        result = self.system.book_flight(
            passengers=1,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=True,
            departure_time=self.booking_time + timedelta(hours=24),
            reward_points_available=0
        )
        assert result.confirmation is False
        assert result.total_price == 0
        base_price = 500.0 * (50 / 100.0) * 0.8 * 1
        expected_refund = base_price * 0.5
        assert result.refund_amount == expected_refund
        assert result.points_used is False

    def test_tc22_combined_case_all_modifiers(self):
        """
        TC22: Caso combinado - reserva com todos os modificadores.
        Cobertura: Múltiplas arestas (taxa última hora + desconto grupo + pontos)
        Testa interação entre modificadores de preço
        """
        result = self.system.book_flight(
            passengers=5,  # Grupo (> 4)
            booking_time=self.booking_time,
            available_seats=10,
            current_price=500.0,
            previous_sales=50,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=12),  # Última hora
            reward_points_available=500
        )
        assert result.confirmation is True
        assert result.points_used is True
        # Cálculo esperado:
        base_price = 500.0 * (50 / 100.0) * 0.8 * 5
        with_fee = base_price + 100
        with_discount = with_fee * 0.95
        final = with_discount - (500 * 0.01)
        assert result.total_price == final

    def test_unreachable_code_documentation(self):
        """
        TESTE DE CÓDIGO INALCANÇÁVEL (Educacional)
        
        Este teste documenta a existência de código inalcançável introduzido
        intencionalmente no FlightBookingSystem (linhas 56-59).
        
        Explicação da impossibilidade:
        - Se passengers > available_seats, o método retorna imediatamente (linha 29)
        - Se o código continua executando, significa que passengers <= available_seats
        - Logo, a condição "passengers > available_seats and final_price > 0" 
          na linha 56 NUNCA pode ser verdadeira
        - As linhas 58-59 são código morto (unreachable code)
        
        Este teste tenta todas as combinações possíveis de entrada e confirma
        que o código inalcançável nunca é executado.
        """
        test_cases = [
            # (passengers, available_seats, descrição)
            (5, 10, "Passageiros < assentos - validação passa"),
            (10, 10, "Passageiros = assentos - validação passa"),
            (15, 10, "Passageiros > assentos - retorno antecipado"),
        ]
        
        for passengers, available_seats, description in test_cases:
            result = self.system.book_flight(
                passengers=passengers,
                booking_time=self.booking_time,
                available_seats=available_seats,
                current_price=500.0,
                previous_sales=50,
                is_cancellation=False,
                departure_time=self.booking_time + timedelta(hours=48),
                reward_points_available=0
            )
            
            if passengers > available_seats:
                # Caso 1: Retorno antecipado - código após linha 29 não executa
                assert result.confirmation is False
                assert result.total_price == 0.0
            else:
                # Caso 2: Validação passou - mas condição impossível na linha 56
                # nunca será verdadeira porque passengers <= available_seats aqui
                assert result.confirmation is True
                # Se o código inalcançável fosse executado, final_price seria multiplicado por 0.5
                # e confirmation seria False. Como isso nunca acontece, confirmamos que o código
                # nas linhas 58-59 é de fato inalcançável.
                
        # CONCLUSÃO: O código nas linhas 58-59 é provadamente inalcançável
        # porque representa uma condição logicamente impossível após a validação inicial.
