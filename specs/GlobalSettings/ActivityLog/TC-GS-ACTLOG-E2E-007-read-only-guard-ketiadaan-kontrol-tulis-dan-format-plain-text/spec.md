---
id: TC-GS-ACTLOG-E2E-007-read-only-guard-ketiadaan-kontrol-tulis-dan-format-plain-text
title: "Guard Read-Only Modul: Baris Non-Klik, Ketiadaan Kontrol Tulis, dan Format Plain Text"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-15
  - TC-GS-ACTLOG-16
  - TC-GS-ACTLOG-221
coverage:
  web: automated
---

# Guard Read-Only Modul: Baris Non-Klik, Ketiadaan Kontrol Tulis, dan Format Plain Text

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat entri log aktivitas pada kedua tab

## Test Steps

### Baris Non-Klik (Purely Informational)
1. Buka Tab Session, lakukan klik pada area baris tabel (sel Activity, User, maupun Note).
2. Verifikasi kursor tetap berbentuk default (bukan pointer tautan).
3. Verifikasi tidak ada drawer, modal popup, maupun navigasi halaman detail yang terbuka.
4. Buka Tab User Action, lakukan klik pada baris data (sel Action, Object, Name).
5. Verifikasi tidak ada respons interaktif atau modal detail yang terbuka.
### Format Plain Text Tanpa Badge
6. Amati sel kolom Activity dan Status pada Tab Session.
7. Verifikasi nilai Activity dan Status ditampilkan sebagai teks biasa (plain text), tanpa kotak badge berwarna atau background pill.
8. Amati sel kolom Action dan Object pada Tab User Action.
9. Verifikasi nilai Action dan Object ditampilkan sebagai teks biasa tanpa badge berwarna.
### Ketiadaan Kontrol Tulis
10. Periksa toolbar, header tabel, dan footer pada Tab Session.
11. Verifikasi tidak terdapat tombol create, edit, delete, maupun kolom seleksi checkbox/bulk action bar.
12. Periksa toolbar, header tabel, dan footer pada Tab User Action.
13. Verifikasi tidak terdapat tombol create, edit, delete, maupun checkbox seleksi baris.

## Notes

- Sesuai ACTLOG-LOGIC-01 modul ini read-only murni, data audit tidak dapat diedit atau dihapus oleh siapapun.
