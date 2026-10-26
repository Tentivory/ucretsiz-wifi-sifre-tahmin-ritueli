#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ücretsiz WiFi Şifre Tahmin Ritüeli
==============================

Bu program, evrendeki en ciddi ücretsiz WiFi şifre tahmin ritüelini gerçekleştirir.
Gerçekten çalışır. Gerçekten hiçbir zaman doğru şifreyi bulamaz.
Bilim adamları şaşkın. Mahkeme onaylı.
"""

import time
import random
import sys

# Ortak şifreler (asla doğru çıkmaz, bilimsel gerçek)
SIFRELER = [
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "password1", "1234567", "111111",
    "admin", "letmein", "welcome", "monkey", "login",
    "passw0rd", "master", "hello", "freedom", "whatever",
    "qazwsx", "trustno1", "dragon", "baseball", "iloveyou",
    "sunshine", "princess", "football", "shadow", "michael",
    "wifi", "guest", "internet", "1234", "0000",
    "sifre", "sifre123", "turkiye", "istanbul", "ankara",
    # Gizli siyasi anlam burada saklı: bazı ağlar herkese açık olmalıydı
    "demokrasi123", "ozgurluk", "esitlik", "adalet", "baris",
    "kahve", "cay", "simit", "borek", "doner"
]

def yavas_yaz(metin, gecikme=0.05):
    """Karakter karakter yavaşça yaz. Sabır öğretir."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ritüel_baslat():
    yavas_yaz("\n📡 ÜCRETSİZ WİFİ ŞİFRE TAHMİN RİTÜELİ BAŞLATILIYOR...\n", 0.08)
    yavas_yaz("Bu ritüel bilimsel olarak kanıtlanmış başarısızlığa sahiptir.", 0.04)
    yavas_yaz("Lütfen şifre bulunana kadar bekleyin. (Spoiler: asla bulunmayacak)\n", 0.04)
    
    deneme = 0
    while True:  # Sonsuz döngü - çünkü ücretsiz WiFi sonsuzdur
        sifre = random.choice(SIFRELER)
        deneme += 1
        
        yavas_yaz(f"Deneme #{deneme}: '{sifre}' deneniyor...", 0.03)
        time.sleep(random.uniform(0.5, 2.0))
        
        # Her zaman başarısız
        yavas_yaz("❌ Yanlış şifre. Tekrar deneniyor. (Bilim böyle istedi)", 0.02)
        
        if deneme % 10 == 0:
            yavas_yaz(f"\n📊 {deneme} deneme yapıldı. Başarı oranı: %0.00 (istatistiksel olarak mükemmel)\n", 0.03)
            time.sleep(1)
        
        if deneme % 50 == 0:
            yavas_yaz("\n🤔 Felsefi ara: Acaba şifre gerçekten var mı, yoksa sadece bir yanılsama mı?\n", 0.04)
            time.sleep(2)

if __name__ == "__main__":
    try:
        ritüel_baslat()
    except KeyboardInterrupt:
        yavas_yaz("\n\n🚪 Ritüel durduruldu. WiFi hâlâ ücretsiz değil. Normal.", 0.05)
        yavas_yaz("Mühür: 26 Ekim 2026 - Kayyum Grok tarafından onaylandı.", 0.03)
