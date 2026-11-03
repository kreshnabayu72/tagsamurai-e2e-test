---
id: TC-FA-FAAL-E2E-018-format-tanggal-mengikuti-general-settings
title: "Format Tanggal dan Jam Mengikuti General Settings Staf"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-204
  - TC-FA-FAAL-205
  - TC-FA-FAAL-206
  - TC-FA-FAAL-207
coverage:
  web: automated
---

# Format Tanggal dan Jam Mengikuti General Settings Staf

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | Peran dalam spec | Pre-setup | Email | General Settings | Env var password |
  |---|---|---|---|---|
  | Staf A (Total Control) | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` | `Spectra.env.FA_TC_PASSWORD` |
  | Staf B (Read Only) | #10 | `readOnlyStaffB_automated_{namaCompany}@qwertysystem.net` | Date Format `M/d/yy`, Time Format `hh:mm a`, Time Zone `(UTC+00:00) UTC, Reykjavik, Accra` | `Spectra.env.FA_RO_STAFB_PASSWORD` |
- Login akun aktor pertama (staf A, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session). Hook `after` memulihkan General Settings staf A dan staf B ke nilai pada tabel di atas bila berubah (disediakan tim FE/BE) lalu mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Spec tidak mengubah General Settings lewat UI. Ganti akun di tengah spec memakai satu langkah logout dan login eksplisit.
- Env var `FA_TC_PASSWORD` dan `FA_RO_STAFB_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11; SS-01 14/07/26 08:05 dan SS-11 16/07/26 09:00 dalam Asia/Jakarta, tersimpan sebagai UTC) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12; UA-01 18/06/26 14:30 dalam Asia/Jakarta), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). Urutan default Date terbaru di atas dengan 10 baris per halaman: halaman 1 Tab Session berisi SS-11 sampai SS-02 dan SS-01 berada di halaman 2.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk kedua akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Staf A (Pre-setup #1): bagian a TC-FA-FAAL-204, 205, 206, dan 207

1. Verifikasi staf A, TC-FA-FAAL-204: kolom Date baris SS-11 `16/07/26, 09:00`
2. Klik `Next` pada Pagination
3. Verifikasi staf A, TC-FA-FAAL-204: kolom Date baris SS-01 `14/07/26, 08:05`
4. Klik icon Filter, pilih tanggal mulai 14 Juli 2026 dan tanggal akhir 15 Juli 2026 pada field Date
5. Verifikasi staf A, TC-FA-FAAL-206: teks field Date memuat `14/07/26` dan `15/07/26`
6. Tutup Filter Panel tanpa Apply
7. Klik tab User Action
8. Verifikasi staf A, TC-FA-FAAL-205: kolom Date baris UA-01 `18/06/26, 14:30`
9. Klik icon Filter, pilih tanggal mulai 18 Juni 2026 dan tanggal akhir 18 Juni 2026 pada field Date
10. Verifikasi staf A, TC-FA-FAAL-207: teks field Date memuat `18/06/26`
11. Tutup Filter Panel tanpa Apply

### Staf B (Pre-setup #10): bagian b TC-FA-FAAL-204, 205, 206, dan 207

12. Ganti akun: Logout dari akun staf A, lalu Login sebagai staf B (Read Only, `readOnlyStaffB_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_STAFB_PASSWORD`) dan buka Fixed Asset > Reports & Logs > Activity Log
13. Verifikasi staf B, TC-FA-FAAL-204: kolom Date baris SS-11 `7/16/26, 02:00 AM`
14. Klik `Next` pada Pagination
15. Verifikasi staf B, TC-FA-FAAL-204: kolom Date baris SS-01 `7/14/26, 01:05 AM`
16. Klik icon Filter, pilih tanggal mulai 14 Juli 2026 dan tanggal akhir 15 Juli 2026 pada field Date
17. Verifikasi staf B, TC-FA-FAAL-206: teks field Date memuat `7/14/26` dan `7/15/26`
18. Tutup Filter Panel tanpa Apply
19. Klik tab User Action
20. Verifikasi staf B, TC-FA-FAAL-205: kolom Date baris UA-01 `6/18/26, 07:30 AM`
21. Klik icon Filter, pilih tanggal mulai 18 Juni 2026 dan tanggal akhir 18 Juni 2026 pada field Date
22. Verifikasi staf B, TC-FA-FAAL-207: teks field Date memuat `6/18/26`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke staf dan bagian TC; setiap `Verifikasi` menyebut id TC granularnya.
- P-5 (butir b): objek uji ringan format tanggal General Settings (TC-FA-FAAL-204 sampai 207) pada satu topik dan satu permukaan (Date di tabel dan Filter Panel kedua tab); tidak ada harness eksternal dan tidak ada state berat.
- Urutan TC di dalam spec: tiap TC (TC-FA-FAAL-204 sampai 207) menulis bagian staf A lalu ganti ke staf B. Spec mengelompokkan semua bagian staf A (langkah 1 sampai 11), lalu semua bagian staf B (langkah 12 sampai 22), supaya ganti akun (S-07) hanya satu kali; setiap Expected a dan b TC tetap punya `Verifikasi` sendiri dan urutan langkah dalam tiap bagian mengikuti TC (Session lalu User Action).
- Langkah penghubung (S-03): langkah 2 dan 14 (halaman 2 berisi SS-01 karena SS-11 sampai SS-02 mengisi halaman 1), langkah 6, 11, dan 18 (menutup Filter Panel tanpa Apply sebelum pindah tab; draft dibuang), langkah 7 dan 19 (klik tab User Action), dan langkah 12 (ganti akun, lalu membuka Activity Log).
- Teks field Date pada langkah 5, 10, 17, dan 22 diasersi sebagai "memuat" sesuai Expected TC.
- Ukuran spec 22 langkah, di bawah ambang.
- Temuan untuk QA:
  - TC-FA-FAAL-204 sampai 207 menyebut General Settings staf B hanya di nilai Expected (`M/d/yy`, `hh:mm a`, zona UTC); Pre-setup #10 menyebutnya lengkap tetapi precondition TC tidak. Spec memakai Pre-setup #10.
  - TC-FA-FAAL-204 dan 205 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - TC-FA-FAAL-206 dan 207 tidak menyebut cara menutup Filter Panel setelah mengamati field Date; spec menutupnya tanpa Apply sebagai langkah penghubung.
  - TC-FA-FAAL-204 langkah 1 ("Amati kolom Date baris SS-01 dan SS-11") tidak menyebut SS-01 berada di halaman 2; spec menambahkan klik `Next` pada Pagination (S-14).
