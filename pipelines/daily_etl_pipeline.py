import subprocess
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def run_scripts():
    """Execute the ETL scripts and print detailed status."""
    try:
        print(f"Starting ETL process at {datetime.now()}")

        # Executar o comando Scrapy para extração de dados
        print("Running Scrapy spider...")
        result = subprocess.run(["scrapy", "crawl", "books"], capture_output=True, text=True, cwd=r"..\Club_Books\src\club_books")
        print("Scrapy output:")
        print(result.stdout)
        if result.stderr:
            print("Scrapy errors:")
            print(result.stderr)

        # Executar o script de transformação
        print("Running transformation script...")
        result = subprocess.run(["python", r"..\Club_Books\etl\transform\transform_data.py"], capture_output=True, text=True)
        print("Transformation script output:")
        print(result.stdout)
        if result.stderr:
            print("Transformation script errors:")
            print(result.stderr)

        # Executar o script de carregamento
        print("Running loading script...")
        result = subprocess.run(["python", r"..\Club_Books\etl\load\load_data.py"], capture_output=True, text=True)
        print("Loading script output:")
        print(result.stdout)
        if result.stderr:
            print("Loading script errors:")
            print(result.stderr)

        print(f"ETL process completed at {datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Configurar o agendador para executar o script diariamente
scheduler = BackgroundScheduler()
scheduler.add_job(run_scripts, 'interval', days=1, start_date=datetime.now().replace(hour=00, minute=00, second=0))
scheduler.start()

# Manter o script em execução
try:
    print("Scheduler started. Waiting for jobs.")
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    print("Shutting down scheduler.")
    scheduler.shutdown()

