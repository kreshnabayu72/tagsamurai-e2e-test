---
id: TC-FA-CAT-E2E-174-defense-in-depth-validasi-server-markup-sql-isolasi-tenant-dan-capability-atp-bagian-2
title: "Defense-in-Depth: Validasi Server, Markup dan SQL pada Nama, Isolasi Tenant, dan Capability ATP Read (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-503
  - TC-FA-CAT-508
  - TC-FA-CAT-509
  - TC-FA-CAT-510
  - TC-FA-CAT-637
coverage:
  web: automated
---

# Defense-in-Depth: Validasi Server, Markup dan SQL pada Nama, Isolasi Tenant, dan Capability ATP Read (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth: validasi server atas request langsung, injeksi XSS dan SQL, isolasi tenant, bypass capability). Pemicu request langsung memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Akun yang dipakai lewat langkah Ganti akun:

  | TC | Aktor | Pre-setup | Email | Password | Client |
  |---|---|---|---|---|---|
  | TC-FA-CAT-510 (langkah 39) | ATP Read (hanya capability Read Manage Asset Transactional Policy) | #12 | `atpRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ATPREAD_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-509 (langkah 45) | Total Control | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | CatFresh (#25) |

- Env var `FA_TC_PASSWORD` dan `FA_ATPREAD_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Halaman awal: hook `beforeEach` suite membuka Categories. Pengecualian: langkah 40 membuka Fixed Asset > Settings > Asset Transactional Policy (TC-FA-CAT-510).
- Data Dinamis (dibuat spec lewat UI; dihapus hook `after` lewat API): kategori `<img src=x onerror=alert(1)> {runId}-174` (Code `XSS1`) dan `Cat'; DROP TABLE categories;-- {runId}-174` (Code `SQL1`) pada CatMain. Suffix `{runId}-174` ditambahkan di belakang payload TC agar nama unik antar run (S-12); payload TC tetap utuh di depan. Code `XSS1` dan `SQL1` literal sesuai TC; hook `before` menghapus sisa kategori ber-Code itu (R-13).
- Payload request langsung TC-FA-CAT-503 (client CatMain, tidak menyimpan data): Category Name 121 karakter `A`; Category Name `Code Bad {runId}-174` dengan Code `AB C!`; Category Name `Desc Long {runId}-174` dengan Description 361 karakter `D`; Category Name `All Categories` dengan Code `AC174`.
- Data client Pre-setup yang dibaca: CatMain (Pre-setup #20, 15 kategori), CatFresh (Pre-setup #25, hanya `Default Category`, tanpa kategori tambahan dari spec lain).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk request langsung dengan sesi API aktor; kemampuan membaca jumlah dan nama kategori dari server (state data); penangkap dialog JavaScript browser (alert) yang aktif sejak langkah 13 dan dilepas di hook `after`.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite (termasuk akun ATP Read dan Total Control CatFresh). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-503: Validasi server menolak payload yang melewati validasi FE

1. Catat baseline jumlah kategori client CatMain dari server
2. Kirim request Create dengan Category Name 121 karakter `A` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
3. Verifikasi server menolak request dengan respons validasi 422 dan pesan field Category Name sesuai V-02
4. Kirim request Create dengan Category Name `Code Bad {runId}-174` dan Code `AB C!` langsung ke server hingga respons diterima
5. Verifikasi server menolak request dengan respons validasi 422 dan pesan field Code sesuai V-07
6. Kirim request Create dengan Category Name `Desc Long {runId}-174` dan Description 361 karakter langsung ke server hingga respons diterima
7. Verifikasi server menolak request dengan respons validasi 422 dan pesan field Description sesuai V-09
8. Kirim request Create dengan Category Name `All Categories` dan Code `AC174` langsung ke server hingga respons diterima
9. Verifikasi server menolak request dengan respons validasi 422 dan pesan field Category Name sesuai V-05
10. Verifikasi tidak ada kategori tersimpan: jumlah kategori dari server sama dengan baseline dan daftar tidak memuat `Code Bad {runId}-174`, `Desc Long {runId}-174`, maupun nama 121 karakter

### TC-FA-CAT-508: Nama berisi markup dirender sebagai teks

11. Klik `[+] Category` pada sidebar
12. Isi Category Name `<img src=x onerror=alert(1)> {runId}-174` dan Code `XSS1`
13. Klik `[Submit]`
14. Ketik Search `<img src=x onerror=alert(1)> {runId}-174`, tekan Enter
15. Verifikasi baris kategori tampil di tabel sebagai teks literal tanpa elemen gambar yang dirender
16. Verifikasi node kategori tampil di sidebar sebagai teks literal tanpa elemen gambar yang dirender
17. Buka Popup Detail kategori `<img src=x onerror=alert(1)> {runId}-174`
18. Verifikasi Popup Detail menampilkan nama sebagai teks literal tanpa elemen gambar yang dirender
19. Tutup Popup Detail
20. Buka Modal Changelog dan filter Category Name `<img src=x onerror=alert(1)> {runId}-174`
21. Verifikasi Modal Changelog menampilkan nama sebagai teks literal tanpa elemen gambar yang dirender
22. Tutup Modal Changelog
23. Verifikasi tidak ada dialog JavaScript (alert) yang muncul selama langkah 13 sampai 22 (tidak ada script dieksekusi)
24. Klik `(←)` pada kotak Search

### TC-FA-CAT-637: Nama berisi string SQL disimpan literal

25. Klik `[+] Category` pada sidebar
26. Isi Category Name `Cat'; DROP TABLE categories;-- {runId}-174` dan Code `SQL1`
27. Klik `[Submit]`
28. Ketik Search `Cat'; DROP TABLE categories;-- {runId}-174`, tekan Enter
29. Verifikasi kategori tersimpan dengan nama literal dan baris tampil apa adanya di tabel
30. Verifikasi node kategori tampil apa adanya di sidebar
31. Buka Popup Detail kategori `Cat'; DROP TABLE categories;-- {runId}-174`
32. Verifikasi Popup Detail menampilkan nama apa adanya
33. Tutup Popup Detail
34. Buka Modal Changelog dan filter Category Name `Cat'; DROP TABLE categories;-- {runId}-174`
35. Verifikasi Modal Changelog menampilkan nama apa adanya
36. Tutup Modal Changelog
37. Klik `(←)` pada kotak Search
38. Verifikasi seluruh kategori Pre-setup #20 (`Default Category`, `Electronics`, `Laptop`, `Monitor`, `Furniture`, `Peripheral`, `Keyboard`, `Mouse`, `Accessory`, `Cable`, `Tools`, `Vehicle`, `Spare Part`, `Bolt`, `Bolt M8`) tetap ada pada daftar kategori dan data kategori lain tidak terdampak

### TC-FA-CAT-510: Capability ATP Read tidak mendapat jalur tulis atau Detail

39. Ganti akun: logout, lalu login sebagai ATP Read (Pre-setup #12) client CatMain dengan `Spectra.env.FA_ATPREAD_PASSWORD`
40. Buka Fixed Asset > Settings > Asset Transactional Policy
41. Verifikasi Sidebar Category Tree menampilkan pohon kategori dengan id, nama, Code, posisi hierarki, dan penanda leaf
42. Verifikasi elipsis dan tombol aksi tulis tidak tersedia pada node
43. Verifikasi Detail kategori tidak tersedia
44. Verifikasi angka Total Asset tidak tampil

### TC-FA-CAT-509: Isolasi tenant

45. Ganti akun: logout, lalu login sebagai Total Control (Pre-setup #1) client CatFresh dengan `Spectra.env.FA_TC_PASSWORD`
46. Buka Fixed Asset > Settings > Categories
47. Verifikasi tabel Categories hanya menampilkan `Default Category` dan tidak memuat kategori client CatMain
48. Verifikasi Sidebar Category Tree hanya menampilkan `Default Category` dan tidak memuat kategori client CatMain
49. Ketik Search `Electronics`, tekan Enter
50. Verifikasi tabel menampilkan empty state `No results found`
51. Klik `(←)` pada kotak Search
52. Ketik `Electronics` pada TreeSearchInput sidebar
53. Verifikasi node `Electronics` tidak tampil pada hasil TreeSearchInput

## Notes

- Spec melewati sekitar 35 langkah (53 langkah). Alasan: seluruh blok berkelas harness yang sama (a) dan berdiri sendiri; tiap blok memakai aktor, client, dan datanya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-FA-CAT-508 dan TC-FA-CAT-637 memakai pola yang sama (buat kategori, baca empat surface). TC-FA-CAT-510 dan TC-FA-CAT-509 berganti akun dan client sehingga diletakkan paling akhir (S-10).
- `K-1`: TC-FA-CAT-503 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-categories-backend.md`.
- Urutan TC dalam spec: 503, 508, 637, 510, 509 (bukan urutan id) supaya TC akun Total Control CatMain berurutan sebelum dua ganti akun (S-10).
- Langkah penghubung (S-03): langkah 14, 28 (Search untuk menemukan baris target), langkah 19, 22, 33, 36 (menutup popup atau modal), langkah 24, 37, 51 (mereset Search), langkah 1 (baseline), langkah 39 dan 45 (ganti akun), langkah 40 dan 46 (buka halaman).
- Langkah 15, 16, 18, 21 menggabung teks literal dan tanpa elemen gambar sebagai satu klausa "dirender sebagai teks" mengikuti judul TC-FA-CAT-508.
- Langkah 23 membuktikan tidak ada script dieksekusi lewat tidak adanya dialog alert; pemicu `onerror` dieksekusi saat gambar gagal dimuat sehingga dialog akan muncul pada surface yang merender nama sebagai HTML.
- Anchor positif absence (bagian 8b butir 2): langkah 47 dan 48 (Default Category tampil) untuk absence kategori CatMain; langkah 50 (empty state `No results found`) untuk hasil Search; sidebar yang sudah termuat (langkah 48) menjadi anchor permukaan untuk TreeSearchInput langkah 53. Langkah 42 sampai 44 memakai pohon yang tampil pada langkah 41 sebagai anchor permukaan.
- Temuan untuk QA:
  - TC-FA-CAT-503 hanya menyebut "pesan field sesuai V-02, V-07, V-09, V-05" tanpa teks pesan; spec mengasersi 422 dan field pesan menurut kode V.
  - TC-FA-CAT-503 langkah 4 tidak menyebut Category Name yang menyertai Code `AB C!` dan Description 361 karakter, serta tidak menyebut Code untuk Category Name `All Categories`; spec memakai nilai bersuffix dan `AC174`.
  - TC-FA-CAT-508 dan TC-FA-CAT-637 tidak menyebut nama bersuffix; spec menambahkan suffix `{runId}-174` di belakang payload.
  - TC-FA-CAT-510 tidak menyebut apakah hasil TreeSearchInput atau elemen lain berbeda dari pohon biasa; spec mengasersi pohon, aksi tulis, Detail, dan Total Asset sesuai Expected.
  - TC-FA-CAT-509 menyebut "Search dan TreeSearchInput" tanpa menyebut bentuk hasil kosong TreeSearchInput; spec hanya mengasersi node `Electronics` tidak tampil.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` dan `FA_ATPREAD_PASSWORD` adalah usulan.
