from datetime import timedelta

import grpc
import pytest
from google.protobuf import empty_pb2, wrappers_pb2

from couchers import errors
from couchers.db import get_user_by_field
from couchers.models import User
from couchers.utils import now
from pb import api_pb2, conversations_pb2, requests_pb2, search_pb2
from tests.test_fixtures import (
    api_session,
    conversations_session,
    db,
    generate_user,
    make_friends,
    requests_session,
    search_session,
    session_scope,
    testconfig,
)


@pytest.fixture(autouse=True)
def _(testconfig):
    pass


def test_visible_user_filter(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user()
    user3, token3 = generate_user(is_deleted=True)
    user4, token4 = generate_user(accepted_tos=0)
    with session_scope() as session:
        user2 = get_user_by_field(session, user2.username)
        user2.is_banned = True
        session.commit()
        session.refresh(user2)
        session.expunge(user2)

        visible_users = session.query(User).filter(User.is_visible).all()
        assert len(visible_users) == 1


def test_get_invisible_users(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user(is_deleted=True)

    # Test get invisible user by username
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.GetUser(api_pb2.GetUserReq(user=user2.username))
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.USER_NOT_FOUND

    # Test get invisible user by id
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.GetUser(api_pb2.GetUserReq(user=str(user2.id)))
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.USER_NOT_FOUND

    # Test get invisible user by email
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.GetUser(api_pb2.GetUserReq(user=user2.email))
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.USER_NOT_FOUND


def test_friend_requests_with_invisible_users(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user(is_deleted=True)
    user3, token3 = generate_user()
    user4, token4 = generate_user()

    # Test send friend request to invisible user
    # Necessary? Can't see user, can't send friend request
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.SendFriendRequest(
                api_pb2.SendFriendRequestReq(
                    user_id=user2.id,
                )
            )
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.USER_NOT_FOUND

    # Check no active FR to start
    with api_session(token1) as api:
        res = api.ListFriendRequests(empty_pb2.Empty())
        assert len(res.sent) == 0
        assert len(res.received) == 0

    # Send friend request to user 1
    with api_session(token3) as api:
        friend_request_id = api.SendFriendRequest(api_pb2.SendFriendRequestReq(user_id=user1.id)).friend_request_id

    # Check 1 received FR
    with api_session(token1) as api:
        res = api.ListFriendRequests(empty_pb2.Empty())
        assert len(res.sent) == 0
        assert len(res.received) == 1

    # Hide sender
    with session_scope() as session:
        user3 = get_user_by_field(session, user3.username)
        user3.is_banned = True
        session.commit()
        session.refresh(user3)
        session.expunge(user3)

    # Check back to no FR
    with api_session(token1) as api:
        res = api.ListFriendRequests(empty_pb2.Empty())
        assert len(res.sent) == 0
        assert len(res.received) == 0

    """""
    # Test view friend request sent by invisible user
    # Necessary? Can't see user, doesn't show up in list of FR
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.GetFriendRequest(
                api_pb2.GetFriendRequestReq(
                    friend_request_id=friend_request_id,
                )
            )
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.FRIEND_REQUEST_NOT_FOUND
    """

    # Test reply friend request sent by invisible user
    # Necessary? FR should be hidden, won't be able to reply
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.RespondFriendRequest(api_pb2.RespondFriendRequestReq(friend_request_id=friend_request_id, accept=True))
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.FRIEND_REQUEST_NOT_FOUND

    # Send FR from user1
    with api_session(token1) as api:
        friend_request_id_2 = api.SendFriendRequest(api_pb2.SendFriendRequestReq(user_id=user4.id)).friend_request_id

    # Check one FR sent
    with api_session(token1) as api:
        res = api.ListFriendRequests(empty_pb2.Empty())
        assert len(res.sent) == 1
        assert len(res.received) == 0

    # Hide recipient
    with session_scope() as session:
        user4 = get_user_by_field(session, user4.username)
        user4.is_banned = True
        session.commit()
        session.refresh(user4)
        session.expunge(user4)

    # Check back to no FR
    with api_session(token1) as api:
        res = api.ListFriendRequests(empty_pb2.Empty())
        assert len(res.sent) == 0
        assert len(res.received) == 0

    # Test cancel friend request sent to invisible user
    # Necessary? Can't see user, request doesn't show up in sent request
    with api_session(token1) as api:
        with pytest.raises(grpc.RpcError) as e:
            api.CancelFriendRequest(api_pb2.CancelFriendRequestReq(friend_request_id=friend_request_id_2))
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.FRIEND_REQUEST_NOT_FOUND


def test_friend_list_with_invisible_users(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user(is_deleted=True)
    user3, token3 = generate_user()

    with api_session(token1) as api:
        res = api.ListFriends(empty_pb2.Empty())
        assert len(res.user_ids) == 0

    make_friends(user1, user2)

    with api_session(token1) as api:
        res = api.ListFriends(empty_pb2.Empty())
        assert len(res.user_ids) == 0

    make_friends(user1, user3)

    with api_session(token1) as api:
        res = api.ListFriends(empty_pb2.Empty())
        assert len(res.user_ids) == 1


def test_host_requests_with_invisible_user(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user(is_deleted=True)
    user3, token3 = generate_user()
    user4, token4 = generate_user()
    user5, token5 = generate_user()

    # Test send host request to invisible user
    # Necessary? Can't see user, so can't send HR
    today_plus_2 = (now() + timedelta(days=2)).strftime("%Y-%m-%d")
    today_plus_3 = (now() + timedelta(days=3)).strftime("%Y-%m-%d")

    with requests_session(token1) as requests:
        with pytest.raises(grpc.RpcError) as e:
            requests.CreateHostRequest(
                requests_pb2.CreateHostRequestReq(
                    to_user_id=user2.id, from_date=today_plus_2, to_date=today_plus_3, text="Test request"
                )
            )
    assert e.value.code() == grpc.StatusCode.NOT_FOUND
    assert e.value.details() == errors.USER_NOT_FOUND

    # Send host request, then delete requester
    with requests_session(token3) as requests:
        host_request_id = requests.CreateHostRequest(
            requests_pb2.CreateHostRequestReq(
                to_user_id=user1.id, from_date=today_plus_2, to_date=today_plus_3, text="Test request"
            )
        ).host_request_id

    with session_scope() as session:
        user3 = get_user_by_field(session, user3.username)
        user3.is_deleted = True
        session.commit()
        session.refresh(user3)
        session.expunge(user3)

    with requests_session(token1) as requests:
        # Test get host request sent by invisible user
        with pytest.raises(grpc.RpcError) as e:
            requests.GetHostRequest(requests_pb2.GetHostRequestReq(host_request_id=host_request_id))
        assert e.value.code() == grpc.StatusCode.NOT_FOUND
        assert e.value.details() == errors.HOST_REQUEST_NOT_FOUND

        # Test reply to host request sent by invisible user
        # Necessary? Can't get host request, can't reply to it
        with pytest.raises(grpc.RpcError) as e:
            requests.RespondHostRequest(
                requests_pb2.RespondHostRequestReq(
                    host_request_id=host_request_id, status=conversations_pb2.HOST_REQUEST_STATUS_ACCEPTED
                )
            )
        assert e.value.code() == grpc.StatusCode.NOT_FOUND
        assert e.value.details() == errors.HOST_REQUEST_NOT_FOUND

    # Send host request, then delete recipient
    with requests_session(token1) as requests:
        requests.CreateHostRequest(
            requests_pb2.CreateHostRequestReq(
                to_user_id=user4.id, from_date=today_plus_2, to_date=today_plus_3, text="Test request"
            )
        )

    with session_scope() as session:
        user4 = get_user_by_field(session, user4.username)
        user4.is_deleted = True
        session.commit()
        session.refresh(user4)
        session.expunge(user4)

    # Test view all host requests excluding those involving invisible users
    with requests_session(token1) as requests:
        res = requests.ListHostRequests(requests_pb2.ListHostRequestsReq())
        assert len(res.host_requests) == 0

        requests.CreateHostRequest(
            requests_pb2.CreateHostRequestReq(
                to_user_id=user5.id, from_date=today_plus_2, to_date=today_plus_3, text="Test request"
            )
        )

        res = requests.ListHostRequests(requests_pb2.ListHostRequestsReq())
        assert len(res.host_requests) == 1


def test_messages_with_invisible_users(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user(is_deleted=True)
    make_friends(user1, user2)

    # Test create message
    # Necessary? If can't see user, can't send message
    with conversations_session(token1) as c:
        with pytest.raises(grpc.RpcError) as e:
            c.CreateGroupChat(conversations_pb2.CreateGroupChatReq(recipient_user_ids=[user2.id]))
    assert e.value.code() == grpc.StatusCode.INVALID_ARGUMENT
    assert e.value.details() == errors.NO_RECIPIENTS

    # Test view messages from invisible user
    # Desired behavior? Should these be viewable or hidden?
    # TODO

    # Test group chat where one user gets banned
    # Desired behavior? Do their messages remain in the group chat?
    # TODO


def test_references_invisible_users(db):
    pass

    # Test invisible user writes reference
    # Necessary? Is this even possible?
    # TODO

    # Test user writes reference for invisible user
    # Necessary? Can't see user, can't write reference
    # TODO


def test_search_function_invisible_users(db):
    user1, token1 = generate_user()
    user2, token2 = generate_user(is_deleted=True)

    with search_session(token1) as api:
        res = api.Search(
            search_pb2.SearchReq(
                query='test_user_',
                include_users=True,
            )
        )
        assert len(res.results) == 1

        res = api.UserSearch(
            search_pb2.UserSearchReq(
                query=wrappers_pb2.StringValue(value='test_user_')
            )
        )
        assert len(res.results) == 1


"""
Future testing:
Event attendance lists
Group member lists
Other lists of users?
"""
