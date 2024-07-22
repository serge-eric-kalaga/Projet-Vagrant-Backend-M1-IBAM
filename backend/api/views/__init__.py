"""
    CONTAIN ALL THE ENDPOINTS
"""

from .auth.login import auth_router
from .auth.user import user_router
from .healthcheck import healthcheck_router