---
id: TC-FA-FAAC-E2E-012-alert-dependensi-akun-chart-of-accounts
title: "Alert Dependensi Akun Chart of Accounts: Teks per Account Function, Posisi di Atas Banner, dan Tidak Tampil Saat Lengkap"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-24
  - TC-FA-FAAC-31
  - TC-FA-FAAC-25
  - TC-FA-FAAC-26
sourceRules: ["§4.1.8#p2", "FAAC-LOGIC-20a", "FAAC-LOGIC-20b", "§10#r12", "§4.1.1#p3", "§4.2a#p1", "FAAC-LOGIC-20d"]
smoke: []
dependsOn: []
trace:
  "§4.1.8#p2": [1, 2, 5, 9]
  "FAAC-LOGIC-20a": [1, 9]
  "FAAC-LOGIC-20b": 2
  "§10#r12": 3
  "§4.1.1#p3": [4, 5]
  "§4.2a#p1": 13
  "FAAC-LOGIC-20d": 14
coverage:
  web: automated
---

# Alert Dependensi Akun Chart of Accounts: Teks per Account Function, Posisi di Atas Banner, dan Tidak Tampil Saat Lengkap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state global, Chart of Accounts bersama per client): keadaan awal yang disiapkan hook `before` lewat fixture BE adalah tidak ada akun Active ber-Account Function Asset Cost, akun Active untuk Accumulated Depreciation dan Depreciation Expense tersedia, dan minimal satu Asset Name belum ter-assign ke Asset Class mana pun (untuk banner TC-FA-FAAC-31). Hook `after` memulihkan Chart of Accounts ke keadaan awal run. Seed disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: fixture BE untuk mengatur akun Active per Account Function dan memulihkannya; disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah Chart of Accounts yang dipakai bersama.

## Test Steps

### TC-FA-FAAC-24: Alert dependensi akun saat satu Account Function wajib tidak punya akun Active

1. Verifikasi Alert warning tampil di atas tabel dengan teks `No active account for Asset Cost in Chart of Accounts. Add one so asset classes can map their accounts.`
2. Verifikasi Alert memuat link `[Go to Chart of Accounts]`
3. Verifikasi Alert tidak memiliki tombol tutup `✕` sehingga tidak dapat ditutup

### TC-FA-FAAC-31: Alert dependensi akun berada di atas banner Asset Name tanpa Asset Class

4. Verifikasi banner Asset Name tanpa Asset Class tampil di atas tabel
5. Verifikasi Alert dependensi akun tampil di atas banner Asset Name tanpa Asset Class dan keduanya di atas tabel

### TC-FA-FAAC-25: Alert menyebut beberapa Account Function dengan urutan tetap

6. Atur Chart of Accounts lewat fixture BE hingga tidak ada akun Active ber-Account Function Asset Cost, Accumulated Depreciation, maupun Depreciation Expense
7. Refresh halaman
8. Klik tab Asset Class
9. Verifikasi Alert warning berbunyi `No active account for Asset Cost, Accumulated Depreciation, Depreciation Expense in Chart of Accounts. Add one so asset classes can map their accounts.` dengan nama Function berurutan Asset Cost, Accumulated Depreciation, Depreciation Expense dipisah koma

### TC-FA-FAAC-26: Alert tidak tampil saat semua Account Function wajib punya akun Active

10. Atur Chart of Accounts lewat fixture BE hingga ada minimal satu akun Active untuk Asset Cost, Accumulated Depreciation, dan Depreciation Expense
11. Refresh halaman
12. Klik tab Asset Class
13. Verifikasi tabel Asset Class tampil di bawah Toolbar
14. Verifikasi Alert dependensi akun Hidden

## Notes

- Langkah penghubung (S-03): langkah 6 dan 10 (mengatur Chart of Accounts lewat fixture BE sebagai precondition tiap TC), langkah 7 dan 8, 11 dan 12 (memuat ulang tab agar Alert dihitung ulang; TC-FA-FAAC-25 dan TC-FA-FAAC-26 langkah 1 berbunyi "Klik tab Asset Class").
- Urutan TC dalam spec: 24, 31, 25, 26. Dua blok pertama memakai keadaan awal hook `before`; keadaan Chart of Accounts lengkap (TC-FA-FAAC-26) di akhir.
- Absence Alert pada langkah 14 didahului langkah 13 (tabel dan Toolbar tampil) sebagai anchor positif (8b butir 2).
- TC-FA-FAAC-27, TC-FA-FAAC-28, TC-FA-FAAC-29, dan TC-FA-FAAC-30 (interaksi Alert) ada di spec 018.
- Temuan untuk QA:
  - TC-FA-FAAC-26 butir "tabel langsung tampil di bawah Toolbar" tidak menyebut banner Asset Name tanpa Asset Class; spec mengasersi tabel di bawah Toolbar dan Alert dependensi akun Hidden, tanpa mengasersi ketiadaan banner.
