# AgentsWith

Types:

```python
from magebank.types import Agent
```

Methods:

- <code title="get /agentsWith/{id}">client.agents_with.<a href="./src/magebank/resources/agents_with.py">retrieve</a>(id) -> <a href="./src/magebank/types/agent.py">Agent</a></code>

# Agents

Types:

```python
from magebank.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentDepositResponse,
    AgentWithdrawResponse,
)
```

Methods:

- <code title="post /agents/create">client.agents.<a href="./src/magebank/resources/agents.py">create</a>(\*\*<a href="src/magebank/types/agent_create_params.py">params</a>) -> <a href="./src/magebank/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /agents/{id}">client.agents.<a href="./src/magebank/resources/agents.py">retrieve</a>(id) -> <a href="./src/magebank/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="post /agents/deposit">client.agents.<a href="./src/magebank/resources/agents.py">deposit</a>(\*\*<a href="src/magebank/types/agent_deposit_params.py">params</a>) -> <a href="./src/magebank/types/agent_deposit_response.py">AgentDepositResponse</a></code>
- <code title="post /agents/withdraw">client.agents.<a href="./src/magebank/resources/agents.py">withdraw</a>(\*\*<a href="src/magebank/types/agent_withdraw_params.py">params</a>) -> <a href="./src/magebank/types/agent_withdraw_response.py">AgentWithdrawResponse</a></code>

# Savings

Types:

```python
from magebank.types import (
    SavingDepositResponse,
    SavingListInvestmentsResponse,
    SavingListInvestmentsByAgentResponse,
    SavingRetrieveDashboardResponse,
    SavingWithdrawResponse,
)
```

Methods:

- <code title="post /savings/deposit">client.savings.<a href="./src/magebank/resources/savings.py">deposit</a>(\*\*<a href="src/magebank/types/saving_deposit_params.py">params</a>) -> <a href="./src/magebank/types/saving_deposit_response.py">SavingDepositResponse</a></code>
- <code title="get /savings/myinvestments">client.savings.<a href="./src/magebank/resources/savings.py">list_investments</a>() -> <a href="./src/magebank/types/saving_list_investments_response.py">SavingListInvestmentsResponse</a></code>
- <code title="get /savings/{agentId}">client.savings.<a href="./src/magebank/resources/savings.py">list_investments_by_agent</a>(agent_id) -> <a href="./src/magebank/types/saving_list_investments_by_agent_response.py">SavingListInvestmentsByAgentResponse</a></code>
- <code title="get /savings/dashboard">client.savings.<a href="./src/magebank/resources/savings.py">retrieve_dashboard</a>() -> <a href="./src/magebank/types/saving_retrieve_dashboard_response.py">SavingRetrieveDashboardResponse</a></code>
- <code title="post /savings/withdraw">client.savings.<a href="./src/magebank/resources/savings.py">withdraw</a>(\*\*<a href="src/magebank/types/saving_withdraw_params.py">params</a>) -> <a href="./src/magebank/types/saving_withdraw_response.py">SavingWithdrawResponse</a></code>

# Payments

Types:

```python
from magebank.types import (
    Payment,
    PaymentApproveResponse,
    PaymentDeclineResponse,
    PaymentRegisterResponse,
)
```

Methods:

- <code title="get /payments/{id}">client.payments.<a href="./src/magebank/resources/payments.py">retrieve</a>(id) -> <a href="./src/magebank/types/payment.py">Payment</a></code>
- <code title="post /payments/setApprove">client.payments.<a href="./src/magebank/resources/payments.py">approve</a>(\*\*<a href="src/magebank/types/payment_approve_params.py">params</a>) -> <a href="./src/magebank/types/payment_approve_response.py">PaymentApproveResponse</a></code>
- <code title="post /payments/setDecline">client.payments.<a href="./src/magebank/resources/payments.py">decline</a>(\*\*<a href="src/magebank/types/payment_decline_params.py">params</a>) -> <a href="./src/magebank/types/payment_decline_response.py">PaymentDeclineResponse</a></code>
- <code title="post /payments/register">client.payments.<a href="./src/magebank/resources/payments.py">register</a>(\*\*<a href="src/magebank/types/payment_register_params.py">params</a>) -> <a href="./src/magebank/types/payment_register_response.py">PaymentRegisterResponse</a></code>

# User

Types:

```python
from magebank.types import UserListPaymentsResponse, UserRetrieveWalletBalanceResponse
```

Methods:

- <code title="get /user/payments">client.user.<a href="./src/magebank/resources/user.py">list_payments</a>(\*\*<a href="src/magebank/types/user_list_payments_params.py">params</a>) -> <a href="./src/magebank/types/user_list_payments_response.py">UserListPaymentsResponse</a></code>
- <code title="get /user/wallet-balance">client.user.<a href="./src/magebank/resources/user.py">retrieve_wallet_balance</a>() -> <a href="./src/magebank/types/user_retrieve_wallet_balance_response.py">UserRetrieveWalletBalanceResponse</a></code>
