from rest_framework import test
from django.urls import reverse 
from tds_rampup.tests.test_api_base import APIMixin


class SubscriberAPIV1Test(test.APITestCase, APIMixin):
    def test_subsscribers_api_returns_status_code_200(self):
        api_url = reverse('rampup:subscribers')
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)
    

    def test_subscribers_api_returns_correct_number_of_subscribers(self):
        wanted_subscribers = 5
        self.make_subscribers_in_batch(5)
        response = self.client.get(reverse('rampup:subscribers'))
        qtd_subscribers_received = len(response.data)
        self.assertEqual(
            wanted_subscribers,
            qtd_subscribers_received
        )
    
    def test_subscriber_api_detail_returns_status_code_200(self):
        needed_name = 'test-value'
        self.make_subscriber(name=needed_name)
        response = self.client.get(reverse('rampup:subscriber_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn(needed_name, content)


    def test_subscriber_api_detail_line_up_returns_correct_values(self):
        needed_name = 'test-value'
        self.make_subscriber(name=needed_name)
        response = self.client.get(reverse('rampup:subscriber_detail_line_up', kwargs={'pk': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(needed_name, content)


    def test_subscriber_api_detail_returns_status_code_404_when_no_records_found(self):
        response = self.client.get(reverse('rampup:subscriber_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 404)

    
    def test_subscribers_api_creates_new_subscriber_with_success(self):
        self.make_location()
        data = {
                "name": "subscriber 100",
                "location": "12345"
        }
        response = self.client.post(
            reverse('rampup:subscribers'),
            data=data
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('name'), data.get('name'))
        self.assertEqual(response.data.get('location'), data.get('location'))


    def test_subscribers_api_returns_400_when_location_does_not_exists(self):
        data = {
                "name": "subscriber 100",
                "location": "44444"
        }
        response = self.client.post(
            reverse('rampup:subscribers'),
            data=data
        )
        
        self.assertEqual(response.status_code, 400)
