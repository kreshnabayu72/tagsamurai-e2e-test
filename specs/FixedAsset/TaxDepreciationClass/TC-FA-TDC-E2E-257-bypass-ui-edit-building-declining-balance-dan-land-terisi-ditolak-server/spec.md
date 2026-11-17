---
id: TC-FA-TDC-E2E-257-bypass-ui-edit-building-declining-balance-dan-land-terisi-ditolak-server
title: "Bypass UI Edit: Building dengan Declining Balance dan Land Terisi Ditolak Server"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-244
  - TC-FA-TDC-245
sourceRules: ["V-14", "R-02", "FATDC-LOGIC-04p.5", "§4.1.1#r8", "V-18", "§4.1.1#r5", "FATDC-LOGIC-03b"]
smoke: []
dependsOn: []
trace:
  "V-14": 5
  "R-02": [6, 14]
  "FATDC-LOGIC-04p.5": [8, 16]
  "§4.1.1#r8": 8
  "V-18": 13
  "§4.1.1#r5": 16
  "FATDC-LOGIC-03b": 16
coverage:
  web: automated
---

# Bypass UI Edit: Building dengan Declining Balance dan Land Terisi Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan intercept: `Spectra.intercept()` di atas backend nyata untuk mengganti payload request Save yang dikirim Drawer Edit; intercept dilepas segera setelah pemicu selesai (S-09). Seed dan pemulihan lewat API mengikuti `suite.md`.
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `bgnE1` | `BGN-E1` | Asset Type Building, Useful Life 20, Allowed Methods Straight Line, Active, Used By 0 |
| `lhnE1` | `LHN-E1` | Asset Type Land, Active, Used By 0 |

- Tabel berisi tujuh class seed bawaan ditambah `BGN-E1` dan `LHN-E1` (9 baris dalam satu halaman Pagination dengan 10 baris per halaman), sehingga baris target tampil tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-244: Edit Building dengan Declining Balance yang lolos dari UI ditolak server

1. Klik link Class Code `BGN-E1` pada tabel
2. Aktifkan intercept request Save: ganti payload Allowed Methods menjadi `Straight Line, Declining Balance`
3. Klik `[Save]`
4. Lepas intercept request Save
5. Verifikasi caption error "Declining balance does not apply to buildings." tampil di bawah field Allowed Methods
6. Verifikasi Drawer Edit tetap terbuka
7. Klik `[×]` pada header Drawer Edit
8. Verifikasi baris `BGN-E1` menampilkan Allowed Methods "Straight Line" dan Effective From "—"

### TC-FA-TDC-245: Edit Land dengan Useful Life atau Allowed Methods terisi yang lolos dari UI ditolak server

9. Klik link Class Code `LHN-E1` pada tabel
10. Aktifkan intercept request Save: ganti payload Useful Life menjadi `10` dan Allowed Methods menjadi `Straight Line`
11. Klik `[Save]`
12. Lepas intercept request Save
13. Verifikasi caption error "Land is not depreciated." tampil di bawah field terkait (Useful Life atau Allowed Methods yang terisi)
14. Verifikasi Drawer Edit tetap terbuka
15. Klik `[×]` pada header Drawer Edit
16. Verifikasi baris `LHN-E1` menampilkan Useful Life (years) "—", Allowed Methods "—", dan Effective From "—"

## Notes

- K-1: TC kelas a dengan payload yang dimanipulasi tetap masuk spec FE+BE; Expected berupa caption error di Drawer dan state data, sehingga asersi memakai UI.
- Langkah penghubung (S-03): langkah 7 dan 15 (menutup Drawer Edit yang field-nya tidak diubah, sehingga tanpa dialog `Unsaved Changes`; payload diganti di jaringan, bukan di field).
- Langkah 8 dan 16 menjadi bukti "tidak ada versi baru dan tidak ada yang tersimpan" lewat kolom Allowed Methods, Useful Life, dan Effective From (versi pertama tanpa Effective From bernilai "—"); klausa log pada Expected b TC-FA-TDC-244 dan TC-FA-TDC-245 ("tidak ada entri log") tidak diasersi di spec ini; asersinya ada di spec absence 274 dengan aksi nyata dan baseline sendiri per TC (S-05).
- Temuan untuk QA:
  - TC-FA-TDC-244 dan TC-FA-TDC-245 langkah 2 menulis "Kirim ulang request Save" tanpa mekanisme dan tanpa perubahan field yang mengaktifkan `[Save]`; Expected-nya berupa caption di Drawer sehingga spec memakai intercept atas request yang dikirim `[Save]`. Bila `[Save]` nonaktif pada Drawer yang belum diubah, QA perlu menjelaskan cara memicu request.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
