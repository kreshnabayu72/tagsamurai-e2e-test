---
id: TC-FA-COA-E2E-066-resilience-create-dan-edit-gagal-5xx-dan-timeout
title: "Resilience Create dan Edit Account: Respons 5xx dan Timeout Mempertahankan Modal dan Input"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-32
  - TC-FA-COA-302
  - TC-FA-COA-41
  - TC-FA-COA-303
coverage:
  web: automated
---

# Resilience Create dan Edit Account: Respons 5xx dan Timeout Mempertahankan Modal dan Input

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Create dan Save Edit dipaksa lewat `Spectra.intercept()`, sedangkan state akun P1 dan tabel dibaca dari backend nyata).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`): akun P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Function Depreciation Expense, Active, Used By 0, belum pernah diekspor). P1 hanya dibaca; semua aksi tulis di spec ini digagalkan sehingga P1 tidak berubah.
- Data Dinamis (tidak ada yang tersimpan; nama dipakai sebagai input form): Account Name `Depreciation Expense – Failure Test {runId}-066` (Code `5-6600`), `Depreciation Expense – Timeout {runId}-066` (Code `5-6910`), `Depreciation Expense – Admin Failure {runId}-066`, `Depreciation Expense – Admin Timeout {runId}-066`. Account Code maksimal 15 karakter sehingga Code tidak dapat bersuffix `{runId}`; suffix dipasang pada Name dan Code literal dibersihkan di hook `before` dan `after` spec ini (R-13).
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`, tanpa endpoint karangan):
  - TC-FA-COA-32: respons Create dipaksa 5xx.
  - TC-FA-COA-302: respons Create tidak diberikan (timeout).
  - TC-FA-COA-41: respons Save Edit dipaksa 5xx.
  - TC-FA-COA-303: respons Save Edit tidak diberikan (timeout).
  Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Hook `before` dan `after` spec ini menghapus akun dengan Code `5-6600` dan `5-6910` bila ada (pembersihan lewat API, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-COA-32: Submit Create gagal 5xx

1. Klik `+ Account` di toolbar
2. Isi Account Code `5-6600`
3. Isi Account Name `Depreciation Expense – Failure Test {runId}-066`
4. Pilih Account Function `Depreciation Expense`
5. Paksa respons Create menjadi 5xx lewat intercept jaringan
6. Klik `[Submit]`
7. Verifikasi toast `Error, failed to create account.` tampil
8. Verifikasi toast tanpa tombol aksi (tidak ada `[Try Again]`)
9. Verifikasi modal Add Account tetap terbuka
10. Verifikasi Account Code `5-6600`, Account Name `Depreciation Expense – Failure Test {runId}-066`, dan Account Function `Depreciation Expense` tetap terisi
11. Lepas intercept respons Create
12. Klik ikon ✕ pada modal Add Account
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`

### TC-FA-COA-302: Timeout saat Create

15. Klik `+ Account` di toolbar
16. Isi Account Code `5-6910`
17. Isi Account Name `Depreciation Expense – Timeout {runId}-066`
18. Pilih Account Function `Depreciation Expense`
19. Putus respons Create lewat intercept jaringan (tidak ada respons)
20. Klik `[Submit]`
21. Verifikasi toast `Connection problem. Please try again.` tampil
22. Verifikasi toast tanpa tombol aksi (tidak ada `[Try Again]`)
23. Verifikasi modal Add Account tetap terbuka
24. Verifikasi Account Code `5-6910`, Account Name `Depreciation Expense – Timeout {runId}-066`, dan Account Function `Depreciation Expense` tetap terisi
25. Lepas intercept respons Create
26. Klik ikon ✕ pada modal Add Account
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`
29. Ketik Search `{runId}-066`, tekan Enter
30. Verifikasi tabel menampilkan `No results found` (tidak ada akun `5-6600` maupun `5-6910` dibuat)
31. Klik `(←)` pada kotak Search

### TC-FA-COA-41: Save Edit gagal 5xx

32. Ketik Search `Fixture.settingsChartOfAccounts.p1.name`, tekan Enter
33. Klik row action `Edit` pada baris akun P1 (`Fixture.settingsChartOfAccounts.p1.code`)
34. Ubah Account Name menjadi `Depreciation Expense – Admin Failure {runId}-066`
35. Paksa respons Save Edit menjadi 5xx lewat intercept jaringan
36. Klik `[Save]`
37. Verifikasi toast `Error, failed to update account.` tampil
38. Verifikasi modal Edit Account tetap terbuka
39. Verifikasi Account Name `Depreciation Expense – Admin Failure {runId}-066` tetap terisi
40. Lepas intercept respons Save Edit
41. Klik ikon ✕ pada modal Edit Account
42. Verifikasi dialog `Unsaved Changes` tampil
43. Klik `[Leave]`

### TC-FA-COA-303: Timeout saat Save Edit

44. Klik row action `Edit` pada baris akun P1 (`Fixture.settingsChartOfAccounts.p1.code`)
45. Ubah Account Name menjadi `Depreciation Expense – Admin Timeout {runId}-066`
46. Putus respons Save Edit lewat intercept jaringan (tidak ada respons)
47. Klik `[Save]`
48. Verifikasi toast `Connection problem. Please try again.` tampil
49. Verifikasi modal Edit Account tetap terbuka
50. Verifikasi Account Name `Depreciation Expense – Admin Timeout {runId}-066` tetap terisi
51. Lepas intercept respons Save Edit
52. Klik ikon ✕ pada modal Edit Account
53. Verifikasi dialog `Unsaved Changes` tampil
54. Klik `[Leave]`
55. Verifikasi baris akun P1 menampilkan Account Name `Depreciation Expense – Admin` (tidak ada perubahan tersimpan oleh TC-FA-COA-41 maupun TC-FA-COA-303)
56. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas b, fault injection). Empat TC berdiri sendiri dan satu kelas harness; jumlah langkah (56) melewati sekitar 35 langkah karena Expected dipecah satu klausa per `Verifikasi` (S-01) dan tiap blok memuat pemicu intercept, pemulihan form dirty (✕, `Unsaved Changes`, `[Leave]`, S-08), serta pelepasan intercept.
- Langkah penghubung (S-03, S-09): langkah 11, 25, 40, 51 (melepas intercept agar tidak bocor ke blok berikutnya); langkah 12-14, 26-28, 41-43, 52-54 (menutup form dirty secara deterministik); langkah 29 dan 31 (Search sufiks `{runId}-066` untuk memeriksa akun tidak terbentuk, lalu kosongkan); langkah 32 dan 56 (Search nama P1 sebagai penemu baris target, R-16, R-23, lalu kosongkan).
- Langkah 30 mencakup Expected c TC-FA-COA-32 dan TC-FA-COA-302 sekaligus karena kedua Name berakhiran `{runId}-066`. Langkah 55 mencakup Expected c TC-FA-COA-41 dan TC-FA-COA-303.
- Klausa "tidak ada log" pada Expected c keempat TC tidak diasersi di spec ini (S-05). Asersi absence log berada di spec absence (kelas g); rujukan: TC-FA-COA-51 dan TC-FA-COA-52 di spec 083, yang tidak memuat TC-FA-COA-32, 302, 41, 303.
- Hook `after` melepas intercept yang tersisa dan menghapus akun Code `5-6600` dan `5-6910` bila ada.
- Temuan untuk QA:
  - Klausa "tidak ada log" pada Expected c TC-FA-COA-32, 302, 41, 303 tidak punya spec absence yang memuatnya (spec 083 hanya memuat TC-FA-COA-51, 52, 96, 118); perlu keputusan apakah dipindah atau cukup tercatat di sini.
  - Search dengan sufiks `{runId}-066` mengasumsikan Search mencocokkan sebagian Account Name; perlu dikonfirmasi tim FE.
  - TC-FA-COA-32 dan 302 memakai Code literal `5-6600` dan `5-6910` yang tidak dapat bersuffix run (maksimal 15 karakter); dibersihkan di hook `before` dan `after`.
  - TC-FA-COA-32, 302, 41, 303 tidak menyebut cara menutup modal setelah kegagalan; spec memakai ✕, `Unsaved Changes`, `[Leave]` sebagai langkah penghubung.
