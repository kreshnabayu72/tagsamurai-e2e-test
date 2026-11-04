---
id: TC-FA-COA-E2E-069-resilience-bulk-gagal-timeout-dan-load-error-tabel
title: "Resilience Bulk Activate dan Deactivate Gagal, Timeout, dan Error State Tabel"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-5
  - TC-FA-COA-300
  - TC-FA-COA-301
  - TC-FA-COA-362
coverage:
  web: automated
---

# Resilience Bulk Activate dan Deactivate Gagal, Timeout, dan Error State Tabel

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons pemuatan daftar, Bulk Activate, dan Bulk Deactivate dipaksa lewat `Spectra.intercept()`, status akun dibaca dari backend nyata).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` yang disediakan tim FE, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - Akun P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Active, Used By 0).
  - Akun P3 `Fixture.settingsChartOfAccounts.p3` (Account Code `4-7001`, Account Name `Gain on Disposal`, Inactive, Used By 0).
  - Akun P4 `Fixture.settingsChartOfAccounts.p4` (Account Code `1-1002`, Account Name `Equipment – Legacy Code`, Inactive, Used By 0).
  - Akun P5 `Fixture.settingsChartOfAccounts.p5` (Account Code `CAP-6100`, Account Name `Capitalization Clearing – Repairs`, Active, Used By 0).
  - Akun P107 `Fixture.settingsChartOfAccounts.p107` (Account Code `4-7113`, Account Name `Gain on Disposal – Timeout Bulk A`, Inactive, Used By 0, sekali pakai) dan P108 `Fixture.settingsChartOfAccounts.p108` (Account Code `1-1104`, Account Name `Equipment – Timeout Bulk B`, Inactive, Used By 0, sekali pakai) untuk TC-FA-COA-362; hasil sebagian mungkin tersimpan di backend sehingga hook `before` dan `after` spec ini memulihkan P107 dan P108 ke Inactive (disediakan tim FE/BE).
  Tidak ada data Dinamis yang dibuat.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`, tanpa endpoint karangan):
  - TC-FA-COA-5: respons pemuatan daftar akun dipaksa 5xx.
  - TC-FA-COA-300: respons Bulk Activate dipaksa 5xx.
  - TC-FA-COA-301: respons Bulk Deactivate dipaksa 5xx.
  - TC-FA-COA-362: respons Bulk Activate tidak diberikan (timeout).
  Permintaan daftar akun setelah kegagalan bulk tidak di-intercept dan diamati untuk asersi tabel disegarkan. Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Pengecualian A-18 (lihat butir "Pengecualian A-18" di `suite.md`): P107 dan P108 adalah akun Pre-setup sekali pakai yang menjadi target Bulk Activate; seed idempotent dan pemulihan ke Inactive dijalankan di hook `before` dan `after` spec ini, dan satu akun serta satu Account Code literal (`4-7113`, `1-1104`) hanya dipakai spec ini. P1, P3, P4, dan P5 hanya dibaca: respons bulk dipaksa 5xx dan dialog dibatalkan dengan `[Cancel]` sehingga datanya tidak berubah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca status akun P107 dan P108 dari backend (langkah 54 dan 56).
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-COA-5: Error State tabel dan Try Again

1. Paksa respons pemuatan daftar akun menjadi 5xx lewat intercept jaringan
2. Muat ulang halaman Chart of Accounts
3. Verifikasi pesan `Unable to load this data.` tampil
4. Verifikasi tombol `[Try Again]` tampil
5. Lepas intercept pemuatan daftar akun
6. Klik `[Try Again]`
7. Verifikasi daftar akun dimuat ulang (tabel menampilkan baris akun)

### TC-FA-COA-300: Bulk Activate gagal 5xx

