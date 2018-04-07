from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_403_FORBIDDEN


class NotAuthenticatedException(APIException):
    """A custom API exception for raising custom error message when user is not
    authenticated
    """

    status_code = HTTP_403_FORBIDDEN
    # FIXME: yes, admin URL is hardcoded, but both Django's reverse() and
    # reverse_lazy() were causing circular imports so for the scope of this
    # task it's left as a FIXME:
    default_detail = ("You're not logged in! login at "
                      "<a href='/admin' target='_blank'>Django Admin</a> and "
                      "then come back to this page")


class SuperuserException(APIException):
    """A custom API exception for raising custom error message when user is not
    superuser
    """

    status_code = HTTP_403_FORBIDDEN
    default_detail = "This action is only allowed for Staff users"
