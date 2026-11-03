---
id: TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android
title: "Mobile Android: Card List, Bottom Sheet, Chip Group, dan Accordion Tab System"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-68
  - TC-AC-RP-69
  - TC-AC-RP-70
  - TC-AC-RP-71
  - TC-AC-RP-72
coverage:
  mobile: automated
---

# Mobile Android: Card List, Bottom Sheet, Chip Group, dan Accordion Tab System

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6); tampilan berupa Card List dengan bottom sheet toolbar. Spec tidak mengubah state server.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang (Tabel Data Uji Pre-setup #22), serta kemampuan mengetuk (tap) dan menahan elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Principal `Siti Nurhaliza`, `totalControlRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_TC_PASSWORD`. Login di aplikasi Android dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #11 (tree group Principal: `Sumatera`), #1 (`Siti Nurhaliza`), #2 (`Bambang Hartono`, Default User), #13 (pemegang Total Control), #14 (penugasan Group Manager `Fajar Nugroho` pada `Sumatera`), #15 (penugasan peran individual untuk jumlah user Tab System).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `+{runId}-017`, maupun cleanup.
- Hook suite web (`beforeEach` pembuka halaman dan flag Guided Tooltip) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah pertama spec ini, dan flag Guided Tooltip `guided_tooltip_seen_role-permission` untuk akun aktor disetel `true` oleh hook `before` suite (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-AC-RP-68: Card List Tab Total Control di mobile

1. Buka halaman `Settings > Role & Permission` di aplikasi Android
2. Verifikasi Tabs dapat di-scroll horizontal bila tidak muat
3. Verifikasi tabel berganti Card List
4. Verifikasi baris 1 card user memuat Name tebal dalam format komponen user (ikon user + "Siti N", dst.) dan `[⋯]`
5. Verifikasi baris 2 card user memuat "Position · Division"
6. Verifikasi baris 3 card user memuat Status
7. Verifikasi toolbar memuat `[⋯]`, `[🔍]`, dan ikon `[Changelog]`
8. Verifikasi tombol "+ Assign" sticky di atas Card List

### TC-AC-RP-69: Bottom sheet toolbar mobile

9. Tap `[⋯]` pada toolbar
10. Verifikasi bottom sheet berisi Column Visibility, Filter, dan Download
11. Tutup bottom sheet
12. Klik tab `System`
13. Tap `[⋯]` pada toolbar Tab System
14. Verifikasi bottom sheet berisi Column Visibility dan Download
15. Verifikasi bottom sheet tidak memuat Filter

### TC-AC-RP-70: Remove Disabled pada card Default User dan diri sendiri

16. Tutup bottom sheet
17. Klik tab `Total Control`
18. Tap `[⋯]` pada card `Bambang Hartono`
19. Verifikasi `Remove` Disabled dengan tooltip "Default User cannot be modified."
20. Tutup menu `[⋯]`
21. Tap `[⋯]` pada card `Siti Nurhaliza`
22. Verifikasi `Remove` Disabled dengan tooltip "You can't manage your own account from here."

### TC-AC-RP-71: Tab Group Manager mobile memakai chip Group

23. Tutup menu `[⋯]`
24. Klik tab `Group Manager`
25. Tap chip "Group" di atas Card List
26. Pilih `Sumatera` pada bottom sheet tree picker
27. Verifikasi card per baris memuat Name dan `[⋯]`, "Group: Sumatera", serta "Position · Division"
28. Verifikasi daftar tersaring ke `Sumatera`

### TC-AC-RP-72: Tab System mobile accordion dengan jumlah user

29. Klik tab `System`
30. Expand accordion Global Role
31. Verifikasi card per role memuat Role Name dan `[⋯]` (menu `Detail`)
32. Verifikasi card per role memuat baris "[N] users" (contoh `Manage group` "8 users")
33. Verifikasi role dengan satu pemegang tampil "1 user"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): langkah 11 dan 16 (menutup bottom sheet), 17 (kembali ke Tab Total Control sebelum TC-AC-RP-70), 20 dan 23 (menutup menu `[⋯]`), 29 (membuka Tab System untuk TC-AC-RP-72). Langkah 12 dan 17 membuka tab yang dibutuhkan asersi berikutnya (S-14).
- Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web; spec ini berjalan di aplikasi Android.
- Temuan untuk QA:
  - TC-AC-RP-68 Expected a menulis "Tabs scroll horizontal bila tidak muat" sebagai kondisi tanpa menyatakan lebar perangkat uji; spec mengasersi sesuai teks TC (langkah 2).
  - TC-AC-RP-69 langkah 3 menyebut `[⋯]` "pada Tab System" tanpa langkah membuka Tab System; spec menambah klik tab `System` (langkah 12) sebagai langkah penghubung.
  - TC-AC-RP-72 Expected menyebut contoh `Manage group` "8 users", tetapi Tabel Data Uji Pre-setup #15 tidak memuat 8 pemegang `Manage group`, dan TC tidak menyebut role mana yang memiliki satu pemegang ("1 user"); spec mengikuti teks TC.
  - TC-AC-RP-71 Expected "daftar tersaring ke `Sumatera`" tanpa menyebut baris mana yang tampil; spec memakai langkah 27 sebagai pembanding bahwa card tampil sebelum asersi tersaring.
  - Post Condition TC-AC-RP-68 sampai 72 bernilai "-" sehingga tidak ada yang diasersi.
