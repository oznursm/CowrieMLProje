CowrieMLProje — Cowrie honeypot loglarını makine öğrenmesi ile analiz eden proje.Proje Hakkında

Bu proje, Cowrie honeypot tarafından toplanan saldırı loglarını işleyip makine öğrenmesi yöntemleriyle analiz ederek anomali tespiti yapmayı amaçlar. ELK stack ile entegrasyon ve veri görselleştirmesi de içerir.

Kurulum

    Python 3.8+ yüklü olmalı.

    Sanal ortam oluştur:

python3 -m venv mlenv
source mlenv/bin/activate  # Linux/macOS  
mlenv\Scripts\activate     # Windows

    Gerekli kütüphaneleri yükle:

pip install -r requirements.txt

    Cowrie log dosyası /home/cowrie/cowrie/var/log/cowrie/cowrie.json konumunda olmalı.

    Kullanım

python main.py

    Program Cowrie loglarını okuyup makine öğrenmesi analizi yapacak.

    Sonuçlar ELK stack üzerinde gösterilecek.

Özellikler

    Cowrie loglarından veri temizleme ve ön işleme

    Anomali tespiti için makine öğrenmesi modelleri (ör. Isolation Forest)

    Sonuçların Elasticsearch ve Kibana ile görselleştirilmesi

