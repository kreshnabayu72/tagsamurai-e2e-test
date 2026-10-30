---
id: TC-GS-IMPORT-E2E-026-validasi-berkas-ditolak-seluruhnya-format-email-access-di-luar-produk
title: "Validasi Berkas Ditolak Seluruhnya: Format Email, Access di Luar Produk, Active Period (Format dan Hari Ini atau Lampau), dan Custom Field Date"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-110
  - TC-GS-IMPORT-111
  - TC-GS-IMPORT-112
  - TC-GS-IMPORT-113
  - TC-GS-IMPORT-122
coverage:
  web: automated
---

# Validasi Berkas Ditolak Seluruhnya: Format Email, Access di Luar Produk, Active Period (Format dan Hari Ini atau Lampau), dan Custom Field Date

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab User Login.
- Data: Client C tanpa draft Tab User Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (data master Pre-setup, Kontrak Fixture R4); produk organisasi Client C: Global Settings dan Fixed Asset (Pre-setup); Custom Field Active Join Date (Date). Tidak ada draft yang tercipta karena berkas ditolak seluruhnya.
- Waktu: nilai Active Period pada berkas dihitung relatif terhadap hari uji (zona waktu Client C, format YYYY-MM-DD) saat berkas disiapkan; tim FE/BE menyiapkan berkas per run.
- Berkas fixture D-07 (isi literal): semua berkas berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period` (kecuali TC 122 yang berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift,Shift Notes,Overtime Hours,Emergency Phone,Join Date`), 3 baris data; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,` (angka pada Email dan Employee ID mengikuti nomor baris data).
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Berkas | Nilai bermasalah | Header Error Banner | Baris pesan Error Banner |
  |---|---|---|---|---|
  | 110 | `user-login-bad-email.csv` | baris ke-3 Email `budi.setiawan@` | "1 row couldn't be imported. Fix the following and upload again:" | `Invalid email format. 3` |
  | 111 | `user-login-bad-access.csv` | baris ke-2 Access `Global Settings;Payroll` | "1 row couldn't be imported. Fix the following and upload again:" | `Access must only contain the following values: Global Settings, Fixed Asset. 2` |
  | 112 | `user-login-bad-active-period.csv` | baris ke-2 Active Period berformat DD/MM/YYYY untuk 31 Desember tahun depan | "1 row couldn't be imported. Fix the following and upload again:" | `Active period must be a date YYYY-MM-DD. 2` |
  | 113 | `user-login-past-active-period.csv` | baris ke-2 Active Period tanggal hari ini; baris ke-3 tanggal kemarin | "2 rows couldn't be imported. Fix the following and upload again:" | `Active Period: Please select a future date. 2, 3` |
  | 122 | `user-login-bad-joindate.csv` | baris ke-2 Join Date 30 Februari tahun berjalan (YYYY-MM-DD, tidak ada di kalender); kolom Custom Field lain kosong | "1 row couldn't be imported. Fix the following and upload again:" | `Join date must be a valid date. 2` |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; penyiapan berkas dengan tanggal relatif hari uji.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-110, 111, 112, 113, 122: berkas User Login ditolak seluruhnya

1. Klik Sub-Tab User Login

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 11; diulang lima kali berurutan, TC 110 sampai 113 lalu 122):

2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
6. Verifikasi Error Banner tampil di dalam modal dengan header sesuai kolom Header Error Banner
7. Verifikasi baris pesan Error Banner sesuai kolom Baris pesan Error Banner
8. Verifikasi tidak ada toast
9. Klik `[Cancel]` pada Modal Column Mapping
10. Verifikasi modal tertutup
11. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 2 sampai 11 diulang lima kali (ekspansi 50 langkah, ditambah langkah 1 menjadi 51); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 11 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: lima blok homogen satu pola (upload berkas User Login bermasalah, Confirm Mapping ditolak seluruhnya, Cancel), tanpa data tercipta; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 8) didahului `Verifikasi` Error Banner tampil di modal (langkah 6 dan 7) sebagai anchor positif; "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Urutan TC dalam spec: 110, 111, 112, 113, 122 (urutan angka TC sumber; TC-GS-IMPORT-122 memakai header yang berbeda sehingga diletakkan terakhir).
- Temuan untuk QA:
  - TC-GS-IMPORT-113 mensyaratkan tanggal hari ini dan kemarin menurut zona waktu client; dekat tengah malam, nilai relatif bisa berbeda antar run. Berkas disiapkan tim FE/BE per run.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama literal tanpa suffix `{runId}` (tidak ada draft yang tercipta).
