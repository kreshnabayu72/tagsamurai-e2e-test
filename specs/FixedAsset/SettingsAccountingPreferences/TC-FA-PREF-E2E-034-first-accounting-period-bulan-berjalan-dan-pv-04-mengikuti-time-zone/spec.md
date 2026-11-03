---
id: TC-FA-PREF-E2E-034-first-accounting-period-bulan-berjalan-dan-pv-04-mengikuti-time-zone
title: "First Accounting Period: Bulan Berjalan dan Bulan Sebelumnya Dapat Dipilih, Jumlah Periode PV-04 Mengikuti Time Zone Entitas"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-146
  - TC-FA-PREF-147
  - TC-FA-PREF-609
  - TC-FA-PREF-610
coverage:
  web: automated
---

# First Accounting Period: Bulan Berjalan dan Bulan Sebelumnya Dapat Dipilih, Jumlah Periode PV-04 Mengikuti Time Zone Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, Time Zone entitas Asia/Jakarta) dengan Preferences nilai awal PA-2 dan PC-1 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, tidak terkunci; belum ada posting penyusutan; semua periode Mar 2026 sampai Dec 2026 Open).
- Jam sistem (clock): jam server dan jam browser diatur bersama. TC-FA-PREF-146 dan 147: 28 Oktober 2026 pukul 10:00 Asia/Jakarta (PA-1, diatur di hook `before`). TC-FA-PREF-609: 31 Oktober 2026 pukul 16:59 UTC (23:59 waktu entitas; langkah 12). TC-FA-PREF-610: 31 Oktober 2026 pukul 17:00 UTC (1 November 2026 pukul 00:00 waktu entitas; langkah 18). Dipulihkan di hook `after` bila spec gagal di tengah. Suite serial (bagian 6).
- State yang diubah spec: jam sistem. Tidak ada Save yang berhasil; form dikembalikan ke nilai tersimpan pada langkah 11, 17, dan 23. Hook `after` memulihkan jam sistem.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" dan "Kendali jam sistem" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-146: Bulan berjalan (Oktober 2026) dapat dipilih sebagai First Accounting Period

1. Pilih tahun "2026" pada Select tahun First Accounting Period
2. Buka daftar opsi Select bulan
3. Pilih bulan "October"
4. Verifikasi opsi "October" dapat dipilih dan Select bulan menampilkan "October"
5. Verifikasi tidak ada caption pada First Accounting Period

### TC-FA-PREF-147: Bulan sebelum bulan berjalan (September 2026) dapat dipilih sebagai First Accounting Period

6. Pilih tahun "2026" pada Select tahun First Accounting Period
7. Buka daftar opsi Select bulan
8. Pilih bulan "September"
9. Verifikasi opsi "September" dapat dipilih dan Select bulan menampilkan "September"
10. Verifikasi tidak ada caption pada First Accounting Period

### Pemulihan First Accounting Period

11. Pilih bulan "March" pada Select bulan First Accounting Period

### TC-FA-PREF-609: Jumlah periode PV-04 memakai bulan berjalan menurut Time Zone entitas sebelum pergantian bulan

12. Atur jam server dan jam browser ke 31 Oktober 2026 pukul 16:59 UTC dengan Time Zone entitas Asia/Jakarta, lalu muat ulang halaman Preferences
13. Ubah Select Fiscal Year Start dari "January" menjadi "November"
14. Klik `[Save changes]`
15. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet "8 accounting periods will be rebuilt." dan "Tax year start also follows Fiscal Year Start.", pertanyaan "Are you sure you want to save these changes?", serta tombol `[Cancel]` dan `[Save]`
16. Klik `[Cancel]` pada dialog
17. Ubah Select Fiscal Year Start dari "November" menjadi "January"

### TC-FA-PREF-610: Jumlah periode PV-04 memakai bulan berjalan menurut Time Zone entitas tepat saat pergantian bulan

18. Atur jam server dan jam browser ke 31 Oktober 2026 pukul 17:00 UTC dengan Time Zone entitas Asia/Jakarta, lalu muat ulang halaman Preferences
19. Ubah Select Fiscal Year Start dari "January" menjadi "November"
20. Klik `[Save changes]`
21. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet "20 accounting periods will be rebuilt." dan "Tax year start also follows Fiscal Year Start.", pertanyaan "Are you sure you want to save these changes?", serta tombol `[Cancel]` dan `[Save]`
22. Klik `[Cancel]` pada dialog
23. Ubah Select Fiscal Year Start dari "November" menjadi "January"

## Notes

- Jam sistem dikendalikan per TC (bagian 6): hook `before` mengatur 28 Oktober 2026 untuk TC-FA-PREF-146 dan 147; langkah 12 dan 18 mengatur ulang jam untuk TC-FA-PREF-609 dan 610; pemulihan di hook `after`.
- Langkah penghubung (S-03): langkah 11, 16, 17, 22, 23 (mengembalikan form ke nilai tersimpan dan menutup dialog tanpa konfirmasi; S-09) dan langkah 12 dan 18 (pengaturan jam dan muat ulang saat form pristine). Dialog Save Changes ditutup dengan `[Cancel]`; tidak ada Save yang dikonfirmasi.
- Expected b TC-FA-PREF-609 dan 610 ("Jumlah periode dihitung dari Mar 2026 sampai Oct 2026" dan "sampai Oct 2027") adalah penjelasan jumlah pada bullet dan tidak teramati terpisah; cukup satu `Verifikasi` pada dialog (S-03).
- Dialog Save Changes diasersi sebagai satu elemen komposit (judul, severity, bullet, pertanyaan, tombol) karena TC menyebutnya utuh dalam satu butir Expected (S-01).
- Temuan untuk QA:
  - Post Condition TC-FA-PREF-609 dan 610 ("Preferences company belum berubah (dialog belum dikonfirmasi)") tidak punya langkah observasi sehingga tidak diasersi (S-01).
  - Expected a TC-FA-PREF-146 dan 147 ("dapat dipilih dan Select bulan menampilkan ...") digabung dalam satu butir; spec menulis satu `Verifikasi` karena satu klausa.
