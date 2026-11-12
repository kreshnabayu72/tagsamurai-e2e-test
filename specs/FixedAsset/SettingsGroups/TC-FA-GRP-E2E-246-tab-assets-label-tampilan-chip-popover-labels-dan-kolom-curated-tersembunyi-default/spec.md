---
id: TC-FA-GRP-E2E-246-tab-assets-label-tampilan-chip-popover-labels-dan-kolom-curated-tersembunyi-default
title: "Tab Assets Label: Tampilan Chip 1-2 Badge + +N more, Popover Labels, dan Kolom Curated Tersembunyi Secara Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1182
  - TC-FA-GRP-1183
  - TC-FA-GRP-1185
coverage:
  web: automated
---

# Tab Assets Label: Tampilan Chip 1-2 Badge + +N more, Popover Labels, dan Kolom Curated Tersembunyi Secara Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Multi Label Node (Pre-setup tambahan, Tabel Dinamis No 9, level 1) berisi hanya aset L1 (Finance, Fragile, Priority), L2 (Fragile, Priority), L3 (Priority), L4 (tanpa label), L5 (Finance); status aset bervariasi. Warehouse A (Tabel A, Assignable) berisi 24 aset aktif variasi Brand, Model/Type, Category, Label, dan status. Katalog Labels memuat warna hex Finance, Fragile, Priority; dibaca lewat kemampuan baca data yang disediakan tim FE/BE. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1185: Kolom curated tersembunyi secara default

1. Ketik Search `Warehouse A` pada Groups List, tekan Enter
2. Buka Detail Warehouse A (Tab Assets)
3. Amati header kolom tabel
4. Verifikasi hanya kolom Name, Asset ID, TAG, Brand, Model/Type, Status, dan Last Updated yang tampil di tabel pada kondisi default
5. Buka Popup Setup Column
6. Amati status seluruh kolom curated
7. Verifikasi kolom Measurement, Category, Label, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), Warranty Expiry, dan Custom Field berstatus curated: unchecked dan enabled
8. Klik ✕ pada Popup Setup Column
9. Tutup Popup Detail Group

### TC-FA-GRP-1182: Kolom Label tampil sebagai chip berwarna, 1–2 badge lalu +N more, urut A–Z, dan —

10. Ganti isi kotak Search Groups List dengan `Multi Label Node`, tekan Enter
11. Buka Detail Multi Label Node (Tab Assets)
12. Buka Popup Setup Column
13. Centang Label
14. Klik [Save]
15. Amati kolom Label pada aset L1 sampai L5
16. Verifikasi L1 menampilkan 2 chip `Finance` dan `Fragile` lalu chip `+1 more` (urut A–Z; `Priority` tersembunyi)
17. Verifikasi L2 menampilkan 2 chip `Fragile` dan `Priority` tanpa `+N more`, serta L3 dan L5 masing-masing 1 chip
18. Verifikasi warna tiap chip mengikuti warna hex label di katalog Labels
19. Verifikasi L4 (tanpa label) menampilkan `—` (bukan blank)

### TC-FA-GRP-1183: Klik chip +N more membuka popover Labels

20. Klik chip `+1 more` pada aset L1
21. Amati isi popover
22. Verifikasi popover berjudul "Labels" terbuka
23. Verifikasi popover memuat seluruh label aset L1 (`Finance`, `Fragile`, `Priority`) sebagai badge penuh berwarna label urut A–Z
24. Verifikasi badge di popover tampil tanpa truncation
25. Klik di luar popover
26. Verifikasi popover tertutup

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): TC-1185 diletakkan pertama karena memeriksa kolom default sebelum kolom Label dicentang; menutup Popup Setup Column dan Popup Detail Group; Setup Column centang Label sebelum TC-1182 (precondition d "kolom curated Label sudah ditampilkan"), yang juga menjadi dasar TC-1183.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Warehouse A`, `Multi Label Node`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA (S-15): (1) TC-1182 dan TC-1183 mensyaratkan kolom Label sudah ditampilkan tetapi langkah TC tidak memuat pencentangan; spec menambahkannya. (2) Katalog Labels dan warna hex tiap label tidak ada di Tabel Data Uji; warna dibaca lewat kemampuan baca data (disediakan tim FE/BE). (3) Expected TC-1185 butir b menyebut "Custom Field" sebagai satu kolom curated padahal Custom Field berupa banyak kolom (Tabel Dinamis No 13); spec mengikuti teks TC.
