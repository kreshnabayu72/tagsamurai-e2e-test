---
id: TC-FA-PREF-E2E-033-first-accounting-period-tahun-berjalan-dan-bulan-setelah-bulan-berjalan
title: "First Accounting Period: Tahun Berjalan Mengosongkan Bulan Setelah Bulan Berjalan dan Bulan Setelah Bulan Berjalan Tidak Dapat Dipilih"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-128
  - TC-FA-PREF-129
  - TC-FA-PREF-148
  - TC-FA-PREF-149
coverage:
  web: automated
---

# First Accounting Period: Tahun Berjalan Mengosongkan Bulan Setelah Bulan Berjalan dan Bulan Setelah Bulan Berjalan Tidak Dapat Dipilih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, Time Zone entitas Asia/Jakarta) dengan Preferences nilai awal PA-2 (First Accounting Period Mar 2026, tidak terkunci, semua setting wajib terisi).
- Jam sistem: tanggal sistem uji 28 Oktober 2026 pukul 10:00 pada Time Zone entitas Asia/Jakarta (PA-1), bulan berjalan = Oktober 2026. Jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after` (bagian 6, butir "Kendali jam sistem" di `suite.md`). Suite serial.
- State yang diubah spec: jam sistem. Tidak ada Save; form dikembalikan ke nilai tersimpan pada langkah 27 dan 28. Hook `after` memulihkan jam sistem.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-128: Mengganti Select tahun ke tahun berjalan mengosongkan bulan yang berada setelah bulan berjalan

1. Pilih tahun "2025" lalu bulan "December" pada First Accounting Period
2. Ganti Select tahun menjadi "2026"
3. Buka daftar opsi Select bulan
4. Verifikasi Select bulan dikosongkan otomatis
5. Verifikasi Select bulan menampilkan placeholder "Select month"
6. Verifikasi opsi November dan December tidak dapat dipilih
7. Verifikasi opsi January sampai October dapat dipilih

### TC-FA-PREF-129: Mengganti Select tahun ke tahun berjalan mempertahankan bulan yang tidak berada setelah bulan berjalan

8. Tutup daftar opsi Select bulan
9. Pilih tahun "2025" lalu bulan "March" pada First Accounting Period
10. Ganti Select tahun menjadi "2026"
11. Verifikasi Select bulan tetap bernilai "March"
12. Verifikasi tidak ada caption pada First Accounting Period

### TC-FA-PREF-148: Bulan setelah bulan berjalan (November 2026) tidak dapat dipilih pada UI

13. Pilih tahun "2026" pada Select tahun First Accounting Period
14. Buka daftar opsi Select bulan
15. Klik opsi "November"
16. Verifikasi opsi "November" dan "December" tampil namun tidak dapat dipilih
17. Verifikasi nilai Select bulan tidak berubah menjadi "November"

### TC-FA-PREF-149: Januari 2000 (batas bawah) dapat dipilih sebagai First Accounting Period

18. Tutup daftar opsi Select bulan
19. Buka daftar opsi Select tahun
20. Pilih tahun "2000" pada Select tahun First Accounting Period
21. Pilih bulan "January"
22. Verifikasi opsi tahun "2000" dan opsi bulan "January" dapat dipilih
23. Verifikasi tidak ada caption pada First Accounting Period
24. Buka daftar opsi Select tahun
25. Verifikasi tidak ada opsi tahun sebelum "2000"
26. Tutup daftar opsi Select tahun
27. Pilih tahun "2026" pada Select tahun First Accounting Period
28. Pilih bulan "March" pada Select bulan First Accounting Period

## Notes

- Jam sistem dikendalikan 28 Oktober 2026 (PA-1) karena Precondition d TC menyebut bulan berjalan; dipulihkan di hook `after`.
- Langkah penghubung (S-03): langkah 8, 18, 26, 27, 28 (menutup daftar opsi dan mengembalikan First Accounting Period ke Mar 2026 agar form tidak berakhir dirty; S-09). Langkah 19 (buka daftar tahun) adalah langkah penghubung ke langkah 20 dan 24.
- Asersi absence opsi tahun sebelum "2000" (langkah 25) berbasis anchor langkah 22 (opsi tahun "2000" tampil pada daftar yang sama; 8b.2).
- Temuan untuk QA:
  - Post Condition tidak ada pada keempat TC; tidak ada yang tidak diasersi.
  - Step 3 TC-FA-PREF-148 ("Klik opsi November") untuk opsi yang tidak dapat dipilih tidak menyebut perilaku daftar opsi setelah klik; spec mengasersi opsi tetap tidak dapat dipilih dan nilai Select tidak berubah.
