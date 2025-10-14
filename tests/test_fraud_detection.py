import pytest
from datetime import datetime, timedelta
from src.fraud.FraudDetectionSystem import FraudDetectionSystem
from src.fraud.Transaction import Transaction


class TestFraudDetectionSystem:
    def setup_method(self):
        self.system = FraudDetectionSystem()
        self.base_time = datetime(2024, 1, 1, 12, 0, 0)

    def test_tc23_normal_transaction_no_flags(self):
        """
        TC23: Transação normal sem flags de fraude.
        Cobertura: Caminho completo sem ativar nenhuma condição de fraude
        Arestas: nó 3 → nó 5 → nó 6 → nó 8 → nó 12 → nó 14 → nó 18
        Par def-uso: Todas variáveis inicializadas (linhas 16-19), usadas no retorno (linha 55)
        """
        current_transaction = Transaction(
            amount=1000.0,
            timestamp=self.base_time,
            location="São Paulo"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=[],
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is False
        assert result.is_blocked is False
        assert result.verification_required is False
        assert result.risk_score == 0

    def test_tc24_high_value_transaction(self):
        """
        TC24: Transação de alto valor.
        Cobertura: Aresta nó 3 → nó 4 (current_transaction.amount > 10000)
        Par def-uso: is_fraudulent definido True (linha 23), verification_required (linha 24),
                     risk_score incrementado (linha 25)
        """
        current_transaction = Transaction(
            amount=15000.0,
            timestamp=self.base_time,
            location="São Paulo"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=[],
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is True
        assert result.verification_required is True
        assert result.risk_score == 50

    def test_tc25_recent_transactions_within_hour(self):
        """
        TC25: Transações recentes dentro da última hora.
        Cobertura: Aresta nó 6 → nó 7 → nó 9 (time_diff_minutes <= 60)
        Par def-uso: recent_transaction_count incrementado (linha 33)
        """
        previous_transactions = [
            Transaction(amount=100.0, timestamp=self.base_time - timedelta(minutes=30), location="SP"),
            Transaction(amount=200.0, timestamp=self.base_time - timedelta(minutes=45), location="SP"),
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="SP"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_blocked is False
        assert result.risk_score == 0

    def test_tc26_old_transactions_not_counted(self):
        """
        TC26: Transações antigas não contadas.
        Cobertura: Aresta nó 7 → nó 6 (time_diff_minutes > 60, não incrementa)
        """
        previous_transactions = [
            Transaction(amount=100.0, timestamp=self.base_time - timedelta(hours=2), location="SP"),
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="SP"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_blocked is False
        assert result.risk_score == 0

    def test_tc27_excessive_recent_transactions(self):
        """
        TC27: Excesso de transações recentes.
        Cobertura: Aresta nó 8 → nó 11 (recent_transaction_count > 10)
        Par def-uso: is_blocked definido True (linha 36), risk_score incrementado (linha 37)
        """
        # Cria 12 transações na última hora
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=i),
                location="SP"
            )
            for i in range(5, 17)  # 12 transações
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="SP"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_blocked is True
        assert result.risk_score == 30

    def test_tc28_rapid_location_change(self):
        """
        TC28: Mudança rápida de localização.
        Cobertura: Aresta nó 12 → nó 13 → nó 15 (minutes_since_last < 30 e locations diferentes)
        Par def-uso: is_fraudulent True (linha 46),
                     verification_required True (linha 47),
                     risk_score incrementado (linha 48)
        """
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=10),
                location="São Paulo"
            )
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="Rio de Janeiro"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is True
        assert result.verification_required is True
        assert result.risk_score == 20

    def test_tc29_location_change_sufficient_time(self):
        """
        TC29: Mudança de localização OK (tempo suficiente).
        Cobertura: Aresta nó 13 → nó 14 (minutes_since_last >= 30)
        """
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(hours=1),
                location="São Paulo"
            )
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="Rio de Janeiro"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is False
        assert result.verification_required is False
        assert result.risk_score == 0

    def test_tc30_same_location_short_period(self):
        """
        TC30: Mesma localização em curto período.
        Cobertura: Aresta nó 13 → nó 14 (last_transaction.location == current_transaction.location)
        """
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=10),
                location="São Paulo"
            )
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="São Paulo"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is False
        assert result.verification_required is False
        assert result.risk_score == 0

    def test_tc31_blacklisted_location(self):
        """
        TC31: Localização em blacklist.
        Cobertura: Aresta nó 14 → nó 17 → nó 18 (location in blacklisted_locations)
        Par def-uso: is_blocked True (linha 52), risk_score = 100 (linha 53)
        """
        current_transaction = Transaction(
            amount=1000.0,
            timestamp=self.base_time,
            location="País Bloqueado"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=[],
            blacklisted_locations=["País Bloqueado"]
        )
        assert result.is_blocked is True
        assert result.risk_score == 100

    def test_tc32_multiple_fraud_conditions(self):
        """
        TC32: Múltiplas condições de fraude.
        Cobertura: Múltiplas arestas de fraude ativadas
        Testa acumulação de risk_score de diferentes fontes
        """
        # Cria 12 transações na última hora para exceder limite
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=i),
                location="São Paulo"
            )
            for i in range(5, 17)
        ]
        # Adiciona transação recente em localização diferente
        previous_transactions.append(
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=5),
                location="Curitiba"
            )
        )
        current_transaction = Transaction(
            amount=15000.0,
            timestamp=self.base_time,
            location="Porto Alegre"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is True
        assert result.is_blocked is True
        assert result.verification_required is True
        assert result.risk_score == 100  # 50 + 30 + 20

    def test_tc33_edge_case_exact_10_transactions(self):
        """
        TC33: Caso limite - exatamente 10 transações.
        Cobertura: Teste de condição de borda (recent_transaction_count == 10)
        """
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=i),
                location="SP"
            )
            for i in range(1, 11)
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="SP"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_blocked is False

    def test_tc34_edge_case_exact_30_minutes(self):
        """
        TC34: Caso limite - exatamente 30 minutos de diferença.
        Cobertura: Teste de condição de borda (minutes_since_last == 30)
        """
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=30),
                location="São Paulo"
            )
        ]
        current_transaction = Transaction(
            amount=300.0,
            timestamp=self.base_time,
            location="Rio de Janeiro"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is False
        assert result.verification_required is False

    def test_tc35_edge_case_exact_10000_amount(self):
        """
        TC35: Caso limite - valor exatamente 10000.
        Cobertura: Teste de condição de borda (amount == 10000)
        """
        current_transaction = Transaction(
            amount=10000.0,
            timestamp=self.base_time,
            location="São Paulo"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=[],
            blacklisted_locations=[]
        )
        assert result.is_fraudulent is False
        assert result.verification_required is False
        assert result.risk_score == 0
