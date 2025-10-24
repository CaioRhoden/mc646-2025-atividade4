import pytest
from datetime import datetime, timedelta
from src.fraud.FraudDetectionSystem import FraudDetectionSystem
from src.fraud.Transaction import Transaction


class TestFraudDetectionSystem:
    def setup_method(self):
        self.system = FraudDetectionSystem()
        self.base_time = datetime(2024, 1, 1, 12, 0, 0)

    def test_normal_transaction_no_flags(self):
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

    def test_high_value_transaction(self):
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

    def test_recent_transactions_within_hour(self):
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
        assert result.is_fraudulent is False
        assert result.verification_required is False

    def test_old_transactions_not_counted(self):
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
        assert result.is_fraudulent is False
        assert result.verification_required is False

    def test_excessive_recent_transactions(self):
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=i),
                location="SP"
            )
            for i in range(5, 17)
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
        assert result.is_fraudulent is False
        assert result.verification_required is False

    def test_rapid_location_change(self):
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

    def test_location_change_sufficient_time(self):
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

    def test_blacklisted_location(self):
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

    def test_multiple_fraud_conditions_accumulate(self):
        previous_transactions = [
            Transaction(
                amount=100.0,
                timestamp=self.base_time - timedelta(minutes=i),
                location="São Paulo"
            )
            for i in range(5, 17)
        ]
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

    def test_edge_case_exact_10_transactions(self):
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

    def test_edge_case_exact_30_minutes(self):
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
        assert result.risk_score == 0

    def test_edge_case_exact_10000_amount(self):
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
        assert result.is_blocked is False

    def test_amount_exact_10001_should_be_flagged(self):
        current_transaction = Transaction(
            amount=10001.0,
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

    def test_61_minutes_old_transaction_not_counted_towards_recent_limit(self):
        previous_transactions = [
            Transaction(amount=10.0, timestamp=self.base_time - timedelta(minutes=i), location="SP")
            for i in range(1, 11)
        ]
        previous_transactions.append(
            Transaction(amount=10.0, timestamp=self.base_time - timedelta(minutes=61), location="SP")
        )
        current_transaction = Transaction(amount=5.0, timestamp=self.base_time, location="SP")
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_blocked is False
        assert result.risk_score == 0

    def test_60_minutes_exact_is_counted_towards_recent_limit(self):
        previous_transactions = [
            Transaction(amount=10.0, timestamp=self.base_time - timedelta(minutes=i), location="SP")
            for i in range(1, 11)
        ]
        previous_transactions.append(
            Transaction(amount=10.0, timestamp=self.base_time - timedelta(minutes=60), location="SP")
        )
        current_transaction = Transaction(amount=5.0, timestamp=self.base_time, location="SP")
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.is_blocked is True
        assert result.risk_score == 30

    def test_high_amount_accumulates_with_prior_recent_risk(self):
        previous_transactions = [
            Transaction(
                amount=10.0,
                timestamp=self.base_time - timedelta(minutes=i),
                location="SP"
            ) for i in range(1, 12)
        ]
        current_transaction = Transaction(
            amount=15000.0,
            timestamp=self.base_time,
            location="SP"
        )
        result = self.system.check_for_fraud(
            current_transaction=current_transaction,
            previous_transactions=previous_transactions,
            blacklisted_locations=[]
        )
        assert result.risk_score == 80
    
        self.system = FraudDetectionSystem()
        self.base_time = datetime(2024, 1, 1, 12, 0, 0)

    def test_risk_is_exactly_50_for_high_value_transaction(self):
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
        assert result.risk_score == 50
        assert result.is_fraudulent is True
        assert result.verification_required is True
