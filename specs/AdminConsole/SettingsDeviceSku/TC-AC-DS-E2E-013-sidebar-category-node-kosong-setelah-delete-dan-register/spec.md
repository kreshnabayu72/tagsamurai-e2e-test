---
id: TC-AC-DS-E2E-013-sidebar-category-node-kosong-setelah-delete-dan-register
title: "Sidebar Category: Node Terpilih Menjadi Kosong setelah Delete dan Kembali Terisi setelah Register"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-600
  - TC-AC-DS-601
coverage:
  web: automated
---

# Sidebar Category: Node Terpilih Menjadi Kosong setelah Delete dan Kembali Terisi setelah Register

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25 (node `Barcode Handheld` tidak memiliki SKU Principal), Device Name #26 (`Rugged Handheld Reader`), Brand #27 (`Arcturus`), file foto `foto-a.jpg` #37, SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data milik spec (hook `before`, lewat sesi API aktor dan fixture BE yang disediakan tim BE/FE): Subcategory `Node Kosong {runId}-013` (di bawah `Handheld Reader`), Device Name `DN Kosong {runId}-013` (Category `Node Kosong {runId}-013`), dan SKU `DEL-{runId}-013` (Device Name `DN Kosong {runId}-013`, Brand `Arcturus`, Model/Type `DK-{runId}`, Range Type `Short Range`, stok 0, 1 foto) sebagai satu-satunya SKU pada node itu, menggantikan `SFR-ZERO-01` pada node `Tunnel Reader` (S-06: target Delete memakai data milik spec).
- Data Dinamis: SKU `NEW-EMP-{runId}-013` (dibuat TC-601 di node `Barcode Handheld`, Model/Type `R-E1`, Range Type `Short Range`, foto `foto-a.jpg`). Hook `after` menghapus `NEW-EMP-{runId}-013`, serta Subcategory, Device Name, dan SKU milik spec bila masih ada, lewat fixture BE.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`.

## Test Steps

### TC-AC-DS-600: Menghapus satu-satunya SKU pada node terpilih

1. Klik tombol Expand/Collapse All pada Sidebar Category
2. Klik node `Node Kosong {runId}-013` pada Sidebar Category
3. Klik ⋯ pada baris `DEL-{runId}-013` lalu pilih `Delete`
4. Klik `[Delete]` pada dialog konfirmasi
5. Verifikasi toast sukses: "Success, device SKU has been deleted."
6. Verifikasi node `Node Kosong {runId}-013` tetap terpilih
7. Verifikasi tabel menampilkan ilustrasi dengan judul "No results found" dan deskripsi "Try adjusting your search or filter."
8. Verifikasi empty state tidak memuat judul "No SKU yet"
9. Klik node `Node Kosong {runId}-013` untuk membatalkan pilihan

### TC-AC-DS-601: Mendaftarkan SKU pada node kosong

10. Klik node `Barcode Handheld` pada Sidebar Category
11. Verifikasi tabel menampilkan ilustrasi dengan judul "No results found" dan deskripsi "Try adjusting your search or filter."
12. Klik tombol `[+ SKU]` pada toolbar
13. Pilih Category `Barcode Handheld` lewat picker Category lalu klik `[Select]`
14. Pilih Device Name `Rugged Handheld Reader`
15. Pilih Brand `Arcturus`
16. Ketik `R-E1` pada Model/Type
17. Ketik `NEW-EMP-{runId}-013` pada SKU
18. Pilih Range Type `Short Range`
19. Unggah `foto-a.jpg`
20. Klik `[Submit]`
21. Verifikasi toast sukses: "Success, device SKU has been registered."
22. Verifikasi tabel kembali menampilkan data dengan satu baris `NEW-EMP-{runId}-013`
23. Verifikasi node `Barcode Handheld` tetap terpilih
24. Klik node `Barcode Handheld` untuk membatalkan pilihan

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-600, TC-601. TC-600 (menghapus data) dan TC-601 (mendaftarkan SKU) saling independen; TC-600 diletakkan lebih dulu karena TC-601 menyisakan satu SKU baru yang dibersihkan hook `after`.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 (membuka semua node; TC-43 menyatakan klik Expand/Collapse All pertama membuka semua node), 2 dan 10 (memilih node), 3 dan 4 (membuka dan mengonfirmasi Delete), 9 dan 24 (membatalkan pilihan node, S-09), 12 sampai 20 (mengisi form Register dan Submit; hasilnya diasersi pada langkah 21 sampai 23).
- TC-600 memakai SKU, Device Name, dan Subcategory milik spec (bukan `SFR-ZERO-01` pada node `Tunnel Reader`) karena SKU Pre-setup tidak boleh dihapus spec (S-06). Node `Tunnel Reader` berisi satu SKU Pre-setup; node milik spec dibuat khusus agar hanya memiliki satu SKU.
- Langkah 22 (satu baris `NEW-EMP-{runId}-013`) memakai nama bersuffix; node `Barcode Handheld` tidak memiliki SKU Principal lain (Pre-setup #29/#30), sehingga barisnya tunggal.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25, #26, #27 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan). TC menamai SKU `NEW-EMP-01`; spec memakai `NEW-EMP-{runId}-013` (bersuffix) dan data hapus milik spec menggantikan `SFR-ZERO-01`.
  - Fixture rancangan: ketersediaan Pre-setup #25/#26/#27 di environment belum diverifikasi; seeding Subcategory khusus bergantung pada kemampuan fixture BE tim BE/FE.
  - TC-601 langkah 4 menggabungkan pengisian form dalam satu langkah; spec memecahnya menjadi langkah 13 sampai 19 mengikuti isi data TC.
  - TC-601 tidak menyebut apakah Category terisi otomatis dari node Sidebar terpilih; spec mengikuti TC dan memilih Category lewat picker.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
