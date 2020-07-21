from rest_framework import pagination

class RoomsPagination(pagination.LimitOffsetPagination):
    max_limit = 4