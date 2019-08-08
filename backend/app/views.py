from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Office
from .serializers import CompanySerializer, OfficeSerializer


# Create your views here.
class CompanyListViewSet(APIView):
    '''
    METHOD: GET
    ENDPOINT: /api/v1/company/
    RESPONSE_EXAMPLE:
    [
        {
            "id": 1,
            "name": "Company1",
            "headquarter_office": {
                "street": "Street 1",
                "city": "city1",
                "postal_code": "12345"
            }
        },
        {
            "id": 2,
            "name": "Company2",
            "headquarter_office": {
                "street": "Street 2",
                "city": "city2",
                "postal_code": "67890"
            }
        }
    ]
    '''
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)


class OfficeListViewSet(APIView):
    '''
    REQUEST_METHOD: GET
    ENDPOINT: /api/v1/office/:company_id
    RESPONSE_EXAMPLE:
    [
        {
            "id": 3,
            "company": 1,
            "headquarter": false,
            "name": "Office 3",
            "street": "Street 3",
            "postal_code": "23456",
            "city": "Moscow",
            "monthly_rent": "32",
        },
        ...
    ]
    '''
    def get(self, request, company_id, format=None):
        if company_id:
            offices = Office.objects.filter(company=company_id).all()  # noqa
        else:
            offices = Office.objects.all()

        serializer = OfficeSerializer(offices, many=True)
        return Response(serializer.data)


class UpdateHeadquarter(APIView):
    '''
    REQUEST_METHOD: PUT,
    ENDPOINT: /api/v1/company/<company_id>/
    REQUEST_PARAM:
    {
        "office_id": 1
    }
    RESPONSE_EXAMPLE:
    [
        {
            "id": 3,
            "company": 1
            "headquarter": true,
            "name": "Office 3",
            "street": "Street 3",
            "postal_code": "23456",
            "city": "city3",
            "monthly_rent": "32",
        }
    ]
    '''
    def put(self, request, pk, format=None):
        Office.objects.filter(company__pk=pk).update(headquarter=False)
        Office.objects.filter(id=request.data['office_id']).update(headquarter=True)
        query_set = Office.objects.filter(company__pk=pk, headquarter=True).all()
        serializer = OfficeSerializer(query_set, many=True)

        return Response(serializer.data)

    def get(self, request, pk, format=None):
        query_set = Office.objects.filter(company__pk=pk).all()
        serializer = OfficeSerializer(query_set)
        return Response(serializer.data)


class CreateCompanyOffice(APIView):
    '''
    METHOD: POST
    ENDPOINT: /api/v1/create_company/
    REQEST PARAM:
    {
        "name": "new company",
        "offices": [
            {
                "name": "Office 4",
                "headquarter": true
                "street": "Street 4",
                "postal_code": "123456",
                "city": "city4",
                "monthly_rent": "30",
            },
            {
                "name": "Office 5",
                "headquarter": false
                "street": "Street 5",
                "postal_code": "456123",
                "city": "city5",
                "monthly_rent": "25",
            }
        ]
    }
    RESPONSE_EXAMPLE:
    [
        {
            "id": 3,
            "name": "Company3",
            "headquarter_office": {
                "street": "Street 4",
                "city": "city4",
                "postal_code": "123456"
            }
        }
    ]
    '''
    def post(self, request):
        company = Company.objects.create(name=request.data['name'])
        for office in request.data['officies']:
            isHeadquarter = False
            if 'isHeadquarter' in office.keys():
                isHeadquarter = office['isHeadquarter']
            Office.objects.create(
                name=office['name'],
                street=office['street'],
                postal_code=office['postal_code'],
                city=office['city'],
                monthly_rent=office['monthly_rent'],
                company=company,
                headquarter=isHeadquarter,
            )
        query_set = Company.objects.filter(name=request.data['name'])
        serializer = CompanySerializer(query_set, many=True)

        return Response(serializer.data)
