---
id: TC-AC-DS-E2E-009-sidebar-category-screening-dan-pilih-node
title: "Sidebar Category: Screening, Pilih Node Induk dan Daun, Tanpa Pilihan, serta Daun Tingkat ke-4"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-36
  - TC-AC-DS-37
  - TC-AC-DS-38
  - TC-AC-DS-41
  - TC-AC-DS-576
coverage:
  web: automated
---

# Sidebar Category: Screening, Pilih Node Induk dan Daun, Tanpa Pilihan, serta Daun Tingkat ke-4

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25, SKU inti #29 dan seed #30 (total 129 SKU Principal, dari seeding). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data hierarki mendalam Pre-setup #42 (data khusus TC-37 dan TC-576): dua Subcategory di bawah `UHF Handheld` yaitu `UHF Handheld Gudang` (tingkat ke-4) dan `UHF Handheld Lapangan` (tingkat ke-4, tanpa Device Name dan tanpa SKU); Device Name `Pemindai Gudang` (Category `UHF Handheld Gudang`); SKU `HHR-GDG-01` (Device Name `Pemindai Gudang`, Brand `Arcturus`, Model/Type `PG-1`, Range Type `Long Range`, stok 0, 1 foto); SKU `HHR-PRT-01` (Device Name `Pemindai Ujung` pada Category `Handheld Reader`, Brand `Kinetia`, Model/Type `PU-1`, Range Type `Short Range`, stok 0, 1 foto). Disiapkan lewat fixture BE pada langkah 23 (bukan di hook `before`, supaya TC-36 sampai TC-41 berjalan pada total 129 SKU) dan dihapus oleh hook `after` lewat fixture BE yang disediakan tim BE/FE; seeding idempotent (dilewati bila sudah ada) dan cleanup hanya menghapus yang dibuat spec ini.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini mengubah data Category dan SKU bersama (hierarki #42) sehingga pemulihannya dijamin hook `after`.

## Test Steps

### TC-AC-DS-36: Screening Sidebar Category

1. Klik tombol Expand/Collapse All pada Sidebar Category
2. Verifikasi judul `Category` tampil rata kiri
3. Verifikasi baris kedua memuat input pencarian pohon dan tombol ikon Expand/Collapse All sejajar
4. Verifikasi pohon memuat `Hardware` (`Handheld Reader` > `UHF Handheld`, `Barcode Handheld`, `Perangkat Pemindai Kode Batang Industri`; `Smart Fixed Reader` > `Portal Reader`, `Tunnel Reader`; `BLE Gateway`) dan `TAG` (`NFC` > `Wearable TAG`, `Asset TAG`)
5. Verifikasi tidak ada tombol aksi `Category` pada Sidebar
6. Verifikasi tidak ada menu aksi ⋯ pada node
7. Verifikasi tab mengambang Collapse tampil di tepi kiri panel
8. Verifikasi tanpa node terpilih, List menampilkan semua SKU dalam scope dengan total 129 SKU

### TC-AC-DS-38: Pilih node daun

9. Klik node `Asset TAG` pada Sidebar Category
10. Verifikasi baris SKU seed tampil pada List
11. Verifikasi setiap baris yang tampil berkategori `Asset TAG`
12. Ketik Search `SRT-`, tekan Enter
13. Verifikasi baris `SRT-ANG-01` dan `SRT-APL-01` tampil
14. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
15. Verifikasi baris `TAG-ARC-OBJ` tampil
16. Ganti isi kotak search dengan `TAG-ARC-USR`, tekan Enter
17. Verifikasi SKU `TAG-ARC-USR` (Category `Wearable TAG`) tidak tampil dan tabel menampilkan "No results found"
18. Klik `(←)` pada kotak Search
19. Klik node `Asset TAG` untuk membatalkan pilihan

### TC-AC-DS-41: Tanpa node terpilih

20. Klik node `Asset TAG`
21. Klik node `Asset TAG` lagi
22. Verifikasi List kembali menampilkan semua SKU dalam scope Principal dengan total 129 SKU

### Persiapan data hierarki mendalam

23. Siapkan data hierarki mendalam Pre-setup #42 lewat fixture BE hingga Subcategory, Device Name, dan SKU tersimpan
24. Muat ulang halaman `Settings > Device > Device SKU`
25. Klik tombol Expand/Collapse All pada Sidebar Category

