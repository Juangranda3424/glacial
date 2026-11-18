from supabase import create_client
from src.config import config

supabase = create_client(config.supabase.url, config.supabase.key)