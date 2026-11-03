---
id: TC-FA-COA-E2E-018-add-account-tutup-form-unsaved-changes-dan-nilai-dikembalikan
title: "Add Account: Tutup Form, Unsaved Changes, dan Nilai Dikembalikan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-236
  - TC-FA-COA-237
  - TC-FA-COA-238
  - TC-FA-COA-239
  - TC-FA-COA-241
coverage:
  web: automated
---

# Add Account: Tutup Form, Unsaved Changes, dan Nilai Dikembalikan

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data: tidak ada data Pre-setup yang dibaca selain tabel akun; nilai `5-6700` hanya diketik dan tidak pernah di-submit, sehingga tidak memakai suffix `{runId}`. Tidak ada akun yang seharusnya tersimpan.
- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `5-6700` bila ada; kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-236: Tutup form belum diisi dengan `[✕]`

1. Klik `+ Account` di toolbar
2. Klik `[✕]` di header modal
3. Verifikasi modal Add Account tertutup
4. Verifikasi dialog Unsaved Changes tidak tampil

### TC-FA-COA-237: Tutup form yang sudah diisi dengan `[✕]`

5. Klik `+ Account` di toolbar
6. Ketik `5-6700` di Account Code
7. Klik `[✕]` di header modal
8. Verifikasi dialog Unsaved Changes tampil dengan teks "You have unsaved changes. Are you sure you want to leave?"
9. Verifikasi dialog memiliki tombol `[Leave]` dan `[Cancel]`
10. Verifikasi modal Add Account tetap terbuka di belakang dialog
11. Verifikasi Account Code di modal tetap `5-6700`

### TC-FA-COA-238: `[Cancel]` pada dialog Unsaved Changes

12. Klik `[Cancel]` pada dialog Unsaved Changes
13. Verifikasi dialog Unsaved Changes tertutup
14. Verifikasi modal Add Account tetap terbuka
15. Verifikasi Account Code tetap `5-6700`

### TC-FA-COA-239: `[Leave]` pada dialog Unsaved Changes

16. Klik `[✕]` di header modal
17. Klik `[Leave]` pada dialog Unsaved Changes
18. Verifikasi dialog dan modal Add Account tertutup
19. Ketik Search `5-6700`, tekan Enter
20. Verifikasi tidak ada akun `5-6700` di tabel: tabel menampilkan "No results found"
21. Klik `(←)` pada kotak Search
22. Klik `+ Account` di toolbar
23. Verifikasi modal Add Account yang dibuka kembali kosong

### TC-FA-COA-241: Nilai diubah lalu dikembalikan

24. Ketik `5-6700` di Account Code
25. Hapus seluruh teks Account Code sehingga kembali kosong
26. Klik `[✕]` di header modal
27. Verifikasi modal Add Account tertutup
28. Verifikasi dialog Unsaved Changes tidak tampil

## Notes

- Spec ini 28 langkah. TC-238 dan TC-239 bergantung pada TC-237 (kolom Dependensi): langkah Klik `+ Account`, ketik `5-6700`, dan klik `[✕]` milik TC-238 dipenuhi oleh langkah 5 sampai 7, dan form dirty yang sama dipakai TC-238 (langkah 12) lalu TC-239 (langkah 16, `[✕]` ulang pada form yang sama). Langkah TC-239 "Klik `+ Account` lagi" adalah langkah 22. Langkah TC-241 "Klik `+ Account`" dipenuhi modal kosong yang dibuka pada langkah 22.
- Langkah penghubung (S-03): langkah 21 (kosongkan Search, S-09). Form dirty TC-237 sampai TC-239 ditutup deterministik lewat `[✕]` dan `[Leave]` (S-08); TC-241 berakhir dengan form tertutup tanpa dialog sehingga tidak ada pemulihan tambahan.
- Pembacaan "tidak ada akun `5-6700` di tabel" (TC-239 b) memakai Search; empty state "No results found" menjadi anchor absence yang sah (8b butir 2). Absence dialog pada langkah 4 dan 28 didahului `Verifikasi` modal tertutup pada langkah 3 dan 27 sebagai anchor.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-239 ("tidak ada akun dibuat dan tidak ada log") tidak punya langkah observasi log di TC; hanya ketiadaan akun di tabel yang diasersi lewat Expected (b).
  - Account Code `5-6700` literal tanpa suffix `{runId}` karena batas 15 karakter; nilai itu tidak pernah di-submit.
