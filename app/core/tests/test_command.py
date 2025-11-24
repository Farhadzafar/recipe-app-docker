from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError
from django.core.management import call_command
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Tests for 'wait_for_db' management command."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when db is not yet available."""
        patched_check.side_effect = [psycopg2Error] * 2 + [OperationalError] * 3 + [True]