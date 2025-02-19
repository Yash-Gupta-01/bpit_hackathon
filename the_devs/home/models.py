from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

district_choices= {
    ("Delhi","Delhi"),
    ("Mumbai","Mumbai"),
    ("Adarsh Nagar","Adarsh Nagar"),
    ("Ashok Vihar","Ashok Vihar"),
    ("Begum Pur","Begum Pur"),
    ("Karala","Karala"),
    ("Narela","Narela"),
    ("Pitam Pura","Pitam Pura"),
    ("Rohini Sub City","Rohini Sub City"),
    ("Shalimar Bagh","Shalimar Bagh"),
    ("Civil Lines","Civil Lines"),
    ("Gulabi Bagh","Gulabi Bagh"),
    ("Kamla Nagar","Kamla Nagar"),
    ("Kashmiri Gate","Kashmiri Gate"),
    ("Kotwali","Kotwali"),
    ("Model Town","Model Town"),
    ("Mori Gate","Mori Gate"),
    ("Sadar Bazaar","Sadar Bazaar"),
    ("Sarai Rohilla","Sarai Rohilla"),
    ("Shakti Nagar","Shakti Nagar"),
    ("Tis Hazari","Tis Hazari"),
    ("Timarpur","Timarpur"),
    ("Wazirabad","Wazirabad"),
    ("GTB Nagar","GTB Nagar"),
    ("Dilshad Garden","Dilshad Garden"),
    ("Naveen Shahdara","Naveen Shahdara"),
    ("New Usmanpur","New Usmanpur"),
    ("Shahdara","Shahdara"),
    ("Shastri Park","Shastri Park"),
    ("Yamuna Vihar","Yamuna Vihar"),
    ("Chandni Chowk","Chandni Chowk"),
    ("Daryaganj","Daryaganj"),
    ("Jhandewalan","Jhandewalan"),
    ("Karol Bagh","Karol Bagh"),
    ("Shastri Nagar","Shastri Nagar"),
    ("Kishanganj","Kishanganj"),
    ("Paharganj","Paharganj"),
    ("Rajender Nagar","Rajender Nagar"),
    ("Barakhamba Road","Barakhamba Road"),
    ("Chanakyapuri","Chanakyapuri"),
    ("Connaught Place","Connaught Place"),
    ("Gole Market","Gole Market"),
    ("INA Colony","INA Colony"),
    ("Laxmibai Nagar","Laxmibai Nagar"),
    ("Pragati Maidan","Pragati Maidan"),
    ("East Vinod Nagar","East Vinod Nagar"),
    ("Jhilmil Colony","Jhilmil Colony"),
    ("Laxmi Nagar","Laxmi Nagar"),
    ("Mayur Vihar","Mayur Vihar"),
    ("Pandav Nagar","Pandav Nagar"),
    ("Preet Vihar","Preet Vihar"),
    ("Anand Vihar","Anand Vihar"),
    ("Shreshtha Vihar","Shreshtha Vihar"),
    ("Vivek Vihar","Vivek Vihar"),
    ("Vasundhara Enclave","Vasundhara Enclave"),
    ("Vishwas Nagar","Vishwas Nagar"),
    ("Vivek Vihar","Vivek Vihar"),
    ("Kamal Hans Nagar","Kamal Hans Nagar"),
    ("Ram Vihar","Ram Vihar"),
    ("Surajmal Vihar","Surajmal Vihar"),
    ("Bank Enclave","Bank Enclave"),
    ("Park End","Park End"),
    ("Yojna Vihar","Yojna Vihar"),
    ("Chattarpur","Chattarpur"),
    ("Green Park","Green Park"),
    ("Gulmohar Park","Gulmohar Park"),
    ("Hauz Khas","Hauz Khas"),
    ("Hauz Khas Village","Hauz Khas Village"),
    ("Khanpur","Khanpur"),
    ("Malviya Nagar","Malviya Nagar"),
    ("Mehrauli","Mehrauli"),
    ("Neeti Bagh","Neeti Bagh"),
    ("Netaji Nagar","Netaji Nagar"),
    ("Safdarjung Enclave","Safdarjung Enclave"),
    ("Sainik Farm","Sainik Farm"),
    ("Saket","Saket"),
    ("Sangam Vihar","Sangam Vihar"),
    ("Sarojini Nagar","Sarojini Nagar"),
    ("Sarvodaya Enclave","Sarvodaya Enclave"),
    ("Siri Fort","Siri Fort"),
    ("South Extension","South Extension"),
    ("Sriniwaspuri","Sriniwaspuri"),
    ("Jor Bagh","Jor Bagh"),
    ("Lodhi Colony","Lodhi Colony"),
    ("Khan Market","Khan Market"),
    ("Sundar Nagar","Sundar Nagar"),
    ("Nizamuddin East","Nizamuddin East"),
    ("Nizamuddin West","Nizamuddin West"),
    ("Sarai Kale Khan","Sarai Kale Khan"),
    ("Jangpura","Jangpura"),
    ("Defence Colony","Defence Colony"),
    ("Lajpat Nagar","Lajpat Nagar"),
    ("New Friends Colony","New Friends Colony"),
    ("Nehru Place","Nehru Place"),
    ("Kalkaji","Kalkaji"),
    ("East of Kailash","East of Kailash"),
    ("Chittaranjan Park","Chittaranjan Park"),
    ("Govindpuri","Govindpuri"),
    ("Greater Kailash","Greater Kailash"),
    ("Alaknanda","Alaknanda"),
    ("Jamia Nagar","Jamia Nagar"),
    ("Okhla","Okhla"),
    ("Sarita Vihar","Sarita Vihar"),
    ("Jaitpur","Jaitpur"),
    ("Tughlaqabad","Tughlaqabad"),
    ("Badarpur","Badarpur"),
    ("Dabri, New Delhi","Dabri, New Delhi"),
    ("Dwarka Sub City","Dwarka Sub City"),
    ("Delhi Cantonment","Delhi Cantonment"),
    ("Dhaula Kuan","Dhaula Kuan"),
    ("Inderpuri","Inderpuri"),
    ("Mahipalpur","Mahipalpur"),
    ("Moti Bagh","Moti Bagh"),
    ("Munirka","Munirka"),
    ("Najafgarh","Najafgarh"),
    ("Naraina Vihar","Naraina Vihar"),
    ("Palam","Palam"),
    ("Rama Krishna Puram","Rama Krishna Puram"),
    ("Sagar Pur","Sagar Pur"),
    ("Vasant Kunj","Vasant Kunj"),
    ("Vasant Vihar","Vasant Vihar"),
    ("Ashok Nagar","Ashok Nagar"),
    ("Bali Nagar","Bali Nagar"),
    ("Fateh Nagar","Fateh Nagar"),
    ("Kirti Nagar","Kirti Nagar"),
    ("Moti Nagar","Moti Nagar"),
    ("Paschim Vihar","Paschim Vihar"),
    ("Patel Nagar","Patel Nagar"),
    ("Punjabi Bagh","Punjabi Bagh"),
    ("Rajouri Garden","Rajouri Garden"),
    ("Tihar Village","Tihar Village"),
    ("Tilak Nagar","Tilak Nagar"),
    ("Vikas Nagar","Vikas Nagar"),
    ("Vikaspuri","Vikaspuri"),

    
}

class Volunteer(models.Model):
    """
    phone_no
    district
    is_active
    author/volunteered_by
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    phone_no = PhoneField(unique=True, blank=False, null=False)
    district = models.CharField(max_length=100, choices=district_choices, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    volunteered_by = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  # Ensured proper string representation

    class Meta:
        verbose_name_plural = 'Volunteer'
        ordering = ['-joined_at']