---
id: TC-FA-FAAC-E2E-085-edit-kasus-tepi-kapitalisasi-class-code-dan-tax-depreciation-class
title: "Edit Asset Class: Kapitalisasi Class Code dan Tax Depreciation Class yang Tidak Lagi Valid"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-173
  - TC-FA-FAAC-179
sourceRules: ["S-14", "T-02", "V-35", "V-36", "§4.1.2#r14", "FAAC-LOGIC-02e", "F-FAAC-02.k18", "V-04", "L-02"]
smoke: []
dependsOn: []
trace:
  "S-14": 3
  "T-02": [7, 19]
  "V-35": 8
  "V-36": 8
  "§4.1.2#r14": 12
  "FAAC-LOGIC-02e": 13
  "F-FAAC-02.k18": [19, 20]
  "V-04": 21
  "L-02": [23, 24]
anchor: [7, 12]
coverage:
  web: automated
---

# Edit Asset Class: Kapitalisasi Class Code dan Tax Depreciation Class yang Tidak Lagi Valid

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke nilai awal oleh fixture BE di hook `before` dan `after`): Asset Class `B-OLDTAX` (memakai Tax Depreciation Class "Bukan bangunan – Kelompok 4" yang kemudian Inactive); Asset Class `B-CASE` (Active, belum pernah diposting); Tax Depreciation Class "Bukan bangunan – Kelompok 2" Active. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Data uji: Class Name "Old Tax Renamed"; Class Code "b-case" (hanya kapitalisasi dari "B-CASE").
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk jumlah entri Changelog (audit trail permanen, S-12).
- State global: Class Code `B-CASE` berubah menjadi "b-case"; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-179: Edit Asset Class yang memakai Tax Depreciation Class Inactive tanpa mengubah class tersimpan

1. Klik link Class Code "B-OLDTAX" di tabel
2. Klik tab "Depreciation"
3. Verifikasi Select Tax Depreciation Class menampilkan nilai tersimpan "Bukan bangunan – Kelompok 4" walau Inactive
4. Klik tab "General"
5. Ubah Class Name menjadi "Old Tax Renamed" tanpa mengubah Tax Depreciation Class dan Tax Method
6. Klik "Save"
7. Verifikasi muncul toast sukses: "Success, asset class has been updated."
8. Verifikasi tidak ada caption V-35 ("This tax depreciation class no longer exists. Please select another.") maupun V-36 ("Selected tax method is not allowed for this tax depreciation class")
9. Klik link Class Code "B-OLDTAX" di tabel
10. Klik tab "Depreciation"
11. Buka Select Tax Depreciation Class dan lihat opsi
12. Verifikasi daftar opsi menawarkan class Active (mis. "Bukan bangunan – Kelompok 2")
13. Verifikasi "Bukan bangunan – Kelompok 4" tidak muncul pada daftar opsi
14. Tutup daftar opsi lalu klik breadcrumb "Asset Class"

### TC-FA-FAAC-173: Ubah Class Code hanya pada huruf besar-kecil dianggap perubahan nyata

15. Baca jumlah entri Changelog sebagai baseline
16. Klik link Class Code "B-CASE" di tabel
17. Ubah Class Code "B-CASE" menjadi "b-case" (hanya kapitalisasi)
18. Klik "Save"
19. Verifikasi Save tidak dianggap No-Op: muncul toast sukses: "Success, asset class has been updated."
20. Verifikasi Class Code di tabel menjadi "b-case"
21. Verifikasi tidak ada caption "Class code already exists" karena record sendiri dikecualikan dari keunikan
22. Buka Changelog
23. Verifikasi selisih jumlah entri Changelog terhadap baseline langkah 15 adalah 1
24. Verifikasi entri teratas memuat baris Action "Edit" Field "Class Code" Old Value "B-CASE" New Value "b-case"

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 179, lalu 173 (mengubah Class Code dan membaca Changelog).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-OLDTAX` dan `B-CASE` adalah seed bertanda `B-*` per TC, dipakai apa adanya; pemulihan oleh fixture BE.
- Langkah penghubung (S-03): langkah 4 (klik tab General, "Pastikan Tab aktif" sebagai aksi), 9 sampai 11 (membuka ulang Detail karena Save mengembalikan ke tabel), 14, 15 (baseline), dan 22.
- Langkah 12 menjadi anchor positif bagi asersi absence langkah 13 (bagian 8b butir 2).
- Teks caption V-35 dan V-36 pada langkah 8 diambil dari PRD §6 karena TC hanya menyebut kodenya.
- Temuan untuk QA: TC-179 menyebut caption hanya dengan kode V-35 dan V-36 tanpa teks; TC-173 tidak menyebut urutan baris Changelog bila beberapa entri jatuh pada menit yang sama (S-14: himpunan baris teratas sebanyak selisih).
