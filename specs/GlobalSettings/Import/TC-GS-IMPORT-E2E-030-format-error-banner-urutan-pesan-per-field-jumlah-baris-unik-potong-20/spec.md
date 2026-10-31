---
id: TC-GS-IMPORT-E2E-030-format-error-banner-urutan-pesan-per-field-jumlah-baris-unik-potong-20
title: "Format Error Banner: Urutan Pesan per Field, Jumlah Baris Unik, Potong 20 Nomor (20 vs 21 vs 25 Baris), Nomor Baris dengan Baris Kosong, dan Kombinasi Dropdown Asing"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-129
  - TC-GS-IMPORT-132
  - TC-GS-IMPORT-583
  - TC-GS-IMPORT-621
  - TC-GS-IMPORT-623
  - TC-GS-IMPORT-624
  - TC-GS-IMPORT-892
coverage:
  web: automated
---

# Format Error Banner: Urutan Pesan per Field, Jumlah Baris Unik, Potong 20 Nomor (20 vs 21 vs 25 Baris), Nomor Baris dengan Baris Kosong, dan Kombinasi Dropdown Asing

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C (Sub-Tab Brand); perpindahan ke User Login ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Brand dan User Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (data master Pre-setup, Kontrak Fixture R4); Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`. Tidak ada draft yang tercipta karena berkas ditolak seluruhnya.
- Waktu: nilai Active Period "tanggal kemarin" dihitung relatif hari uji (zona waktu Client C, format YYYY-MM-DD) saat berkas disiapkan oleh tim FE/BE.
- Berkas fixture D-07 (isi literal): berkas Brand berheader `Brand Name,Catatan`; berkas User Login berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period` (kecuali TC 892); baris valid User Login mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,` (angka pada Email dan Employee ID mengikuti nomor baris data).
- Tabel "Parameter validasi" (satu baris per blok TC, urut menurut Sub-Tab; langkah per baris identik):

  | TC | Sub-Tab | Berkas | Nilai bermasalah | Header Error Banner | Baris pesan Error Banner (berurutan) |
  |---|---|---|---|---|---|
  | 129 | Brand | `brand-25-empty.csv` | 25 baris data seluruhnya Brand Name kosong dengan Catatan `x` | "25 rows couldn't be imported. Fix the following and upload again:" | `Brand name must not be empty. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 and 5 more` |
  | 583 | Brand | `brand-blank-then-invalid.csv` | baris data 1 `Acme Corp,A`; baris data 2 `,` (kosong sepenuhnya); baris data 3 `,Catatan x` (Brand Name kosong) | "1 row couldn't be imported. Fix the following and upload again:" | `Brand name must not be empty. 3` |
  | 623 | Brand | `brand-20-empty.csv` | 20 baris data seluruhnya Brand Name kosong dengan Catatan `x` | "20 rows couldn't be imported. Fix the following and upload again:" | `Brand name must not be empty. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20` |
  | 624 | Brand | `brand-21-empty.csv` | 21 baris data seluruhnya Brand Name kosong dengan Catatan `x` | "21 rows couldn't be imported. Fix the following and upload again:" | `Brand name must not be empty. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 and 1 more` |
  | 132 | User Login | `user-login-mixed.csv` (4 baris data) | baris ke-2 First Name kosong, baris ke-3 Email `x@`, baris ke-4 Active Period tanggal kemarin | "3 rows couldn't be imported. Fix the following and upload again:" | `First name must not be empty. 2`, `Invalid email format. 3`, `Active Period: Please select a future date. 4` |
  | 621 | User Login | `user-login-multi-rule.csv` (4 baris data) | baris ke-2 melanggar dua aturan (First Name kosong dan Email `x@`), baris ke-3 melanggar satu aturan (Email `y@`) | "2 rows couldn't be imported. Fix the following and upload again:" | `First name must not be empty. 2`, `Invalid email format. 2, 3` |
  | 892 | User Login | `user-login-shift-badmail.csv`: header `First Name,Last Name,Email,Division,Position,Access,Shift`; #1 Siti, Rahmawati, `siti.rahmawati@example.com`, Engineering, kosong, Global Settings, Shift `Lembur`; #2 Budi, Santoso, Email `budi.santoso@`, Engineering, kosong, Global Settings, Shift `Pagi`; #3 Andi, Pratama, `andi.pratama@example.com`, Engineering, kosong, Global Settings, Shift `Piket` | Dropdown Shift asing (`Lembur`, `Piket`) bersama Email tidak valid pada baris ke-2 | "1 row couldn't be imported. Fix the following and upload again:" | hanya satu baris pesan `Invalid email format. 2`; tidak ada baris pesan untuk Shift `Lembur` maupun `Piket` |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; penyiapan berkas dengan tanggal relatif hari uji.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-129, 583, 623, 624 (Brand) lalu TC-GS-IMPORT-132, 621, 892 (User Login)

Untuk setiap baris tabel "Parameter validasi" (langkah 1 sampai 11; diulang tujuh kali berurutan: TC 129, 583, 623, 624, 132, 621, 892):

1. Klik Sub-Tab sesuai kolom Sub-Tab
2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
6. Verifikasi Error Banner tampil di dalam modal dengan header sesuai kolom Header Error Banner
7. Verifikasi baris pesan Error Banner sesuai kolom Baris pesan Error Banner (berurutan)
8. Verifikasi tidak ada toast
9. Klik `[Cancel]` pada Modal Column Mapping
10. Verifikasi modal tertutup
11. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 1 sampai 11 diulang tujuh kali (ekspansi 77 langkah); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 1 sampai 11 (konvensi 8b butir 7). Langkah 1 memilih Sub-Tab sesuai tabel (aksi idempoten bila sudah aktif).
- Alasan di atas sekitar 35 langkah: tujuh blok homogen satu pola (upload berkas bermasalah, Confirm Mapping ditolak seluruhnya, Cancel), tanpa data tercipta; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 8) didahului `Verifikasi` Error Banner tampil di modal (langkah 6 dan 7) sebagai anchor positif; "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Pada blok TC-GS-IMPORT-892, "0 baris masuk staging" (Expected c) dicakup langkah 11 (tanpa Staging Table). Langkah "Perhatikan Error Banner dan Staging Table" di Langkah Uji TC-GS-IMPORT-892 dicakup langkah 6, 7, dan 11.
- Temuan untuk QA:
  - Judul TC-GS-IMPORT-129 dan TC-GS-IMPORT-623 memuat sisa pola placeholder yang tidak terbaca ("...diikuti 1 → "and 1 more" · N → "and [N] more"") sehingga kalimat judul rusak; Expected TC-GS-IMPORT-129 memakai nilai konkret "and 5 more" dan Expected TC-GS-IMPORT-623 tidak memuat suffix itu. Spec mengikuti Expected.
  - TC-GS-IMPORT-132 dan 892 mensyaratkan Active Period "tanggal kemarin" menurut zona waktu client; dekat tengah malam nilai relatif dapat berbeda antar run. Berkas disiapkan tim FE/BE per run.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nilai data literal tanpa suffix `{runId}` (tidak ada draft yang tercipta).
