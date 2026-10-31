---
id: TC-GS-IMPORT-E2E-029-validasi-berkas-ditolak-seluruhnya-pada-user-non-login-represented-by
title: "Validasi Berkas Ditolak Seluruhnya pada User Non Login: Represented By, Email, Active Period, First Name, Last Name, Division Kosong, serta Custom Field Numeric, Phone, dan Date"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-124
  - TC-GS-IMPORT-125
  - TC-GS-IMPORT-126
  - TC-GS-IMPORT-127
  - TC-GS-IMPORT-611
  - TC-GS-IMPORT-614
  - TC-GS-IMPORT-615
  - TC-GS-IMPORT-616
coverage:
  web: automated
---

# Validasi Berkas Ditolak Seluruhnya pada User Non Login: Represented By, Email, Active Period, First Name, Last Name, Division Kosong, serta Custom Field Numeric, Phone, dan Date

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab User Non Login.
- Data: Client C tanpa draft Tab User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (data master Pre-setup, Kontrak Fixture R4); User Login aktif `rina.admin.c@example.com` (Pre-setup); Custom Field Active Overtime Hours (Numeric, Decimal Places 2), Emergency Phone (Phone), Join Date (Date). Tidak ada draft yang tercipta karena berkas ditolak seluruhnya.
- Waktu: nilai Active Period "tanggal kemarin" (TC 126) dihitung relatif hari uji (zona waktu Client C, format YYYY-MM-DD) saat berkas disiapkan oleh tim FE/BE.
- Berkas fixture D-07 (isi literal): berheader `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period` (TC 124, 125, 126, 127, 611) atau ditambah `,Shift,Shift Notes,Overtime Hours,Emergency Phone,Join Date` (TC 614, 615, 616); baris valid mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,` (angka pada Email mengikuti nomor baris data); kolom Custom Field lain kosong.
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Berkas | Nilai bermasalah | Header Error Banner | Baris pesan Error Banner (berurutan) |
  |---|---|---|---|---|
  | 124 | `user-non-login-empty-rep.csv` (3 baris) | baris ke-2 Represented By kosong | "1 row couldn't be imported. Fix the following and upload again:" | `Represented by must not be empty. 2` |
  | 125 | `user-non-login-bad-email.csv` (3 baris) | baris ke-2 Email `siti.rahayu` | "1 row couldn't be imported. Fix the following and upload again:" | `Invalid email format. 2` |
  | 126 | `user-non-login-bad-ap.csv` (3 baris) | baris ke-2 Active Period tanggal kemarin | "1 row couldn't be imported. Fix the following and upload again:" | `Active Period: Please select a future date. 2` |
  | 127 | `user-non-login-empty-first.csv` (3 baris) | baris ke-3 First Name kosong | "1 row couldn't be imported. Fix the following and upload again:" | `First name must not be empty. 3` |
  | 611 | `user-non-login-empty-multi.csv` (4 baris) | baris ke-2 Last Name kosong, baris ke-3 Email kosong, baris ke-4 Division kosong | "3 rows couldn't be imported. Fix the following and upload again:" | `Last name must not be empty. 2`, `Email must not be empty. 3`, `Division must not be empty. 4` |
  | 614 | `user-non-login-bad-overtime.csv` (4 baris) | Overtime Hours baris ke-2 `abc`, ke-3 `1234567890123456` (16 digit), ke-4 `1.234` | "3 rows couldn't be imported. Fix the following and upload again:" | `Overtime hours must be a number. 2`, `Overtime hours: Max. 15 characters. 3`, `Overtime hours must have at most 2 decimal places. 4` |
  | 615 | `user-non-login-bad-phone.csv` (5 baris) | Emergency Phone baris ke-2 `+999 81234567` (kode negara tidak ada di katalog), ke-3 `+62 8123abc`, ke-4 `+62 812` (3 digit), ke-5 `+62 8123456789012345` (16 digit) | "4 rows couldn't be imported. Fix the following and upload again:" | `Emergency phone must include a valid country code. 2`, `Emergency phone must be numeric. 3`, `Emergency phone: Min. 4 characters. 4`, `Emergency phone: Max. 15 characters. 5` |
  | 616 | `user-non-login-bad-joindate.csv` (3 baris) | baris ke-2 Join Date 30 Februari tahun berjalan (YYYY-MM-DD, tidak ada di kalender) | "1 row couldn't be imported. Fix the following and upload again:" | `Join date must be a valid date. 2` |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; penyiapan berkas dengan tanggal relatif hari uji.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-124, 125, 126, 127, 611, 614, 615, 616: berkas User Non Login ditolak seluruhnya

1. Klik Sub-Tab User Non Login

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 11; diulang delapan kali berurutan, TC 124 sampai 127, 611, 614, 615, 616):

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
- Langkah 2 sampai 11 diulang delapan kali (ekspansi 80 langkah, ditambah langkah 1 menjadi 81); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 11 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: delapan blok homogen satu pola (upload berkas User Non Login bermasalah, Confirm Mapping ditolak seluruhnya, Cancel), tanpa data tercipta; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 8) didahului `Verifikasi` Error Banner tampil di modal (langkah 6 dan 7) sebagai anchor positif; "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-126 mensyaratkan Active Period tanggal kemarin menurut zona waktu client; dekat tengah malam nilai relatif dapat berbeda antar run. Berkas disiapkan tim FE/BE per run.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nilai data literal tanpa suffix `{runId}` (tidak ada draft yang tercipta).
