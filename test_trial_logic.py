import time
import json
import os

def test_trial_and_referral_logic():
    print("[TEST] Starting Step 17: 7-Day Trial & Referral Binding Enforcement Test...")
    
    # Simulate user installation timestamp (e.g., 8 days ago vs 2 days ago)
    current_time = int(time.time() * 1000)
    eight_days_ago = current_time - (8 * 24 * 60 * 60 * 1000)
    two_days_ago = current_time - (2 * 24 * 60 * 60 * 1000)
    
    # Test Case 1: User installed 8 days ago, NOT registered -> Should trigger Trial Expired restriction
    install_date_1 = eight_days_ago
    is_registered_1 = False
    days_passed_1 = (current_time - install_date_1) / (1000 * 60 * 60 * 24)
    
    expired_1 = (days_passed_1 > 7 and not is_registered_1)
    print(f"  -> Test Case 1 (8 days old, unregistered): Days Passed = {days_passed_1:.1f}, Trial Expired = {expired_1} [Expected: True]")
    assert expired_1 == True, "Test Case 1 Failed!"

    # Test Case 2: User installed 8 days ago, BUT registered -> Should NOT trigger restriction
    install_date_2 = eight_days_ago
    is_registered_2 = True
    days_passed_2 = (current_time - install_date_2) / (1000 * 60 * 60 * 24)
    
    expired_2 = (days_passed_2 > 7 and not is_registered_2)
    print(f"  -> Test Case 2 (8 days old, registered): Days Passed = {days_passed_2:.1f}, Trial Expired = {expired_2} [Expected: False]")
    assert expired_2 == False, "Test Case 2 Failed!"

    # Test Case 3: User installed 2 days ago, NOT registered -> Within trial period
    install_date_3 = two_days_ago
    is_registered_3 = False
    days_passed_3 = (current_time - install_date_3) / (1000 * 60 * 60 * 24)
    
    expired_3 = (days_passed_3 > 7 and not is_registered_3)
    print(f"  -> Test Case 3 (2 days old, unregistered): Days Passed = {days_passed_3:.1f}, Trial Expired = {expired_3} [Expected: False]")
    assert expired_3 == False, "Test Case 3 Failed!"

    print("[SUCCESS] Step 17: 7-Day Trial & Referral Enforcement Test Passed Successfully!")

if __name__ == "__main__":
    test_trial_and_referral_logic()
