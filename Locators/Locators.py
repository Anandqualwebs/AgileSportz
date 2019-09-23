class locators():


# Login Page
    email_textbox_xpath = "//input[@id='email']"
    password_textbox_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@class='btn btn-rounded btn-primary btn-block mt-2']"
    Invalid_Credential_text_xpath = "//div[#'toast-container']"
    valid_Credential_text_xpath = "//span[contains(text(),'Dashboard')]"
    profile_icon_xpath = "//img[@id='userDropdown']"
    logout_linktext = "Logout"

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

# League Admin
# Match

    game_tab_xpath = "//span[contains(text(),'Game')]"
    select_opponent_xpath = "//select[@name='opponent']"
    match_location_xpath = "//input[@placeholder='Location']"
    match_date_xpath = "//input[@placeholder='Date']"
    match_time_xpath = "//input[@placeholder='Time']"

# Team Admin
# Sprints
    sprint_tab_xpath = "//span[contains(text(),'Sprints')]"
    sprint_number_xpath = "//input[@placeholder='Sprint Number']"
    sprint_start_date_xpath = "//input[@placeholder='Start date']"
    sprint_number_date_xpath = "//input[@placeholder='End date']"
    match_1_checkbox_css = "div.row div.col-md-3.match-box.ng-star-inserted:nth-child(1) mat-checkbox.mat-checkbox.mat-accent:nth-child(1) label.mat-checkbox-layout > div.mat-checkbox-inner-container.mat-checkbox-inner-container-no-side-margin"
    match_2_checkbox_css = "div.row div.col-md-3.match-box.ng-star-inserted:nth-child(2) mat-checkbox.mat-checkbox.mat-accent:nth-child(1) label.mat-checkbox-layout > div.mat-checkbox-inner-container.mat-checkbox-inner-container-no-side-margin"
    match_3_checkbox_css = "div.row div.col-md-3.match-box.ng-star-inserted:nth-child(3) mat-checkbox.mat-checkbox.mat-accent:nth-child(1) label.mat-checkbox-layout > div.mat-checkbox-inner-container.mat-checkbox-inner-container-no-side-margin"
    sprint_add_xpath = "//span[contains(text(),'Add')]"

    edit_sprint_xpath = "//button[@class='icons-button']"
    sprint_status_xpath = "//select[@name='status']"
#card
    select_match_xpath = "//select[@name='match_name']"
    coach_card_input_1 = "//tr[1]//td[3]//input[1]"
    coach_card_input_2 = "//tr[1]//td[4]//input[1]"
    coach_card_input_3 = "//tr[1]//td[5]//input[1]"
    coach_card_input_4 = "//tr[1]//td[6]//input[1]"

    player_1_card_input_1 = "//tr[2]//td[3]//input[1]"
    player_1_card_input_2 = "//tr[2]//td[4]//input[1]"
    player_1_card_input_3 = "//tr[2]//td[5]//input[1]"
    player_1_card_input_4 = "//tr[2]//td[6]//input[1]"

    player_2_card_input_1 = "//tr[3]//td[3]//input[1]"
    player_2_card_input_2 = "//tr[3]//td[4]//input[1]"
    player_2_card_input_3 = "//tr[3]//td[5]//input[1]"
    player_2_card_input_4 = "//tr[3]//td[6]//input[1]"

    player_3_card_input_1 = "//tr[4]//td[3]//input[1]"
    player_3_card_input_2 = "//tr[4]//td[4]//input[1]"
    player_3_card_input_3 = "//tr[4]//td[5]//input[1]"
    player_3_card_input_4 = "//tr[4]//td[6]//input[1]"

    actual_save_edit_button_1_xpath = "//tr[1]//button[1]"
    actual_save_edit_button_2_xpath = "//tr[2]//button[1]"
    actual_save_edit_button_3_xpath = "//tr[3]//button[1]"
    actual_save_edit_button_4_xpath = "//tr[4]//button[1]"


# Analyst/coach/player
# Agility Card
    card_tab_xpath = "//span[contains(text(),'Agility Card')]"
    game_1_link_text = "Game1"
    game_2_link_text = "Game2"

    coach_assign_css = "[class='card col-md-3 mt-2 player_Space isCoach'] .mat-raised-button"
    player_1_assign_css = "div.app-admin-wrap.layout-sidebar-large.clearfix:nth-child(2) div.main-content-wrap.sidenav-open.d-flex.flex-column div.row div.col-md-12.all-player-card.mt-0:nth-child(3) div.row.mt-0 div.card.col-md-3.mt-2.player_Space:nth-child(2) div.row.mt-3 div.col-md-4.text-center > a.mat-raised-button.mat-primary"
    player_2_assign_css = "div.app-admin-wrap.layout-sidebar-large.clearfix:nth-child(2) div.main-content-wrap.sidenav-open.d-flex.flex-column div.row div.col-md-12.all-player-card.mt-0:nth-child(3) div.row.mt-0 div.card.col-md-3.mt-2.player_Space:nth-child(3) div.row.mt-3 div.col-md-4.text-center > a.mat-raised-button.mat-primary"
    player_3_assign_css = "div.app-admin-wrap.layout-sidebar-large.clearfix:nth-child(2) div.main-content-wrap.sidenav-open.d-flex.flex-column div.row div.col-md-12.all-player-card.mt-0:nth-child(3) div.row.mt-0 div.card.col-md-3.mt-2.player_Space:nth-child(4) div.row.mt-3 div.col-md-4.text-center > a.mat-raised-button.mat-primary"

    assign_submit_button_xpath = "//span[@class='mat-button-wrapper']"

    matrics_1_xpath = "//mat-checkbox[@id='1']//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"
    matrics_2_xpath = "//mat-checkbox[@id='2']//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"
    matrics_3_xpath = "//mat-checkbox[@id='3']//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"
    matrics_4_xpath = "//mat-checkbox[@id='4']//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"
    matrics_5_xpath = "//mat-checkbox[@id='5']//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"

    plan_tab_xpath = "//h6[contains(text(),'Planned')]"
    Actual_tab_xpath = "//h6[contains(text(),'Actual')]"

# Analyst
# post game survey
    survey_tab_xpath = "//span[contains(text(),'Post Game Survey')]"
    survey_match_1_submit_xpath = "//tr[1]//button[1]"
    survey_match_2_submit_xpath = "//tr[2]//button[1]"
    survey_question_1_checkbox_xpath = "//mat-radio-button[@id='mat-radio-20']"
    survey_question_2_checkbox_xpath = "//mat-radio-button[@id='mat-radio-30']"
    survey_question_3_checkbox_xpath = "//mat-radio-button[@id='mat-radio-40']"
    survey_question_4_checkbox_xpath = "//mat-radio-button[@id='mat-radio-50']"
    survey_question_5_checkbox_xpath = "//mat-radio-button[@id='mat-radio-60']"
    survey_common_submit_xpath = "//span[contains(@class,'mat-button-wrapper')]"

















