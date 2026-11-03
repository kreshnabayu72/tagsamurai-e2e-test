---
id: TC-AC-DC-E2E-085-sinkron-device-name-rename-dan-hapus
title: "Sinkron Category dengan Device Name dan Device SKU: Rename, Node Baru, dan Node Dihapus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-231
  - TC-AC-DC-232
  - TC-AC-DC-233
coverage:
  web: automated
---

# Sinkron Category dengan Device Name dan Device SKU: Rename, Node Baru, dan Node Dihapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah. Device Name Pre-setup #15 dan Device SKU Pre-setup #16 tidak diubah.
- Data Dinamis (suffix `{runId}-085`), dibuat lewat sesi API aktor di hook `before` di bawah `Handheld Reader`:
  - `Dipakai Rename {runId}-085` (leaf), Device Name `HR-Rename {runId}-085` dengan Category `Dipakai Rename {runId}-085`, dan Device SKU `SKU-Rename {runId}-085` pada Device Name itu (dipakai sebagai precondition TC-AC-DC-231, tidak diasersi). Node direname menjadi `Rename Baru {runId}-085` pada langkah 4.
  - `Hapus Sinkron {runId}-085` (leaf, target Delete TC-AC-DC-233).
  - Node yang dibuat spec lewat UI: `Opsi Uji {runId}-085` (langkah 27).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh; urutan: Device SKU, Device Name, lalu node): hapus lewat API `SKU-Rename {runId}-085`, `HR-Rename {runId}-085`, `Rename Baru {runId}-085`, `Opsi Uji {runId}-085`, dan `Hapus Sinkron {runId}-085` bila masih ada.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category sebelum aksi (N231, langkah 1) karena Changelog adalah audit trail permanen (S-12). Field wajib popup Create Device Name selain Category tidak disebut TC dan disediakan tim FE.
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-231: Rename Category tercermin di Device Name, Device SKU, dan dropdown Category

1. Baca dan catat jumlah entri Changelog Category sebagai N231 (kemampuan baca)
2. Expand `Hardware`, lalu expand `Handheld Reader`
3. Hover node `Dipakai Rename {runId}-085`, lalu klik aksi Edit
4. Ubah nama menjadi "Rename Baru {runId}-085", lalu klik `[Save]`
5. Tunggu aksi selesai
6. Ketik Search tabel Device Name `HR-Rename {runId}-085`, tekan Enter
7. Verifikasi kolom Category pada baris `HR-Rename {runId}-085` menampilkan "Rename Baru {runId}-085"
8. Klik `(←)` pada kotak Search tabel Device Name
9. Klik `+ Device Name` pada toolbar, buka dropdown Category, lalu expand `Hardware` dan `Handheld Reader` pada dropdown
10. Verifikasi Sidebar Category menampilkan "Rename Baru {runId}-085"
11. Verifikasi Sidebar Category tidak lagi menampilkan "Dipakai Rename {runId}-085"
12. Verifikasi opsi dropdown Category pada popup menampilkan "Rename Baru {runId}-085"
13. Verifikasi opsi dropdown Category pada popup tidak lagi menampilkan "Dipakai Rename {runId}-085"
14. Tutup popup Create Device Name lewat `[×]`
15. Pindah ke sub-tab `Device SKU`
16. Expand `Hardware`, lalu expand `Handheld Reader`
17. Verifikasi Sidebar Category pada Device SKU menampilkan "Rename Baru {runId}-085"
18. Verifikasi Sidebar Category pada Device SKU tidak lagi menampilkan "Dipakai Rename {runId}-085"
19. Klik ikon Changelog pada header Sidebar Category
20. Ketik Search `Rename Baru {runId}-085`, tekan Enter
21. Verifikasi jumlah entri Changelog Category bertambah tepat satu dibanding N231 (entri lama tidak hilang; kemampuan baca)
22. Verifikasi hasil Search memuat satu entri Edit dengan Old Value "Dipakai Rename {runId}-085" dan New Value "Rename Baru {runId}-085"
23. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-232: Node baru langsung menjadi opsi Category selectable di form Device Name

