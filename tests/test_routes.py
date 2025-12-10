import pytest

# 1. Test Signup (Basic Integration)
def test_signup(client):
    response = client.post("/users/signup", json={
        "username": "unittest",
        "email": "unit@test.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "unit@test.com"

# 2. Test Login (Updated for JWT)
def test_login(client):
    # Ensure user exists first
    client.post("/users/signup", json={"username":"jwtuser","email":"jwt@test.com","password":"password123"})
    
    response = client.post("/users/login", json={
        "email": "jwt@test.com",
        "password": "password123"
    })
    assert response.status_code == 200
    # Verify we got a Security Token back
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

# 3. Test Profile Update (The Feature Logic)
def test_update_profile(client):
    # Create user
    res = client.post("/users/signup", json={"username":"profuser","email":"prof@test.com","password":"123"})
    user_id = res.json()["id"]

    # Update Bio
    response = client.put(f"/users/{user_id}/profile", json={
        "bio": "Updated Bio",
        "location": "Updated Loc"
    })
    assert response.status_code == 200
    assert response.json()["bio"] == "Updated Bio"

# 4. Test Password Change (New Logic - Positive Scenario)
def test_change_password_success(client):
    # Create user
    res = client.post("/users/signup", json={"username":"pwduser","email":"pwd@test.com","password":"oldpassword"})
    user_id = res.json()["id"]

    # Change Password
    response = client.put(f"/users/{user_id}/password", json={
        "old_password": "oldpassword",
        "new_password": "newpassword"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Password updated successfully"

    # Try Logging in with NEW password
    login_res = client.post("/users/login", json={"email":"pwd@test.com", "password":"newpassword"})
    assert login_res.status_code == 200

# 5. Test Password Change (New Logic - Negative Scenario)
def test_change_password_fail(client):
    # Create user
    res = client.post("/users/signup", json={"username":"failuser","email":"fail@test.com","password":"realpassword"})
    user_id = res.json()["id"]

    # Try with WRONG old password
    response = client.put(f"/users/{user_id}/password", json={
        "old_password": "wrongpassword",
        "new_password": "newpassword"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect old password"

# 6. Test Delete Account (Integration)
def test_delete_account(client):
    # Create user
    res = client.post("/users/signup", json={"username":"deluser","email":"del@test.com","password":"123"})
    user_id = res.json()["id"]

    # Delete
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    # Verify user is gone
    check = client.get(f"/users/{user_id}")
    assert check.status_code == 404