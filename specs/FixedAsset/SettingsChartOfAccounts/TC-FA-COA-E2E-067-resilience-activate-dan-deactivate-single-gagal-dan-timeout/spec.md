---
id: TC-FA-COA-E2E-067-resilience-activate-dan-deactivate-single-gagal-dan-timeout
title: "Resilience Activate dan Deactivate Single: Respons 5xx dan Timeout Mengembalikan Switch dan Mempertahankan Dialog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-57
  - TC-FA-COA-58
  - TC-FA-COA-304
  - TC-FA-COA-361
coverage:
  web: automated
---

# Resilience Activate dan Deactivate Single: Respons 5xx dan Timeout Mengembalikan Switch dan Mempertahankan Dialog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Deactivate dan Activate dipaksa lewat `Spectra.intercept()`, status akun dibaca dari backend nyata).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` yang disediakan tim FE, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - Akun P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Active, Used By 0).
  - Akun P3 `Fixture.settingsChartOfAccounts.p3` (Account Code `4-7001`, Account Name `Gain on Disposal`, Inactive, Used By 0).
  Kedua akun hanya dibaca; semua aksi status digagalkan sehingga status tidak berubah dan tidak ada data Dinamis yang dibuat.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`, tanpa endpoint karangan):
  - TC-FA-COA-57: respons Deactivate dipaksa 5xx.
  - TC-FA-COA-58: respons Activate dipaksa 5xx.
  - TC-FA-COA-304: respons Deactivate tidak diberikan (timeout).
  - TC-FA-COA-361: respons Activate tidak diberikan (timeout).
  Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-COA-57: Deactivate gagal 5xx

1. Ketik Search `Fixture.settingsChartOfAccounts.p1.name`, tekan Enter
2. Klik switch Status pada baris akun P1 (`Fixture.settingsChartOfAccounts.p1.code`) sehingga dialog Deactivate (D-01) terbuka
3. Paksa respons Deactivate menjadi 5xx lewat intercept jaringan
4. Klik `[Deactivate]` pada dialog D-01
5. Verifikasi toast `Error, failed to deactivate account.` tampil
6. Verifikasi switch Status akun P1 kembali Active (nilai tersimpan)
7. Verifikasi dialog D-01 tetap terbuka
8. Lepas intercept respons Deactivate
9. Klik `[Cancel]` pada dialog D-01

### TC-FA-COA-304: Timeout saat Deactivate

10. Klik switch Status pada baris akun P1 (`Fixture.settingsChartOfAccounts.p1.code`) sehingga dialog D-01 terbuka
11. Putus respons Deactivate lewat intercept jaringan (tidak ada respons)
12. Klik `[Deactivate]` pada dialog D-01
13. Verifikasi toast `Connection problem. Please try again.` tampil
14. Verifikasi dialog D-01 tetap terbuka
15. Verifikasi switch Status akun P1 kembali Active
16. Lepas intercept respons Deactivate
17. Klik `[Cancel]` pada dialog D-01

### TC-FA-COA-58: Activate gagal 5xx

18. Klik `(←)` pada kotak Search
19. Ketik Search `Fixture.settingsChartOfAccounts.p3.name`, tekan Enter
20. Klik switch Status pada baris akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) sehingga dialog konfirmasi Activate (D-14) terbuka
21. Paksa respons Activate menjadi 5xx lewat intercept jaringan
22. Klik `[Activate]` pada dialog D-14
23. Verifikasi toast `Error, failed to activate account.` tampil
24. Verifikasi switch Status akun P3 kembali Inactive (nilai tersimpan)
25. Verifikasi dialog D-14 tetap terbuka
26. Lepas intercept respons Activate
27. Klik `[Cancel]` pada dialog D-14

### TC-FA-COA-361: Timeout saat Activate

28. Klik switch Status pada baris akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) sehingga dialog D-14 terbuka
29. Putus respons Activate lewat intercept jaringan (tidak ada respons)
30. Klik `[Activate]` pada dialog D-14
31. Verifikasi toast `Connection problem. Please try again.` tampil
32. Verifikasi dialog D-14 tetap terbuka
33. Verifikasi switch Status akun P3 kembali Inactive
34. Lepas intercept respons Activate
35. Klik `[Cancel]` pada dialog D-14
36. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas b, fault injection). Spec memuat 36 langkah, sedikit di atas sekitar 35 langkah: empat TC berdiri sendiri dalam satu kelas harness dan Expected dipecah satu klausa per `Verifikasi` (S-01), sehingga tidak dipecah lebih jauh.
- Langkah penghubung (S-03, S-09): langkah 1, 18, 19, 36 (Search nama akun sebagai penemu baris target, R-16, R-23, lalu kosongkan); langkah 2, 10, 20, 28 (membuka dialog konfirmasi lewat switch Status yang menjadi precondition TC); langkah 8, 16, 26, 34 (melepas intercept); langkah 9, 17, 27, 35 (menutup dialog dengan `[Cancel]`, label tombol dari TC lain di rumpun yang sama).
- Expected b dan c TC-FA-COA-57 dan TC-FA-COA-58 sama-sama menyebut switch kembali ke nilai tersimpan; keduanya diasersi satu kali (langkah 6 dan 24), dialog tetap terbuka pada langkah 7 dan 25.
- Pembagian TC lintas spec (S-05): klausa "tidak ada log" pada Expected c TC-FA-COA-304 dan TC-FA-COA-361 diasersi di spec 100, yang memuat pemicu timeout yang sama dengan baseline sendiri. Spec ini tidak mengasersi log.
- Temuan untuk QA:
  - TC-FA-COA-57 dan 58 tidak memuat langkah membuka dialog D-01 dan D-14; spec menambahkannya dari precondition TC-FA-COA-304 dan 361 (klik switch Status).
  - Tidak ada langkah menutup dialog setelah kegagalan di TC; `[Cancel]` dipakai sebagai langkah penghubung.
