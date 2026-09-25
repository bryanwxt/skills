# Existing code: `reportcli` (Python 3.12 package; ruff, ruff format and mypy --strict configured in CI; pytest)

`src/reportcli/cli.py`:

```python
import click

from reportcli.repo import UserRepo

repo = UserRepo.from_env()


@click.group()
def cli() -> None:
    """Reporting commands."""


@cli.command("list-users")
@click.option("--active/--all", default=True, help="Only active users (default) or all users.")
def list_users(active: bool) -> None:
    """Print users, one per line: id<TAB>email."""
    for user in repo.list_users(active=active):
        click.echo(f"{user.id}\t{user.email}")
```

`src/reportcli/repo.py` (excerpt):

```python
class UserRepo:
    def list_users(self, active: bool = True) -> Iterator[User]:
        """Yield users ordered by id."""
        query = "SELECT id, email FROM users" + (" WHERE active" if active else "") + " ORDER BY id"
        yield from self._rows(query)
```

`tests/test_cli.py` uses click's `CliRunner` with an in-memory `UserRepo` fake.
