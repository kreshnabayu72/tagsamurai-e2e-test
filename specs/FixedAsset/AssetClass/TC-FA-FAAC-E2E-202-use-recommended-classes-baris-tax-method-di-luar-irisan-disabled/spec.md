---
id: TC-FA-FAAC-E2E-202-use-recommended-classes-baris-tax-method-di-luar-irisan-disabled
title: "Use Recommended Classes: Baris dengan Tax Method di Luar Irisan Disabled dengan Tooltip"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-744
sourceRules: ["FAAC-LOGIC-16c", "FAAC-LOGIC-02l", "ST-12", "F-FAAC-07.k7", "E-FAAC-125"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-16c": [4, 7]
  "FAAC-LOGIC-02l": [4, 5]
  "ST-12": 5
  "F-FAAC-07.k7": [4, 5, 8]
  "E-FAAC-125": 5
anchor: [2]
coverage:
  web: automated
---

# Use Recommended Classes: Baris dengan Tax Method di Luar Irisan Disabled dengan Tooltip

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data (state client): client belum memiliki Asset Class (tabel kosong, EmptyState tampil) dan Tax Depreciation Class rekomendasi Active. Versi Scheduled `Bukan bangunan – Kelompok 3` sejak M+2 yang hanya mengizinkan `Straight Line` disetel fixture BE sebagai keadaan awal (TC-744 dan TC-747) di hook `before` dan dibatalkan di hook `after`; `Bukan bangunan – Kelompok 3` Active mengizinkan `Straight Line` dan `Declining Balance` pada versi Current. Seed disediakan tim FE/BE. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M.
- Data Dinamis: tidak ada. Spec tidak membuat Asset Class (tidak ada klik `Create`) sehingga tidak ada cleanup Asset Class.
- Kemampuan teknis (disediakan tim FE/BE): hover pada checkbox baris (langkah 3); klik checkbox Disabled (langkah 6); pembacaan tooltip checkbox Disabled; fixture BE untuk menyetel dan membatalkan versi Scheduled Tax Depreciation Class.
- State global: versi Scheduled `Bukan bangunan – Kelompok 3` disetel di hook `before` dan dibatalkan di hook `after`; dialog `Use Recommended Classes` ditutup lewat `Cancel` pada akhir spec.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-744: Baris Recommended Classes dengan Tax Method di luar irisan Disabled dengan tooltip

1. Klik link `Use recommended classes` pada EmptyState tabel
2. Verifikasi baris `HEAVY-EQ` tampil dengan Tax Depreciation Class `Bukan bangunan – Kelompok 3` dan Tax Method `Declining Balance`
3. Arahkan kursor ke checkbox baris `HEAVY-EQ`
4. Verifikasi checkbox baris `HEAVY-EQ` Disabled
5. Verifikasi tooltip: `Tax method Declining Balance is not available for tax depreciation class Bukan bangunan – Kelompok 3.`
6. Klik checkbox baris `HEAVY-EQ`
7. Verifikasi checkbox baris `HEAVY-EQ` tidak tercentang (tidak dapat dicentang)
8. Verifikasi checkbox baris `BLDG` Enabled
9. Klik checkbox baris `BLDG`
10. Verifikasi checkbox baris `BLDG` tercentang
11. Klik checkbox baris `BLDG` untuk membatalkan centang
12. Klik `Cancel`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-744). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03): langkah 11 (membatalkan centang agar dialog tidak berisi perubahan) dan langkah 12 (menutup dialog); hook `beforeEach` suite menutup dialog `Unsaved Changes` bila tampil sebagai jaring pengaman.
- Langkah 2 menjadi anchor positif bagi asersi pada baris `HEAVY-EQ`; langkah 7 diasersi sebelum aksi yang mengubah state berikutnya (bagian 8b butir 5).
- Temuan untuk QA: TC-744 tidak menyebut cara menutup dialog sesudah uji; spec memakai `Cancel`.
