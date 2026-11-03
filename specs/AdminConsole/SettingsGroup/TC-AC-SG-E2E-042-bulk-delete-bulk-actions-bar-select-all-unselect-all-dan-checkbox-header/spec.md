---
id: TC-AC-SG-E2E-042-bulk-delete-bulk-actions-bar-select-all-unselect-all-dan-checkbox-header
title: "Bulk Delete: Bulk Actions Bar, Select All dan Unselect All, serta Checkbox Header"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-151
  - TC-AC-SG-152
  - TC-AC-SG-153
coverage:
  web: automated
---

# Bulk Delete: Bulk Actions Bar, Select All dan Unselect All, serta Checkbox Header

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`, dibaca saja), nama literal karena TC mengasersi nama baris: `Hapus Bulk 1` sampai `Hapus Bulk 6` (tanpa entitas) di antara 24 node entitas ini.
- N total = 24 node (node All Groups tanpa Search; diturunkan dari seeding Pre-setup #21 dan dikonfirmasi lewat Fixture BE, bukan dibaca dari tabel satu halaman, bagian 8b butir 10). Ukuran halaman default 10 baris sehingga tabel memiliki tiga halaman.
- Spec ini hanya memilih baris dan tidak pernah mengonfirmasi Delete; tidak ada node yang dihapus atau diubah, Last Updated tidak berubah (S-06). Hook `before` dan `after` memastikan baseline Pre-setup #21 lewat Fixture BE.
- Kemampuan teknis: Fixture BE (pemulihan baseline dan hitungan node entitas), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-151: Bulk Actions Bar muncul saat baris terpilih dan hilang saat seleksi dikosongkan

1. Ketik Search `Hapus Bulk`, tekan Enter
2. Verifikasi sedikitnya satu baris tampil di tabel
3. Verifikasi tidak ada Bulk Actions Bar di atas tabel
4. Centang kolom Checkbox pada baris `Hapus Bulk 1`
5. Verifikasi Bulk Actions Bar menampilkan "1 Group selected"
6. Centang kolom Checkbox pada baris `Hapus Bulk 2`
7. Verifikasi Bulk Actions Bar menampilkan "2 Groups selected"
8. Verifikasi ikon `×` dan tombol `Bulk Action` (`BulkActionButton`) tampil pada Bulk Actions Bar
9. Klik `Bulk Action`
10. Verifikasi overlay berisi aksi `Delete` (ikon `DeleteBin6Line`, severity danger)
11. Tutup overlay dengan menekan Esc
12. Klik ikon `×` pada Bulk Actions Bar
13. Verifikasi seluruh seleksi kosong (checkbox `Hapus Bulk 1` dan `Hapus Bulk 2` tidak tercentang)
14. Verifikasi Bulk Actions Bar hilang

### TC-AC-SG-152: Tombol Select All ([N] records) berganti menjadi Unselect All saat seluruh data terpilih

15. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
16. Centang kolom Checkbox pada baris pertama tabel
17. Klik "Select All (24 records)" pada Bulk Actions Bar
18. Verifikasi Bulk Actions Bar menampilkan "24 Groups selected" (seluruh baris yang cocok lintas halaman)
19. Verifikasi tombol berganti menjadi "Unselect All"
20. Hilangkan centang satu baris
21. Verifikasi tombol kembali menjadi "Select All (24 records)"
22. Klik "Select All (24 records)"
23. Klik "Unselect All"
24. Verifikasi seluruh seleksi dibatalkan
25. Verifikasi Bulk Actions Bar menutup

### TC-AC-SG-153: Checkbox header kolom hanya memilih baris yang tampil di halaman aktif

26. Centang checkbox pada header kolom Checkbox
27. Verifikasi hanya baris yang tampil pada halaman 1 yang terpilih (Bulk Actions Bar menampilkan "10 Groups selected")
28. Pindah ke halaman 2
29. Verifikasi baris di halaman 2 tidak terpilih
30. Klik ikon `×` pada Bulk Actions Bar

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16); langkah 11 (menutup overlay yang dibuka untuk asersi langkah 10); langkah 12 dan 15 (membersihkan seleksi dan Search, S-09); langkah 16 (memilih satu baris agar Bulk Actions Bar tampil); langkah 30 (membersihkan seleksi).
- Langkah 18 (`Verifikasi Bulk Actions Bar menampilkan "24 Groups selected"`) dan langkah 27 ("10 Groups selected") adalah asersi tambahan yang hitungannya tidak tertulis di Expected TC-AC-SG-152 dan TC-AC-SG-153 (Expected hanya menyebut seluruh baris cocok lintas halaman dan hanya baris halaman 1): teks hitungan memperkuat bukti cakupan seleksi dan diturunkan dari N total 24 node serta ukuran halaman 10, sehingga dipertahankan.
- Langkah 9 sampai 11 adalah tambahan untuk mengasersi overlay `Bulk Action` yang disebut Expected TC-AC-SG-151 butir b; TC tidak memberi langkah yang membuka overlay (S-03).
- Temuan untuk QA:
  - TC-AC-SG-152 langkah 2 mengklik "Select All ([N] records)" tanpa menyebut baris yang dicentang lebih dulu; spec memilih satu baris pertama agar Bulk Actions Bar tampil.
  - TC-AC-SG-152 langkah 4 "Klik 'Unselect All' setelah memilih semua lagi" ditulis sebagai klik "Select All (24 records)" lalu "Unselect All".
  - TC-AC-SG-153 Expected "baris di halaman 2 tidak terpilih" tidak menyebut cara cek; spec memeriksa checkbox baris di halaman 2.
