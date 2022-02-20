from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.core.files import File
from django.test import TestCase
from django.urls import reverse
from ..models import Blog, Profile
from django.test import Client


class BlogListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for item in range(5):
            Blog.objects.create(
                name=f"name{item}",
                description=f"descr {item}"
            )
        user1 = User.objects.create_user(username='testuser1', email='ja@ls.com', password='12345')
        Profile.objects.create(
            user=user1,
            phone=1111111112,
            city="aa",
            verification=True
        )

    def test_blog_page(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Блог")
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_detail_page(self):
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

    def test_create_blog_page(self):
        user = self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "description")
        self.assertTemplateUsed(response, 'blog/blog_form.html')
        user = self.client.login(username='testuser1', password='12345')
        use = User.objects.get(username='testuser1')
        profile = Profile.objects.get(user=use)
        profile.verification = True
        profile.save()
        with open("./media/1.jpeg", "rb") as f:
            response = self.client.post(reverse('create'),
                                        {'file': f, 'name': 'test', 'description': 'testt'}, follow=True)
            self.assertRedirects(response, expected_url=reverse('blog'), status_code=302, target_status_code=200)


    def test_profile_page(self):
        user = self.client.login(username='testuser1', password='12345')
        username = User.objects.get(username='testuser1').username
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, username)

    def test_registeer_page(self):
        respone = self.client.get(reverse('register'))
        self.assertEqual(respone.status_code, 200)
        self.assertTemplateUsed(respone, 'blog/register.html')
        with open("./media/1.jpeg", "rb") as f:
            response = self.client.post(reverse('register'),
                                        {'first_name': 'ddkkk', 'last_name': 'sds', 'phone': 1111232121,
                                         'city': 'sdf', 'password1': 'admin1admin',
                                         'password2': 'admin1admin',
                                         'avatar': f, 'username': 'user12'}, follow=True)
            self.assertRedirects(response, expected_url=reverse('blog'), status_code=302, target_status_code=200)
            self.assertTrue(response.context['user'].is_active)

    def test_profile_edit_page(self):
        user = self.client.login(username='testuser1', password='12345')
        profile = User.objects.get(username='testuser1')
        response = self.client.get(reverse('profile-edit', args=[profile.id]))
        self.assertEqual(response.status_code, 200)
        with open("./media/1.jpeg", "rb") as f:
            response = self.client.post(reverse('profile-edit', args=[profile.id]),
                                        {'first_name': 'ddkkk', 'last_name': 'sds', 'phone': 1111232121,
                                         'city': 'sdf', 'password': 'admin1admin',
                                         'avatar': f}, follow=True)
            self.assertRedirects(response, expected_url=reverse('blog'), status_code=302, target_status_code=200)

    def test_upload_page(self):
        user = self.client.login(username='testuser1', password='12345')
        profile = User.objects.get(username='testuser1')
        response = self.client.get(reverse('upload-file'))
        self.assertEqual(response.status_code, 200)
        with open("./media/test.csv", "r") as f:
            response = self.client.post(reverse('upload-file'), {'file': f})
            self.assertRedirects(response, expected_url=reverse('blog'), status_code=302, target_status_code=200)

    def test_login_page(self):
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': '12345'})
        self.assertRedirects(response, expected_url=reverse('blog'), status_code=302, target_status_code=200)

    def test_logout_page(self):
        user = self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, expected_url=reverse('blog'), status_code=302, target_status_code=200)