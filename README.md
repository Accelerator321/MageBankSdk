

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Async Usage](#async-usage)
- [API Methods & Examples](#api-methods--examples)
  - [Agent Operations](#agent-operations)
    - [Retrieve agent by ID](#retrieve-agent-by-id)
    - [Create a new agent](#create-a-new-agent)
    - [Deposit funds into agent](#deposit-funds-into-agent)
    - [Withdraw funds from agent](#withdraw-funds-from-agent)
  - [Payment Operations](#payment-operations)
    - [Approve a payment](#approve-a-payment)
    - [Decline a payment](#decline-a-payment)
    - [Export payment data](#export-payment-data)
    - [Register a new payment](#register-a-new-payment)
    - [List user payments](#list-user-payments)
    - [Retrieve payment details](#retrieve-payment-details)
  - [Savings Operations](#savings-operations)
    - [Create savings deposit](#create-savings-deposit)
    - [Withdraw from savings](#withdraw-from-savings)
    - [List all investments](#list-all-investments)
    - [List investments by agent](#list-investments-by-agent)
    - [Retrieve savings dashboard](#retrieve-savings-dashboard)
  - [Investment Operations](#investment-operations)
    - [Calculate interest](#calculate-interest)
    - [Retrieve current interest rate](#retrieve-current-interest-rate)
  - [User Operations](#user-operations)
    - [Retrieve wallet balance](#retrieve-wallet-balance)
  - [Transaction Operations](#transaction-operations)
    - [Get summary of transactions](#get-summary-of-transactions)
- [Available Response Types](#available-response-types)
- [Nested params](#nested-params)
- [Handling errors](#handling-errors)
- [Advanced](#advanced)
- [Versioning](#versioning)
- [Requirements](#requirements)
- [Contributing](#contributing)

## Documentation

The full API of this library can be found in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install --pre magebank
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from magebank import Magebank

mage = Magebank(
    api_key=os.environ.get("MAGEBANK_API_KEY"),
)

agent = mage.agents_with.retrieve("REPLACE_ME")
print(agent.id)
```

While you can provide a `auth_token` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `MAGEBANK_AUTH_TOKENOptional environment variable="My Auth Token"` to your `.env` file
so that your Auth Token is not stored in source control.

## Async usage

Simply import `AsyncMagebank` instead of `Magebank` and use `await` with each API call:

```python
import os
import asyncio
from magebank import AsyncMagebank

mage = AsyncMagebank(
    api_key=os.environ.get("MAGEBANK_API_KEY"),
)


async def main() -> None:
    agent = await mage.agents_with.retrieve("REPLACE_ME")
    print(agent.id)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## API Methods & Examples

### Agent Operations

#### Retrieve agent by ID
```python
agent = mage.agents_with.retrieve("agent_12345")
print(f"Agent Name: {agent.name}, Balance: {agent.balance} {agent.currency}")

# Convert to dictionary for easier manipulation
agent_dict = agent.to_dict()
print(agent_dict)
```

**Parameters:**
- **Required:**
  - `id` (string) - The unique identifier of the agent

**Response Schema:**
```python
{
    "id": "agent_k77NTwxp2Ym3JCmVsKtXQA",
    "name": "Payment Assistant",
    "description": "Handles payment processing for customer support",
    "status": "active",
    "walletAddress": "WalletAddress{ addressId: '0x9d20dE668c8F9fb431cf6D6BBA48ee60Fe8E2BAB', networkId: 'base-sepolia', walletId: '07f490dc-34e3-447f-9972-df2778fcb3c3' }",
    "balance": "100",
    "currency": "USDC",
    "paymentRules": {
        "dailyLimit": 1000,
        "transactionLimit": 100,
        "requireApprovalForAll": false,
        "requireApprovalAboveAmount": 50
    },
    "tags": ["customer-support", "payments"],
    "created": "2025-04-15T11:00:08.432269+00:00"
}
```

#### Create a new agent
```python
new_agent = mage.agents.create(
    name="Business Expense Account",
    userid="user_12345",
    balance=1000.00,
    currency="USD",
    dailylimit=200.00,
    description="Expense account for marketing team",
    requireapprovalaboveamount=500.00,
    requireapprovalforall=False,
    tags=["marketing", "expenses"],
    transactionlimit=2000.00,
    walletaddress="wallet_xyz123"
)
print(f"Created agent with ID: {new_agent.id}")

# Convert response to dictionary
agent_data = new_agent.to_dict()
print(f"Full agent data: {agent_data}")
```

**Parameters:**
- **Required:**
  - `name` (string) - Name of the agent
  - `userid` (string) - User ID associated with the agent
- **Optional:**
  - `balance` (number) - Initial balance for the agent
  - `currency` (string) - Currency type (e.g., "USD")
  - `dailylimit` (number) - Daily spending limit
  - `description` (string) - Description of the agent's purpose
  - `requireapprovalaboveamount` (number) - Amount above which approval is required
  - `requireapprovalforall` (boolean) - Whether all transactions require approval
  - `tags` (array of strings) - Tags for categorization
  - `transactionlimit` (number) - Maximum transaction amount
  - `walletaddress` (string) - Associated wallet address

**Response Schema:**
```python
{
    "id": "agent_bRSEFnMRD1fvkMM39hzPdM",
    "apikey": "mag_eJwVyN0OgiAYANA3cprT1qV_tY8E0jCVuyILSMtNG-LTt87l6SySt4NQVCGoVvCIggneZSASCOE1NpcE7ZzOopH_Q1c-12A4K4e8zgxnMJM0sjjxFE3xJmc4wDUsre4lGUpJzzDB0Mt7AiFmwiUaAppin1ijeCMN6M9C1mKD12ihTPiPwjkNZXQPme6DbGlNBc9aPfcCbb_dMRb2MbE-vqIKzdgtfgVGPxc",
    "name": "Payment Assistant",
    "description": "Handles payment processing for customer support",
    "status": "active",
    "walletAddress": {
        "addressId": "",
        "networkId": "base-sepolia",
        "walletId": ""
    },
    "balance": "6",
    "currency": "USDC",
    "paymentRules": {
        "dailyLimit": 1000,
        "transactionLimit": 100,
        "requireApprovalAboveAmount": 50,
        "requireApprovalForAll": false
    },
    "tags": ["customer-support", "payments"],
    "created": "2025-05-03T18:52:39.911685+00:00",
    "transferResult": {
        "success": true,
        "txHash": "0x123...abc",
        "message": "Successfully transferred 6 USDC from user to agent wallet"
    },
    "faucetTransaction": {
        "success": true,
        "txHash": "0xabc...123",
        "message": "ETH testnet funds received via faucet"
    }
}
```

#### Deposit funds into agent
```python
deposit = mage.agents.deposit(
    agentid="agent_12345",
    amount=500.00,
    userid="user_12345",
    currency="USD"
)
print(f"Deposit successful: {deposit.id}, New balance: {deposit.new_balance}")

# Access response data as dictionary
deposit_data = deposit.to_dict()
print(f"Transaction hash: {deposit_data['txHash']}")
```

**Parameters:**
- **Required:**
  - `agentid` (string) - ID of the agent to deposit into
  - `amount` (number) - Amount to deposit
  - `userid` (string) - ID of the user making the deposit
- **Optional:**
  - `currency` (string) - Currency of the deposit

**Response Schema:**
```python
{
    "success": true,
    "txHash": "0x123...abc",
    "message": "Successfully deposited 50 USDC to agent",
    "updatedBalance": "150"
}
```

#### Withdraw funds from agent
```python
withdrawal = mage.agents.withdraw(
    agentid="agent_12345",
    amount=200.00,
    userid="user_12345",
    currency="USD"
)
print(f"Withdrawal successful: {withdrawal.id}, New balance: {withdrawal.new_balance}")

# Convert to dictionary for processing
withdrawal_data = withdrawal.to_dict()
if withdrawal_data['success']:
    print(f"Transaction completed: {withdrawal_data['message']}")
```

**Parameters:**
- **Required:**
  - `agentid` (string) - ID of the agent to withdraw from
  - `amount` (number) - Amount to withdraw
  - `userid` (string) - ID of the user making the withdrawal
- **Optional:**
  - `currency` (string) - Currency of the withdrawal

**Response Schema:**
```python
{
    "success": true,
    "txHash": "0x123...abc",
    "message": "Successfully withdrew 50 USDC from agent to user",
    "updatedBalance": "50"
}
```

### Payment Operations

#### Approve a payment
```python
approval = mage.payments.set_approve(paymentId="payment_12345")
print(f"Payment approved: {approval.status}")

# Get response details as dictionary
approval_data = approval.to_dict()
print(f"Approval message: {approval_data['message']}")
```

**Parameters:**
- **Required:**
  - `paymentId` (string) - ID of the payment to approve

**Response Schema:**
```python
{
    "message": "Approval Status Done."
}
```

#### Decline a payment
```python
decline = mage.payments.set_decline(paymentId="payment_12345")
print(f"Payment declined: {decline.status}")

# Access full decline response
decline_data = decline.to_dict()
print(f"Status: {decline_data['status']}")
print(f"Message: {decline_data['message']}")
```

**Parameters:**
- **Required:**
  - `paymentId` (string) - ID of the payment to decline

**Response Schema:**
```python
{
    "message": "Payment declined successfully",
    "status": "Decline",
    "txHash": null
}
```

#### Export payment data
```python
from datetime import date

export = mage.payments.export(
    format="csv",
    dateRange={
        "start": date.fromisoformat("2025-01-01"),
        "end": date.fromisoformat("2025-04-30")
    }
)
print(f"Export generated: {export.url}")

# Get export details as dictionary
export_data = export.to_dict()
print(f"Export format: {export_data['format']}")
print(f"Download URL: {export_data['url']}")
```

**Parameters:**
- **Required:**
  - `format` (string) - Export format (e.g., "csv")
- **Optional:**
  - `dateRange` (object) - Date range for export
    - `start` (string) - Start date in ISO format
    - `end` (string) - End date in ISO format

**Response Schema:**
```python
{
    "url": "https://example.com/export/payments_2025-01-01_2025-04-30.csv",
    "format": "csv",
    "dateRange": {
        "start": "2025-01-01",
        "end": "2025-04-30"
    },
    "recordCount": 150
}
```

#### Register a new payment
```python
payment = mage.payments.register(
    name="Office Supplies Purchase",
    paymentdetails={
        "amount": 149.99,
        "currency": "USD",
        "method": "bank_transfer"
    },
    receiveragentid="agent_67890",
    senderagentid="agent_12345",
    contactdetails={
        "email": "accounting@example.com",
        "phoneNumber": "+15551234567"
    },
    tags=["office", "supplies"],
    type="expense"
)
print(f"Payment registered with ID: {payment.id}, Status: {payment.status}")

# Convert payment response to dictionary
payment_data = payment.to_dict()
print(f"Payment details: {payment_data}")
```

**Parameters:**
- **Required:**
  - `name` (string) - Name/description of the payment
  - `paymentdetails` (object) - Payment details
    - `amount` (number) - Payment amount
    - `currency` (string) - Payment currency
    - `method` (string) - Payment method
  - `receiveragentid` (string) - ID of the receiving agent
  - `senderagentid` (string) - ID of the sending agent
- **Optional:**
  - `contactdetails` (object) - Contact information
    - `email` (string) - Email address
    - `phoneNumber` (string) - Phone number
  - `tags` (array of strings) - Payment tags
  - `type` (string) - Type of payment

**Response Schema:**
```python
{
    "id": "payee_wDG5cavUCoK53uvFzTvkey",
    "name": "Vendor XYZ2",
    "type": "External",
    "status": "New",
    "createdat": "2025-04-17T10:28:18.512792",
    "approvalRequired": true
}
```

#### List user payments
```python
all_payments = mage.user.list_payments()
print(f"Found {len(all_payments.results)} payments")

approved_payments = mage.user.list_payments(approvalStatus="approved")
print(f"Found {len(approved_payments.results)} approved payments")

# Convert payments list to dictionary for processing
payments_data = all_payments.to_dict()
for payment in payments_data['results']:
    print(f"Payment {payment['id']}: {payment['direction']} - {payment['paymentdetails']['amount']} {payment['paymentdetails']['currency']}")
```

**Parameters:**
- **Optional:**
  - `approvalStatus` (string) - Filter by approval status

**Response Schema:**
```python
[
    {
        "id": "payee_8tJo7vZb1RKo4oeyWuqgK",
        "senderagentid": "agent_8tJo7vZb1RKo4oeyWuqgK",
        "receiveragentid": "agent_7tJo7vZb1RKo4oeyWuqgK",
        "initiatedBy": "Alice",
        "receivedBy": "Bob",
        "direction": "outgoing",
        "name": "Payment from Alice to Bob",
        "approvalstatus": "Approved",
        "createdat": "2025-04-07T12:00:00Z",
        "type": "EXTERNAL",
        "paymentdetails": {
            "method": "CRYPTO_ADDRESS",
            "amount": 100,
            "currency": "USDC"
        }
    }
]
```

#### Retrieve payment details
```python
payment = mage.payments.retrieve("payment_12345")
print(f"Payment: {payment.id}")
print(f"Status: {payment.status}")
print(f"Amount: {payment.amount} {payment.currency}")
print(f"Created: {payment.created_at}")

# Get full payment details as dictionary
payment_data = payment.to_dict()
print(f"Full payment data: {payment_data}")
```

**Parameters:**
- **Required:**
  - `id` (string) - ID of the payment to retrieve

**Response Schema:**
```python
{
    "id": "payee_wDG5cavUCoK53uvFzTvkey",
    "name": "Vendor XYZ Payment",
    "type": "EXTERNAL",
    "senderagentid": "agent_eC6ZezevNsqxvoKmQrUuoU",
    "receiveragentid": "agent_k77NTwxp2Ym3JCmVsKtXQA",
    "status": "New",
    "approvalstatus": "Approved, Declined, Pending, Waiting, Waiting for Sender Approval",
    "approvalrequired": true,
    "paymentdetails": {
        "method": "CRYPTO_ADDRESS",
        "amount": 6,
        "currency": "USDC"
    },
    "contactdetails": {
        "email": "contact@vendorxyz.com",
        "phoneNumber": "+1234567890"
    },
    "tags": ["vendor", "regular"],
    "createdat": "2025-04-17T10:28:18.512792+00:00",
    "approvedat": "2025-04-17T11:30:00.000000+00:00"
}
```

### Savings Operations

#### Create savings deposit
```python
deposit = mage.savings.deposit(
    agentId="agent_12345",
    amount=1000.00
)
print(f"Investment created: {deposit.investment_id}, APY: {deposit.apy}%")

# Get deposit response as dictionary
deposit_data = deposit.to_dict()
print(f"Success: {deposit_data['success']}")
print(f"Message: {deposit_data['message']}")
```

**Parameters:**
- **Required:**
  - `agentId` (string) - ID of the agent to deposit from
  - `amount` (number) - Amount to invest in savings

**Response Schema:**
```python
{
    "success": true,
    "message": "Successfully invested 0.5 USDC."
}
```

#### Withdraw from savings
```python
withdrawal = mage.savings.withdraw(investmentId="investment_12345")
print(f"Withdrawal successful: {withdrawal.amount} {withdrawal.currency}")

# Get withdrawal details as dictionary
withdrawal_data = withdrawal.to_dict()
print(f"Withdrawal status: {withdrawal_data['success']}")
print(f"Message: {withdrawal_data['message']}")
```

**Parameters:**
- **Required:**
  - `investmentId` (string) - ID of the investment to withdraw from

**Response Schema:**
```python
{
    "success": true,
    "message": "Withdrawal completed successfully."
}
```

#### List all investments
```python
investments = mage.savings.list_investments()
print(f"Total investments: {len(investments.investments)}")

# Convert to dictionary for detailed processing
investments_data = investments.to_dict()
for investment in investments_data['investments']:
    print(f"Investment ID: {investment['id']}, Amount: {investment['amount']} {investment['currency']}")
```

**Parameters:**
- None required

**Response Schema:**
```python
{
    "investments": [
        {
            "id": "inv_k77NTwxp2Ym3JCmVsKtXQA",
            "agent_id": "agent_k77NTwxp2Ym3JCmVsKtXQA",
            "amount": 1000,
            "invested_at": "2025-04-15T11:00:08.432269+00:00",
            "status": "active",
            "current_value": "1050.00",
            "interest_earned": "50.00"
        }
    ]
}
```

#### List investments by agent
```python
agent_investments = mage.savings.list_investments_by_agent(agent_id="agent_12345")
print(f"Agent has {len(agent_investments.investments)} investments")

# Convert response to dictionary
investments_data = agent_investments.to_dict()
for investment in investments_data['investments']:
    print(f"Investment ID: {investment['id']}, Amount: {investment['amount']} {investment['currency']}")
```

**Parameters:**
- **Required:**
  - `agent_id` (string) - ID of the agent to list investments for

**Response Schema:**
```python
{
    "investments": [
        {
            "id": "inv_k77NTwxp2Ym3JCmVsKtXQA",
            "agent_id": "agent_k77NTwxp2Ym3JCmVsKtXQA",
            "amount": 1000,
            "invested_at": "2025-04-15T11:00:08.432269+00:00",
            "status": "active",
            "current_value": "1050.00",
            "interest_earned": "50.00"
        }
    ]
}
```

#### Retrieve savings dashboard
```python
dashboard = mage.savings.retrieve_dashboard()
print(f"Total savings: {dashboard.total_savings} {dashboard.currency}")
print(f"Total interest earned: {dashboard.total_interest_earned} {dashboard.currency}")
print(f"Active investments: {dashboard.active_investments_count}")
```

**Parameters:**
- None required

### Investment Operations

#### Calculate interest
```python
interest_calculation = mage.investment.calculate_interest(
    amount=10000,
    term_months=12,
    currency="USD"
)
print(f"Calculated interest: {interest_calculation.interest}")
print(f"Total return: {interest_calculation.total_return}")
print(f"APY: {interest_calculation.apy}%")

# Get detailed calculation as dictionary
calculation_data = interest_calculation.to_dict()
print(f"Calculation steps: {calculation_data['calculation']['steps']}")
```

**Parameters:**
- **Required:**
  - `amount` (number) - Investment amount
  - `term_months` (number) - Investment term in months
- **Optional:**
  - `currency` (string) - Currency for the investment

**Response Schema:**
```python
{
    "principal": 1000,
    "days": 365,
    "interestRate": 4.5,
    "interestEarned": "45.00",
    "totalAmount": "1045.00",
    "annualYield": "4.50%",
    "calculation": {
        "formula": "principal × rate × (days ÷ 365)",
        "steps": [
            "1000 × 0.045 × 365/365",
            "1000 × 0.045 × 1.000000",
            "1000 × 0.045000",
            "45.000000"
        ]
    }
}
```

#### Retrieve current interest rate
```python
interest_rate = mage.investment.retrieve_interest_rate()
print(f"Current interest rate: {interest_rate.rate}%")
print(f"Minimum term: {interest_rate.min_term_months} months")
print(f"Maximum term: {interest_rate.max_term_months} months")

# Get interest rate details as dictionary
rate_data = interest_rate.to_dict()
print(f"Last updated: {rate_data['lastUpdated']}")
```

**Parameters:**
- None required

**Response Schema:**
```python
{
    "interestRate": 4.5,
    "lastUpdated": "2025-05-04T12:00:00.000Z"
}
```

### User Operations

#### Retrieve wallet balance
```python
wallet = mage.user.retrieve_wallet_balance()
print(f"Current balance: {wallet.balance} {wallet.currency}")
print(f"Available balance: {wallet.available_balance} {wallet.currency}")

# Get wallet details as dictionary
wallet_data = wallet.to_dict()
print(f"Balance source: {wallet_data['source']}")
print(f"Message: {wallet_data['message']}")
```

**Parameters:**
- None required

**Response Schema:**
```python
{
    "success": true,
    "balance": "100.50",
    "asset": "USDC",
    "message": "Balance retrieved successfully",
    "source": "blockchain"
}
```

### Transaction Operations

#### Get summary of transactions
```python
from datetime import date

summary = mage.transactions.retrieve_summary(
    start_date="2025-01-01",
    end_date="2025-04-30"
)
print(f"Total transactions: {summary.count}")
print(f"Total volume: {summary.volume} {summary.currency}")
print(f"Average transaction size: {summary.average}")

# Get complete summary as dictionary
summary_data = summary.to_dict()
print(f"Summary details: {summary_data}")
```

**Parameters:**
- **Required:**
  - `start_date` (string) - Start date for the summary period
  - `end_date` (string) - End date for the summary period

**Response Schema:**
```python
{
    "count": 150,
    "volume": "15000.00",
    "currency": "USDC",
    "average": "100.00",
    "period": {
        "start": "2025-01-01T00:00:00Z",
        "end": "2025-04-30T23:59:59Z"
    },
    "breakdown": {
        "deposits": 75,
        "withdrawals": 45,
        "payments": 30
    }
}
```

## Available Response Types 

The SDK returns typed response objects for each API call. Here's a list of available types:

```python
from magebank.types import (
    # Agent types
    Agent,
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentDepositResponse,
    AgentWithdrawResponse,
    
    # Investment types
    InvestmentCalculateInterestResponse,
    InvestmentRetrieveInterestRateResponse,
    
    # Payment types
    Payment,
    PaymentApproveResponse, 
    PaymentDeclineResponse,
    PaymentRegisterResponse,
    
    # User types
    UserListPaymentsResponse,
    UserRetrieveWalletBalanceResponse,
    
    # Savings types
    SavingCreateDepositResponse,
    SavingCreateWithdrawalResponse,
    SavingListInvestmentsResponse,
    SavingListInvestmentsByAgentResponse,
    SavingRetrieveDashboardResponse
)
```

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from magebank import Magebank

mage = Magebank()

mage.payments.export(
    format="csv",
    date_range={
        "end": date.fromisoformat("2019-12-27"),
        "start": date.fromisoformat("2019-12-27"),
    },
)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `magebank.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `magebank.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `magebank.APIError`.

```python
import magebank
from magebank import Magebank

mage = Magebank()

try:
    mage.agents_with.retrieve("REPLACE_ME")
except magebank.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except magebank.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except magebank.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from magebank import Magebank

# Configure the default for all requests:
mage = Magebank(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
mage.with_options(max_retries=5).agents_with.retrieve("REPLACE_ME")
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from magebank import Magebank

# Configure the default for all requests:
mage = Magebank(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
mage = Magebank(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
mage.with_options(timeout=5.0).agents_with.retrieve("REPLACE_ME")
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `MAGEBANK_LOG` to `info`.

```shell
$ export MAGEBANK_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from magebank import Magebank

mage = Magebank()
response = mage.agents_with.with_raw_response.retrieve("REPLACE_ME")
print(response.headers.get('X-My-Header'))

agents_with = response.parse()  # get the object that `agents_with.retrieve()` would have returned
print(agents_with.id)
```

These methods return an [`APIResponse`](https://github.com/Accelerator321/MageBankSdk/tree/main/src/magebank/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/Accelerator321/MageBankSdk/tree/main/src/magebank/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with mage.agents_with.with_streaming_response.retrieve("REPLACE_ME") as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `mage.get`, `mage.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = mage.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from magebank import Magebank, DefaultHttpxClient

mage = Magebank(
    # Or use the `MAGEBANK_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
mage.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from magebank import Magebank

with Magebank() as mage:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Accelerator321/MageBankSdk/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import magebank
print(magebank.__version__)
```

## Requirements

Python 3.8 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
