import os
from dataclasses import dataclass

from . import env  # noqa: F401  (al importarlo se carga el .env)


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"La variable {name} no está configurada")
    return value


@dataclass(frozen=True)
class JwtConfig:
    public_key: str


@dataclass(frozen=True)
class SupabaseConfig:
    url: str
    public_url: str
    key: str


@dataclass(frozen=True)
class Config:
    port: int
    frontend_url: str
    jwt: JwtConfig
    supabase: SupabaseConfig


config = Config(
    port=int(os.getenv("PORT_COMMERCIAL", 3002)),
    frontend_url=get_env("URL_DOMAIN"),
    jwt=JwtConfig(
        public_key=get_env("PUBLIC_KEY"),
    ),
    supabase=SupabaseConfig(
        url=get_env("SUPABASE_URL"),
        public_url=get_env("SUPABASE_URL_PUBLIC"),
        key=get_env("SUPABASE_KEY"),
    ),
)