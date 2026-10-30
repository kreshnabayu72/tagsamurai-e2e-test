---
id: TC-GS-FILEMGR-E2E-031-search-tabel-utama
title: "Search Tabel Utama: Siklus Toolbar, Substring, Case-Insensitive, Size, Trim, dan Karakter Khusus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-13
  - TC-GS-FILEMGR-115
  - TC-GS-FILEMGR-116
  - TC-GS-FILEMGR-117
  - TC-GS-FILEMGR-119
  - TC-GS-FILEMGR-120
coverage:
  web: automated
---

# Search Tabel Utama: Siklus Toolbar, Substring, Case-Insensitive, Size, Trim, dan Karakter Khusus

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data File Manager.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Tabel A2): 33 file aktif (F01 `budi-avatar.jpg` s.d. F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, F09-F33 `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), 4 halaman pada ukuran halaman 10, format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2 (tanpa sisa file, Recycle Bin, atau Changelog dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris dalam spec ini mengasumsikan dataset Tabel A2 segar tanpa sisa dari spec lain.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Cleanup: hook `after` mengosongkan Search, Filter, dan Sort tabel utama, mengembalikan ukuran halaman 10, dan menampilkan semua kolom (preferensi UI, state per tab).
- Kemampuan teknis: membaca info pagination (total baris) tabel utama; mendeteksi dialog `alert` browser (untuk TC-GS-FILEMGR-120); seeding Tabel A2 lewat fixture BE.
- TC-GS-FILEMGR-13, 115, 116, 117, 119, 120: Tabel A2 (33 file aktif) tersedia; kata kunci Search di langkah (`avatar`, `BUDI`, `jpeg`, `alexander`, `sinta`, `zzzxyz`, `2.4 MB`, `GB`, ` avatar `, `   `, `%`, `_`, `<script>alert(1)</script>`, `zzzxyz-tidak-ada`).

## Test Steps

### TC-GS-FILEMGR-115: Siklus interaksi Search toolbar (screening)

1. Klik icon Search di toolbar
2. Verifikasi input Search melebar
3. Verifikasi fokus otomatis berada di input Search
4. Verifikasi placeholder input Search `Search file name, user name...`
5. Ketik `avatar` di input Search tanpa menekan Enter
6. Verifikasi ikon `(✕)` muncul pada input Search
7. Verifikasi tabel belum tersaring (info pagination menunjukkan 33 baris)
8. Tekan Enter
9. Verifikasi tabel hanya memuat satu baris `budi-avatar.jpg`
10. Klik ikon `(✕)` di input Search
11. Verifikasi input Search kosong
12. Verifikasi input Search tetap terbuka
13. Verifikasi tabel tetap menampilkan hasil `budi-avatar.jpg`
14. Tekan Enter pada input yang sudah kosong
15. Verifikasi tabel kembali menampilkan 33 baris
16. Ganti isi kotak search dengan `avatar`, tekan Enter
17. Klik ikon panah `(←)` di kiri input Search
18. Verifikasi input Search menutup
19. Verifikasi kata kunci Search dikosongkan
20. Verifikasi tabel langsung kembali ke 33 baris

### TC-GS-FILEMGR-13: Tampilan tabel utama saat Search tidak menemukan hasil

21. Ketik Search `zzzxyz-tidak-ada`, tekan Enter
22. Verifikasi ilustrasi tampil dengan judul `No results found`
23. Verifikasi deskripsi `Try adjusting your search or filter.`
24. Verifikasi tampilan ini adalah state hasil kosong terfilter dan bukan empty state `No files yet`
25. Klik `(←)` pada kotak Search

### TC-GS-FILEMGR-116: Search substring dan case-insensitive pada File Name, File Format, User Name, dan Uploaded By

26. Ketik Search `avatar`, tekan Enter
27. Verifikasi (File Name, `avatar`) tabel hanya memuat satu baris `budi-avatar.jpg`
28. Ganti isi kotak search dengan `BUDI`, tekan Enter
29. Verifikasi (File Name huruf besar, tidak membedakan huruf besar-kecil) tabel hanya memuat satu baris `budi-avatar.jpg`
30. Ganti isi kotak search dengan `jpeg`, tekan Enter
31. Verifikasi (File Format) tabel hanya memuat satu baris `alex-photo.jpeg`
32. Ganti isi kotak search dengan `alexander`, tekan Enter
33. Verifikasi (User Name `Alexander Graham Bell`) tabel hanya memuat satu baris `alex-photo.jpeg`
34. Ganti isi kotak search dengan `sinta`, tekan Enter
35. Verifikasi (Uploaded By `Sinta Maharani`) tabel hanya memuat satu baris `rudi-hartono.png`
36. Ganti isi kotak search dengan `zzzxyz`, tekan Enter
37. Verifikasi empty state `No results found` tampil
38. Verifikasi deskripsi `Try adjusting your search or filter.`

### TC-GS-FILEMGR-117: Search kolom Size mencocokkan nilai yang tampil

39. Klik `(←)` pada kotak Search
40. Ketik Search `2.4 MB`, tekan Enter
41. Verifikasi tabel hanya memuat satu baris `budi-avatar.jpg`
42. Klik `(←)` pada kotak Search
43. Ketik Search `GB`, tekan Enter
44. Verifikasi tabel hanya memuat satu baris `big-banner.png`

### TC-GS-FILEMGR-119: Kata kunci Search di-trim dan kata kunci hanya spasi dianggap kosong

45. Ganti isi kotak search dengan ` avatar ` (spasi di awal dan akhir), tekan Enter
46. Verifikasi hasil sama dengan `avatar`: tabel hanya memuat satu baris `budi-avatar.jpg`
47. Verifikasi isi input Search tetap ` avatar `
48. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
49. Verifikasi kata kunci hanya spasi diperlakukan kosong: tabel kembali menampilkan 33 baris

### TC-GS-FILEMGR-120: Karakter khusus dicocokkan sebagai teks biasa pada Search

50. Ganti isi kotak search dengan `%`, tekan Enter
51. Verifikasi empty state `No results found` tampil (bukan seluruh baris)
52. Ganti isi kotak search dengan `_`, tekan Enter
53. Verifikasi empty state `No results found` tampil
54. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
55. Verifikasi empty state `No results found` tampil
56. Verifikasi tidak ada skrip yang berjalan (tidak ada dialog `alert` browser)
57. Verifikasi teks kata kunci `<script>alert(1)</script>` tampil apa adanya di input Search
58. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-FILEMGR-115 (siklus input, screening) pertama, lalu TC-GS-FILEMGR-13 (state hasil kosong), lalu TC-GS-FILEMGR-116, 117, 119, 120. TC-GS-FILEMGR-13 ditaruh sesudah 115 (urutan sumber 13, 115, 116, 117, 119, 120 dengan 115 didahulukan sebagai screening siklus, prinsip 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 39 (mengosongkan Search sebelum TC-GS-FILEMGR-117; TC sumber menulis "Kosongkan Search lalu cari", ditulis sebagai klik `(←)`) dan langkah 58 (mereset Search di akhir spec; hook `after` menjadi cadangan). Langkah "ganti isi kotak search dengan `X`, tekan Enter" memakai kotak Search yang sudah terbuka dari langkah sebelumnya.
- P-5: TC-GS-FILEMGR-120 (Security, kata kunci `<script>alert(1)</script>`) adalah satu TC objek-uji ringan kelas a tanpa harness eksternal dan tanpa state berat; ia berada di spec fungsional Search yang permukaannya sama (satu TC kelas a, di bawah batas dua TC per spec).
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 58 langkah): semua blok membaca tabel utama yang sama (Tabel A2) tanpa mengubah data, topik tunggal (Search), akun satu; tiap blok diakhiri dengan Search dikosongkan sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya, dan kegagalan satu asersi hasil Search tidak membuat blok lain kehilangan makna (soft assertion). Kegagalan keras pada langkah membuka input Search pada TC-GS-FILEMGR-115 menghentikan blok sesudahnya; risiko ini diterima karena input Search yang sama dipakai semua blok.
- Temuan untuk QA:
  - Seeding Tabel A2 (33 file aktif), dan reset Recycle Bin dan Changelog ke Tabel A3 dan A4 antar spec (Changelog tidak dapat dibersihkan lewat UI), tidak punya mekanisme yang tertulis di TC; ditulis sebagai kemampuan fixture BE "disediakan tim FE/BE" tanpa endpoint karangan (S-13).
  - TC-GS-FILEMGR-120: TC tidak menyebut cara memeriksa "tidak ada skrip berjalan"; spec mengasersi tidak ada dialog `alert` browser.
  - TC-GS-FILEMGR-117 langkah 2 dan TC-GS-FILEMGR-13 tidak mendefinisikan cara "Kosongkan Search"; ditulis klik `(←)` (butir 9 bagian 8b).
  - Jumlah baris `33` pada TC-GS-FILEMGR-115 sampai 119 mengasumsikan tidak ada baris tambahan D05, D06, atau D08 (Tabel Data Uji Dinamis) dari spec lain.
