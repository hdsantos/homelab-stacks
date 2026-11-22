from prometheus_client import start_http_server, Gauge
import subprocess
import re

g = Gauge('intel_gpu_engine_busy_percent', 'Intel GPU busy', ['engine'])

if __name__ == '__main__':
    start_http_server(9981)
    print("Exporter iniciado na 9981")
    proc = subprocess.Popen(['intel_gpu_top', '-J', '-s', '500'], stdout=subprocess.PIPE, text=True, bufsize=1)
    curr_engine = None
    for line in proc.stdout:
        m_eng = re.search(r'"(Render/3D|Blitter|Video|VideoEnhance)"\s*:', line)
        if m_eng:
            curr_engine = m_eng.group(1)
        m_busy = re.search(r'"busy"\s*:\s*([\d\.]+)', line)
        if m_busy and curr_engine:
            try:
                busy = float(m_busy.group(1))
                g.labels(engine=curr_engine).set(busy)
            except:
                pass
            curr_engine = None
