---
id: TC-FA-FAAC-E2E-039-create-validasi-units-dan-residual-value
title: "Create Asset Class: Validasi Total Estimated Units, Unit Type, dan Residual Value"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-110
  - TC-FA-FAAC-111
  - TC-FA-FAAC-112
  - TC-FA-FAAC-113
sourceRules: ["V-16", "§8.4#r9", "V-15", "V-14", "V-17", "FI-06", "§4.2f#b2"]
smoke: []
dependsOn: []
trace:
  "V-16": 5
  "§8.4#r9": [6, 14]
  "V-15": [8, 10]
  "V-14": 13
  "V-17": [16, 18, 20, 22]
  "FI-06": 23
  "§4.2f#b2": 25
coverage:
  web: automated
---

# Create Asset Class: Validasi Total Estimated Units, Unit Type, dan Residual Value

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active, mengizinkan Tax Method `Declining Balance`). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Semua Submit di spec ini ditolak validasi sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup; Class Code `B-X5`, `B-X6` dan nilai uji lain adalah input uji kebijakan yang submit-nya diblokir dan boleh literal.
- Kemampuan teknis: membaca jumlah Asset Class lewat kemampuan baca BE (disediakan tim FE/BE) untuk baseline N0 sebelum Submit pertama.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel

### TC-FA-FAAC-112: Submit Units of Production dengan Unit Type belum dipilih

3. Isi Class Code `B-X6` dan Class Name `X6`; pilih Method `Units of Production`, isi Useful Life `60` dan Total Estimated Units `1000` tanpa memilih Unit Type; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` dan Tax Method `Declining Balance`
4. Klik `Submit`
5. Verifikasi caption: `Unit type must not be empty`
6. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-111: Total Estimated Units bernilai 0 atau kurang

7. Ganti isi Total Estimated Units dengan `0`
8. Verifikasi caption langsung muncul: `Total estimated units must be greater than 0`
9. Ganti isi Total Estimated Units menjadi `1`
10. Verifikasi tidak ada caption pada Total Estimated Units

### TC-FA-FAAC-110: Submit Units of Production dengan Total Estimated Units kosong

11. Kosongkan isi Total Estimated Units dan pilih Unit Type `Kilometer`; Class Code `B-X5` dan Class Name `X5` menggantikan isian sebelumnya
12. Klik `Submit`
13. Verifikasi caption: `Total estimated units must not be empty`
14. Verifikasi jumlah Asset Class sama dengan N0 (tidak ada Asset Class dibuat)

### TC-FA-FAAC-113: Residual Value di luar rentang menurut unit

15. Pilih unit Percent pada Residual Value dan ketik Residual Value `101`
16. Verifikasi caption: `Residual value must be between 0 and 100`
17. Ganti ke unit Amount dan ketik Residual Value `-1`
18. Verifikasi caption: `Residual value must be 0 or more`
19. Ketik Residual Value `0` pada unit Amount
20. Verifikasi tidak ada caption pada Residual Value
21. Ganti ke unit Percent dan ketik Residual Value `100`
22. Verifikasi tidak ada caption pada Residual Value
23. Verifikasi batas nilai mengikuti unit yang terpilih (Percent: 0 sampai 100; Amount: 0 atau lebih)

### Penutup

24. Klik breadcrumb `Asset Class`
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-110 sampai 113). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di dalam spec: TC-112, TC-111, TC-110, TC-113. Alasannya: TC-112 mensyaratkan Unit Type belum dipilih dan TC-110 mensyaratkan Total Estimated Units kosong; urutan ini membuat tiap TC dimulai dari state form yang dibutuhkannya tanpa membuka form berulang (prinsip 13 bagian 3) dan tanpa mengosongkan select Unit Type, yang caranya tidak ada di TC.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), bagian awal langkah 11 (mengosongkan Total Estimated Units dan mengganti Class Code dan Class Name), dan langkah 24 sampai 26 (menutup form dirty, S-08).
- Asersi "tidak ada Asset Class dibuat" (langkah 6 dan 14) memakai selisih terhadap baseline N0 dengan anchor positif berupa caption penolakan pada langkah yang mendahuluinya. Asersi "tidak ada caption" (langkah 10, 20, 22) didahului caption pada field yang sama (langkah 8, 16, 18).
- Expected TC-113 butir c ("batas nilai mengikuti unit yang terpilih") ditulis sebagai satu `Verifikasi` (langkah 23) sebagai kesimpulan dari langkah 16 sampai 22 (S-03, kesimpulan tidak teramati terpisah).
- Temuan untuk QA:
  - TC-113 menggabungkan caption dan "tidak ada caption" untuk empat nilai dalam tiga butir Expected; butir c memuat klausa kesimpulan ("batas nilai mengikuti unit") tanpa langkah observasi tersendiri.
  - TC-110 dan TC-112 menyebut "pilih Tax Depreciation Class dan Tax Method valid" tanpa nilai; spec memakai `Bukan bangunan – Kelompok 3` dan `Declining Balance` seperti TC-97.
