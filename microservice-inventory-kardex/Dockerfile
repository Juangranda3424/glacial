# docker build -t papijuan/glacial:inventory-kardex-1.0.0 .
# docker push papijuan/glacial:inventory-kardex-1.0.0

# --- Base: Node + pnpm ---
FROM node:22-alpine AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
WORKDIR /app

# --- Etapa 1: Todas las dependencias (incluye devDependencies para compilar) ---
FROM base AS deps
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile

# --- Etapa 2: Compilar TypeScript ---
FROM deps AS build
COPY tsconfig.json ./
COPY src ./src
RUN pnpm run build

# --- Etapa 3: Solo dependencias de producción ---
FROM base AS prod-deps
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --prod --frozen-lockfile

# --- Etapa 4: Imagen final ---
FROM node:22-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production

COPY --chown=node:node package.json ./
COPY --chown=node:node --from=prod-deps /app/node_modules ./node_modules
COPY --chown=node:node --from=build /app/dist ./dist

USER node

EXPOSE 3002

CMD ["node", "dist/app.js"]
