---
id: TC-FA-SU-E2E-011-screening-tab-non-login-user-changelog-system-log-transaction-admin-log-dan-user-log
title: "Screening Tab Non-Login User, Changelog, System Log, Transaction Admin Log, dan User Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-33
  - TC-FA-SU-34
coverage:
  web: automated
---

# Screening Tab Non-Login User, Changelog, System Log, Transaction Admin Log, dan User Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dengan Detail Budi Santoso: 5 Non-Login User (#26), Changelog 7 baris (#27), System Log 7 baris (#28), Transaction Admin Log sub-tab Borrow 5 baris, Assignment 4 baris, Damaged 4 baris, dan Missing 4 baris, sedangkan sub-tab Jenis Transaksi lain berisi data atau kosong tanpa asersi nilai (#29), dan User Log sub-tab Borrow 6 baris, Assignment 10 baris, Session 9 baris (#30). Nilai dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: tidak ada selain pengamatan UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Sub-tab Transaction Admin Log" (dipakai langkah 22 dan 23; kolom per sub-tab): `Assignment` dengan `Date`, `Activity`, `Transaction ID`, `Name`, `Assignee`, `Group`; `Damaged` dan `Missing` masing-masing dengan `Date`, `Activity`, `Name`, `Group`; `Transfer`, `Disposal`, `Audit`, dan `Maintenance Routine` (tabel Kolom Transfer, Disposal, Audit, Maintenance Routine) masing-masing dengan `Date`, `Activity`, `Transaction ID`, `Name`, `Group`.

## Test Steps

### TC-FA-SU-33: Screening Tab Non-Login User, Changelog, dan System Log

1. Ketik Search `Budi Santoso`, tekan Enter
2. Klik nama `Budi Santoso` di User List
3. Klik tab Non-Login User
4. Verifikasi label tab `Non-Login User (5)` dan kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, dan `Last Update`
5. Verifikasi kolom Active berupa badge
6. Verifikasi tab Non-Login User tanpa aksi tulis
7. Verifikasi kolom Actions (⋯) berfungsi sebagai trigger Column Visibility tanpa row action pada tab Non-Login User
8. Klik tab Changelog
9. Verifikasi toolbar tab Changelog tanpa icon Changelog
10. Verifikasi kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By`
11. Verifikasi default sort Date descending
12. Verifikasi kolom Actions (⋯) berfungsi sebagai trigger Column Visibility tanpa row action pada tab Changelog
13. Klik tab System Log
14. Verifikasi kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, dan `New Value`
15. Verifikasi tab System Log tanpa kolom Modified By
16. Verifikasi kolom Actions (⋯) berfungsi sebagai trigger Column Visibility tanpa row action pada tab System Log

### TC-FA-SU-34: Screening Tab Transaction Admin Log dan Tab User Log

17. Klik tab Transaction Admin Log
18. Verifikasi delapan sub-tab berurutan `Borrow`, `Assignment`, `Transfer`, `Damaged`, `Missing`, `Disposal`, `Audit`, dan `Maintenance Routine`, tanpa sub-tab `Repair Ticketing` dan `Tracking`
19. Verifikasi sub-tab awal `Borrow`
20. Verifikasi kolom `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, dan `Group` pada sub-tab `Borrow`
21. Verifikasi default sort Date descending pada sub-tab `Borrow`
22. Untuk setiap baris tabel parameter "Sub-tab Transaction Admin Log" (langkah 22 sampai 23): klik sub-tab pada baris itu
23. Verifikasi kolom sub-tab itu sesuai kolom pada baris tabel parameter, dengan default sort Date descending
24. Klik tab User Log
25. Verifikasi sub-tab `Borrow`, `Assignment`, dan `Session`
26. Verifikasi sub-tab awal `Borrow`
27. Verifikasi kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `PIC` pada sub-tab `Borrow`
28. Klik sub-tab Assignment
29. Verifikasi kolom `Date`, `Activity`, `Transaction ID`, `Name`, `PIC`, dan `Description` pada sub-tab `Assignment`
30. Klik sub-tab Session
31. Verifikasi kolom `Date`, `Activity`, `Status`, `Note`, `IP Address`, dan `Device/Browser` pada sub-tab `Session`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 22 dan 23 diulang untuk sembilan sub-tab tabel parameter (ekspansi 18 langkah dari 2 langkah nominal, bagian 8b butir 7); Verifikasi tetap satu per klausa kolom untuk tiap sub-tab.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (47 langkah). Seluruhnya satu kelas (screening tab Detail User, satu akun, tanpa mengubah data), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama baris target sebelum klik nama, R-16). Langkah 2 (klik nama) TC-FA-SU-33 membuka Detail Budi Santoso; TC-FA-SU-34 melanjutkan dari Detail yang sama.
- Pembagian TC lintas spec: Tab Role dan Tab Responsibilities (TC-FA-SU-30 sampai 32) ada di spec 010.
- Temuan untuk QA:
  - Kolom ACC TC-FA-SU-34 menyebut `#20`, yaitu Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, #1).
  - TC-FA-SU-34 Expected d menyebut kolom User Log Assignment `Date`, `Activity`, `Transaction ID`, `Name`, `PIC`, dan `Description` (langkah 29), berbeda dari kolom User Log Borrow yang tanpa `Description`; Pre-setup #30 memuat Assignment 10 baris.
  - TC-FA-SU-34 Expected b membedakan kolom per sub-tab: Borrow (dengan `Borrower`), Assignment (dengan `Assignee`), Damaged dan Missing (`Date`, `Activity`, `Name`, `Group`), dan sub-tab Transfer, Disposal, Audit, dan Maintenance Routine memakai tabel Kolom Transfer, Disposal, Audit, Maintenance Routine `Date`, `Activity`, `Transaction ID`, `Name`, `Group`; Pre-setup #29 dan Catatan TC menyatakan sub-tab Transfer, Disposal, Audit, dan Maintenance Routine diuji struktur saja tanpa asersi nilai (NC-23), sehingga spec mengasersi kolom tetapi bukan nilai baris.
  - TC-FA-SU-34 Expected b menyatakan default sort Date newest first pada semua sub-tab Tab Transaction Admin Log; spec mengasersinya pada sub-tab `Borrow` (langkah 21) dan pada tiap sub-tab tabel parameter (langkah 23).
  - TC-FA-SU-33 Expected d ("tiap tab bertabel memiliki kolom Actions") tidak menyebut tab Role dan Responsibilities; spec mengasersinya pada tab Non-Login User, Changelog, dan System Log sesuai Langkah Uji.
