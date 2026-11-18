# Para Iniciar un microservicio nuevo con NodeJS con TypeScript y PNPM

Como primer paso, es necesario instalar PNPM de manera global en tu sistema, para ello puedes ejecutar el siguiente comando:

```bash
npm install -g pnpm
``` 

Una vez que tienes PNPM instalado, puedes crear un nuevo proyecto con el siguiente comando:

```bash
pnpm init
```

Luego, es necesario instalar las dependencias necesarias para trabajar con TypeScript. Puedes hacerlo ejecutando el siguiente comando:

```bash
pnpm add express

pnpm add -D nodemon 

pnpm add dotenv cors zod @supabase/supabase-js

pnpm add -D typescript tsx @types/node @types/express @types/cors

```

### Configurar TypeScript (tsconfig.json)

Genera el archivo de configuración de TypeScript ejecutando:

```bash
pnpm tsc --init
```

### Para iniciar el cada microservicio, es necesario agregar un script en el archivo `package.json` para ejecutar el servidor con nodemon. Puedes agregar el siguiente script:


Cada microservicio tendrá un archivo `app.ts` dentro de la carpeta `src`, el cual será el punto de entrada para el servidor. El script para iniciar el servidor con nodemon se verá de la siguiente manera:

```json
"dev": "nodemon --watch src --ext ts,json --exec tsx src/app.ts",
"build": "tsc",
"start": "node dist/app.js"
```

Con esto, podrás iniciar el servidor de tu microservicio ejecutando el siguiente comando:

```bash
pnpm dev

pnpm build && pnpm start
```


# Estructura de el nombre de los archivos

Para la estructura de los archivos, se recomienda seguir una convención de nombres clara y consistente por lo que se nombrar usando camelCase todos los archivos de la siguiente manera:

```
user.service.ts
order.service.ts
product.service.ts
```

# Para iniciar un microservicio nuevo con Python y FastAPI

Cada microservicio tendrá un archivo `app.py` dentro de la carpeta `src`, el cual será el punto de entrada para el servidor. Para iniciar el servidor, puedes ejecutar el siguiente comando:


Como primer paso, es necesario instalar las dependencias necesarias para trabajar con FastAPI. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

```bash
cd microservice-commercial
python -m src.app
```

# Estructura de el nombre de los archivos

Para la estructura de los archivos, se recomienda seguir una convención de nombres clara y consistente por lo que se nombrar usando snake_case todos los archivos de la siguiente manera:

```
user_service.py
order_service.py
product_service.py
```

# Arquitectura de carpetas para cada microservicio

Para la arquitectura de carpetas, se recomienda seguir una estructura clara y organizada para cada microservicio. A continuación, se muestra un ejemplo de cómo podría ser la estructura de carpetas para un microservicio:


Como ejemplo tenemos el microservicio de `auth-service`, el cual sirve de ejemplo para la estructura de carpetas y archivos dentro de cada microservicio.
```
src/
├── controllers/
├── models/
├── routes/
├── services/
├── dto/
├── config/
├── middlewares/
├── repositories/
```

# Commits Semánticos

Se recomienda seguir una convención de commits semánticos para mantener un historial de cambios claro y organizado. A continuación, se muestra un ejemplo de cómo podrían ser los mensajes de commit:

```
feat: Agregar nueva funcionalidad para autenticación de usuarios
fix: Corregir error en la validación de datos en el servicio de productos
docs: Actualizar documentación del microservicio de órdenes
refactor: Refactorizar código para mejorar la legibilidad en el servicio de usuarios
test: Agregar pruebas unitarias para el servicio de autenticación
chore: Actualizar dependencias del proyecto
```

# Instrucciones para la generación de claves RSA

### Para generar un par de claves RSA, puedes utilizar el siguiente script `keypair.sh` que se encuentra en la carpeta `shared-keys` del proyecto. Este script utiliza OpenSSL para generar las claves y guardarlas en la carpeta `shared-keys`.

Como se muestra a continuación, el script `keypair.sh` generará un par de claves RSA (una privada y una pública) y las guardará en la carpeta `shared-keys`. Asegúrate de tener OpenSSL instalado en tu sistema para ejecutar este script correctamente.

```
bash shared-keys/keypair.sh
```