echo "Aguardando o banco de dados estar disponível..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Aplicando migrações..."
python manage.py migrate
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput


echo "Iniciando o servidor Django..."
exec gunicorn --bind 0.0.0.0:8000 --workers 2 zaapsign_backend.wsgi:application
