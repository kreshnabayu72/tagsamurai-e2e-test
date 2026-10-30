---
id: TC-GS-POS-E2E-028-search-tabel-utama
title: "Search Tabel Utama Position: Siklus Interaksi, Substring, Case-insensitive, Trim, Hasil Kosong, Scope Kolom, dan Visibilitas Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-152
  - TC-GS-POS-153
  - TC-GS-POS-154
  - TC-GS-POS-155
  - TC-GS-POS-156
  - TC-GS-POS-157
  - TC-GS-POS-158
coverage:
  web: automated
---

# Search Tabel Utama Position: Siklus Interaksi, Substring, Case-insensitive, Trim, Hasil Kosong, Scope Kolom, dan Visibilitas Name

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record).
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.searchSeed028`): 13 Position `HR Business Partner {runId}-028`, `IT Support Specialist {runId}-028`, `Temporary Staff {runId}-028`, `iOS Developer {runId}-028`, `Legal Counsel {runId}-028`, `Marketing Executive {runId}-028`, `Quality Assurance Analyst {runId}-028`, `Data Engineer {runId}-028`, `Office Administrator {runId}-028`, `Logistics Coordinator {runId}-028`, `Payroll Specialist {runId}-028`, `Security Officer {runId}-028`, dan `Training Coordinator {runId}-028` (Data Dinamis No. 1-13). Dengan 7 record Pre-setup, jumlah baris tabel N = 20. N diturunkan dari seeding (7 Pre-setup + 13 Data Dinamis) dan ditulis di sini, tidak dibaca dari tabel; total Position di environment tepat 20 saat spec berjalan karena suite berjalan serial (`suite.md`) dan Position seed spec lain sudah dibersihkan hook `after` spec itu.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-028` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: salin dan tempel teks (clipboard browser) untuk TC-GS-POS-157; pembacaan fokus input, nilai input Search (termasuk spasi di depan dan belakang), dan visibilitas kolom.
- State global: ukuran halaman tabel diubah ke 25 (langkah 1) dan dikembalikan ke 10 (langkah 58); visibilitas kolom Name disembunyikan lalu ditampilkan kembali oleh TC-GS-POS-158 (langkah 48 dan 54), dan hook `after` cadangan memulihkan Setup Column ke bawaan.

## Test Steps

### TC-GS-POS-152: Siklus interaksi Search toolbar tabel utama

1. Ubah ukuran halaman tabel ke 25
2. Hover ikon Search
3. Verifikasi tooltip "Search"
4. Klik ikon Search
5. Verifikasi input Search melebar
6. Verifikasi input Search langsung fokus
7. Verifikasi placeholder input "Search position name..."
8. Ketik `Manager` (belum Enter)
9. Verifikasi icon `✕` muncul di dalam input
10. Verifikasi tabel belum tersaring (masih 20 baris)
11. Tekan Enter
12. Verifikasi baris `IT Manager` tampil di tabel
13. Verifikasi tabel hanya menampilkan Name yang mengandung `Manager`
14. Klik icon `✕` di dalam input
15. Verifikasi teks input kosong
16. Verifikasi input tetap terbuka
17. Verifikasi input Search fokus
18. Verifikasi tabel tetap menampilkan hasil `Manager`
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan seluruh data (20 baris)
21. Ketik `Manager`, tekan Enter
22. Klik icon `←`
23. Verifikasi input Search tertutup
24. Verifikasi tabel langsung kembali menampilkan seluruh data (20 baris)
25. Klik ikon Search
26. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-POS-153: Search Name, potongan kata (substring)

27. Ketik Search `Coord`, tekan Enter
28. Verifikasi hanya baris `Logistics Coordinator {runId}-028`, `Sales Coordinator`, dan `Training Coordinator {runId}-028` yang tampil
29. Klik icon `←`

### TC-GS-POS-154: Search Name, tidak case-sensitive

30. Ketik Search `LEGAL COUNSEL`, tekan Enter
31. Verifikasi baris `Legal Counsel {runId}-028` tampil
32. Klik icon `←`

### TC-GS-POS-155: Search, spasi depan/belakang keyword diabaikan

33. Ketik Search `  Legal Counsel  `, tekan Enter
34. Verifikasi baris `Legal Counsel {runId}-028` tampil (hasil sama dengan keyword tanpa spasi)
35. Verifikasi isi search box tetap tampil seperti diketik (`  Legal Counsel  `)
36. Klik icon `←`

