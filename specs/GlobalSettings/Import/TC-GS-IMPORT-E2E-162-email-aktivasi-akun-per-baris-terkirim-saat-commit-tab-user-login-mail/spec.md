---
id: TC-GS-IMPORT-E2E-162-email-aktivasi-akun-per-baris-terkirim-saat-commit-tab-user-login-mail
title: "Email aktivasi akun per baris terkirim saat commit Tab User Login (mail-catcher)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-737
coverage:
  web: automated
---

# Email aktivasi akun per baris terkirim saat commit Tab User Login (mail-catcher)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit nyata di Client E (membuat 8 User Login) yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`. Produk organisasi Client E: Global Settings dan Fixed Asset.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; mail-catcher tidak didefinisikan di Tabel Pre-setup maupun Data Dinamis TC, lihat Temuan untuk QA):
  - Mail-catcher lingkungan uji yang menampung seluruh email keluar modul Auth ke alamat `@example.com` dan dapat dibaca lewat API uji (polling). Baseline jumlah email dicatat per alamat sebelum aksi (S-12).
  - Skrip fixture reset Client E (D-47: hapus draft, hapus User Login hasil commit, reset hasil commit terakhir) dan seeding draft D-54.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang selesai (bukan menunggu jam).
- Data Dinamis (milik spec ini; User Login hasil commit dihapus oleh hook `after`): D-54 `user-login-commit-8.csv` (draft User Login 8 baris `pending` di Client E): kolom First Name; Last Name; Email; Division; Position; Employee ID; Access; Active Period; Shift; Overtime Hours; baris #1 Rizky Pratama `rizky.pratama@example.com` (Engineering, Senior Developer, EMP-5001, `Global Settings;Fixed Asset`, Shift Siang); #2 Sinta Maharani `sinta.maharani@example.com` (Marketing, Position kosong, `Global Settings`, Active Period H+30 format YYYY-MM-DD, Shift Siang); #3 Doni Kurniawan `doni.kurniawan@example.com` (Finance, Finance Manager, `Fixed Asset`, Shift Pagi); #4 Eka Putri `eka.putri@example.com` (Warehouse, Technician, `Global Settings`, Overtime Hours 1.25); #5 Fajar Hidayat `fajar.hidayat@example.com` (Gudang, Supervisor, `Global Settings;Fixed Asset`); #6 Gita Savitri `gita.savitri@example.com` (Gudang, Store Manager, `Global Settings`); #7 Hendra Gunawan `hendra.gunawan@example.com` (Gudang, Position kosong, `Fixed Asset`); #8 Indah Permata `indah.permata@example.com` (Finance, Position kosong, `Global Settings`); sel yang tidak disebut kosong; semua baris valid dan unik. Email berdomain `@example.com` ditulis literal sesuai TC karena ditampung mail-catcher dan dihapus oleh reset.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus draft Client E, hapus 8 User Login hasil commit, reset hasil commit terakhir dan penanda Banner Hasil Commit, kosongkan mail-catcher untuk 8 alamat itu, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-737: Commit Tab User Login mengirim email aktivasi per baris ke 8 alamat

1. Reset Client E (D-47) dan seed draft User Login D-54 (8 baris `pending`) lewat skrip fixture
2. Catat jumlah email pada mail-catcher untuk masing-masing dari 8 alamat (`rizky.pratama`, `sinta.maharani`, `doni.kurniawan`, `eka.putri`, `fajar.hidayat`, `gita.savitri`, `hendra.gunawan`, `indah.permata` @example.com) sebagai baseline
3. Muat ulang halaman Import > User Login
4. Klik `[Import (8)]`
5. Tunggu aksi selesai (permintaan mendapat respons)
6. Tunggu commit selesai: muat ulang halaman Import > User Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
7. Verifikasi Dropzone tampil
8. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
9. Baca seluruh email pada mail-catcher untuk 8 alamat itu (polling)
10. Verifikasi jumlah email baru pada mail-catcher bertambah tepat 8 dari baseline langkah 2 (masing-masing alamat bertambah tepat 1)
11. Verifikasi seluruh email baru memiliki Subject "Activate your TAG Samurai account"
12. Verifikasi email baru terkirim satu per alamat ke `rizky.pratama@example.com`, `sinta.maharani@example.com`, `doni.kurniawan@example.com`, `eka.putri@example.com`, `fajar.hidayat@example.com`, `gita.savitri@example.com`, `hendra.gunawan@example.com`, dan `indah.permata@example.com`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah email aktivasi per baris yang dibaca lewat mail-catcher setelah commit (spec TC tunggal untuk harness mail-catcher).
- Spec singkat (12 langkah) sehingga tidak melewati sekitar 35 langkah.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1), pencatatan baseline (langkah 2), muat ulang halaman Import > User Login (langkah 3), "Tunggu aksi selesai (permintaan mendapat respons)" persis sesudah klik `[Import (8)]` dan sebelum polling (langkah 5; bagian 8b butir 8), polling job (langkah 6), dan pembacaan mail-catcher (langkah 9). Langkah 7 dan 8 menjadi anchor positif (commit selesai) sebelum asersi email.
- Asersi email memakai baseline jumlah per alamat (S-12) dan tidak memakai anchor baris seed.
- Temuan untuk QA:
  - Penanda selesai untuk klik `[Import (8)]` (langkah 5) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-737 memakai mail-catcher yang tidak didefinisikan di Tabel Pre-setup maupun Data Dinamis; kebutuhan lingkungan ini ditulis di Prerequisites dan disediakan tim FE/BE.
  - TC-GS-IMPORT-737 menyatakan "mail-catcher kosong sebelum TC"; spec memakai baseline jumlah email per alamat sebagai pengganti pengosongan agar tidak bergantung pada pengosongan global.
  - Post Condition TC-GS-IMPORT-737 (8 record User Login baru berstatus `Pending Activation` di User > User List > Login User Client E; draft dihapus) tidak punya langkah observasi di TC dan tidak diasersi (S-01); penghapusan 8 User Login dikerjakan hook `after`.
  - TC-GS-IMPORT-737 menulis Active Period H+30 relatif hari eksekusi; nilai dihitung saat seeding.