### TC-AC-DS-37: Pilih node induk

26. Klik nomor halaman 2 pada Pagination
27. Klik node `Handheld Reader` pada Sidebar Category
28. Verifikasi node `Handheld Reader` ter-highlight
29. Verifikasi List memuat SKU yang melekat pada `Handheld Reader` itu sendiri (`HHR-PRT-01`, Device Name `Pemindai Ujung`) dan SKU berkategori `UHF Handheld` (`HHR-ARC-100`, `HHR-ARC-200`), `UHF Handheld Gudang` pada tingkat ke-4 (`HHR-GDG-01`), `Barcode Handheld`, dan `Perangkat Pemindai Kode Batang Industri` (`HHR-BIG-01`)
30. Verifikasi SKU `HHR-GDG-01` pada tingkat ke-4 tampil walau bukan anak langsung `Handheld Reader`
31. Verifikasi SKU `SFR-VEL-4P` (`Portal Reader`), `BLE-KIN-GW1` (`BLE Gateway`), dan `TAG-ARC-USR` (TAG) tidak tampil pada List
32. Verifikasi Pagination kembali ke halaman 1

### TC-AC-DS-576: Pilih node daun tingkat ke-4

33. Klik node `Handheld Reader` untuk membatalkan pilihan
34. Klik node `UHF Handheld Gudang` pada Sidebar Category
35. Verifikasi node `UHF Handheld Gudang` ter-highlight
36. Verifikasi List hanya memuat SKU `HHR-GDG-01`
37. Verifikasi SKU `HHR-ARC-100`, `HHR-ARC-200` (Category `UHF Handheld`), dan `HHR-PRT-01` (Category `Handheld Reader`) tidak tampil pada List
38. Klik node `UHF Handheld Gudang` untuk membatalkan pilihan

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-36, TC-38, TC-41, persiapan data hierarki #42, TC-37, TC-576. TC-37 dan TC-576 diletakkan sesudah seeding #42 dan TC-36, TC-38, TC-41 sebelumnya karena ketiganya mengasersi pohon dan total 129 SKU tanpa data #42 (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 25 (membuka semua node agar pohon terlihat; TC-43 menyatakan klik Expand/Collapse All pertama membuka semua node), 9, 12, 14, 16 (memilih node dan Search untuk menemukan baris target, R-16), 18, 19, 33, 38 (mengosongkan Search dan membatalkan pilihan node, S-09), 20, 21, 23, 24, 26 (klik ke halaman 2 sebelum memilih node, supaya pengembalian ke halaman 1 pada langkah 32 teramati, S-14), 27, 34.
- Langkah 10 dan 11, 13 dan 15 memeriksa SKU seed dan SKU bernama pada List yang tersaring node `Asset TAG`; baris bernama dicari lewat Search karena tidak berada di halaman 1 (SKU seed `SEED-001` sampai `SEED-119` mendahuluinya pada sort SKU A-Z). Verifikasi absence langkah 17 didahului langkah 13 dan 15 (baris `Asset TAG` lain tampil) dan "No results found" hasil Search (anchor).
- Spec melewati sekitar 35 langkah (38 langkah). Alasan pertahanan: seluruh blok memeriksa pohon Sidebar Category dan filter List atas pilihan node dalam satu kelas (fungsional Sidebar Category) pada satu halaman; blok data hierarki mendalam #42 hanya dibuat sekali dan dipakai TC-37 dan TC-576; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25, #29, #30, dan #42 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan). Seeding #42 memakai nama literal (idempotent, serial) sampai ada keputusan.
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 dan hierarki #42 di environment belum diverifikasi.
  - TC-36 tidak menyebut apakah pohon default tertutup atau terbuka; spec memakai Expand/Collapse All lebih dulu mengikuti TC-43.
  - TC-37 langkah 3 dan TC-576 tidak menyebut cara membatalkan pilihan node sebelum TC berikutnya; spec menambah langkah penghubung (klik node yang sama).
  - TC-38 Expected a menyebut "seluruh SKU seed" tanpa jumlah; spec memeriksa baris seed pada halaman aktif.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
