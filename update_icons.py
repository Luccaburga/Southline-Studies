import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CDN
html = html.replace('<script src="https://unpkg.com/@phosphor-icons/web"></script>', 
'''<!-- IonIcons (Elegante, nativo iOS) -->
    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>''')

# Replace Hero Clouds
old_clouds = '''<div class="hero-bg-logo-wrapper">
            <img src="Imagen_nube.png" alt="" class="hero-cloud cloud-1">
            <img src="Imagen_nube.png" alt="" class="hero-cloud cloud-2">
            <img src="Imagen_nube.png" alt="" class="hero-cloud cloud-3">
            <img src="LogoMarca1.png" alt="Southline Studio Logo Animado" class="hero-bg-logo">
        </div>'''
new_clouds = '''<div class="hero-bg-logo-wrapper">
            <img src="Imagen_nube.png" alt="Cloud Background" class="hero-bg-sky">
            <img src="LogoMarca1.png" alt="Southline Studio Logo Animado" class="hero-bg-logo">
        </div>'''
html = html.replace(old_clouds, new_clouds)

# Replace WhatsApp Links
html = html.replace('href="#contacto" class="btn btn-primary"', 'href="https://wa.me/5491127201600" target="_blank" class="btn btn-primary"')
html = html.replace('href="https://wa.me/1234567890"', 'href="https://wa.me/5491127201600"')
html = html.replace('1234567890', '5491127201600')

# Dictionary of Phosphor classes to IonIcons
icon_map = {
    'ph ph-list': 'menu-outline',
    'ph-bold ph-caret-down': 'chevron-down-outline',
    'ph ph-arrow-right': 'arrow-forward-outline',
    'ph-fill ph-check-circle': 'checkmark-circle',
    'ph-fill ph-robot': 'hardware-chip-outline',
    'ph-fill ph-storefront': 'storefront-outline',
    'ph-fill ph-browser': 'globe-outline',
    'ph-fill ph-user-focus': 'person-circle-outline',
    'ph-fill ph-chat-circle-dots': 'chatbubbles-outline',
    'ph ph-x-circle text-accent': 'close-circle-outline" class="text-accent',
    'ph ph-layout': 'browsers-outline',
    'ph ph-buildings': 'business-outline',
    'ph ph-wrench': 'build-outline',
    'ph ph-whatsapp-logo': 'logo-whatsapp',
    'ph-fill ph-trend-up': 'trending-up-outline',
    'ph-fill ph-clock': 'time-outline',
    'ph-fill ph-currency-circle-dollar': 'cash-outline',
    'ph ph-check text-accent': 'checkmark-outline" class="text-accent',
    'ph ph-paper-plane-tilt': 'paper-plane-outline',
    'ph ph-caret-down': 'chevron-down-outline',
    'ph ph-hands-clapping contact-icon text-accent': 'happy-outline" class="contact-icon text-accent',
    'ph ph-envelope-simple': 'mail-outline',
    'ph ph-envelope': 'mail-outline'
}

for ph_cls, ion_name in icon_map.items():
    pattern = r'<i class="' + re.escape(ph_cls) + r'"></i>'
    replacement = f'<ion-icon name="{ion_name}"></ion-icon>'
    html = re.sub(pattern, replacement, html)

# Extra fallback for any missed ph icons
# regex to catch: <i class="something ph-something"></i>
# Although we mapped all exactly. Let's do a fallback replace for anything with ph-
html = re.sub(r'<i class="ph[^"]*"></i>', '<!-- icon replaced -->', html) # Just in case

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML Updated!")

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.nav-link i', '.nav-link ion-icon')

old_cloud_css = '''.hero-cloud {
    position: absolute;
    z-index: -1;
    filter: blur(15px);
    opacity: 0.7;
    pointer-events: none;
}
.cloud-1 { top: 5%; left: 5%; width: 400px; animation: floatCloud 25s ease-in-out infinite alternate; filter: blur(25px); opacity: 0.5; }
.cloud-2 { bottom: 5%; right: 5%; width: 500px; animation: floatCloud 20s ease-in-out infinite alternate-reverse; filter: blur(20px); opacity: 0.6; }
.cloud-3 { top: 40%; right: 15%; width: 350px; animation: floatCloud 30s ease-in-out infinite alternate; opacity: 0.4; filter: blur(30px); }

@keyframes floatCloud {
    0% { transform: translateY(0) translateX(0); }
    100% { transform: translateY(-50px) translateX(30px); }
}'''

new_cloud_css = '''.hero-bg-sky {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    z-index: -1;
    opacity: 0.8;
    pointer-events: none;
}'''

css = css.replace(old_cloud_css, new_cloud_css)

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS Updated!")
