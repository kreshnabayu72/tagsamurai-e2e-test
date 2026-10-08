---
id: TC-GS-ACTLOG-E2E-047-sinkronisasi-format-tanggal-dan-waktu-general-settings
title: "Sinkronisasi Format Tanggal dan Waktu Mengikuti Konfigurasi General Settings di Kedua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-191
  - TC-GS-ACTLOG-192
  - TC-GS-ACTLOG-193
  - TC-GS-ACTLOG-194
coverage:
  web: automated
---

# Sinkronisasi Format Tanggal dan Waktu Mengikuti Konfigurasi General Settings di Kedua Tab

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat entri log tersimpan pada UTC 14 Jul 2026, 17:30

## Test Steps

### Konfigurasi Format DD/MM/YY (24 Jam)
1. Konfigurasikan General Settings: Date Format 'DD/MM/YY', Time Format 'HH:mm', Time Zone '(UTC+07:00) Bangkok, Hanoi, Jakarta'.
2. Buka Tab Session, amati sel kolom Date pada entri uji.
3. Verifikasi sel Date menampilkan tanggal '15/07/26' dan waktu '00:30'.
4. Buka Tab User Action, verifikasi sel Date menampilkan format yang sama.
5. Buka Filter Panel, pilih tanggal 14 Jul 2026 pada field Date, verifikasi teks input menampilkan '14/07/26'.
### Konfigurasi Format DD MMM YY (12 Jam)
6. Ubah General Settings: Date Format 'DD MMM YY', Time Format 'hh:mm a', Time Zone '(UTC+08:00) Kuala Lumpur, Singapore, Makassar'.
7. Buka kembali Tab Session dan User Action.
8. Verifikasi sel Date pada kedua tab menampilkan tanggal '15 Jul 26' dan jam '01:30 AM'.
### Perubahan Format Dinamis
9. Lakukan pergantian format tanggal di General Settings pada tab browser lain, simpan.
10. Kembali ke Activity Log dan muat ulang halaman, verifikasi seluruh format tanggal langsung terkonversi sesuai format terbaru.

## Notes

- Format stempel waktu mematuhi konfigurasi terpusat General Settings secara real-time.
