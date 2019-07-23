class locators():


# Login Page
    email_textbox_xpath = "//input[@id='email']"
    password_textbox_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@class='btn btn-rounded btn-primary btn-block mt-2']"
    Invalid_Credential_text_xpath = "//div[#'toast-container']"
    valid_Credential_text_xpath = "//span[contains(text(),'Dashboard')]"

# common
    add_new_button_xpath = "//button[@class='btn btn-outline-primary']"
    new_add_submit_button_xpath = "//button[@class='mr-10 mat-raised-button mat-primary']"

# Leagues page
    league_tab_xpath = "//span[contains(text(),'Leagues')]"
    league_name_input_xpath = "//input[@placeholder='League Name']"
    league_location_input_xpath = "//input[@placeholder='League Location']"

# League Tables
    table_league_names_xpath = "//tbody//td[2]"
    table_league_admin_names_xpath = "//tbody//td[3]"
    table_league_team_number_xpath = "//tbody//td[4]"
    table_league_number_of_games_xpath = "//tbody//td[5]"

# Teams page
    team_tab_xpath = "//span[contains(text(),'Teams')]"
    select_league_xpath = "//select[@name='league_name']"
    team_name_input_xpath = "//input[@placeholder='Team Name']"
    team_location_input_xpath = "//input[@placeholder='Team Location']"
    select_founded_year_xpath = "//select[@name='league']"
    number_of_sprints_xpath = "//input[@placeholder='No of sprints']"
    sub_domain_input_xpath = "//input[@placeholder='Sub Domain']"

    add_new_team_admin_checkbox = "//mat-radio-button[@id='mat-radio-3']//div[@class='mat-radio-outer-circle']"
    team_admin_first_name_css = "#mat-input-7"
    team_admin_last_name_css = "#mat-input-8"
    team_admin_email_css = "#mat-input-9"
    team_admin_user_name_css = "#mat-input-10"

    add_new_league_admin_checkbox = "//mat-radio-button[@id='mat-radio-6']//div[@class='mat-radio-outer-circle']"
    league_admin_first_name_css = "#mat-input-11"
    league_admin_last_name_css = "#mat-input-12"
    league_admin_email_css = "#mat-input-13"
    league_admin_user_name_css = "#mat-input-14"

# Team Tables
    table_team_names_xpath = "//tbody//td[2]"
    table_team_location_xpath = "//tbody//td[3]"
    table_team_founded_year_xpath = "//tbody//td[4]"
    table_team_admin_name_xpath = "//tbody//td[5]"
    table_team_league_name_xpath = "//tbody//td[6]"
    table_team_league_number_of_sprints_xpath = "//tbody//td[7]"
    table_team_league_number_of_games_xpath = "//tbody//td[8]"

# users page
    user_tab_xpath = "//span[contains(text(),'Users')]"
    select_user_type_xpath = "//select[@name='user_userType']"
    add_new_team_xpath = "//div[contains(text(),'Add New')]"
    select_team_xpath = "//select[@name='user_role']"
    user_first_name_xpath = "//input[@id='firstName']"
    user_last_name_xpath = "//input[@placeholder='Last Name']"
    user_email_xpath = "//input[@placeholder='Email']"
    user_username_xpath = "//input[@placeholder='Username']"


# Match page
    match_tab_xpath = "//span[contains(text(),'Match')]"

