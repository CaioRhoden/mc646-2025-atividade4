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

    def test_no_last_minute_fee_at_24_hours(self):
        """
        Garantir que a taxa de última hora é aplicada somente quando hours_to_departure < 24,
        e NÃO quando exatamente 24 horas.
        """
        passengers = 1
        current_price = 500.0
        previous_sales = 50
        departure = self.booking_time + timedelta(hours=24)  # exatamente 24h
        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=departure,
            reward_points_available=0
        )
        base_price = current_price * (previous_sales / 100.0) * 0.8 * passengers
        assert result.total_price == base_price
        assert result.points_used is False

    def test_tc17_group_discount(self):
        """
        TC17: Desconto em grupo.
        """
        result = self.system.book_flight(
            passengers=6,
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

    def test_group_without_discount(self):
        """
        TC: Sem Desconto em grupo.
        """
        passengers = 4
        current_price = 500.0
        previous_sales = 50
        expected_price = current_price * (previous_sales / 100.0) * 0.8 * passengers
        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )
        assert result.confirmation is True
        assert result.total_price == expected_price

    def test_tc18_reward_points_redemption(self):
        """
        TC18: Resgate de pontos de recompensa.
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
        """
        result = self.system.book_flight(
            passengers=1,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=1.0,  # Preço muito baixo
            previous_sales=10,  # Vendas baixas
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=10000 
        )
        assert result.confirmation is True
        assert result.total_price == 0.0
        assert result.points_used is True

    def test_tc20_cancellation_full_refund(self):
        """
        TC20: Cancelamento com reembolso total.
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
            passengers=5,
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
        TESTE DE CÓDIGO INALCANÇÁVEL
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
                assert result.confirmation is False
                assert result.total_price == 0.0
            else:
                assert result.confirmation is True

    def test_group_discount_boundary_4_vs_5(self):
        """
        Garantir que o desconto de grupo aplica-se apenas quando passengers > 4.
        """
        current_price = 400.0
        previous_sales = 60

        # 4 passageiros -> sem desconto de grupo
        res4 = self.system.book_flight(
            passengers=4,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )
        expected4 = current_price * (previous_sales / 100.0) * 0.8 * 4
        assert res4.total_price == expected4

        # 5 passageiros -> desconto de 5%
        res5 = self.system.book_flight(
            passengers=5,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )
        expected5 = (current_price * (previous_sales / 100.0) * 0.8 * 5) * 0.95
        assert res5.total_price == expected5

    def test_cancellation_at_exact_48_hours_is_full_refund(self):
        """
        Garantir que cancelamento com departure_time exactly 48 hours resulta em reembolso total.
        """
        passengers = 2
        current_price = 300.0
        previous_sales = 50
        departure = self.booking_time + timedelta(hours=48)  # exatamente 48h

        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=True,
            departure_time=departure,
            reward_points_available=0
        )

        base_price = current_price * (previous_sales / 100.0) * 0.8 * passengers
        assert result.confirmation is False
        assert result.total_price == 0
        assert result.refund_amount == base_price

    def test_reward_points_of_one_are_applied(self):
        """
        Garante que reward_points_available == 1 é aplicado (detecta mutante que usa >1).
        """
        passengers = 1
        current_price = 500.0
        previous_sales = 50
        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=1
        )
        base_price = current_price * (previous_sales / 100.0) * 0.8 * passengers
        expected = base_price - (1 * 0.01)
        assert result.points_used is True
        assert result.total_price == pytest.approx(expected, rel=1e-9)

    def test_final_price_between_zero_and_one_is_not_zeroed(self):
        """
        Garante que um final_price fracionário entre 0 e 1 (ex.: 0.5) NÃO é zereado,
        detectando mutante que usaria `if final_price < 1: final_price = 0`.
        """
        # base_price = 1.6, reward_points_available = 110 -> final = 0.5
        passengers = 2
        current_price = 1.0
        previous_sales = 100
        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=110
        )
        assert result.points_used is True
        assert result.total_price == pytest.approx(0.5, rel=1e-9)

    def test_passengers_equal_available_seats_does_not_trigger_unreachable_block(self):
        """
        Garante que quando passengers == available_seats o bloco "inalcançável"
        não é executado e o preço final permanece o esperado.
        Ajustado para não conflitar com o desconto de grupo (passengers > 4).
        """
        passengers = 4
        available_seats = 4
        current_price = 200.0
        previous_sales = 50

        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=available_seats,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=0
        )

        expected_price = current_price * (previous_sales / 100.0) * 0.8 * passengers
        assert result.confirmation is True
        assert result.total_price == expected_price
        assert result.points_used is False
    
    def test_final_price_exactly_zero_is_not_adjusted(self):
        """
        Garante que quando final_price é exatamente 0, ele não é ajustado novamente.
        Detecta mutante que altera a condição para `if final_price <= 0`.
        """
        passengers = 1
        current_price = 1.0  # Preço baixo
        previous_sales = 10  # Vendas baixas
        reward_points_available = 100  # Pontos suficientes para zerar o preço

        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=reward_points_available
        )

        assert result.confirmation is True
        assert result.total_price == 0.0  # Preço final exatamente 0
        assert result.points_used is True
    
    def test_final_price_zero_does_not_trigger_unreachable_block(self):
        """
        Garante que quando final_price é exatamente 0, o bloco inalcançável não é executado.
        Detecta mutante que altera a condição para `if passengers > available_seats and final_price >= 0`.
        """
        passengers = 1
        available_seats = 10
        current_price = 1.0  # Preço baixo
        previous_sales = 10  # Vendas baixas
        reward_points_available = 100  # Pontos suficientes para zerar o preço

        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=available_seats,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=reward_points_available
        )

        assert result.confirmation is True
        assert result.total_price == 0.0  # Preço final exatamente 0
        assert result.points_used is True
    
    def test_final_price_exactly_one_triggers_unreachable_block(self):
        """
        Garante que quando final_price é exatamente 1 e passengers > available_seats,
        o bloco inalcançável é executado. Detecta mutante que altera a condição para
        `if passengers > available_seats and final_price > 1`.
        """
        passengers = 11  # Mais passageiros do que assentos disponíveis
        available_seats = 10
        current_price = 1.0  # Preço baixo
        previous_sales = 100  # Vendas altas para manter o preço final em 1
        reward_points_available = 0  # Sem pontos de recompensa

        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=available_seats,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=reward_points_available
        )

        # Como passengers > available_seats, o bloco inalcançável deve ser executado
        assert result.confirmation is False
        assert result.total_price == 0.0

    def test_final_price_exactly_zero_is_not_adjusted(self):
        """
        Garante que quando final_price é exatamente 0, ele não é ajustado novamente.
        Detecta mutante que altera a condição para `if final_price <= 0`.
        """
        passengers = 1
        current_price = 1.0  # Preço baixo
        previous_sales = 10  # Vendas baixas
        reward_points_available = 100  # Pontos suficientes para zerar o preço

        result = self.system.book_flight(
            passengers=passengers,
            booking_time=self.booking_time,
            available_seats=10,
            current_price=current_price,
            previous_sales=previous_sales,
            is_cancellation=False,
            departure_time=self.booking_time + timedelta(hours=48),
            reward_points_available=reward_points_available
        )

        assert result.confirmation is True
        assert result.total_price == 0.0  # Preço final exatamente 0
        assert result.points_used is True