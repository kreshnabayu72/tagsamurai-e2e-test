---
id: TC-AC-ACHA-E2E-007-entity-gate-akses-menu-dan-form
title: "Entity Gate: Akses Menu dan Form Allocate per Tipe Entitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-44
  - TC-AC-ACHA-45
  - TC-AC-ACHA-46
  - TC-AC-ACHA-47
coverage:
  web: automated
---

# Entity Gate: Akses Menu dan Form Allocate per Tipe Entitas

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (tabel akun per entitas):

| TC | Entitas | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-44 | Total Control Principal PT ABC | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-45 | Total Control Distributor PT Global Distribusi | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| TC-46 | Total Control Partner CV Mitra Solusi | #43 | `totalControlPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| TC-47 | Total Control Partner CV Karya Mandiri | #46 | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` |

- Login akun aktor pertama (Total Control Principal) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): entitas Pre-setup #2 sampai #5 (PT ABC tanpa wallet; PT Global Distribusi dengan kantong sumber tunggal PT ABC; CV Mitra Solusi dengan kantong sumber tunggal PT Global Distribusi; CV Karya Mandiri dengan dua kantong sumber PT Global Distribusi dan PT ABC). Form dibuka dan ditutup tanpa mengisi field sehingga tidak ada data yang dibuat.
- General Settings Pre-setup #1 tidak diubah. State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD`, `AC_DA_TC_P1_PASSWORD`, dan `AC_DA_TC_P2_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-44: Entity gate Principal

1. Verifikasi item menu `Allocation > Device Allocation` tampil di sidebar
2. Verifikasi halaman List Device Allocation terbuka
3. Klik `[+ Allocation]`
4. Verifikasi form Allocate Device terbuka
5. Verifikasi From berupa label read-only `PT ABC (Principal)`
6. Verifikasi field Pay From tidak dirender sama sekali
7. Verifikasi Preview (Estimated Cost, Your Pocket Balance) tidak dirender
8. Klik `[×]` untuk menutup form Allocate Device

### Ganti akun ke Total Control Distributor

9. Logout dari akun Total Control Principal
10. Login sebagai Total Control Distributor (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)

### TC-AC-ACHA-45: Entity gate Distributor

11. Verifikasi item menu `Allocation > Device Allocation` tampil di sidebar
12. Klik item menu `Allocation > Device Allocation`
13. Verifikasi halaman List Device Allocation terbuka
14. Klik `[+ Allocation]`
15. Verifikasi form Allocate Device terbuka
16. Verifikasi From berupa label read-only `PT Global Distribusi (Distributor)`
17. Verifikasi Pay From pre-filled `PT ABC (Principal)`
18. Verifikasi Pay From disabled
19. Verifikasi tombol `[View Price Catalog]` tampil di samping field Pay From
20. Klik `[×]` untuk menutup form Allocate Device

### Ganti akun ke Total Control Partner CV Mitra Solusi

21. Logout dari akun Total Control Distributor
22. Login sebagai Total Control Partner CV Mitra Solusi (`totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P1_PASSWORD`)

### TC-AC-ACHA-46: Entity gate Partner dengan satu kantong sumber

23. Verifikasi item menu `Allocation > Device Allocation` tampil di sidebar
24. Klik item menu `Allocation > Device Allocation`
25. Verifikasi halaman List Device Allocation terbuka
26. Klik `[+ Allocation]`
27. Verifikasi form Allocate Device terbuka
28. Verifikasi From berupa label read-only `CV Mitra Solusi (Partner)`
29. Verifikasi Pay From pre-filled `PT Global Distribusi (Distributor)`
30. Verifikasi Pay From disabled
31. Klik `[×]` untuk menutup form Allocate Device

### Ganti akun ke Total Control Partner CV Karya Mandiri

32. Logout dari akun Total Control Partner CV Mitra Solusi
33. Login sebagai Total Control Partner CV Karya Mandiri (`totalControlPartner2_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P2_PASSWORD`)

### TC-AC-ACHA-47: Entity gate Partner dengan lebih dari satu kantong

34. Verifikasi item menu `Allocation > Device Allocation` tampil di sidebar
35. Klik item menu `Allocation > Device Allocation`
36. Verifikasi halaman List Device Allocation terbuka
37. Klik `[+ Allocation]`
38. Verifikasi form Allocate Device terbuka
39. Verifikasi Pay From berupa dropdown wajib dipilih dengan placeholder "Select source pocket"
40. Buka dropdown Pay From
41. Verifikasi dropdown Pay From berisi dua opsi berlabel pola "[Source Entity Name] (Type)": `PT Global Distribusi (Distributor)` dan `PT ABC (Principal)`
42. Tekan Esc untuk menutup dropdown
43. Klik `[×]` untuk menutup form Allocate Device

## Notes

- Ukuran spec (di atas 35 langkah): empat blok entitas, tiap blok memakai akun berbeda dan Expected form berbeda (bukan perulangan tabel); tiap Expected menjadi `Verifikasi` sendiri (S-01) dan satu dataset Pre-setup dipakai bersama.
- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec Entity Gate (akses menu dan form per tipe entitas); tidak ada aksi tulis.
- Spec ditulis per blok entitas karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); langkah tiap entitas tidak identik (Expected form berbeda), jadi bukan perulangan tabel. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)).
- Langkah penghubung (S-03): langkah logout dan login pada subjudul "Ganti akun ...", dan langkah `[×]` yang menutup form. Form ditutup dalam keadaan bersih (tidak ada field diisi, Pay From pre-filled bukan input pengguna) sehingga dialog `Unsaved Changes` tidak diharapkan.
- Pembagian TC lintas spec: entity gate Client (TC-48, TC-49) ada di spec 009; isi lengkap form Allocate (field, opsi, validasi) di spec 016 sampai 018.
- Temuan untuk QA:
  - TC-44 sampai TC-47 Langkah Uji 1 menulis "Buka menu Allocation > Device Allocation"; untuk akun pertama halaman sudah dibuka hook `beforeEach`, sehingga spec hanya memverifikasi item menu tampil dan halaman terbuka tanpa mengulang klik menu.
  - TC-46 dan TC-47 tidak memuat Expected untuk `[View Price Catalog]` dan Preview; spec tidak mengasersinya.
  - Perilaku dialog `Unsaved Changes` saat menutup form yang hanya berisi nilai pre-filled (Pay From) tidak dinyatakan TC; spec menganggap form bersih (prinsip 6).
  - Post Condition TC-44 sampai TC-47 bernilai `-`.
