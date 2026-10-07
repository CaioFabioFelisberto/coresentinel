import logging
import time
from datetime import datetime
import psutil
from plyer import notification

# Configuração de Logs
LOG_FILE = "system_health.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Limites de Alerta (Thresholds)
THRESHOLD_RAM_PERCENT = 90.0
THRESHOLD_CPU_PERCENT = 90.0
THRESHOLD_DISK_TEMP = 60.0 

INTERVALO_VERIFICACAO_SEGUNDOS = 0.5

def enviar_notificacao(titulo: str, mensagem: str):
    """Dispara notificação nativa no SO."""
    try:
        notification.notify(
            title=titulo,
            message=mensagem,
            app_name="System Health Monitor",
            timeout=5
        )
    except Exception as e:
        logging.error(f"Falha ao enviar notificação nativa: {e}")

def obter_temperatura_cpu():
    """Tenta obter temperatura da CPU (suporte nativo psutil varia no Windows/Linux)."""
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                for entry in entries:
                    if entry.current:
                        return entry.current
    return None

def monitorar_sistema():
    logging.info("Iniciando Agente de Monitoramento do Sistema...")
    print("🚀 Monitor de Saúde do Sistema iniciado. Pressione Ctrl+C para encerrar.")

    while True:
        try:
            ram_uso = psutil.virtual_memory().percent
            cpu_uso = psutil.cpu_percent(interval=1)
            cpu_temp = obter_temperatura_cpu()

            log_msg = f"RAM: {ram_uso}% | CPU: {cpu_uso}%"
            if cpu_temp:
                log_msg += f" | Temp CPU: {cpu_temp}°C"
            
            logging.info(log_msg)

            # 2. Verificação de Alertas
            # Alerta RAM
            if ram_uso >= THRESHOLD_RAM_PERCENT:
                alerta = f"Uso de RAM crítico: {ram_uso}%"
                logging.warning(alerta)
                enviar_notificacao("⚠️ Alerta de Memoria", alerta)

            # Alerta CPU
            if cpu_uso >= THRESHOLD_CPU_PERCENT:
                alerta = f"Uso de CPU elevado: {cpu_uso}%"
                logging.warning(alerta)
                enviar_notificacao("⚠️ Alerta de Processador", alerta)

        except Exception as e:
            logging.error(f"Erro durante a rodada de monitoramento: {e}")

        time.sleep(INTERVALO_VERIFICACAO_SEGUNDOS)

if __name__ == "__main__":
    try:
        monitorar_sistema()
    except KeyboardInterrupt:
        print("\n🛑 Monitor encerra com sucesso.")
        logging.info("Agente finalizado pelo usuario.")