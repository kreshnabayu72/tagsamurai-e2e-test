---
id: TC-FA-CAT-E2E-137-tabel-assets-detail-navigasi-paginasi-dan-genuine-empty
title: "Tabel Assets Popup Detail: Navigasi Paginasi, Reset ke Halaman 1, dan Tabel Kosong (Genuine Empty)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-594
  - TC-FA-CAT-617
coverage:
  web: automated
---

# Tabel Assets Popup Detail: Navigasi Paginasi, Reset ke Halaman 1, dan Tabel Kosong (Genuine Empty)

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup CatMain #20 untuk TC-FA-CAT-617: `Monitor` di bawah `Electronics` (Code `ELEC-MN`, leaf, Total Asset 0) sehingga tabel Assets kosong; tidak ada kategori atau aset yang diubah.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- Kemampuan teknis: membaca isi berkas unduhan CSV (nama berkas, baris header, jumlah baris data); disediakan tim FE.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Verifikasi halaman 1 menampilkan 10 baris
4. Klik kontrol halaman berikutnya
5. Verifikasi halaman 2 memuat 2 aset sisa dari 12 aset (`Laptop HP - 3` dan `Laptop HP - 4` pada default sort Name A-Z)
6. Klik kontrol halaman sebelumnya
7. Verifikasi tabel kembali ke halaman 1 dengan 10 aset
8. Ketik halaman `2` pada input nomor halaman, tekan `Enter`
9. Verifikasi halaman 2 terbuka
10. Ketik halaman `0` pada input nomor halaman, tekan `Enter`
11. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2
12. Ketik halaman `99` pada input nomor halaman, tekan `Enter`
13. Verifikasi input `99` diabaikan dan tabel tetap di halaman 2
14. Ketik halaman `abc` pada input nomor halaman, tekan `Enter`
15. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2
16. Klik header kolom Name untuk mengganti sort
17. Verifikasi tabel tetap di halaman 2
18. Ganti jumlah baris per halaman menjadi 25
19. Verifikasi tabel kembali ke halaman 1
20. Verifikasi tabel menampilkan 12 aset pada satu halaman
21. Ganti jumlah baris per halaman menjadi 10
22. Klik header kolom Name hingga urutan kembali netral ke default Name A-Z
23. Klik kontrol halaman berikutnya
24. Ketik Search `Laptop`, tekan Enter
25. Verifikasi tabel mereset ke halaman 1
26. Klik `(←)` pada kotak Search
27. Klik kontrol halaman berikutnya
28. Klik icon Filter, pilih Name `Laptop Dell` dan `Laptop HP`, lalu klik `[Apply]`
29. Verifikasi tabel mereset ke halaman 1
30. Klik icon close (✕) pada Popup Detail

### TC-FA-CAT-617: Tabel Assets kosong (genuine empty)

31. Klik node `Electronics` di Sidebar Category Tree
32. Klik elipsis (⋯) pada baris `Monitor` > `Detail`
33. Verifikasi empty state `No assets assigned` dengan `No assets are currently assigned to this category.` tampil pada tabel Assets
34. Verifikasi toolbar Search, Filter, dan Download tetap tampil
35. Klik Download > `Download as CSV`
36. Verifikasi tidak ada toast
37. Verifikasi berkas `Category-Assets.csv` terunduh
38. Buka berkas `Category-Assets.csv`
39. Verifikasi berkas hanya berisi baris header kolom yang visible tanpa baris data
40. Klik icon Filter
41. Buka dropdown Status
42. Verifikasi dropdown Status menampilkan teks `No options available`

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah yang mengembalikan page size ke 10 dan Sort ke netral sesudah langkah 18, langkah `(←)` pada Search, dan langkah pindah ke halaman berikutnya sebelum Search dan Filter (kondisi awal "halaman 2" yang dibutuhkan asersi reset, S-14).
- Spec melewati sekitar 35 langkah (nominal 42). Alasan: dua blok kecil pada Popup Detail yang sama; blok TC-FA-CAT-594 memuat delapan langkah TC dengan lima butir Expected bermajemuk.
- Tanpa toast pada unduhan TC-FA-CAT-617 (langkah 36) diasersi segera setelah klik Download dan sebelum `Verifikasi` berkas terunduh (langkah 37); klik format menjadi anchor positif yang buktinya menyusul pada langkah 37 (bagian 8b butir 11 dan butir 5). Langkah menutup Popup Detail dan memilih node `Electronics` adalah langkah penghubung.
- Temuan untuk QA:
  - TC-FA-CAT-617 berlabel HINT `f` (binary buffer); isi berkas dibaca lewat kemampuan teknis di Prerequisites.
  - TC-FA-CAT-594 Expected a menyebut halaman 2 memuat `Laptop HP - 3` dan `Laptop HP - 4` pada default sort Name A-Z; spec hanya mengasersi jumlah (2 aset) dan dua nama itu sesuai TC.
  - TC-FA-CAT-594 langkah 8 memilih Filter Name `Laptop Dell` dan `Laptop HP` yang secara kumulatif menyisakan 12 aset sehingga halaman 2 tetap ada; reset ke halaman 1 diasersi sesuai Expected e.
