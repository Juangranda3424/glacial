import './env.js';

const getEnv = (name: string): string => {
    const value = process.env[name];

    if (!value) {
        throw new Error(`La variable ${name} no está configurada`);
    }

    return value;
};

export const config = {
    port: Number(process.env.PORT_INVENTORY_KARDEX ?? 3002),

    frontendUrl: getEnv('URL_DOMAIN'),

    jwt: {
        publicKey: getEnv('PUBLIC_KEY')
    },

    supabase: {
        url: getEnv('SUPABASE_URL'),
        publicUrl: getEnv('SUPABASE_URL_PUBLIC'),
        key: getEnv('SUPABASE_KEY')
    }
};
