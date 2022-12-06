import os

import pytest

os.environ["FASTAPI_CONFIG"] = "testing"  # noqa

from pytest_factoryboy import register
from project.users.factories import UserFactory
from project.tdd.factories import MemberFactory

register(UserFactory)
register(MemberFactory)


def test_model(db_session, member):
    assert member.username
    assert member.avatar
    assert not member.avatar_thumbnail
