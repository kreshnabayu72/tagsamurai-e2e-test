---
id: TC-FA-FAAC-E2E-048-create-tax-depreciation-class-tanpa-metode
title: "Create Asset Class: Tax Depreciation Class Tanpa Metode Membuat Tax Method Read-Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-128
coverage:
  web: automated
---

# Create Asset Class: Tax Depreciation Class Tanpa Metode Membuat Tax Method Read-Only

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Tax Depreciation Class `Tanah` (Active, tanpa metode). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: Asset Class `B-TANAH` (Class Name `Tanah Uji`) dibuat oleh langkah 7. Kode literal dipertahankan karena Class Code dibatasi 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12, nama literal); hook `before` menghapus `B-TANAH` bila sisa run sebelumnya masih ada (R-13) lewat API/fixture BE, dan hook `after` menghapus `B-TANAH` yang dibuat spec ini (cleanup tidak berasumsi setup berhasil penuh).
- Kemampuan teknis: membaca Asset Class `B-TANAH` lewat kemampuan baca BE; menghapus Asset Class lewat API/fixture BE (disediakan tim FE/BE).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah selain Asset Class `B-TANAH` (dihapus oleh hook `after`).
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-128: Tax Depreciation Class tanpa metode membuat Tax Method read-only

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`
3. Pilih Tax Depreciation Class `Tanah`
4. Verifikasi Tax Method read-only dengan nilai `—`
5. Verifikasi Tax Method tidak wajib dan tidak menampilkan caption
6. Isi field lain dengan nilai valid: Class Code `B-TANAH`, Class Name `Tanah Uji`, Method `Straight Line`, Useful Life `60`
7. Klik `Submit`
8. Verifikasi tidak ada caption Tax Method setelah Submit (Submit tidak ditolak karena Tax Method)
9. Verifikasi Asset Class `B-TANAH` tersimpan (dibaca lewat kemampuan baca BE)

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-128). Tidak ada TC hanya-BE di spec ini. TC-FA-FAAC-126 dan 127 (Tax Method mengikuti Tax Depreciation Class tanpa membuat Asset Class) ada di spec 045.
- Spec ini membuat data (Asset Class `B-TANAH`) dan butuh cleanup sehingga berdiri sendiri; spec 045 tidak membuat data (bagian 3, pemisah nyata).
- Langkah penghubung (S-03): langkah 6 mengisi field lain agar Submit valid sesuai langkah TC ("dengan field lain valid"). Langkah 9 membuktikan Submit berhasil lewat kemampuan baca BE dan menjadi anchor positif untuk asersi absence caption pada langkah 8.
- Temuan untuk QA:
  - TC-128 butir b ("Submit tidak ditolak karena Tax Method") tidak menyebut tampilan sesudah Submit sukses (toast atau navigasi); spec mengasersi tidak adanya caption Tax Method dan keberadaan record lewat kemampuan baca BE.
  - TC-128 langkah 3 menyebut "field lain valid" tanpa nilai; spec memakai Class Code `B-TANAH`, Class Name `Tanah Uji`, Method `Straight Line`, Useful Life `60`.
