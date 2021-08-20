import json

from rest_framework import status

from news.tests.factories import NoticeFactory


def test_select_notices(customer_client):
    notice = NoticeFactory()
    response = customer_client.get(f"/v1/notice/", content_type="application/json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert notice.id == json.loads(response.content)[0].get('id')


def test_select_notices_with_filters(customer_client):

    title = "Hoje vai Chover"
    notice = NoticeFactory(title=title)
    response = customer_client.get(f"/v1/notice/?title={title}", content_type="application/json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert notice.id == json.loads(response.content)[0].get('id')


def test_select_notices_with_filters_empty(customer_client):

    title = "Hoje vai Chover"
    notice = NoticeFactory(title="Hoje nao vai chover")
    response = customer_client.get(f"/v1/notice/?title={title}", content_type="application/json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


def test_select_notices_update(customer_client):

    notice = NoticeFactory(title="Hoje nao vai chover")

    payload = {'title': 'Hoje vai Chover'}
    response = customer_client.patch(f"/v1/notice/{notice.id}/", content_type="application/json", data=json.dumps(payload))

    # THEN
    assert response.status_code == status.HTTP_200_OK


def test_select_notices_delete(customer_client):

    notice = NoticeFactory()
    response = customer_client.delete(f"/v1/notice/{notice.id}/")

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
