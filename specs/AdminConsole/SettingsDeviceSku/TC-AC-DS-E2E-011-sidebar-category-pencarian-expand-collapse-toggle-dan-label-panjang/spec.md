---
id: TC-AC-DS-E2E-011-sidebar-category-pencarian-expand-collapse-toggle-dan-label-panjang
title: "Sidebar Category: Pencarian Pohon, Expand/Collapse All, Toggle Floating, dan Label Node Panjang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-42
  - TC-AC-DS-43
  - TC-AC-DS-44
  - TC-AC-DS-557
  - TC-AC-DS-558
coverage:
  web: automated
---

# Sidebar Category: Pencarian Pohon, Expand/Collapse All, Toggle Floating, dan Label Node Panjang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25 dan SKU inti #29 serta seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data khusus Pre-setup #40 (hanya TC-558): Subcategory `Perangkat Pemindai Kode Batang Industri Berdaya Tahan Tinggi untuk Gudang Berat` (79 karakter) di bawah `Handheld Reader`, disiapkan lewat fixture BE pada langkah 33 dan dihapus oleh hook `after` lewat fixture BE yang disediakan tim BE/FE; seeding idempotent (dilewati bila sudah ada) dan cleanup hanya menghapus yang dibuat spec ini.
- State yang diubah spec: status panel Sidebar Category (tersimpan per user per halaman) pada TC-44 dan TC-557; spec memulihkannya ke terbuka pada langkah 19 dan 32.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`.

## Test Steps

### TC-AC-DS-43: Tombol Expand/Collapse All

1. Klik tombol Expand/Collapse All pada Sidebar Category
2. Verifikasi semua node induk terbuka dan anak node tampil
3. Klik tombol Expand/Collapse All lagi
4. Verifikasi semua node induk tertutup

### TC-AC-DS-42: Pencarian pohon dijalankan dengan Enter

5. Klik tombol Expand/Collapse All pada Sidebar Category
6. Ketik `Portal` pada input pencarian Sidebar tanpa menekan Enter
7. Verifikasi pohon belum tersaring, node `Asset TAG` dan `Tunnel Reader` masih tampil
8. Tekan Enter pada input pencarian Sidebar
9. Verifikasi pohon menampilkan `Portal Reader` beserta parent `Smart Fixed Reader` dan `Hardware`
10. Verifikasi node yang tidak cocok (`Asset TAG`, `Tunnel Reader`) disembunyikan
11. Kosongkan input pencarian Sidebar lalu tekan Enter
12. Verifikasi seluruh pohon tampil kembali

### TC-AC-DS-44: Floating toggle dan status tersimpan

13. Klik tab mengambang Collapse di tepi kiri panel
14. Verifikasi panel Sidebar Category tertutup
15. Verifikasi konten tabel melebar penuh
16. Verifikasi tab mengambang berada di tepi kanan layar
17. Muat ulang halaman `Settings > Device > Device SKU`
18. Verifikasi panel Sidebar Category tetap tertutup
19. Klik tab mengambang Open
20. Verifikasi panel Sidebar Category terbuka kembali

### TC-AC-DS-557: Tooltip dan aria-label tombol floating

21. Hover tab mengambang di tepi kiri panel
22. Verifikasi tooltip `Collapse Category Tree` tampil saat hover
23. Pindahkan fokus keyboard dengan Tab ke tab mengambang itu
24. Verifikasi tooltip `Collapse Category Tree` tampil saat fokus keyboard
25. Verifikasi atribut aria-label tab mengambang bernilai `Collapse Category Tree`
26. Klik tab mengambang
27. Hover tab mengambang di tepi kanan layar
28. Verifikasi tooltip `Open Category Tree` tampil saat hover
29. Pindahkan fokus keyboard dengan Tab ke tab mengambang itu
30. Verifikasi tooltip `Open Category Tree` tampil saat fokus keyboard
31. Verifikasi atribut aria-label tab mengambang bernilai `Open Category Tree`
32. Klik tab mengambang untuk membuka panel

### TC-AC-DS-558: Label node panjang

33. Siapkan Subcategory Pre-setup #40 lewat fixture BE hingga Subcategory tersimpan
34. Muat ulang halaman `Settings > Device > Device SKU`
35. Klik tombol Expand/Collapse All pada Sidebar Category
36. Verifikasi label node `Perangkat Pemindai Kode Batang Industri Berdaya Tahan Tinggi untuk Gudang Berat` terpotong dan ter-render rapi
37. Verifikasi panel Sidebar tidak melebar melebihi w-64 (256px)
38. Hover node `Perangkat Pemindai Kode Batang Industri Berdaya Tahan Tinggi untuk Gudang Berat`
39. Verifikasi tooltip nama lengkap `Perangkat Pemindai Kode Batang Industri Berdaya Tahan Tinggi untuk Gudang Berat` tampil saat hover
40. Pindahkan fokus keyboard dengan Tab ke node itu
41. Verifikasi tooltip nama lengkap `Perangkat Pemindai Kode Batang Industri Berdaya Tahan Tinggi untuk Gudang Berat` tampil saat fokus keyboard

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-43, TC-42, TC-44, TC-557, TC-558. TC-43 diletakkan pertama karena TC itu menguji klik pertama membuka semua node dari keadaan awal pohon (S-10); TC-558 diletakkan terakhir karena membutuhkan seeding data khusus #40.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3, 5, 6, 8, 11 (aksi pohon yang hasilnya diasersi pada langkah berikutnya; langkah 5 membuka semua node agar node `Asset TAG` dan `Tunnel Reader` terlihat), 13, 17, 19 (aksi toggle dan muat ulang), 21, 23, 26, 27, 29, 32 (hover, fokus, dan klik toggle; langkah 32 memulihkan panel terbuka, S-09), 33 sampai 35, 38, 40.
- TC-558 Expected b: tooltip hanya diasersi untuk label yang terpotong (langkah 39 dan 41).
- Spec melewati sekitar 35 langkah (41 langkah). Alasan pertahanan: seluruh blok menguji perilaku panel Sidebar Category yang sama dalam satu kelas (screening perilaku Sidebar, tanpa mengubah data SKU); satu seeding Subcategory khusus dipakai TC-558 di akhir; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25 dan #40 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan). Seeding #40 memakai nama literal (idempotent, serial) sampai ada keputusan.
  - Fixture rancangan: ketersediaan Pre-setup #25 dan #40 di environment belum diverifikasi.
  - TC-44 Expected a menyebut "setelah langkah 1 panel tertutup" padahal klik tab ada pada langkah 2 TC; spec mengasersi setelah klik tab.
  - TC-42, TC-43, dan TC-558 tidak menyebut keadaan awal pohon (terbuka atau tertutup) pada halaman yang baru dibuka; spec memakai klik Expand/Collapse All pertama yang membuka semua node (TC-43).
  - TC-557 tidak merinci cara membaca atribut aria-label; cara pembacaan disediakan tim FE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
