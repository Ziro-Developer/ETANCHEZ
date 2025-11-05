#!/usr/bin/env python3


SAFE_WARN = (
"\n[AVISO] Esta es una simulación. ETANCHEZ NO
realiza acciones dañinas ni accede a archivos reales.\n"
)


# pequeños efectos


def slow_print(s, delay=0.03):
for ch in s:
sys.stdout.write(ch)
sys.stdout.flush()
time.sleep(delay)
sys.stdout.write('\n')




def spinner(duration=2.0, prefix=''):
chars = ['|','/','-','\\']
t0 = time.time()
i = 0
while time.time() - t0 < duration:
sys.stdout.write('\r' + prefix + ' ' + chars[i % len(chars)])
sys.stdout.flush()
time.sleep(0.07)
i += 1
sys.stdout.write('\r' + prefix + ' done\n')




def fake_ips(count=6):
out = []
for _ in range(count):
out.append('.'.join(str(random.randint(1,254)) for _ in range(4)))
return out




def main():
print(CLEAR)
print(ASCII)
slow_print("Iniciando comprobación de integridad...", 0.02)
spinner(1.4, '[Sistema]')


for msg in MESSAGES:
slow_print(f"[ETANCHEZ] {msg}", delay=0.02 + random.random()*0.02)
spinner(0.8, '[...]')


slow_print('\nEnumerando nodos sospechosos...')
ips = fake_ips(8)
for ip in ips:
slow_print(f" - Nodo detectado: {ip}")
time.sleep(0.18)


# ASCII glitch
slow_print('\nGenerando arte aleatorio...')
for _ in range(6):
line = ''.join(random.choice('▓▒░█▙▟▛▜▚▞') for _ in range(48))
print(line)
time.sleep(0.06)


slow_print(SAFE_WARN, delay=0.005)


slow_print('Finalizado. Pulse ENTER para salir...', 0.01)
try:
input()
except KeyboardInterrupt:
pass


if __name__ == '__main__':
main()
