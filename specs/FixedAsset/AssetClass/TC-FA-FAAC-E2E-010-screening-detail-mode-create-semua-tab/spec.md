---
id: TC-FA-FAAC-E2E-010-screening-detail-mode-create-semua-tab
title: "Screening Halaman Detail Mode Create: Tab General, Depreciation, Accounts, dan Asset Names"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-15
  - TC-FA-FAAC-16
  - TC-FA-FAAC-17
  - TC-FA-FAAC-20
coverage:
  web: automated
---

# Screening Halaman Detail Mode Create: Tab General, Depreciation, Accounts, dan Asset Names

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): Chart of Accounts memuat akun Active per Account Function (Asset Cost, Accumulated Depreciation, Depreciation Expense, Gain on Disposal, Loss on Disposal) dan satu akun Inactive `19999 – Inactive Cost` ber-function Asset Cost. Seed disediakan tim FE/BE (lihat `suite.md`).
- Spec ini hanya membuka form dan membaca; tidak ada field yang diisi dan tidak ada data yang dibuat atau diubah.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-15: Screening Halaman Detail mode Create tab General

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Verifikasi breadcrumb `Settings > Accounting > Asset Class > Add Asset Class`
3. Verifikasi judul `Add Asset Class`
4. Verifikasi tidak ada Badge Status
5. Verifikasi tidak ada Alert versi Scheduled
6. Verifikasi bar tab berisi `General`, `Depreciation`, `Accounts`, `Asset Names`
7. Verifikasi tab `General` aktif
8. Verifikasi field Class Code kosong dengan placeholder `Enter class code`
9. Verifikasi helper Class Code `Letters, numbers, hyphens, underscores, and dots only (e.g. HEAVY-EQ)`
10. Verifikasi field Class Name kosong dengan placeholder `Enter class name`
11. Verifikasi field Description kosong dengan placeholder `Enter description`
12. Verifikasi field Last Posted Period dan Last Exported Period tidak tampil
13. Verifikasi footer tetap terlihat di bawah halaman berisi tombol `Clear Field` dan `Submit`
14. Verifikasi tombol `Save` tidak ada

### TC-FA-FAAC-16: Screening Halaman Detail mode Create tab Depreciation

15. Klik tab Depreciation
16. Verifikasi Method pada kartu Commercial menampilkan placeholder `Select method`
17. Klik select Method
18. Verifikasi opsi Method `Straight Line`, `Declining Balance`, `Units of Production`, `Not Depreciated`
19. Tutup daftar opsi dengan Esc
20. Verifikasi Depreciation Start Convention bernilai awal `Full month from in-service date`
21. Klik select Depreciation Start Convention
22. Verifikasi opsi `Full month from in-service date`, `Start next month`, `Daily prorata`
23. Tutup daftar opsi dengan Esc
24. Verifikasi Residual Value menampilkan placeholder `Enter residual value` dengan unit awal `Percent`
25. Verifikasi field Useful Life, Declining Rate, Total Estimated Units, dan Unit Type belum tampil
26. Arahkan kursor ke ikon info di samping label Depreciation Start Convention
27. Verifikasi tooltip `When depreciation starts for the Commercial book. For an asset in service on 20 March: Full month from in-service date counts all of March; Start next month starts in April; Daily prorata counts 12/31 of March.`
28. Verifikasi Tax Depreciation Class pada kartu Fiscal menampilkan placeholder `Select tax depreciation class`
29. Verifikasi Tax Method menampilkan placeholder `Select tax method`
30. Verifikasi Useful Life & Rate fiskal menampilkan `—`
31. Verifikasi Tax Depreciation Start Rule bernilai awal `Month of expenditure`
32. Klik select Tax Depreciation Start Rule
33. Verifikasi opsi `Month of expenditure` dan `Month of use`
34. Verifikasi helper opsi `Month of use` berbunyi `Requires approval from the tax authority.`
35. Tutup daftar opsi dengan Esc
36. Arahkan kursor ke ikon info di samping label Tax Depreciation Start Rule
37. Verifikasi tooltip `When depreciation starts for the Fiscal book. Month of expenditure starts in the month the cost is incurred; Month of use starts in the month the asset is first used and requires approval from the tax authority.`
38. Verifikasi Capitalization Threshold pada kartu Capitalization menampilkan placeholder `Enter capitalization threshold`
39. Verifikasi helper Capitalization Threshold `Leave empty to use the company default.`

### TC-FA-FAAC-17: Screening Halaman Detail mode Create tab Accounts

40. Klik tab Accounts
41. Verifikasi deskripsi di atas field (teks biasa, bukan Alert) berbunyi `Accounts can be left empty, but journals cannot be exported until Asset Cost, Accumulated Depreciation, and Depreciation Expense are set.`
42. Verifikasi tepat lima field: Asset Cost, Accumulated Depreciation, Depreciation Expense, Gain on Disposal, Loss on Disposal
43. Verifikasi tidak ada field Capitalization Offset
44. Verifikasi semua placeholder field berbunyi `Select account`
45. Verifikasi helper Gain on Disposal `Leave empty to use the company default gain account.`
46. Verifikasi helper Loss on Disposal `Leave empty to use the company default loss account.`
47. Klik select Asset Cost
48. Verifikasi opsi berformat `[Account Code] – [Account Name]` dan berurut kode akun A-Z
49. Verifikasi opsi hanya memuat akun Active dengan Account Function sesuai
50. Verifikasi akun Inactive `19999 – Inactive Cost` tidak ditawarkan
51. Verifikasi di dasar daftar ada `+ Create account`
52. Tutup daftar opsi dengan Esc
53. Klik select Gain on Disposal
54. Verifikasi daftar opsi juga memuat akun ber-function Loss on Disposal
55. Tutup daftar opsi dengan Esc

### TC-FA-FAAC-20: Tab Asset Names pada Halaman Detail mode Create

56. Klik tab Asset Names
57. Verifikasi tab `Asset Names` Enabled (tidak Disabled) dan dapat dibuka
58. Verifikasi tombol `+ Assign Asset Names` tampil pada toolbar tab
59. Klik breadcrumb `Asset Class` untuk meninggalkan form

## Notes

- Spec melewati sekitar 35 langkah (59 langkah): keempat blok adalah screening satu form yang sama (Halaman Detail mode Create) pada dataset yang sama dan tanpa input, tiap tab berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan pembukaan form. Langkah bertambah karena `Verifikasi` dipecah per klausa (S-01) dan tiap select dibuka lalu ditutup.
- Langkah penghubung (S-03): langkah 19, 23, 35, 52, dan 55 (menutup daftar opsi dengan Esc), langkah 59 (meninggalkan form yang tidak berubah; form tidak dirty sehingga tidak ada dialog `Unsaved Changes`).
- Tooltip (langkah 27 dan 37) diasersi segera sesudah kursor diarahkan (8b butir 5).
- Temuan untuk QA:
  - TC-FA-FAAC-16 langkah 5 membuka select Method, Depreciation Start Convention, dan Tax Depreciation Start Rule tanpa menyebut menutupnya; spec menutup dengan Esc sebagai langkah penghubung.
  - TC-FA-FAAC-17 butir d menyebut opsi "berurut kode akun A-Z" tanpa data kode; asersi mengikuti Chart of Accounts seed.
