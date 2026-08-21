# security.py 
# security related funtions for authn

# env variables
from config import settings
# timestamps for jwt expiration
from datetime import datetime, timedelta, timezone
# jwterror and jwt to create and decode tokens, and throw errors
from jose import JWTError, jwt
# bcrypt for password hashing
import bcrypt
# import logigng so we can add logging in the future
import logging
logger = logging.getLogger(__name__)

# jwt configurations
SECRET_KEY = settings.JWT_SECRET
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# password hasing function handled through passlib
def hash_password (password: str) -> str:
    # convert plaintext string into raw bytes
    password_bytes = password.encode('utf-8')

    # generate new and random salt
    salt = bcrypt.gensalt()

    # hash bytes and decode final result into string
    hashed_bytes = bcrypt.hashpw(password_bytes, salt) 
    return hashed_bytes.decode('utf-8')


# password verification function, remove salt hash raw password, compare
def verify_password (plain_password: str, hashed_password: str) -> bool: 
    # convert both strings into bytes for bcrypt comparison
    plain_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes) 



def create_access_token (data: dict) -> str: 
    # copy for safety, generate jwt string
    to_encode = data.copy()

    # calculate exact expiration
    expire = datetime.now(timezone.utc) + timedelta( minutes = ACCESS_TOKEN_EXPIRE_MINUTES )

    # add the expiration field to token payload
    to_encode.update(
        {
            "exp":expire
        }
    )

    # cryptographically sign the payload with the secret key
    encoded_jwt = jwt.encode (
        to_encode, 
        SECRET_KEY, 
        algorithm = ALGORITHM
    )

    return encoded_jwt



# read a token string, return payload data if valid
def verify_access_token ( token: str) -> dict | None: 
    try: 
        payload = jwt.decode (
            token,
            SECRET_KEY, 
            algorithms=[ALGORITHM]
        )

        return payload
    except JWTError as e: 
        # add log warning
        logger.warning( f"Invalid JWT: {e}")
        return None 