---
id: TC-FA-NOTIF-E2E-004-empty-state-client-tanpa-notifikasi
title: "Empty State Client Tanpa Notifikasi: Badge Hidden, Dropdown Panel, dan Notification Center"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-2
  - TC-FA-NOTIF-16
  - TC-FA-NOTIF-24
coverage:
  web: automated
---

# Empty State Client Tanpa Notifikasi: Badge Hidden, Dropdown Panel, dan Notification Center

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel, Notification Center).
- Akun aktor: Total Control client baru Pre-setup #16 (`newClientTotalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFEMPTY_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; flag `guided_tooltip_seen_fa-notification` = true). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Data: akun #16 tidak punya notifikasi. Spec hanya membaca data dan tidak memicu event apa pun untuk akun ini.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor dan flag Guided Tooltip (akun #16 sudah true).

## Test Steps

### TC-FA-NOTIF-2: Badge Bell icon hidden saat tidak ada notifikasi belum dibaca

1. Verifikasi Bell icon tampil pada top bar
2. Verifikasi badge Bell icon tidak tampil sama sekali (hidden), bukan angka `0` pudar

### TC-FA-NOTIF-16: Dropdown Panel: Empty state saat belum ada notifikasi

3. Klik Bell icon
4. Verifikasi Illustration tampil
5. Verifikasi Title `No notifications yet`
6. Verifikasi Description `You're all caught up! New notifications will appear here.`
7. Verifikasi Header `Notifications` dan `[Show All]` tetap tampil

### TC-FA-NOTIF-24: Notification Center: Empty state Tab All saat belum ada notifikasi

8. Klik `[Show All]` untuk membuka Notification Center
9. Verifikasi Illustration tampil pada Tab All
10. Verifikasi Title `No notifications yet`
11. Verifikasi Description `You're all caught up! New notifications will appear here.`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Asersi tambahan di luar Expected TC (S-03): langkah 1 (Bell icon tampil sebagai anchor positif sebelum asersi badge hidden; 8b butir 2).
- Langkah penghubung (S-03): langkah 8 membuka Notification Center dari Dropdown Panel yang masih terbuka dari langkah 3 (TC-24 menulis "Buka Notification Center").
- Temuan untuk QA:
  - TC-24 tidak menyebut Tab aktif saat halaman dibuka; spec mengasumsikan Tab All aktif secara default (konsisten dengan judul TC).