24. Pindah ke sub-tab `Device Name`
25. Expand `Hardware`, lalu expand `Handheld Reader`
26. Hover node `Handheld Reader`, lalu klik aksi `+ Subcategory`
27. Ketik "Opsi Uji {runId}-085", lalu klik `[Submit]`
28. Tunggu aksi selesai
29. Klik `+ Device Name` pada toolbar, buka dropdown Category, lalu expand `Hardware` dan `Handheld Reader` pada dropdown
30. Verifikasi dropdown Category memuat opsi "Opsi Uji {runId}-085" sebagai node selectable tanpa refresh halaman
31. Tutup popup Create Device Name lewat `[×]`

### TC-AC-DC-233: Node yang dihapus hilang dari sidebar filter dan dropdown Category

32. Hover node `Hapus Sinkron {runId}-085`, lalu klik aksi Delete
33. Klik `[Delete]` pada dialog konfirmasi
34. Tunggu aksi selesai
35. Klik `+ Device Name` pada toolbar, buka dropdown Category, lalu expand `Hardware` dan `Handheld Reader` pada dropdown
36. Verifikasi Sidebar Category dan dropdown Category masih menampilkan node lain: "Rename Baru {runId}-085" dan "Opsi Uji {runId}-085"
37. Verifikasi "Hapus Sinkron {runId}-085" tidak ada lagi di Sidebar Category
38. Verifikasi "Hapus Sinkron {runId}-085" tidak ada lagi di dropdown Category

## Notes

- Langkah penghubung (S-03): langkah 14, 23, dan 31 (menutup popup dan modal tanpa perubahan form), langkah 15 dan 24 (pindah sub-tab yang diminta TC), langkah 16 dan 25 (membuka cabang tree pada sub-tab yang baru), langkah 5, 28, dan 34 (Tunggu aksi selesai sesudah `[Save]` langkah 4, `[Submit]` langkah 27, dan `[Delete]` langkah 33 yang hasilnya tidak diasersi langsung, 8b butir 8), serta Search pada langkah 6 (menemukan baris Device Name target, R-16) dan 20 (menemukan entri target di Changelog).
- Langkah 8 mengosongkan Search tabel Device Name sesuai bagian 8b butir 9.
- Alasan melewati 35 langkah (spec ini 38 langkah, tiga di antaranya langkah Tunggu aksi selesai): ketiga blok (TC-231, 232, 233) dijalankan sebagai satu kelas harness fungsional dengan data awal milik tiap blok sendiri. Pengecualian: langkah 36 (blok TC-233) memakai node hasil blok 231 (`Rename Baru {runId}-085`) dan blok 232 (`Opsi Uji {runId}-085`) sebagai pembanding, sehingga kegagalan blok 231 atau 232 membuat asersi langkah 36 kehilangan pembandingnya; spec tidak dipecah karena konvensi tidak mewajibkannya.
- Langkah 38 menjadi akhir spec dengan popup Create Device Name terbuka tanpa perubahan form; hook `beforeEach` suite menutup dialog (bagian 4, reset state ringan).
- Anchor absence (bagian 8b butir 2): langkah 36 (node lain pada surface yang sama tampil) mendahului langkah 37 dan 38; langkah 10 mendahului 11, langkah 12 mendahului 13, dan langkah 17 mendahului 18.
- Pembagian TC lintas spec: Delete diblok oleh Device Name dan Delete setelah pengacu dihapus ada di spec 086; Changelog untuk Edit yang sama ada di spec 079 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-231 Expected d menulis "12 entri lama tidak berubah" (jumlah absolut). Karena audit trail permanen, spec mengasersi selisih tepat satu terhadap N231 (S-12) dan satu entri Edit bersuffix; isi tiap entri lama tidak diperiksa.
  - TC memakai node, Device Name, dan Device SKU literal Pre-setup (#14 `Dipakai Leaf`, #15 `HR-100`, #16 `SKU-FN-1`); spec memakai data bersuffix milik spec (keputusan data tulis). Asersi pada kolom Category baris Device Name bergantung pada baris yang ditemukan lewat Search (R-16).
  - TC-AC-DC-231 langkah 5 ("Perhatikan baris `HR-100`") tidak menyebut cara menemukan baris di tabel yang berhalaman; spec memakai Search.
  - TC-AC-DC-233 Expected b ("seluruh node lain tetap tampil") bersifat universal; spec memeriksa dua node milik spec yang dijamin ada sebagai pembanding.
