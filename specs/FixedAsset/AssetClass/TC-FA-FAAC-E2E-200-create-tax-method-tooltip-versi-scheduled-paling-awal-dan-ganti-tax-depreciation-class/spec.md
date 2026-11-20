---
id: TC-FA-FAAC-E2E-200-create-tax-method-tooltip-versi-scheduled-paling-awal-dan-ganti-tax-depreciation-class
title: "Create Asset Class: Tooltip Opsi Disabled Memakai Effective From Versi Scheduled Paling Awal dan Ganti Tax Depreciation Class Menghitung Ulang Tax Method"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-742
  - TC-FA-FAAC-743
sourceRules: ["FAAC-LOGIC-02l", "FAAC-LOGIC-02m", "ST-38", "F-FAAC-01.k15", "E-FAAC-121", "FI-03"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02m": [6, 9]
  "ST-38": [6, 22]
  "F-FAAC-01.k15": 6
  "E-FAAC-121": 6
  "FAAC-LOGIC-02l": [19, 22, 26]
  "FI-03": [19, 26]
anchor: [9, 6]
coverage:
  web: automated
---

# Create Asset Class: Tooltip Opsi Disabled Memakai Effective From Versi Scheduled Paling Awal dan Ganti Tax Depreciation Class Menghitung Ulang Tax Method

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca; seed Tax Depreciation Class Active, belum dipakai Asset Class): `Seed Irisan B` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; tiga versi Scheduled: M+2 mengizinkan `Straight Line` dan `Declining Balance`, M+4 hanya `Straight Line`, M+6 hanya `Straight Line`); `Seed Irisan A` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; satu versi Scheduled sejak M+2 hanya mengizinkan `Straight Line`); `Bukan bangunan – Kelompok 3` dan `Bukan bangunan – Kelompok 1` (Active, mengizinkan `Straight Line` dan `Declining Balance`, tanpa versi Scheduled). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M.
- Data Dinamis: tidak ada. Spec tidak melakukan Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis (disediakan tim FE/BE): hover pada opsi select (langkah 5, 8, dan 21); pembacaan tooltip opsi Disabled; seed Tax Depreciation Class beserta versi Scheduled lewat fixture BE.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir tiap blok TC.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-742: Tooltip opsi Disabled memakai Effective From versi Scheduled paling awal yang tidak mengizinkan metode

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`
3. Pilih Tax Depreciation Class `Seed Irisan B`
4. Buka select Tax Method
5. Arahkan kursor ke opsi `Declining Balance`
6. Verifikasi opsi `Declining Balance` Disabled dengan tooltip `Not allowed from <M+4 dalam format MMM yyyy>.`
7. Verifikasi tooltip bukan `<M+2 dalam format MMM yyyy>` dan bukan `<M+6 dalam format MMM yyyy>` (versi M+2 mengizinkan, M+4 adalah yang paling awal yang tidak mengizinkan)
8. Arahkan kursor ke opsi `Straight Line`
9. Verifikasi opsi `Straight Line` Enabled
10. Verifikasi opsi `Straight Line` tanpa tooltip Disabled
11. Klik breadcrumb `Asset Class`
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-FA-FAAC-743: Ganti Tax Depreciation Class mengosongkan Tax Method di luar irisan class baru dan mempertahankan yang di dalam irisan

14. Klik tombol `+ Asset Class` di toolbar tabel
15. Klik tab `Depreciation`
16. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3`
17. Pilih Tax Method `Declining Balance`
18. Ganti Tax Depreciation Class menjadi `Seed Irisan A`
19. Verifikasi Tax Method dikosongkan karena `Declining Balance` di luar irisan `Seed Irisan A`
20. Buka select Tax Method
21. Arahkan kursor ke opsi `Declining Balance`
22. Verifikasi opsi `Declining Balance` Disabled dengan tooltip `Not allowed from <M+2 dalam format MMM yyyy>.`
23. Pilih Tax Method `Straight Line`
24. Verifikasi Tax Method `Straight Line` terpilih
25. Ganti Tax Depreciation Class menjadi `Bukan bangunan – Kelompok 1`
26. Verifikasi Tax Method `Straight Line` dipertahankan karena termasuk irisan `Bukan bangunan – Kelompok 1`
27. Klik breadcrumb `Asset Class`
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-742 dan 743). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03): langkah 11 sampai 13 dan 27 sampai 29 menutup form dirty (S-08); langkah 20 membuka select Tax Method agar opsi dapat diamati, sesuai kalimat "perhatikan select Tax Method" pada TC.
- Asersi absence langkah 7 didahului langkah 6 pada tooltip yang sama; asersi absence tooltip langkah 10 didahului langkah 9 (bagian 8b butir 2 dan 5).
- Urutan TC-743 mengikuti state layar: pilih class dan metode, ganti class, amati, pilih `Straight Line`, ganti class lagi (butir a, b, c TC).
- Temuan untuk QA: TC-742 tidak menyebut apakah tooltip opsi `Straight Line` memuat teks lain; spec hanya mengasersi bahwa tidak ada tooltip Disabled.
