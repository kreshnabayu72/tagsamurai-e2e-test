---
id: TC-FA-COA-E2E-025-edit-account-refresh-sidebar-dan-esc-pada-form-dirty
title: "Edit Account: Refresh, Sidebar, dan Esc pada Form Dirty"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-251
  - TC-FA-COA-252
  - TC-FA-COA-357
coverage:
  web: automated
---

# Edit Account: Refresh, Sidebar, dan Esc pada Form Dirty

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin`, Function Depreciation Expense | Active, Used By 0, belum pernah diekspor; hanya dibaca (tidak ada `[Save]` pada spec ini) | TC-251, TC-357, TC-252 |

- Nilai uji: Account Name diubah menjadi `Depreciation Expense – Admin Draft` (TC-251, TC-252) dan `Depreciation Expense – Admin Esc` (TC-357); nilai tersimpan P1 `Depreciation Expense – Admin`.
- Kemampuan teknis: menangkap dan menolak (tetap di halaman) konfirmasi bawaan browser `beforeunload` pada TC-251, disediakan tim FE; hook `beforeEach` suite yang mengonfirmasi `beforeunload` tidak mengganggu langkah ini karena konfirmasi ditangkap spec lebih dulu.
- Menu sidebar tujuan pada TC-252: salah satu menu sidebar di luar halaman Chart of Accounts yang dipilih tim FE (TC tidak menyebut menu tertentu; lihat Temuan untuk QA).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-251: Refresh halaman saat nilai berbeda dari nilai tersimpan memunculkan konfirmasi bawaan browser

1. Ketik Search `5-6001`, tekan Enter
2. Klik row action `Edit` pada akun P1 (`5-6001`)
3. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
4. Muat ulang halaman (F5)
5. Verifikasi konfirmasi bawaan browser (beforeunload) tampil
6. Tolak konfirmasi sehingga tetap di halaman
7. Klik `[✕]` di header modal
8. Verifikasi dialog Unsaved Changes tampil
9. Klik `[Leave]`

### TC-FA-COA-357: Tekan `Esc` pada form yang sudah diubah memunculkan dialog Unsaved Changes; `Esc` pada dialog itu setara `[Cancel]`

10. Klik row action `Edit` pada akun P1 (`5-6001`)
11. Ganti isi Account Name dengan `Depreciation Expense – Admin Esc`
12. Tekan `Esc`
13. Verifikasi dialog Unsaved Changes tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
14. Verifikasi modal Edit Account tetap terbuka
15. Tekan `Esc` lagi saat dialog Unsaved Changes tampil
16. Verifikasi dialog tertutup (setara `[Cancel]`)
17. Verifikasi modal Edit Account tetap terbuka
18. Verifikasi Account Name tetap `Depreciation Expense – Admin Esc`
19. Klik `[✕]` di header modal
20. Verifikasi dialog Unsaved Changes tampil
21. Klik `[Leave]`

### TC-FA-COA-252: Klik menu sidebar saat nilai berbeda dari nilai tersimpan memunculkan dialog Unsaved Changes, `[Cancel]` tetap di form dan `[Leave]` berpindah halaman

22. Klik row action `Edit` pada akun P1 (`5-6001`)
23. Ganti isi Account Name dengan `Depreciation Expense – Admin Draft`
24. Klik salah satu menu sidebar di luar halaman ini
25. Verifikasi dialog Unsaved Changes tampil dengan teks "You have unsaved changes. Are you sure you want to leave?"
26. Klik `[Cancel]` pada dialog Unsaved Changes
27. Verifikasi user tetap di halaman Chart of Accounts dengan modal Edit Account terbuka
28. Verifikasi Account Name tetap `Depreciation Expense – Admin Draft`
29. Klik menu sidebar yang sama lagi
30. Klik `[Leave]` pada dialog Unsaved Changes
31. Verifikasi user berpindah ke halaman tujuan menu sidebar
32. Buka kembali Fixed Asset > Settings > Accounting > Chart of Accounts
33. Ketik Search `5-6001`, tekan Enter
34. Verifikasi Account Name P1 di tabel tetap `Depreciation Expense – Admin` sehingga perubahan dibuang

## Notes

- Urutan TC: TC-251, TC-357, lalu TC-252, karena TC-252 meninggalkan halaman Chart of Accounts dan harus berada di akhir; langkah 32 sampai 34 kembali ke modul asal dan membuktikan perubahan dibuang (S-14, S-10).
- Langkah penghubung (S-03, R-16): Search Account Code membuka baris target (langkah 1, 33); langkah 6 menolak konfirmasi bawaan browser sehingga form tetap dirty, lalu form ditutup deterministik lewat langkah 7 sampai 9 (S-08); `[Leave]` pada langkah 21 menutup form dirty TC-357; langkah 32 membuka kembali halaman asal.
- Dialog Unsaved Changes pada langkah 8 dan 20 diasersi sesuai S-08. Search pada langkah 1 berlaku sampai langkah 24 (sidebar mereset Search, sehingga langkah 33).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05); Post Condition TC-357 ("tidak ada perubahan tersimpan dan tidak ada log") dan TC-252 ("Data P1 tidak berubah") hanya diasersi sejauh Expected (langkah 18, 34).
- Temuan untuk QA:
  - TC-252 langkah 3 menyebut "salah satu menu sidebar di luar halaman ini" tanpa menyebut menu tujuan; halaman tujuan pada Expected c juga tidak dinamai. Menu tujuan perlu ditetapkan tim FE.
  - TC-357 Post Condition "tidak ada log" tidak punya langkah observasi di TC sehingga tidak diasersi.
