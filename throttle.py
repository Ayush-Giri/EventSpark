from rest_framework.throttling import AnonRateThrottle


class CustomUserThrottle(AnonRateThrottle):
    scope = "custom_user_signup"
