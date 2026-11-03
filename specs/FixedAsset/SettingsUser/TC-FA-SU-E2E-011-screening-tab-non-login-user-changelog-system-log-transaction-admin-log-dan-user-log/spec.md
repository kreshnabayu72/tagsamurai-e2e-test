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
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dengan Detail Budi Santoso: 5 Non-Login User (#26), Changelog 7 baris (#27), System Log 7 baris (#28), Transaction Admin Log 5 baris sub-tab Borrowing & Assignment dengan sub-tab lain berisi data atau kosong tanpa asersi nilai (#29), dan User Log sub-tab Borrow 6 baris, Assignment 5 baris, Session 9 baris (#30). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: tidak ada selain pengamatan UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Sub-tab Transaction Admin Log" (dipakai langkah 21 dan 22): `Transfer`, `Disposal`, `Damaged`, `Missing`, `Audit`, `Repair Ticketing`, `Tracking`, `Maintenance Routine`.

## Test Steps

### TC-FA-SU-33: Screening Tab Non-Login User, Changelog, dan System Log

1. Klik nama `Budi Santoso` di User List
2. Klik tab Non-Login User
3. Verifikasi label tab `Non-Login User (5)` dan kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, dan `Last Update`
4. Verifikasi kolom Active berupa badge
5. Verifikasi tab Non-Login User tanpa aksi tulis
6. Verifikasi kolom Actions (⋯) berfungsi sebagai trigger Column Visibility tanpa row action pada tab Non-Login User
7. Klik tab Changelog
8. Verifikasi toolbar tab Changelog tanpa icon Changelog
9. Verifikasi kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By`
10. Verifikasi default sort Date descending
11. Verifikasi kolom Actions (⋯) berfungsi sebagai trigger Column Visibility tanpa row action pada tab Changelog
12. Klik tab System Log
13. Verifikasi kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, dan `New Value`
14. Verifikasi tab System Log tanpa kolom Modified By
15. Verifikasi kolom Actions (⋯) berfungsi sebagai trigger Column Visibility tanpa row action pada tab System Log

### TC-FA-SU-34: Screening Tab Transaction Admin Log dan Tab User Log

16. Klik tab Transaction Admin Log
17. Verifikasi sembilan sub-tab `Borrowing & Assignment`, `Transfer`, `Disposal`, `Damaged`, `Missing`, `Audit`, `Repair Ticketing`, `Tracking`, dan `Maintenance Routine`
18. Verifikasi sub-tab awal `Borrowing & Assignment`
19. Verifikasi kolom `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, dan `Transaction Status` pada sub-tab `Borrowing & Assignment`
20. Verifikasi default sort Date descending pada sub-tab `Borrowing & Assignment`
21. Untuk setiap baris tabel parameter "Sub-tab Transaction Admin Log" (langkah 21 sampai 22): klik sub-tab pada baris itu
22. Verifikasi kolom `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, dan `Transaction Status` pada sub-tab itu
23. Klik tab User Log
24. Verifikasi sub-tab `Borrow`, `Assignment`, dan `Session`
25. Verifikasi sub-tab awal `Borrow`
26. Verifikasi kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `PIC` pada sub-tab `Borrow`
27. Klik sub-tab Assignment
28. Verifikasi kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `PIC` pada sub-tab `Assignment`
29. Klik sub-tab Session
30. Verifikasi kolom `Date`, `Activity`, `Status`, `Note`, `IP Address`, dan `Device/Browser` pada sub-tab `Session`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 21 dan 22 diulang untuk delapan sub-tab tabel parameter (ekspansi 16 langkah dari 2 langkah nominal, bagian 8b butir 7); Verifikasi tetap satu per klausa kolom untuk tiap sub-tab.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (44 langkah). Seluruhnya satu kelas (screening tab Detail User, satu akun, tanpa mengubah data), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah 1 TC-FA-SU-33 membuka Detail Budi Santoso; TC-FA-SU-34 melanjutkan dari Detail yang sama.
- Pembagian TC lintas spec: Tab Role dan Tab Responsibilities (TC-FA-SU-30 sampai 32) ada di spec 010.
- Temuan untuk QA:
  - TC-FA-SU-34 Expected b menyebut kolom untuk Tab Transaction Admin Log tanpa membedakan sub-tab; Pre-setup #29 dan Catatan TC menyatakan delapan sub-tab selain `Borrowing & Assignment` diuji struktur saja tanpa asersi nilai (NC-23), sehingga spec mengasersi kolom tetapi bukan nilai baris.
  - TC-FA-SU-34 Expected b menyebut "default sort Date descending" tanpa menyatakan sub-tab mana; spec mengasersinya pada sub-tab `Borrowing & Assignment` yang berisi 5 baris dengan sedikitnya dua tanggal berbeda.
  - TC-FA-SU-33 Expected d ("tiap tab bertabel memiliki kolom Actions") tidak menyebut tab Role dan Responsibilities; spec mengasersinya pada tab Non-Login User, Changelog, dan System Log sesuai Langkah Uji.
