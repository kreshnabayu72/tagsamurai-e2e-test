---
id: TC-GS-USER-E2E-068-user-log-kolom-dan-sort
title: 'Tab User Log: kolom, format Device / Browser, dan sort IP Address berbasis string'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-112
  - TC-GS-USER-356
coverage:
  web: automated
---

# Tab User Log: kolom, format Device / Browser, dan sort IP Address berbasis string

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Doni Pratama" punya riwayat login berhasil dan gagal, logout, serta sesi produk (Fixed Asset)
- Riwayat memuat setidaknya satu baris dengan Device / Browser tidak terparse, dan baris dengan IP Address `9.1.1.1` serta `10.0.0.1`
- Spec ini tidak mengubah data

## Test Steps

### Kolom dan isi

1. Buka User Detail "Doni Pratama" > Tab User Log
2. Verifikasi 6 kolom persis: Date, Activity, Status, Note, IP Address, Device / Browser, dengan urutan default Date terbaru dulu
3. Verifikasi Device / Browser berformat "[Browser] on [OS]" (mis. "Chrome on Windows") dan `—` bila tidak terparse
4. Verifikasi Login berhasil dan gagal menampilkan Status sebagai teks biasa, sedangkan Logout dan Session menampilkan Status `—`
5. Verifikasi Note sesi bersufiks produk, mis. "Session started (Fixed Asset)"

### Sort IP Address

6. Klik header kolom IP Address untuk urutan naik
7. Verifikasi `10.0.0.1` tampil sebelum `9.1.1.1`, karena urutannya alfabetis berbasis string dan bukan numerik per oktet

## Notes

- Sumber `user.md` bagian 4.2, 4.2a (Tab: User Log), dan 8.4.
- TC sumber `TC-GS-USER-356` memakai contoh `10.0.0.1` dan `192.168.1.5`, yang tampil dengan urutan sama pada sort string maupun numerik. Spec ini memakai `9.1.1.1` dan `10.0.0.1` supaya kedua cara sort berbeda hasilnya.
- Riwayat login dan IP tertentu disiapkan tim FE lewat seeding atau login berulang.
