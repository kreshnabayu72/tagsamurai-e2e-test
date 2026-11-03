---
id: TC-FA-RP-E2E-221-modal-changelog-search-dan-filter-4
title: "Modal Changelog: Search dan Filter (4/6)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-719
  - TC-FA-RP-720
  - TC-FA-RP-721
  - TC-FA-RP-722
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter (4/6)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Entri seed #42 ditambahkan fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen (S-12): spec tidak mengasumsikan total entri tetap dan tidak mengasersi total seluruh entri; entri seed dikenali lewat kombinasi Action, User Name, Old Value, dan New Value. Spec ini tidak mengubah data.

## Test Steps

### Isi opsi dropdown Filter (TC 719)

1. Klik ikon Changelog pada toolbar.
2. Klik ikon Filter.
3. Buka dropdown field Action.
4. Verifikasi opsi Action: `Assign`, `Remove`, `Auto-Revert`.
5. Buka dropdown field User Name.
6. Verifikasi opsi User Name: `Rina Wulandari`, `Ahmad Fauzi`, `Budi Santoso`, `Fitri Handayani`, `Maya Anggraeni` (opsi dari entri seed Pre-setup #42; hanya pengguna yang tercatat pada entri log yang menjadi opsi, pengguna tanpa entri tidak muncul; opsi dari entri lain audit trail permanen tidak dihitung).
7. Buka dropdown field Modified By.
8. Verifikasi opsi Modified By: `Siti Rahmawati`, `Prasetyo Hadi`, `Rina Wulandari`.

### Search internal dropdown Filter (TC 720)

9. Buka dropdown field Action.
10. Ketik `aut` pada kotak pencarian dropdown.
11. Verifikasi daftar opsi Action menyempit ke opsi yang memuat `aut` tanpa membedakan huruf besar kecil: `Auto-Revert`.
12. Ganti isi kotak pencarian dropdown dengan `zzz`.
13. Verifikasi dropdown menampilkan keadaan tanpa opsi cocok.
14. Tutup dropdown dengan klik di luar dropdown.

### Logika OR di dalam satu field (TC 721)

15. Pilih opsi `Auto-Revert` dan `Remove` pada field Action.
16. Klik `[Apply]`.
17. Verifikasi entri seed Pre-setup #42 Auto-Revert Fitri Handayani dan Remove Budi Santoso tampil (gabungan OR, bukan irisan; entri seed diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung).
18. Verifikasi entri seed Pre-setup #42 lain tidak tampil.
19. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Logika AND antar field berbeda (TC 722)

20. Pilih opsi `Assign` pada field Action.
21. Pilih opsi `Budi Santoso` pada field User Name.
22. Klik `[Apply]`.
23. Verifikasi dari entri seed Pre-setup #42 (diidentifikasi lewat kombinasi Action, User Name, Old Value, New Value; entri lain dari audit trail permanen tidak dihitung), hanya Assign Budi Santoso (`—` ke `Total Control`) yang tampil.
24. Verifikasi entri seed Remove Budi Santoso (User Name sama, Action berbeda) tidak tampil.
25. Verifikasi entri seed Assign Rina Wulandari, Assign Ahmad Fauzi, dan Assign Maya Anggraeni (Action sama, User Name berbeda) tidak tampil.
26. Klik `[Clear Field]`, lalu klik `[Apply]`.
27. Klik ikon Filter untuk menutup panel.

## Notes

- Langkah penghubung (S-03): langkah 14 (menutup dropdown), 19 dan 26 (membersihkan Filter), dan 27 (menutup panel). Langkah 23 menjadi anchor positif bagi asersi absence langkah 24 dan 25 (bagian 8b butir 2).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 720 Expected butir b ("keadaan tanpa opsi cocok") tidak menyebut teks UI; spec mengasersi keadaan tanpa opsi tanpa menyebut teks.
  - TC 722 tidak menyatakan apakah panel Filter tetap terbuka sesudah `[Apply]`; spec mengasumsikan panel tetap terbuka.
