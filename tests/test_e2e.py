from playwright.sync_api import Page, expect

def test_full_user_flow(page: Page):
    # NOTE: Ensure your server is running on localhost:8000 before running this!
    
    # 1. Go to Register Page
    page.goto("http://127.0.0.1:8000/register-ui")
    
    # 2. Fill out Registration
    page.fill("#username", "playwright_user")
    page.fill("#email", "playwright@test.com")
    page.fill("#password", "secret123")
    page.click("button[type='submit']")
    
    # 3. Wait for Redirect to Login
    page.wait_for_url("**/login-ui")
    
    # 4. Login
    page.fill("#email", "playwright@test.com")
    page.fill("#password", "secret123")
    page.click("button[type='submit']")
    
    # 5. Check we are on Profile
    page.wait_for_url("**/profile-ui")
    expect(page.locator("h2")).to_contain_text("User Profile")
    
    # 6. Update Bio (Positive Scenario)
    page.fill("#bio", "Automated Bio")
    page.fill("#location", "Test City")
    page.click("text=Update Profile")
    
    # 7. Check Success Message
    expect(page.locator("#message")).to_contain_text("Profile Updated")
    
    # 8. Delete Account (Cleanup)
    page.on("dialog", lambda dialog: dialog.accept()) # Accept the "Are you sure?" popup
    page.click("#deleteBtn")
    
    # 9. Ensure back at Login
    page.wait_for_url("**/login-ui")