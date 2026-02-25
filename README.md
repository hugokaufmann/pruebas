# pruebas

Instrucciones rápidas:

- Crear un entorno virtual e instalar dependencias.
- Configurar la variable de entorno `DJANGO_SECRET_KEY` antes de desplegar.

Ejemplo (Linux/macOS):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Copiar .env.example a .env y editar
cp .env.example .env
export DJANGO_SECRET_KEY="$(cat .env | grep DJANGO_SECRET_KEY | cut -d'=' -f2-)"
python manage.py migrate
python manage.py runserver
```

Nota: `pruebas/settings.py` ya intenta leer `DJANGO_SECRET_KEY` desde el entorno. Si el repo es público, rota la clave que esté expuesta en `settings.py` y no la compartas.