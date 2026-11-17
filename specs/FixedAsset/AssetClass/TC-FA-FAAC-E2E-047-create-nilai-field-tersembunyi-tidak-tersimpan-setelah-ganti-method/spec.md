---
id: TC-FA-FAAC-E2E-047-create-nilai-field-tersembunyi-tidak-tersimpan-setelah-ganti-method
title: "Create Asset Class: Nilai Field yang Disembunyikan Karena Ganti Method Tidak Ikut Tersimpan"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-125
sourceRules: ["§[F-FAAC-01] Create Asset Class#b3", "§[F-FAAC-01] Create Asset Class#r12", "F-FAAC-02.k20", "FI-01"]
smoke: []
dependsOn: []
trace:
  "§[F-FAAC-01] Create Asset Class#b3": 6
  "§[F-FAAC-01] Create Asset Class#r12": 7
  "F-FAAC-02.k20": 11
  "FI-01": 11
coverage:
  web: automated
---

# Create Asset Class: Nilai Field yang Disembunyikan Karena Ganti Method Tidak Ikut Tersimpan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Tax Depreciation Class `Bukan bangunan – Kelompok 3` (Active, mengizinkan Tax Method `Declining Balance`). Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: Asset Class `B-HID` (Class Name `Hidden Value`) dibuat oleh langkah 5. Kode literal dari TC dipertahankan karena Class Code dibatasi 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12, nama literal); hook `before` menghapus `B-HID` bila sudah ada sisa run sebelumnya (R-13) lewat API/fixture BE, dan hook `after` menghapus `B-HID` yang dibuat spec ini (cleanup tidak berasumsi setup berhasil penuh).
- Kemampuan teknis: membaca Asset Class `B-HID` lewat kemampuan baca BE; menghapus Asset Class lewat API/fixture BE (disediakan tim FE/BE).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah selain Asset Class `B-HID` (dihapus oleh hook `after`).
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-125: Nilai field yang disembunyikan karena ganti Method tidak ikut tersimpan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Isi Class Code `B-HID` dan Class Name `Hidden Value`
3. Pilih Method `Declining Balance`, isi Useful Life `48` dan Declining Rate `40`; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3` dan Tax Method `Declining Balance`
4. Ganti Method menjadi `Straight Line`
5. Klik `Submit`
6. Verifikasi Asset Class `B-HID` tersimpan (dibaca lewat kemampuan baca BE)
7. Verifikasi tidak ada caption Declining Rate setelah Submit
8. Buka mode Edit Asset Class `B-HID`
9. Klik tab `Depreciation`
10. Ganti Method kembali ke `Declining Balance`
11. Verifikasi field Declining Rate kosong (nilai `40` tidak tersimpan)
12. Kembalikan Method ke nilai tersimpan `Straight Line`
13. Klik breadcrumb `Asset Class`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-125). Tidak ada TC hanya-BE di spec ini. TC-FA-FAAC-121 sampai 124 dan 645 (field dinamis tanpa membuat Asset Class) ada di spec 044.
- Spec ini membuat data (Asset Class `B-HID`) dan butuh cleanup sehingga berdiri sendiri; spec field dinamis Method (044) tidak membuat data (bagian 3, pemisah nyata).
- Langkah penghubung (S-03): langkah 12 (memulihkan Method ke nilai tersimpan agar form Edit tidak dirty, S-09) dan langkah 13 (menutup form Edit; setelah pemulihan form tidak berbeda dari record tersimpan sehingga dialog `Unsaved Changes` tidak diasersi). Langkah 6 membuktikan Submit berhasil lewat kemampuan baca BE dan menjadi anchor positif asersi absence langkah 7 serta anchor langkah 11.
- Temuan untuk QA:
  - TC-125 butir a ("Submit berhasil tanpa caption Declining Rate") tidak menyebut tampilan sesudah Submit sukses (toast atau navigasi); spec mengasersi tidak adanya caption dan keberadaan record lewat kemampuan baca BE.
  - TC-125 langkah 5 ("Pada mode Edit buka tab Depreciation") tidak menyebut cara masuk ke mode Edit (otomatis sesudah Submit atau lewat tabel); langkah 8 menulis "Buka mode Edit" tanpa cara spesifik.
