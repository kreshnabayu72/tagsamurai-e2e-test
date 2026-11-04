---
id: TC-FA-COA-E2E-068-resilience-delete-single-dan-bulk-delete-gagal-dan-timeout
title: "Resilience Delete Single dan Bulk Delete: Respons 5xx dan Timeout Mempertahankan Dialog dan Data"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-65
  - TC-FA-COA-305
  - TC-FA-COA-71
coverage:
  web: automated
---

# Resilience Delete Single dan Bulk Delete: Respons 5xx dan Timeout Mempertahankan Dialog dan Data

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Delete dipaksa lewat `Spectra.intercept()`, keberadaan akun dibaca dari backend nyata).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` yang disediakan tim FE, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - Akun P3 `Fixture.settingsChartOfAccounts.p3` (Account Code `4-7001`, Account Name `Gain on Disposal`, Inactive, Used By 0, Last Used kosong).
  - Akun P5 `Fixture.settingsChartOfAccounts.p5` (Account Code `CAP-6100`, Account Name `Capitalization Clearing – Repairs`, Used By 0, Last Used kosong; dipilih bersama P3 pada Bulk Delete TC-FA-COA-71).
  Kedua akun hanya dibaca; semua Delete digagalkan sehingga akun tidak terhapus dan tidak ada data Dinamis yang dibuat.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`, tanpa endpoint karangan):
  - TC-FA-COA-65: respons Delete single dipaksa 5xx.
  - TC-FA-COA-305: respons Delete single tidak diberikan (timeout).
  - TC-FA-COA-71: respons Bulk Delete dipaksa 5xx; permintaan daftar akun setelahnya tidak di-intercept dan diamati untuk asersi tabel disegarkan.
  Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-COA-65: Delete single gagal 5xx

1. Ketik Search `Fixture.settingsChartOfAccounts.p3.name`, tekan Enter
2. Klik row action `Delete` pada baris akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) sehingga dialog Delete (D-07) terbuka
3. Paksa respons Delete menjadi 5xx lewat intercept jaringan
4. Klik `[Delete]` pada dialog D-07
5. Verifikasi toast `Error, failed to delete account.` tampil
6. Verifikasi akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) tetap ada di tabel
7. Verifikasi dialog D-07 tetap terbuka dengan bullet akun P3
8. Lepas intercept respons Delete
9. Klik `[Cancel]` pada dialog D-07

### TC-FA-COA-305: Timeout saat Delete single

10. Klik row action `Delete` pada baris akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) sehingga dialog D-07 terbuka
11. Putus respons Delete lewat intercept jaringan (tidak ada respons)
12. Klik `[Delete]` pada dialog D-07
13. Verifikasi toast `Connection problem. Please try again.` tampil
14. Verifikasi dialog D-07 tetap terbuka
15. Verifikasi akun P3 (`Fixture.settingsChartOfAccounts.p3.code`) tetap ada di tabel
16. Lepas intercept respons Delete
17. Klik `[Cancel]` pada dialog D-07

### TC-FA-COA-71: Bulk Delete gagal 5xx

18. Centang baris akun P3 (`Fixture.settingsChartOfAccounts.p3.code`)
19. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p5.name`, tekan Enter
20. Centang baris akun P5 (`Fixture.settingsChartOfAccounts.p5.code`)
21. Klik `Delete` pada Bulk Action Bar sehingga dialog Delete bulk (D-08) terbuka
22. Paksa respons Bulk Delete menjadi 5xx lewat intercept jaringan
23. Klik `[Delete]` pada dialog D-08
24. Verifikasi toast `Error, failed to delete account.` tampil
25. Verifikasi seleksi akun P3 dan P5 tetap tampil
26. Verifikasi Bulk Action Bar tetap tampil
27. Verifikasi tabel disegarkan (permintaan daftar akun dikirim ulang setelah respons 5xx)
28. Verifikasi dialog D-08 tetap terbuka dengan daftar akun terpilih P3 dan P5
29. Lepas intercept respons Bulk Delete
30. Klik `[Cancel]` pada dialog D-08
31. Lepas seleksi akun terpilih
32. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas b, fault injection). Tiga TC berdiri sendiri dalam satu kelas harness; 32 langkah berada di bawah sekitar 35.
- Langkah penghubung (S-03, S-09): langkah 1 dan 32 (Search nama P3 sebagai penemu baris target, R-16, R-23, lalu kosongkan); langkah 2 dan 10 (membuka dialog D-07 lewat row action `Delete`, precondition TC-FA-COA-65 dan 305); langkah 18-21 (memilih P3 dan P5 sebagai precondition TC-FA-COA-71; Search diganti antar pemilihan sesuai 8b.9); langkah 8, 16, 29 (melepas intercept); langkah 9, 17, 30 (menutup dialog dengan `[Cancel]`); langkah 31 (melepas seleksi, S-09).
- Langkah 27 diamati lewat pengamatan permintaan daftar akun pada intercept jaringan; endpoint mengikuti halaman, tanpa endpoint karangan.
- Pembagian TC lintas spec (S-05): klausa "tidak ada entri log" pada Expected c TC-FA-COA-65 dan TC-FA-COA-305, serta Post Condition TC-FA-COA-71, diasersi di spec 099, yang memuat pemicu Delete yang sama dengan baseline sendiri. Spec ini tidak mengasersi log.
- Post Condition TC-FA-COA-71 ("sebagian akun mungkin sudah terhapus") tidak diasersi karena respons dipaksa 5xx oleh intercept sehingga tidak ada penghapusan sebagian di backend.
- Temuan untuk QA:
  - TC-FA-COA-71 menyebut P3 dan P5 "eligible", sedangkan Pre-setup mencatat P5 Active; bila Delete hanya untuk akun Inactive, bulk Delete akan terblokir sebelum dialog D-08. Spec mengikuti TC.
  - TC-FA-COA-71 tidak menjelaskan bagaimana kedua akun dipilih pada tabel multi-halaman; spec memakai Search per akun dengan asumsi seleksi bertahan saat Search diganti (perlu dikonfirmasi tim FE).
