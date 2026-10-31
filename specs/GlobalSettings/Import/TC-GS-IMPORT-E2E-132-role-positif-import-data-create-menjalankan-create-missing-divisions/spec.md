---
id: TC-GS-IMPORT-E2E-132-role-positif-import-data-create-menjalankan-create-missing-divisions
title: "Role positif Import data (Create): menjalankan Create Missing Divisions dan Options tanpa capability Division atau Custom Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-348
  - TC-GS-IMPORT-920
coverage:
  web: automated
---

# Role positif Import data (Create): menjalankan Create Missing Divisions dan Options tanpa capability Division atau Custom Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji dan akun pembanding:

| Role | Akun | Env var |
|---|---|---|
| Import data (Create) Client C (Kiki Amalia), capability Import data C dan R, tanpa capability Division, Position, atau Custom Field | `importCreate_automated_qaTeam3@qwertysystem.net` | `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD` |
| Total Control Client C (Rudi Hartanto), pengamat hasil | `totalControl_automated_qaTeam3@qwertysystem.net` | `Spectra.env.GS_CLIENTC_TC_PASSWORD` |

- Login akun Import data (Create) Client C sekali di hook `before`. Langkah login di `## Test Steps` hanya untuk ganti akun. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Client C); langkah pertama berpindah ke Tab User Login.
- Data Pre-setup (tidak diubah permanen; dipulihkan sesudah tiap TC, Kontrak Fixture R1-R2): Client C tanpa draft Tab User Login; daftar Division berisi 5 item `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` dan `Logistik` belum ada; Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`; `Lembur` dan `Piket` belum menjadi opsi.
- Data Dinamis (fixture baru, berkas literal dari TC):
  - `Fixture.import.userLoginLogistik4` (user-login-logistik-4.csv, D-45): 4 baris User Login standar (Siti Rahmawati, Budi Santoso, Andi Pratama, Rina Wijaya), Division `Logistik`, Position kosong.
  - `Fixture.import.userLoginShiftLembur` (user-login-shift-lembur.csv, D-79): 3 baris, Shift `Lembur` (#1), `lembur ` (#2), `Siang` (#3).
- Kemampuan teknis yang disediakan tim FE/BE: reset draft Client C; penghapusan Division `Logistik` dan opsi `Lembur` hasil spec lewat API; pemulihan sesi.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus Division `Logistik` Client C, hapus opsi `Lembur` dari Custom Field `Shift`, hapus draft Client C, pulihkan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: master data Client C berubah sementara; suite berjalan serial.
- Env var yang dipakai: `GS_CLIENTC_IMPORTCREATE_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-348: Import data (Create) menjalankan Create Missing Divisions

1. Buka Tab User Login pada halaman Import
2. Klik [Upload File] di toolbar dan pilih berkas user-login-logistik-4.csv
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
5. Verifikasi toast sukses "Success, division has been created."
6. Muat ulang halaman Import > User Login
7. Verifikasi keempat baris berstatus `pending`
8. Logout dari akun Import data (Create) Client C
9. Login sebagai Total Control Client C
10. Buka Global Settings > User > Division
11. Verifikasi daftar Division memuat `Logistik` dan berisi 6 baris pada tabel
12. Pulihkan state: hapus Division `Logistik` dan draft Client C lewat fixture
13. Logout dari Total Control Client C
14. Login sebagai Import data (Create) Client C

### TC-GS-IMPORT-920: Import data (Create) menjalankan Create Missing Options

15. Buka Tab User Login pada halaman Import
16. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-lembur.csv
17. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
18. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
19. Verifikasi toast sukses "Success, option has been created."
20. Muat ulang halaman Import > User Login
21. Verifikasi ketiga baris berstatus `pending`
22. Logout dari akun Import data (Create) Client C
23. Login sebagai Total Control Client C
24. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
25. Verifikasi Value Setting `Shift` memuat `Pagi`, `Siang`, `Malam`, `Lembur` dengan `Lembur` di akhir daftar

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-348, 920).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan. Ada dua kali ganti akun eksplisit (langkah 8 sampai 9 dan langkah 22 sampai 23) serta satu kali kembali ke akun Import data (Create) (langkah 13 sampai 14); bagian sesudah ganti akun tetap bermakna karena tiap TC menyiapkan draft sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 15 (berpindah ke Tab User Login); langkah 12 (pemulihan Division `Logistik` dan draft Client C sesuai Kontrak Fixture R1-R2 agar TC-GS-IMPORT-920 mulai tanpa draft); langkah 13 sampai 14 (kembali ke akun Import data (Create) untuk TC kedua). Langkah 6 dan 20 memuat ulang halaman sebagai bagian dari observasi Expected.
- Setelah TC kedua, sesi berakhir di akun Total Control Client C; hook `after` memulihkan sesi ke akun default suite (S-07).
- Prinsip: aktor Import data (Create) tidak memiliki capability Division atau Custom Field, dan justru itu objek uji (hak akses Import data yang cukup). Aksi mutasi dilakukan oleh akun yang diuji; Total Control Client C hanya pengamat hasil.
- Versi negatif untuk role Read Only ada di spec 131.
- Temuan untuk QA:
  - TC-GS-IMPORT-348 menulis `Import data (Create) Client C tanpa capability Create pada modul Division`, sedangkan TC-GS-IMPORT-920 menulis `tanpa capability Manage user and role pada modul Custom Field`; kedua rumusan capability tidak sama (nama capability dan modul) dan tidak ada langkah yang memverifikasi bahwa akun benar-benar tidak memiliki capability itu. Spec mengikuti kedua TC.
  - TC-GS-IMPORT-348 Expected c menyebut "6 baris pada tabel" setelah menambah `Logistik` pada 5 Division Pre-setup; spec mengasersi 6 baris sesuai TC (berasumsi Client C tidak memiliki Division lain).
  - Post Condition TC-GS-IMPORT-348 (b) dan TC-GS-IMPORT-920 tidak punya langkah observasi tambahan di luar Expected; yang sudah diasersi hanya yang ada di Expected.
  - TC-GS-IMPORT-348 dan 920 bertanda FE Test `Need API` tanpa menyebut endpoint; spec tidak menyebut endpoint (S-13).
