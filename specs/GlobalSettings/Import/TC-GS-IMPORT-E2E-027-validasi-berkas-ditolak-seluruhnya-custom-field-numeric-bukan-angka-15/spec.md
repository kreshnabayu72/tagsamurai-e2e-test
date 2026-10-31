---
id: TC-GS-IMPORT-E2E-027-validasi-berkas-ditolak-seluruhnya-custom-field-numeric-bukan-angka-15
title: "Validasi Berkas Ditolak Seluruhnya: Custom Field Numeric (Bukan Angka, Lebih dari 15 Digit, Desimal) dan Phone (Kode Negara, Non-Numerik, Kurang dari 4 dan Lebih dari 15 Digit)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-115
  - TC-GS-IMPORT-116
  - TC-GS-IMPORT-117
  - TC-GS-IMPORT-118
  - TC-GS-IMPORT-119
  - TC-GS-IMPORT-120
  - TC-GS-IMPORT-121
coverage:
  web: automated
---

# Validasi Berkas Ditolak Seluruhnya: Custom Field Numeric (Bukan Angka, Lebih dari 15 Digit, Desimal) dan Phone (Kode Negara, Non-Numerik, Kurang dari 4 dan Lebih dari 15 Digit)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab User Login.
- Data: Client C tanpa draft Tab User Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (data master Pre-setup, Kontrak Fixture R4); Custom Field Active Overtime Hours (Numeric, Decimal Places 2) dan Emergency Phone (Phone). Tidak ada draft yang tercipta karena berkas ditolak seluruhnya.
- Berkas fixture D-07 (isi literal): semua berkas berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift,Shift Notes,Overtime Hours,Emergency Phone,Join Date`, 3 baris data; kolom Custom Field lain kosong; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,` (angka pada Email dan Employee ID mengikuti nomor baris data); baris ke-2 memuat nilai bermasalah sesuai tabel.
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik; header Error Banner untuk semua baris: "1 row couldn't be imported. Fix the following and upload again:"):

  | TC | Berkas | Nilai bermasalah (baris ke-2) | Baris pesan Error Banner |
  |---|---|---|---|
  | 115 | `user-login-bad-overtime.csv` | Overtime Hours `abc` | `Overtime hours must be a number. 2` |
  | 116 | `user-login-long-overtime.csv` | Overtime Hours `1234567890123456` (16 digit) | `Overtime hours: Max. 15 characters. 2` |
  | 117 | `user-login-dec-overtime.csv` | Overtime Hours `1.234` (Decimal Places = 2) | `Overtime hours must have at most 2 decimal places. 2` |
  | 118 | `user-login-bad-phone-cc.csv` | Emergency Phone `+999 81234567` (kode negara `+999` tidak ada di katalog) | `Emergency phone must include a valid country code. 2` |
  | 119 | `user-login-bad-phone-nan.csv` | Emergency Phone `+62 8123abc` | `Emergency phone must be numeric. 2` |
  | 120 | `user-login-short-phone.csv` | Emergency Phone `+62 812` (3 digit setelah kode negara) | `Emergency phone: Min. 4 characters. 2` |
  | 121 | `user-login-long-phone.csv` | Emergency Phone `+62 8123456789012345` (16 digit setelah kode negara) | `Emergency phone: Max. 15 characters. 2` |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-115, 116, 117, 118, 119, 120, 121: berkas User Login dengan Custom Field Numeric dan Phone bermasalah

1. Klik Sub-Tab User Login

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 11; diulang tujuh kali berurutan, TC 115 sampai 121):

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
- Langkah 2 sampai 11 diulang tujuh kali (ekspansi 70 langkah, ditambah langkah 1 menjadi 71); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 11 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: tujuh blok homogen satu pola (upload berkas User Login dengan Custom Field bermasalah, Confirm Mapping ditolak seluruhnya, Cancel), tanpa data tercipta; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi absence "tidak ada toast" (langkah 8) didahului `Verifikasi` Error Banner tampil di modal (langkah 6 dan 7) sebagai anchor positif; "tanpa Staging Table dan tanpa Unsaved Banner" (langkah 11) didahului `Verifikasi` Upload Dropzone tampil pada kalimat yang sama.
- Temuan untuk QA:
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - Nilai Custom Field pada berkas literal tanpa suffix `{runId}` (tidak ada draft yang tercipta).
