---
id: TC-FA-COA-E2E-024-edit-account-tutup-form-unsaved-changes-dan-backdrop
title: "Edit Account: Tutup Form, Unsaved Changes, dan Backdrop"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-245
  - TC-FA-COA-246
  - TC-FA-COA-247
  - TC-FA-COA-248
  - TC-FA-COA-249
  - TC-FA-COA-250
coverage:
  web: automated
---

# Edit Account: Tutup Form, Unsaved Changes, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin`, Function Depreciation Expense | Active, Used By 0, belum pernah diekspor; hanya dibaca (tidak ada `[Save]` pada spec ini) | TC-245 sampai TC-250 |

- Nilai uji: Account Name diubah menjadi `Depreciation Expense – Admin Draft`; nilai tersimpan P1 `Depreciation Expense – Admin`.
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-245: Tutup modal dengan `[✕]` tanpa perubahan nilai tidak memunculkan dialog Unsaved Changes

1. Ketik Search `5-6001`, tekan Enter
2. Klik row action `Edit` pada akun P1 (`5-6001`)
3. Klik `[✕]` di header modal
4. Verifikasi modal Edit Account tertutup
5. Verifikasi dialog Unsaved Changes tidak tampil

### TC-FA-COA-246: Tutup modal dengan nilai berbeda dari nilai tersimpan memunculkan dialog Unsaved Changes

6. Klik row action `Edit` pada akun P1 (`5-6001`)
7. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
8. Klik `[✕]` di header modal
9. Verifikasi dialog Unsaved Changes tampil dengan teks "You have unsaved changes. Are you sure you want to leave?"
10. Verifikasi dialog memiliki tombol `[Leave]` dan `[Cancel]`
11. Klik `[Leave]`

### TC-FA-COA-247: `[Cancel]` pada dialog Unsaved Changes mempertahankan modal Edit dan input

12. Klik row action `Edit` pada akun P1 (`5-6001`)
13. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
14. Klik `[✕]` di header modal
15. Klik `[Cancel]` pada dialog Unsaved Changes
16. Verifikasi dialog Unsaved Changes tertutup
17. Verifikasi modal Edit Account tetap terbuka
18. Verifikasi Account Name tetap `Depreciation Expense – Admin Draft`
19. Klik `[✕]` di header modal
20. Verifikasi dialog Unsaved Changes tampil
21. Klik `[Leave]`

### TC-FA-COA-248: `[Leave]` pada dialog Unsaved Changes menutup modal dan membuang perubahan

22. Klik row action `Edit` pada akun P1 (`5-6001`)
23. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
24. Klik `[✕]` di header modal
25. Klik `[Leave]` pada dialog Unsaved Changes
26. Verifikasi dialog dan modal Edit Account tertutup
27. Verifikasi Account Name P1 di tabel tetap `Depreciation Expense – Admin`

### TC-FA-COA-249: Klik backdrop saat nilai berbeda tidak menutup modal dan tidak memunculkan dialog

28. Klik row action `Edit` pada akun P1 (`5-6001`)
29. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
30. Klik area backdrop di luar modal
31. Verifikasi modal Edit Account tetap terbuka dengan nilai yang diubah
32. Verifikasi dialog Unsaved Changes tidak tampil
33. Klik `[✕]` di header modal
34. Verifikasi dialog Unsaved Changes tampil
35. Klik `[Leave]`

### TC-FA-COA-250: Nilai diubah lalu dikembalikan identik dengan nilai tersimpan ditutup tanpa dialog Unsaved Changes

36. Klik row action `Edit` pada akun P1 (`5-6001`)
37. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
38. Ganti isi Account Name dengan `Depreciation Expense – Admin`
39. Klik `[✕]` di header modal
40. Verifikasi modal Edit Account tertutup
41. Verifikasi dialog Unsaved Changes tidak tampil

## Notes

- Spec 41 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik aksi (menutup form Edit) pada akun dan form yang sama (P1); enam kasus berurutan, tiap kasus membuka form dari keadaan bersih, dan pola buka Edit, ubah Account Name, tutup lalu `Verifikasi` berulang per kasus (8b.7) sehingga kegagalan satu kasus tidak membuat kasus lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Search Account Code membuka baris target (langkah 1; berlaku untuk seluruh spec karena Search tidak diubah); `[Leave]` pada langkah 11, 21, dan 35 menutup form dirty deterministik sebelum kasus berikutnya (S-08, S-09). Dialog Unsaved Changes pada langkah 20 dan 34 diasersi sesuai S-08.
- Klik `[Leave]` pada langkah 25 adalah aksi TC-248 sendiri (bukan langkah pemulihan); langkah 15 adalah aksi TC-247.
- Asersi "Dialog Unsaved Changes tidak tampil" (langkah 5, 32, 41) didahului `Verifikasi` modal tertutup atau modal tetap terbuka pada kasus yang sama (8b.2).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-248 ("Data P1 tidak berubah dan tidak ada log") tidak punya langkah observasi log di TC; yang diasersi hanya Expected b (Account Name P1 di tabel tetap).
