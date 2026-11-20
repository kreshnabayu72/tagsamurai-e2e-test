---
id: TC-FA-FAAC-E2E-201-create-tax-method-irisan-kosong-semua-opsi-disabled-dan-submit-ditolak
title: "Create Asset Class: Irisan Tax Method Kosong Membuat Semua Opsi Disabled dan Submit Ditolak"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-746
sourceRules: ["FAAC-LOGIC-02m", "F-FAAC-01.k16", "E-FAAC-122", "ST-38", "V-20", "V-36"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02m": 11
  "ST-38": 13
  "F-FAAC-01.k16": [11, 15, 17]
  "E-FAAC-122": 17
  "V-20": 17
anchor: [10, 17]
coverage:
  web: automated
---

# Create Asset Class: Irisan Tax Method Kosong Membuat Semua Opsi Disabled dan Submit Ditolak

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): `Seed Irisan D` (Active; versi Current hanya mengizinkan `Straight Line`; satu versi Scheduled sejak M+2 hanya mengizinkan `Declining Balance` sehingga irisan kosong); `Bukan bangunan – Kelompok 1` (Active, mengizinkan `Straight Line` dan `Declining Balance`, tanpa versi Scheduled). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M.
- Data Dinamis: Class Code `B-EMPTY` dan Class Name `Empty Intersection` adalah input uji yang Submit-nya ditolak validasi (literal maks 15 karakter, tidak pernah tersimpan sehingga tanpa cleanup). Method `Straight Line` dan Useful Life `48`.
- Kemampuan teknis (disediakan tim FE/BE): hover pada opsi select (langkah 12) dan klik opsi Disabled (langkah 14); pembacaan tooltip opsi Disabled; kemampuan baca BE untuk jumlah Asset Class (baseline N0).
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps
1. Catat jumlah Asset Class lewat kemampuan baca BE sebagai baseline N0
2. Klik tombol `+ Asset Class` di toolbar tabel
3. Isi Class Code `B-EMPTY`
4. Isi Class Name `Empty Intersection`
5. Klik tab `Depreciation`
6. Pilih Method `Straight Line`
7. Isi Useful Life `48`
8. Pilih Tax Depreciation Class `Seed Irisan D`
9. Buka select Tax Method
10. Verifikasi opsi `Straight Line` tampil pada select Tax Method
11. Verifikasi seluruh opsi Tax Method yang tampil (`Straight Line`) Disabled
12. Arahkan kursor ke opsi `Straight Line`
13. Verifikasi tooltip opsi: `Not allowed from <M+2 dalam format MMM yyyy>.`
14. Klik opsi `Straight Line`
15. Verifikasi Tax Method tetap kosong (opsi tidak dapat dipilih)
16. Klik `Submit`
17. Verifikasi caption pada field Tax Method: `Tax method must not be empty`
18. Verifikasi jumlah Asset Class sama dengan N0 (Asset Class `B-EMPTY` tidak dibuat)
19. Ganti Tax Depreciation Class menjadi `Bukan bangunan – Kelompok 1`
20. Buka select Tax Method
21. Verifikasi opsi `Straight Line` dan `Declining Balance` Enabled
22. Klik breadcrumb `Asset Class`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-746). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03): langkah 1 (baseline N0, S-12), langkah 3 sampai 8 (mengisi field wajib agar Submit mengevaluasi Tax Method; TC menyebut Class Code, Class Name, Method, dan Useful Life), langkah 20 (membuka select Tax Method untuk diamati), dan langkah penutup form dirty (S-08).
- Langkah 10 menjadi anchor positif bagi asersi universal "seluruh opsi yang tampil Disabled" pada langkah 11; langkah 17 (caption penolakan) menjadi anchor bagi asersi selisih jumlah pada langkah 18 (bagian 8b butir 2).
- Pada irisan kosong hanya `Straight Line` yang tampil karena opsi harus pernah diizinkan versi Current (FAAC-LOGIC-02m); `Declining Balance` hanya ada di versi Scheduled sehingga tidak ditawarkan.
- Temuan untuk QA: TC-746 butir b menyebut Submit ditolak tanpa menyebut caption field wajib lain; spec hanya mengasersi caption Tax Method.
