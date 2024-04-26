from rest_framework import test
from django.urls import reverse 
from tds_rampup.tests.test_api_base import APIMixin


class LocationAPIV1Test(test.APITestCase, APIMixin):
    def test_locations_api_returns_status_code_200(self):
        api_url = reverse('rampup:locations')
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)
    

    def test_locations_api_returns_correct_number_of_locations(self):
        self.make_location()
        response = self.client.get(reverse('rampup:locations'))
        qtd_subscribers_received = len(response.data)
        self.assertEqual(
            1,
            qtd_subscribers_received
        )
    
    def test_locations_api_detail_returns_status_code_200_and_correct_values(self):
        needed_zip_code = '54321'
        self.make_location(zip_code=needed_zip_code)
        response = self.client.get(reverse('rampup:locations_detail', kwargs={'pk': needed_zip_code}))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn(needed_zip_code, content)


    def test_locations_api_detail_returns_status_code_404_when_no_records_found(self):
        response = self.client.get(reverse('rampup:locations_detail', kwargs={'pk': '12345'}))
        self.assertEqual(response.status_code, 404)


    def test_locations_api_creates_new_location_with_success(self):
        self.make_package()
        data = {
                'zip_code': '11111',
                'packages': ['package-test']
        }
        response = self.client.post(
            reverse('rampup:locations'),
            data=data
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('zip_code'), data.get('zip_code'))
        self.assertEqual(response.data.get('packages'), data.get('packages'))


    def test_locations_api_returns_400_when_missing_field(self):
        self.make_package()
        data = {
                'zip_code': '11111',
                'packages': ['not-existent']
        }
        response = self.client.post(
            reverse('rampup:locations'),
            data=data
        )
        self.assertEqual(response.status_code, 400)

