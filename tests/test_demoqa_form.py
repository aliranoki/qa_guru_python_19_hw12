import allure

from demoqa_tests.model.pages.registration_page import RegistrationPage

@allure.title("Successful fill form")
def test_form(setup_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    # Заполнение формы
    with allure.step("Fill form"):
        registration_page.fill_first_name('John')
        registration_page.fill_last_name('Doe')
        registration_page.fill_user_email('john.doe@example.com')
        registration_page.set_gender()
        registration_page.fill_phone_number('1234567890')
        registration_page.fill_date_of_birth('2000', 'August', '15')
        registration_page.choose_subjects('Arts')
        registration_page.select_hobbies('sports', 'reading')
        registration_page.upload_picture()
        registration_page.fill_address('123 Main Street, Apt 4B, New York, NY 10001')
        registration_page.fill_state('Rajasthan')
        registration_page.fill_city('Jaiselmer')
        registration_page.submit_form()


    # Проверка результатов
    # Проверка заголовка модального окна
    with allure.step("Check form results"):
        registration_page.should_popup_title_be('Thanks for submitting the form')

        # Проверка данных в таблице
        registration_page.should_student_name_be('Student Name John Doe')
        registration_page.should_student_email_be('Student Email john.doe@example.com')
        registration_page.should_student_gender_be('Gender Male')
        registration_page.should_student_mobile_be('Mobile 1234567890')
        registration_page.should_student_date_of_birth_be('Date of Birth 15 August,2000')
        registration_page.should_student_subjects_be('Subjects Arts')
        registration_page.should_student_hobbies_be('Hobbies Sports, Reading')
        registration_page.should_student_picture_be('Picture picture.png')
        registration_page.should_student_address_be('Address 123 Main Street, Apt 4B, New York, NY 10001')
        registration_page.should_student_state_and_city_be('State and City Rajasthan Jaiselmer')

