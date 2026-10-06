---
id: TC-AC-SU-E2E-036-detail-user-tab-system-log-display-filter-dan-export
title: "Detail User Tab System Log (aksi oleh user ini sebagai aktor): struktur kolom, scoping per-app, dan export CSV"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-134
  - TC-AC-SU-135
  - TC-AC-SU-137
  - TC-AC-SU-138
  - TC-AC-SU-139
  - TC-AC-SU-141
coverage:
  web: automated
---

# Detail User Tab System Log (aksi oleh user ini sebagai aktor): struktur kolom, scoping per-app, dan export CSV

## Prerequisites

- Login sebagai Role: Principal Total Control
- Target pengguna adalah admin yang pernah melakukan mutasi (Activate/Deactivate/Edit role) terhadap user lain di Admin Console

## Test Steps

### Screening Tab System Log dan Verifikasi Struktur

1. Buka Detail User > Tab `System Log` untuk admin target
2. Verifikasi tabel memuat 7 kolom data: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`
3. Verifikasi entri log yang tampil adalah seluruh aksi yang dilakukan OLEH pengguna ini sebagai aktor, di mana kolom `Name` mencantumkan target user yang dimodifikasi
4. Verifikasi urutan default tabel adalah kolom `Date` Descending

### Verifikasi Aturan Entri dan Export

1. Periksa kemungkinan nilai pada kolom Action, verifikasi aksi `Create User` dan `Delete User` TIDAK PERNAH muncul (karena modul ini tidak memiliki fitur CRUD identitas user)
2. Verifikasi event `Email Confirmed` tidak muncul di tab ini (merupakan event identitas GS)
3. Amati kolom `Object` pada entri edit role yang dipicu dari Tab Role, verifikasi tertulis `Object = Settings > User > Role`
4. Klik tombol `[Download]`, verifikasi file terunduh dengan nama `System-Log-[User Name].csv`

## Notes

- System Log di Admin Console terisolasi per aplikasi dan tidak dikonsolidasikan ke Global Settings.
