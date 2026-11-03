---
id: TC-FA-PREF-E2E-151-deferred-export-journal-jumlah-baris-menurut-journal-grouping-dan-group-assignable
title: "[DEFERRED] Export Journal: jumlah baris menurut Journal Grouping dan Group Assignable"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-488
  - TC-FA-PREF-489
  - TC-FA-PREF-490
  - TC-FA-PREF-491
  - TC-FA-PREF-492
coverage:
  web: automated
---

# [DEFERRED] Export Journal: jumlah baris menurut Journal Grouping dan Group Assignable

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul konsumen Export Journal yang belum disusun). Jumlah baris berkas adalah asersi fungsional; nilai sel dimensi diasersi lewat `P-10` (lihat Notes).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (bulan berjalan Oktober 2026); data aset Export Journal PC-17: enam aset menyusut dengan akun Beban Penyusutan yang sama (dua laptop dan satu printer di Group Indonesia > Jakarta, IT Equipment, Category Elektronik > Laptop dan Elektronik > Printer; satu laptop di Group Indonesia > Bandung, IT Equipment; dua mobil di Group Indonesia > Jakarta, Vehicles, Category Kendaraan > Mobil); struktur Group Indonesia (induk) berisi Jakarta dan Bandung (Assignable); untuk TC-FA-PREF-492 Group Assignable Jakarta Barat di bawah Group induk Indonesia > Jakarta (path Indonesia > Jakarta > Jakarta Barat). Data modul Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Journal Grouping per TC (dibentuk lewat seed): "Group", "Category", dan "Asset Class" untuk TC-FA-PREF-488; "Group" saja untuk TC-FA-PREF-489 dan 492; kosong untuk TC-FA-PREF-490 dan awal TC-FA-PREF-491.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan enam aset PC-17; ekspor jurnal penyusutan bulan ini lewat UI Export Journal; pembaca berkas XLSX hasil ekspor (jumlah baris per akun, nilai kolom, total Debit dan Credit), disediakan tim FE.
- State global yang diubah: Journal Grouping company; dikembalikan ke nilai awal PC-1 ("Group") oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-488: Journal Grouping Group, Category, dan Asset Class menulis 4 baris untuk akun Beban Penyusutan

1. Seed Journal Grouping tersimpan "Group", "Category", dan "Asset Class" dan enam aset menyusut PC-17 hingga tersimpan
2. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
3. Buka file ekspor
4. Verifikasi file ekspor memuat 4 baris untuk akun Beban Penyusutan: (Group, Category, Asset Class) Indonesia > Jakarta, Elektronik > Laptop, IT Equipment; Indonesia > Jakarta, Elektronik > Printer, IT Equipment; Indonesia > Bandung, Elektronik > Laptop, IT Equipment; dan Indonesia > Jakarta, Kendaraan > Mobil, Vehicles

### TC-FA-PREF-489: Journal Grouping Group saja menulis 2 baris untuk akun Beban Penyusutan

5. Seed Journal Grouping tersimpan "Group" saja dan enam aset menyusut PC-17 hingga tersimpan
6. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
7. Buka file ekspor
8. Verifikasi file ekspor memuat 2 baris untuk akun Beban Penyusutan: Indonesia > Jakarta dan Indonesia > Bandung

### TC-FA-PREF-490: Journal Grouping kosong menulis 6 baris untuk akun Beban Penyusutan

9. Seed Journal Grouping tersimpan kosong dan enam aset menyusut PC-17 hingga tersimpan
10. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
11. Buka file ekspor
12. Verifikasi file ekspor memuat 6 baris untuk akun Beban Penyusutan: satu baris per aset tanpa peringkasan

### TC-FA-PREF-491: Total Debit dan total Kredit file ekspor sama untuk semua pilihan Journal Grouping

13. Seed Journal Grouping tersimpan kosong dan enam aset menyusut PC-17 hingga tersimpan
14. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
15. Catat total Debit dan total Kredit file ekspor pertama
16. Buka Fixed Asset > Settings > Accounting > Preferences
17. Ubah Journal Grouping menjadi "Group", "Category", dan "Asset Class" pada MultiSelect Journal Grouping
18. Klik [Save changes]
19. Tunggu aksi selesai
20. Buka Export Journal dan ekspor jurnal penyusutan bulan yang sama
21. Catat total Debit dan total Kredit file ekspor kedua
22. Verifikasi total Debit dan total Kredit ekspor kedua sama dengan ekspor pertama

### TC-FA-PREF-492: Dimensi Group memakai Group Assignable, bukan Group induk

23. Seed Journal Grouping tersimpan "Group" dan aset ditempatkan pada Group Assignable Jakarta Barat di bawah Group induk Jakarta (path Indonesia > Jakarta > Jakarta Barat) hingga tersimpan
24. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
25. Buka file ekspor
26. Verifikasi kolom Group berisi path penuh "Indonesia > Jakarta > Jakarta Barat" (Group Assignable)
27. Verifikasi kolom Group tidak berisi Group induk "Indonesia > Jakarta" saja
28. Pulihkan Journal Grouping ke "Group" dan penempatan aset ke nilai awal PC-17 lewat seed hingga tersimpan

## Notes

- P-10: TC-FA-PREF-488, 489, 490, dan 492 menulis Expected berupa isi berkas ekspor (nilai dimensi Group, Category, Asset Class dan nilai kolom Group) bersama jumlah baris, pada alur ekspor yang sama; klausa isi berkas ditulis sebagai `Verifikasi` satu per klausa. Alasan: nilai dimensi per baris menentukan jumlah baris yang diasersi dan alur ekspor tidak dapat dipisah dari asersi itu. TC-FA-PREF-492 tidak memuat klausa UI selain berkas; lihat Temuan untuk QA.
- Langkah penghubung (S-03): langkah 16 (membuka layar Preferences), langkah 19 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah surface), langkah 28 (pemulihan state, S-09, R-08).
- Langkah 15 dan 21 adalah langkah `Catat` tanpa `Verifikasi` untuk asersi pada langkah 22 (S-03).
- Seed per TC (langkah 1, 5, 9, 13, 23) membentuk precondition tanpa bergantung hasil TC sebelumnya.
- Temuan untuk QA:
  - TC-FA-PREF-492 objek ujinya hanya isi berkas (nilai sel kolom Group) tanpa asersi UI; menurut bagian 3 prinsip 13f TC seperti itu semestinya spec kelas f sendiri, tetapi penempatannya di spec ini mengikuti keputusan pengelompokan; mohon QA mengonfirmasi atau memindahkannya ke spec kelas f (152 atau 153).
  - TC-FA-PREF-488 Post Condition ("Total Debit dan total Kredit sama pada semua pilihan") dan TC-FA-PREF-489 dan 490 dengan Post Condition yang sama tidak punya langkah observasi di TC dan tidak diasersi; asersi total ada pada TC-FA-PREF-491 (S-01).
  - TC-FA-PREF-488 sampai 492 menyebut "ekspor jurnal penyusutan bulan ini" tanpa nama berkas atau label tombol ekspor; spec memakai teks TC.
  - TC-FA-PREF-491 langkah TC "Ubah Journal Grouping ... lalu Save" tidak menyebut hasil Save; spec tidak mengasersi toast atau dialog dan hanya menunggu aksi selesai.
  - TC-FA-PREF-491 Expected tidak menyebut nilai total; spec membandingkan kedua berkas tanpa nilai absolut.
  - TC-FA-PREF-493 sampai 503 (isi berkas) ada di spec 152 dan 153.
