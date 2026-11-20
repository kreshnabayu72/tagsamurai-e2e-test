---
id: TC-FA-FAAC-E2E-199-create-tax-method-opsi-disabled-tooltip-dan-metode-hanya-scheduled-tidak-ditawarkan
title: "Create Asset Class: Opsi Tax Method di Luar Irisan Disabled dengan Tooltip dan Metode yang Hanya Ada di Versi Scheduled Tidak Ditawarkan"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-740
  - TC-FA-FAAC-741
sourceRules: ["FAAC-LOGIC-02f", "FAAC-LOGIC-02l", "FAAC-LOGIC-02m", "ST-38", "F-FAAC-01.k15", "E-FAAC-121", "N-22"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02f": [5, 20]
  "FAAC-LOGIC-02l": [6, 8]
  "FAAC-LOGIC-02m": [6, 22]
  "ST-38": 8
  "F-FAAC-01.k15": [6, 22]
  "E-FAAC-121": [6, 22]
  "N-22": 8
anchor: [20]
coverage:
  web: automated
---

# Create Asset Class: Opsi Tax Method di Luar Irisan Disabled dengan Tooltip dan Metode yang Hanya Ada di Versi Scheduled Tidak Ditawarkan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca; seed Tax Depreciation Class Active, belum dipakai Asset Class): `Seed Irisan A` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; satu versi Scheduled sejak M+2 hanya mengizinkan `Straight Line`); `Seed Irisan C` (Active; versi Current hanya mengizinkan `Straight Line`; satu versi Scheduled sejak M+2 mengizinkan `Straight Line` dan `Declining Balance`). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M.
- Data Dinamis: tidak ada. Spec tidak melakukan Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis (disediakan tim FE/BE): hover pada opsi select (langkah 7); klik opsi Disabled (langkah 9); pembacaan tooltip opsi Disabled; seed Tax Depreciation Class beserta versi Scheduled lewat fixture BE.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir tiap blok TC.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-740: Opsi Tax Method di luar irisan Disabled dengan tooltip saat versi Scheduled tidak mengizinkannya

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`
3. Pilih Tax Depreciation Class `Seed Irisan A`
4. Buka select Tax Method
5. Verifikasi opsi `Straight Line` Enabled
6. Verifikasi opsi `Declining Balance` Disabled
7. Arahkan kursor ke opsi `Declining Balance`
8. Verifikasi tooltip opsi `Declining Balance`: `Not allowed from <M+2 dalam format MMM yyyy>.`
9. Klik opsi `Declining Balance`
10. Verifikasi Tax Method tetap kosong (opsi `Declining Balance` tidak terpilih)
11. Klik opsi `Straight Line`
12. Verifikasi Tax Method `Straight Line` terpilih
13. Klik breadcrumb `Asset Class`
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`

### TC-FA-FAAC-741: Metode yang hanya ada di versi Scheduled Tax Depreciation Class tidak ditawarkan pada Tax Method

16. Klik tombol `+ Asset Class` di toolbar tabel
17. Klik tab `Depreciation`
18. Pilih Tax Depreciation Class `Seed Irisan C`
19. Buka select Tax Method
20. Verifikasi opsi `Straight Line` tampil pada select Tax Method
21. Verifikasi opsi `Straight Line` Enabled
22. Verifikasi opsi `Declining Balance` tidak muncul sama sekali pada select Tax Method (bukan Disabled)
23. Klik breadcrumb `Asset Class`
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-740 dan 741). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03): langkah 13 sampai 15 dan 23 sampai 25 menutup form dirty (S-08).
- Asersi absence langkah 22 didahului langkah 20 dan 21 sebagai anchor positif pada select yang sama (bagian 8b butir 2).
- Pemisahan opsi: `Declining Balance` pada `Seed Irisan A` tampil Disabled karena pernah diizinkan versi Current lalu dibuang versi Scheduled; pada `Seed Irisan C` opsi itu tidak ditawarkan karena baru ada di versi Scheduled (FAAC-LOGIC-02m).
- Temuan untuk QA: TC-740 butir c tidak menyebut apakah select tetap terbuka sesudah klik opsi Disabled; spec hanya mengasersi Tax Method tetap kosong.
