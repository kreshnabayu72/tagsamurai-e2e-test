---
id: TC-GS-IMPORT-E2E-025-validasi-berkas-ditolak-seluruhnya-first-name-last-name-email-division
title: "Validasi Berkas Ditolak Seluruhnya: First Name, Last Name, Email, Division, dan Access Kosong pada User Login"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-104
  - TC-GS-IMPORT-105
  - TC-GS-IMPORT-106
  - TC-GS-IMPORT-107
  - TC-GS-IMPORT-108
coverage:
  web: automated
---

# Validasi Berkas Ditolak Seluruhnya: First Name, Last Name, Email, Division, dan Access Kosong pada User Login

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab User Login.
- Data: Client C tanpa draft Tab User Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (data master Pre-setup, Kontrak Fixture R4). Tidak ada draft yang tercipta karena berkas ditolak seluruhnya.
- Berkas fixture D-07 (isi literal): semua berkas berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`, 3 baris data; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,` (angka pada Email dan Employee ID mengikuti nomor baris data); baris ke-2 memuat nilai bermasalah sesuai tabel.
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik; header Error Banner untuk semua baris: "1 row couldn't be imported. Fix the following and upload again:"):

  | TC | Berkas | Nilai bermasalah (baris ke-2) | Baris pesan Error Banner |
  |---|---|---|---|
  | 104 | `user-login-empty-first-name.csv` | First Name kosong | `First name must not be empty. 2` |
  | 105 | `user-login-empty-last-name.csv` | Last Name kosong | `Last name must not be empty. 2` |
  | 106 | `user-login-empty-email.csv` | Email kosong | `Email must not be empty. 2` |
  | 107 | `user-login-empty-division.csv` | Division kosong | `Division must not be empty. 2` |
  | 108 | `user-login-empty-access.csv` | Access kosong | `Access must not be empty. 2` |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-104, 105, 106, 107, 108: berkas User Login ditolak seluruhnya

1. Klik Sub-Tab User Login

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 11; diulang lima kali berurutan, TC 104 sampai 108):

2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi Modal Column Mapping tetap terbuka dengan mapping yang sudah diisi
6. Verifikasi Error Banner tampil di dalam modal dengan header "1 row couldn't be imported. Fix the following and upload again:"
7. Verifikasi baris pesan Error Banner sesuai kolom Baris pesan Error Banner
8. Verifikasi tidak ada toast
9. Klik `[Cancel]` pada Modal Column Mapping
10. Verifikasi modal tertutup
11. Verifikasi halaman menampilkan Upload Dropzone tanpa Staging Table dan tanpa Unsaved Banner

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 2 sampai 11 diulang lima kali (ekspansi 50 langkah, ditambah langkah 1 menjadi 51); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 11 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: lima blok homogen satu pola (upload berkas User Login bermasalah, Confirm Mapping ditolak seluruhnya, Cancel), tanpa data tercipta; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 8) didahului `Verifikasi` Error Banner tampil di modal (langkah 6 dan 7) sebagai anchor positif yang terhubung ke pemicu (Confirm Mapping); asersi "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Temuan untuk QA:
  - Pola nilai valid pada berkas ("angka pada Email dan Employee ID mengikuti nomor baris data") disediakan tim FE/BE sesuai Data Uji TC; nama literal tanpa suffix `{runId}` (tidak ada draft yang tercipta).
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
