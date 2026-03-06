'''
1 Standard Library
2 Third-party
3 Local application : 없음
'''
#1.standard library(python에 기본 포함된 라이브러리)
from collections import OrderedDict

#2.django(pip 등으로 설치한 외부 라이브러리)
from django.conf import settings

#2-1.Third party(pip 등으로 설치한 외부 라이브러리)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


'''
1. Query 처리
2. 응답구조  
'''
class CustomPageNumberPagination(PageNumberPagination):
    default_page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE",10)

    def paginate_queryset(self, queryset, request, view=None):
        page_size = request.query_params.get("page_size", self.default_page_size)

        if page_size == "all":
            self.page_size = len(queryset)

        else:
            try:
                self.page_size = int(page_size)
            except ValueError:
                self.page_size = self.default_page_size

        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):

        return Response(
            OrderedDict([
                #주고 받는 데이터
                ("data", data),
                ("page_size", len(data)),
                #페이지 관련 META 정보
                ("total_count", self.page.paginator.count),
                ("page_count", self.page.paginator.num_pages),
                ("current_page", self.page.number),
                #이동 정보 관련 
                ("next", self.get_next_link()),
                ("previous", self.get_previous_link()),
            ])
        )

'''
현재 pagination은 페이지 조회를 해서 10개 혹은 20개 등 목록 조회를 하는 데에 목적이 있다. 
기능 변경한다면 
사용자가 유동적으로 50개 보기 20개 보기 옵션을 선택할 수 있도록 하는 것도 좋을 것 같다.
또 스크롤해서 인스타 피드를 보는 방식의 경우에는 
앞 뒤로 보여줄 내용이 유동적으로 바뀌는 방식의 로직을 추가하고 응답구조도 변경하는 것이 좋을 것 같다.
'''