### TC-GS-POS-156: Search tanpa hasil menampilkan empty state hasil pencarian

37. Ketik Search `Astronaut`, tekan Enter
38. Verifikasi Illustration tampil
39. Verifikasi Title "No results found"
40. Verifikasi Description "Try adjusting your search or filter."
41. Klik icon `←`

### TC-GS-POS-157: Search tidak mencari kolom Last Updated

42. Salin teks tanggal persis dari sel Last Updated salah satu baris
43. Tempel teks tanggal itu pada Search, tekan Enter
44. Verifikasi Illustration tampil
45. Verifikasi Title "No results found"
46. Verifikasi Description "Try adjusting your search or filter."
47. Klik icon `←`

### TC-GS-POS-158: Search terikat visibilitas kolom Name

48. Buka Popup Setup Column, sembunyikan kolom Name, klik `[Save]`
49. Verifikasi kontrol Search tetap tampil
50. Ketik Search `Legal`, tekan Enter
51. Verifikasi Illustration tampil
52. Verifikasi Title "No results found"
53. Verifikasi Description "Try adjusting your search or filter."
54. Buka Popup Setup Column, tampilkan kembali kolom Name, klik `[Save]`
55. Ganti isi kotak search dengan `Legal`, tekan Enter
56. Verifikasi baris `Legal Counsel {runId}-028` tampil
57. Klik icon `←`
58. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti urutan TC sumber. TC-GS-POS-158 mengubah visibilitas kolom (Setup Column) sehingga ditaruh paling akhir; seluruh TC lain hanya membaca dan tidak mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 25 agar seluruh N = 20 baris tampil pada satu halaman sehingga "seluruh data" dapat diasersi), langkah 29, 32, 36, 41, 47, dan 57 (`←` menutup input dan mengosongkan keyword sebelum TC berikutnya), langkah 42 (menyalin teks tanggal), serta langkah 58 (mengembalikan ukuran halaman ke 10).
- Langkah 25 dan 26 (membuka kembali input Search dan memverifikasi kosong) berasal dari Expected f TC-GS-POS-152 ("mengosongkan keyword"). Search pada TC-GS-POS-153 sampai 158 ditulis atomik ("Ketik Search `X`, tekan Enter") sesuai bagian 8b butir 9 konvensi; klik ikon Search eksplisit hanya pada siklus TC-GS-POS-152 (langkah 4 dan 25).
- Langkah 55 mengganti isi kotak search dengan `Legal` lalu Enter (langkah 4 TC-GS-POS-158, "Ketik `Legal` + Enter lagi"), sehingga hasil Search tidak bergantung pada isi kotak yang tersisa dari langkah 50.
- Langkah 12 (baris `IT Manager` tampil) adalah anchor positif tambahan di luar Expected TC supaya asersi "hanya Name yang mengandung `Manager`" pada langkah 13 tidak lolos pada tabel kosong.
- Pembagian TC lintas spec: Filter Last Updated tabel utama (TC-GS-POS-159 sampai 164) ada di spec 029; kombinasi Search, Filter, Sort, dan Pagination di spec 030; Setup Column tabel utama di spec 032.
- Spec memuat 58 langkah (di atas smell sekitar 35 langkah). Seluruhnya satu kelas harness (Search tabel utama), satu akun, satu dataset; tiap blok TC memulai dari state Search tertutup dan tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - TC-GS-POS-152 langkah 1 sampai 6 tidak menyebut jumlah baris awal dan ukuran halaman; spec memakai N = 20 dari seeding dan ukuran halaman 25 agar "seluruh data" teramati pada satu halaman.
  - TC-GS-POS-157 tidak menyebut format teks Last Updated yang disalin; spec menyalin teks sel apa adanya.
  - TC-GS-POS-158 langkah 4 ("Ketik `Legal` + Enter lagi") tidak menyebut apakah kotak Search masih terbuka dan berisi sesudah `[Save]` Setup Column; spec mengganti isi kotak (langkah 55).
  - Nama Data Dinamis No. 4-13 pada TC sumber (`iOS Developer` ... `Training Coordinator`) dan No. 1-3 diberi suffix `{runId}-028`; Expected TC yang menyebut nama tanpa suffix (`Legal Counsel`, `Logistics Coordinator`, `Training Coordinator`) diasersi pada nama bersuffix.