8. Ketik Search `Fixture.settingsChartOfAccounts.p3.name`, tekan Enter
9. Centang baris akun P3 (`Fixture.settingsChartOfAccounts.p3.code`)
10. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p4.name`, tekan Enter
11. Centang baris akun P4 (`Fixture.settingsChartOfAccounts.p4.code`)
12. Klik `Activate` pada Bulk Action Bar sehingga dialog D-15 terbuka
13. Paksa respons Bulk Activate menjadi 5xx lewat intercept jaringan
14. Klik `[Activate]` pada dialog D-15
15. Verifikasi toast `Error, failed to activate account.` tampil
16. Verifikasi dialog D-15 tetap terbuka
17. Verifikasi counter Bulk Action Bar `2 Accounts selected` (seleksi akun P3 dan P4 dipertahankan)
18. Verifikasi Bulk Action Bar dipertahankan
19. Verifikasi tabel disegarkan (permintaan daftar akun dikirim ulang setelah respons 5xx)
20. Lepas intercept respons Bulk Activate
21. Klik `[Cancel]` pada dialog D-15
22. Lepas seleksi akun terpilih

### TC-FA-COA-301: Bulk Deactivate gagal 5xx

23. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p1.name`, tekan Enter
24. Centang baris akun P1 (`Fixture.settingsChartOfAccounts.p1.code`)
25. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p5.name`, tekan Enter
26. Centang baris akun P5 (`Fixture.settingsChartOfAccounts.p5.code`)
27. Klik `Deactivate` pada Bulk Action Bar sehingga dialog D-02 terbuka
28. Paksa respons Bulk Deactivate menjadi 5xx lewat intercept jaringan
29. Klik `[Deactivate]` pada dialog D-02
30. Verifikasi toast `Error, failed to deactivate account.` tampil
31. Verifikasi dialog D-02 tetap terbuka
32. Verifikasi counter Bulk Action Bar `2 Accounts selected` (seleksi akun P1 dan P5 dipertahankan)
33. Verifikasi Bulk Action Bar dipertahankan
34. Verifikasi tabel disegarkan (permintaan daftar akun dikirim ulang setelah respons 5xx)
35. Lepas intercept respons Bulk Deactivate
36. Klik `[Cancel]` pada dialog D-02
37. Lepas seleksi akun terpilih

### TC-FA-COA-362: Timeout saat Bulk Activate

38. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p107.name`, tekan Enter
39. Centang baris akun P107 (`Fixture.settingsChartOfAccounts.p107.code`)
40. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p108.name`, tekan Enter
41. Centang baris akun P108 (`Fixture.settingsChartOfAccounts.p108.code`)
42. Klik `Activate` pada Bulk Action Bar sehingga dialog D-15 terbuka
43. Putus respons Bulk Activate lewat intercept jaringan (tidak ada respons)
44. Klik `[Activate]` pada dialog D-15
45. Verifikasi toast `Connection problem. Please try again.` tampil
46. Verifikasi toast tanpa tombol aksi
47. Verifikasi dialog D-15 tetap terbuka setelah langkah 44
48. Lepas intercept respons Bulk Activate
49. Klik `[Cancel]` pada dialog D-15
50. Verifikasi counter Bulk Action Bar `2 Accounts selected` (seleksi akun P107 dan P108 masih tampil)
51. Verifikasi Bulk Action Bar masih tampil
52. Verifikasi tabel disegarkan (permintaan daftar akun dikirim ulang setelah timeout)
53. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p107.name`, tekan Enter
54. Verifikasi status baris akun P107 (`Fixture.settingsChartOfAccounts.p107.code`) pada tabel sama dengan status P107 di backend
55. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p108.name`, tekan Enter
56. Verifikasi status baris akun P108 (`Fixture.settingsChartOfAccounts.p108.code`) pada tabel sama dengan status P108 di backend
57. Lepas seleksi akun terpilih
58. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas b, fault injection). Spec memuat 58 langkah, di atas sekitar 35 langkah. Alasan: empat TC berdiri sendiri dalam satu kelas harness; tiap TC bulk butuh dua akun yang berbeda nama sehingga dipilih lewat dua Search (R-23, 8b.9); Expected dipecah satu klausa per `Verifikasi` (S-01); dan tiap blok memuat pelepasan intercept serta pembersihan seleksi (S-09).
- Langkah penghubung (S-03, S-09): langkah 2 (memuat ulang halaman agar permintaan daftar yang di-intercept dikirim); langkah 8-11, 23-26, 38-41 (memilih dua akun lewat Search per akun, precondition TC; langkah 58 mengosongkan Search); langkah 5, 20, 35, 48 (melepas intercept); langkah 21, 36, 49 (menutup dialog dengan `[Cancel]`; langkah 49 adalah langkah 5 TC-FA-COA-362); langkah 22, 37, 57 (melepas seleksi); langkah 53 dan 55 (Search tiap akun sebelum membaca statusnya, R-23, butir 8b.13).
- Seleksi dua akun yang dipilih lewat dua Search berurutan diamati lewat counter Bulk Action Bar (langkah 17, 32, 50), karena tabel hanya menampilkan hasil Search terakhir; status akun dibaca per akun setelah Search akun itu (langkah 53 sampai 56).
- `A-18`: TC-FA-COA-362 memakai akun Pre-setup sekali pakai P107 dan P108 (Code literal `4-7113` dan `1-1104`) sebagai target Bulk Activate yang di-timeout; pemulihan di hook `before` dan `after`.
- Langkah 5 melepas intercept sebelum `[Try Again]` agar klik memuat ulang dari backend; TC-FA-COA-5 tidak menyebut kapan simulasi 5xx berhenti.
- Langkah 19, 34, dan 52 diamati lewat pengamatan permintaan daftar akun pada intercept jaringan; endpoint mengikuti halaman, tanpa endpoint karangan.
- Pembagian TC lintas spec (S-05): klausa "tidak ada log untuk akun yang tidak berubah" (Post Condition TC-FA-COA-300 dan TC-FA-COA-301) diasersi di spec 102, yang memuat pemicu bulk yang sama dengan baseline sendiri. Spec ini tidak mengasersi log.
- Temuan untuk QA:
  - TC-FA-COA-362 Expected d ("status terkini kedua akun") tidak menentukan status yang diharapkan; hasil sebagian bisa tersimpan (P107, P108, Q7), sehingga spec hanya mengasersi bahwa tabel sesuai status backend (langkah 54 dan 56). Perlu penajaman Expected di TC.
  - TC-FA-COA-300 dan 301 tidak menentukan apakah hasil sebagian bisa tersimpan; respons dipaksa 5xx sehingga tidak ada perubahan, dan kedua TC memakai akun Pre-setup bersama P1, P3, P4, P5.
  - TC-FA-COA-5 tidak menyebut cara memicu pemuatan ulang untuk menerapkan simulasi 5xx; spec memuat ulang halaman (langkah 2).
  - Asumsi bahwa seleksi bertahan saat isi Search diganti perlu dikonfirmasi tim FE; TC tidak menjelaskan cara memilih dua akun pada tabel multi-halaman.
  - Label tombol `[Cancel]` pada dialog D-02 dan D-15 diambil dari rumpun TC yang sama (bukan dari baris sumber spec ini).
