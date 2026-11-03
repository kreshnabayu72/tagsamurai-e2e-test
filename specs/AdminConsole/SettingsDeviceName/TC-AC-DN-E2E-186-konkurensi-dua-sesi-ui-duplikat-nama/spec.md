---
id: TC-AC-DN-E2E-186-konkurensi-dua-sesi-ui-duplikat-nama
title: "Konkurensi Dua Sesi UI: Create dan Edit ke Nama yang Sama, Submit Kedua Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-576
  - TC-AC-DN-572
coverage:
  web: automated
---

# Konkurensi Dua Sesi UI: Create dan Edit ke Nama yang Sama, Submit Kedua Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi pertama: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi kedua (konteks browser terpisah, hasilnya diasersi): Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Sesi kedua login dan membuka halaman pada langkah 2 dan 3, dan konteksnya ditutup pada langkah 35.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Measurement `Unit`, node pohon Category `Antenna`. Nama dinamis dibentuk `<nama dasar> {runId}-186` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after`; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Nama | Measurement | Category | Dipakai oleh |
  |---|---|---|---|---|
  | N1 | `Race Scanner {runId}-186` (sesi pertama) dan `race scanner {runId}-186` (sesi kedua) | `Unit` | `Antenna` | TC-AC-DN-576 (dibuat langkah UI) |
  | R1 | `Cable Konflik {runId}-186` | `Unit` | `Antenna` | TC-AC-DN-572 (diubah sesi pertama menjadi `Shared Name {runId}-186`) |
  | R2 | `Door Konflik {runId}-186` | `Unit` | `Antenna` | TC-AC-DN-572 (diubah sesi kedua menjadi `shared name {runId}-186`) |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

1. Buka konteks browser kedua
2. Di sesi kedua, login sebagai Maya Putri (`Spectra.env.AC_DN_TC2_PASSWORD`)
3. Di sesi kedua, buka halaman `Settings > Device > Device Name`

### TC-AC-DN-576: Dua sesi Create nama sama berbeda huruf besar-kecil

4. Di sesi pertama, klik `+ Device Name`
5. Di sesi pertama, ketik "Race Scanner {runId}-186" pada field Device Name, pilih Measurement `Unit`, dan Category `Antenna`
6. Di sesi kedua, klik `+ Device Name`, ketik "race scanner {runId}-186" pada field Device Name, pilih Measurement `Unit`, dan Category `Antenna`
7. Di sesi pertama, klik `[Submit]`
8. Verifikasi toast sukses "Success, device name has been created." di sesi pertama
9. Di sesi kedua, klik `[Submit]`
10. Verifikasi inline error "Device name already exists" di bawah field Device Name pada sesi kedua
11. Verifikasi form Create sesi kedua tetap terbuka
12. Verifikasi input "race scanner {runId}-186" dipertahankan pada sesi kedua
13. Di sesi kedua, klik icon `(✕)` pada form
14. Di sesi kedua, verifikasi dialog `Unsaved Changes` tampil
15. Di sesi kedua, klik `[Leave]`
16. Di sesi pertama, ketik Search `Race Scanner {runId}-186`, tekan Enter
17. Verifikasi List sesi pertama memuat satu baris "Race Scanner {runId}-186"

### TC-AC-DN-572: Dua sesi Edit dua record ke nama yang sama

18. Di sesi pertama, ketik Search `Konflik {runId}-186`, tekan Enter
19. Di sesi pertama, buka menu aksi pada baris `Cable Konflik {runId}-186`, klik `Edit`
20. Di sesi pertama, kosongkan field Device Name lalu ketik "Shared Name {runId}-186"
21. Di sesi kedua, ketik Search `Konflik {runId}-186`, tekan Enter
22. Di sesi kedua, buka menu aksi pada baris `Door Konflik {runId}-186`, klik `Edit`
23. Di sesi kedua, kosongkan field Device Name lalu ketik "shared name {runId}-186"
24. Di sesi pertama, klik `[Save]`
25. Verifikasi toast sukses "Success, device name has been updated." di sesi pertama
26. Di sesi kedua, klik `[Save]`
27. Verifikasi inline error "Device name already exists" di bawah field Device Name pada sesi kedua
28. Verifikasi form Edit sesi kedua tetap terbuka
29. Verifikasi input "shared name {runId}-186" dipertahankan pada sesi kedua
30. Di sesi pertama, ketik Search `Konflik {runId}-186`, tekan Enter
31. Verifikasi List sesi pertama memuat baris `Door Konflik {runId}-186`
32. Verifikasi List sesi pertama memuat satu baris "Shared Name {runId}-186"
33. Di sesi kedua, kembalikan field Device Name ke nilai tersimpan `Door Konflik {runId}-186`
34. Di sesi kedua, klik icon `(✕)` pada form
35. Tutup konteks browser kedua

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Konteks UI kedua dipakai karena hasil di sesi kedua (inline error, form tetap terbuka) diasersi (bagian 3 butir P-2: konteks yang diasersi bukan pemicu), sehingga spec ini kelas c dan tidak memakai `P-2`. Pelaku kedua tidak lewat sesi API di spec ini.
- Langkah penghubung (S-03, R-16): langkah 1 sampai 3 menyiapkan sesi kedua (login eksplisit, S-07); langkah 16, 18, 21 (Search) menemukan baris record milik spec; langkah 13 sampai 15 menutup form dirty secara deterministik (S-08, S-09); langkah 33 dan 34 mengembalikan field dan menutup form sesi kedua yang tidak berubah dari nilai tersimpan; langkah 35 menutup konteks kedua (S-09).
- Anchor (8b butir 2): toast sukses langkah 25 mendahului asersi List langkah 31 dan 32; baris `Door Konflik {runId}-186` tampil pada langkah 31 sebagai pembanding. TC-AC-DN-572 Expected d ("List memuat satu baris Shared Name dan baris Door Antenna") ditulis dengan nama record milik spec.
- Record milik spec (S-06, S-12): R1 dan R2 menggantikan `Cable Tester` dan `Door Antenna` Pre-setup #16 TC sumber; Pre-setup #16 tidak diubah.
- Urutan: TC-AC-DN-576 mendahului TC-AC-DN-572 supaya sesi kedua yang sama dipakai; urutan ini membalik sourceTc kanonis (572 lalu 576) tanpa dampak pada data karena record tiap blok berdiri sendiri.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-576 (hanya satu record `Race Scanner` tersimpan; diamati lewat langkah 17) dan TC-AC-DN-572 (record `Door Antenna` tidak berubah).
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-186` (S-12).
