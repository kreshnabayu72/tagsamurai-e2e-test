---
id: TC-FA-FAAC-E2E-040-create-validasi-tax-method-threshold-dan-akun-ganda
title: "Create Asset Class: Validasi Tax Depreciation Class, Tax Method, Capitalization Threshold, dan Akun Ganda"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-114
  - TC-FA-FAAC-115
  - TC-FA-FAAC-116
  - TC-FA-FAAC-117
sourceRules: ["V-19", "ST-04", "F-FAAC-01.k4", "V-20", "V-22", "V-38", "§8.4#r9", "§4.2f#b2"]
smoke: []
dependsOn: []
trace:
  "V-19": 5
  "ST-04": 6
  "F-FAAC-01.k4": [7, 11]
  "V-20": 10
  "V-22": [13, 15]
  "V-38": [20, 22, 23]
  "§8.4#r9": 24
  "§4.2f#b2": 26
coverage:
  web: automated
---

# Create Asset Class: Validasi Tax Depreciation Class, Tax Method, Capitalization Threshold, dan Akun Ganda

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active, mengizinkan Tax Method `Declining Balance`); akun Chart of Accounts `11001 – Machinery Cost` (Active, dipakai di field Asset Cost dan Accumulated Depreciation; hanya dibaca). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Semua Submit di spec ini ditolak validasi sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup; Class Code `B-X7`, `B-X8`, `B-X9` dan nilai uji lain adalah input uji kebijakan yang submit-nya diblokir dan boleh literal.
- Kemampuan teknis: membaca jumlah Asset Class lewat kemampuan baca BE (disediakan tim FE/BE) untuk baseline N0 sebelum Submit pertama.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel

### TC-FA-FAAC-114: Submit dengan Tax Depreciation Class belum dipilih

3. Isi Class Code `B-X7`, Class Name `X7`, Method `Straight Line`, Useful Life `60` tanpa memilih Tax Depreciation Class
4. Klik `Submit`
5. Verifikasi caption: `Tax depreciation class must not be empty`
6. Verifikasi tab Depreciation diberi titik peringatan
7. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-115: Submit dengan Tax Method kosong pada Tax Depreciation Class yang punya metode

8. Ganti isi Class Code dengan `B-X8` dan Class Name dengan `X8`; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` tanpa memilih Tax Method
9. Klik `Submit`
10. Verifikasi caption: `Tax method must not be empty`
11. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-116: Capitalization Threshold negatif

12. Ketik Capitalization Threshold `-1`
13. Verifikasi caption langsung muncul: `Capitalization threshold must be 0 or more`
14. Ganti isi Capitalization Threshold menjadi `0`
15. Verifikasi tidak ada caption pada Capitalization Threshold

### TC-FA-FAAC-117: Akun yang sama dipakai dua field akun (selain Gain dan Loss on Disposal)

16. Ganti isi Class Code dengan `B-X9` dan Class Name dengan `X9`; pilih Tax Method `Declining Balance` sehingga semua field wajib valid
17. Klik tab `Accounts`
18. Pilih Asset Cost `11001 – Machinery Cost`
19. Pilih `11001 – Machinery Cost` pada Accumulated Depreciation
20. Verifikasi caption langsung muncul saat memilih di Accumulated Depreciation: `Account already used for Asset Cost. Choose a different account.`
21. Klik `Submit`
22. Verifikasi Submit diblokir (halaman tetap terbuka)
23. Verifikasi tab Accounts dibuka selama konflik masih ada
24. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### Penutup

25. Klik breadcrumb `Asset Class`
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-114 sampai 117). Tidak ada TC hanya-BE di spec ini.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 2 dan tiap TC melanjutkan isian TC sebelumnya. Method `Straight Line` dan Useful Life `60` dari langkah 3 tetap terisi untuk TC-115 sampai TC-117.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), langkah 16 (melengkapi field wajib agar konflik akun menjadi satu-satunya penyebab penolakan, sesuai Pre-condition langkah TC-117), dan langkah 25 sampai 27 (menutup form dirty, S-08).
- Asersi "tidak ada Asset Class dibuat" (langkah 7, 11, 24) memakai selisih terhadap baseline N0 dengan anchor positif berupa caption penolakan pada langkah yang mendahuluinya. Asersi "tidak ada caption" (langkah 15) didahului caption pada field yang sama (langkah 13).
- Temuan untuk QA:
  - TC-116 tidak menyebut tab tempat Capitalization Threshold berada; spec tidak menambah langkah pindah tab.
  - TC-117 butir b menggabungkan tiga klausa (Submit diblokir, tab Accounts dibuka, tidak ada Asset Class dibuat); ditulis satu `Verifikasi` per klausa.
