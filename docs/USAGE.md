# revcat CLI usage

RevenueCat CLI

**Usage**:

```console
$ revcat [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `v1`: API v1

## `revcat v1`

API v1

**Usage**:

```console
$ revcat v1 [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `customers`: Manage customers
* `entitlements`: Manage entitlements

### `revcat v1 customers`

Manage customers

**Usage**:

```console
$ revcat v1 customers [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Gets the latest Customer Info for the...
* `delete`: Deletes a Customer.

#### `revcat v1 customers get`

Gets the latest Customer Info for the customer with the given App User ID, or creates a new customer if it doesn&#x27;t exist.

**Usage**:

```console
$ revcat v1 customers get [OPTIONS]
```

**Options**:

* `--api-key TEXT`: Your RevenueCat API key  [env var: REVENUECAT_API_KEY; required]
* `--user-id TEXT`: The App User ID of the Customer. Wrap in single quotes to ensure all characters such as $ are not dropped.  [env var: REVENUECAT_USER_ID; required]
* `--environment [production|sandbox]`: The environment to use.  [env var: REVENUECAT_ENVIRONMENT; default: production]
* `--help`: Show this message and exit.

#### `revcat v1 customers delete`

Deletes a Customer.

**Usage**:

```console
$ revcat v1 customers delete [OPTIONS]
```

**Options**:

* `--api-key TEXT`: Your RevenueCat API key  [env var: REVENUECAT_API_KEY; required]
* `--user-id TEXT`: The App User ID of the Customer. Wrap in single quotes to ensure all characters such as $ are not dropped.  [env var: REVENUECAT_USER_ID; required]
* `--environment [production|sandbox]`: The environment to use.  [env var: REVENUECAT_ENVIRONMENT; default: production]
* `--help`: Show this message and exit.

### `revcat v1 entitlements`

Manage entitlements

**Usage**:

```console
$ revcat v1 entitlements [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `grant`: Grants a Customer an entitlement.
* `revoke`: Revokes a Customer&#x27;s entitlement.
* `grant-from-export`: Grants entitlements to customers from a...

#### `revcat v1 entitlements grant`

Grants a Customer an entitlement. Does not override or defer a store transaction, applied simultaneously.

**Usage**:

```console
$ revcat v1 entitlements grant [OPTIONS]
```

**Options**:

* `--api-key TEXT`: Your RevenueCat API key  [env var: REVENUECAT_API_KEY; required]
* `--user-id TEXT`: The App User ID of the Customer. Wrap in single quotes to ensure all characters such as $ are not dropped.  [env var: REVENUECAT_USER_ID; required]
* `--entitlement-id TEXT`: The identifier for the entitlement you want to grant to the Customer  [required]
* `--end-time [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: When the entitlement should expire (e.g. &#x27;2024-12-31T23:59:59&#x27;).
* `--duration [daily|three_day|weekly|two_week|monthly|two_month|three_month|six_month|yearly|lifetime]`: The duration of the entitlement.
* `--start-time [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: When the entitlement should start (defaults to now).
* `--environment [production|sandbox]`: The environment to use.  [env var: REVENUECAT_ENVIRONMENT; default: production]
* `--help`: Show this message and exit.

#### `revcat v1 entitlements revoke`

Revokes a Customer&#x27;s entitlement.

**Usage**:

```console
$ revcat v1 entitlements revoke [OPTIONS]
```

**Options**:

* `--api-key TEXT`: Your RevenueCat API key  [env var: REVENUECAT_API_KEY; required]
* `--user-id TEXT`: The App User ID of the Customer. Wrap in single quotes to ensure all characters such as $ are not dropped.  [env var: REVENUECAT_USER_ID; required]
* `--entitlement-id TEXT`: The identifier for the entitlement you want to revoke from the Customer  [required]
* `--environment [production|sandbox]`: The environment to use.  [env var: REVENUECAT_ENVIRONMENT; default: production]
* `--help`: Show this message and exit.

#### `revcat v1 entitlements grant-from-export`

Grants entitlements to customers from a CSV file.

**Usage**:

```console
$ revcat v1 entitlements grant-from-export [OPTIONS]
```

**Options**:

* `--api-key TEXT`: Your RevenueCat API key  [env var: REVENUECAT_API_KEY; required]
* `--file-path PATH`: The path to the CSV file containing the customer data  [required]
* `--entitlement-id TEXT`: The identifier for the entitlement you want to grant to the Customer  [required]
* `--end-time [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: When the entitlement should expire (e.g. &#x27;2024-12-31T23:59:59&#x27;).
* `--duration [daily|three_day|weekly|two_week|monthly|two_month|three_month|six_month|yearly|lifetime]`: The duration of the entitlement.
* `--start-time [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: When the entitlement should start (defaults to now).
* `--user-id-field TEXT`: The field in the CSV file that contains the user ID  [default: app_user_id]
* `--environment [production|sandbox]`: The environment to use.  [env var: REVENUECAT_ENVIRONMENT; default: production]
* `--seconds-per-request INTEGER`: The number of seconds to wait between requests.  [default: 1]
* `--help`: Show this message and exit.
