---
id: TC-GS-FILEMGR-E2E-035-sort-tabel-utama
title: "Sort Tabel Utama: Siklus 3 Tahap, Nama Lengkap, Nilai Byte, Perpindahan Kolom, dan Tie-Breaker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-143
  - TC-GS-FILEMGR-144
  - TC-GS-FILEMGR-145
  - TC-GS-FILEMGR-146
  - TC-GS-FILEMGR-147
  - TC-GS-FILEMGR-148
coverage:
  web: automated
---

# Sort Tabel Utama: Siklus 3 Tahap, Nama Lengkap, Nilai Byte, Perpindahan Kolom, dan Tie-Breaker

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data File Manager.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Tabel A2): 33 file aktif (F01 `budi-avatar.jpg` s.d. F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, F09-F33 `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), 4 halaman pada ukuran halaman 10, format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2 (tanpa sisa file, Recycle Bin, atau Changelog dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris dalam spec ini mengasumsikan dataset Tabel A2 segar tanpa sisa dari spec lain.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Data uji: File Name, File Format, User Name (`Dewi Kartika` F04 dan `Dewi Kusuma` F09, tampil sama `Dewi K`), Uploaded By (`Sinta Maharani` F05 dan `System` F02), Size (F04 `1.0 KB`, `staff-photo-01.jpg` `200.0 KB`, F01 `2.4 MB`, F08 `3.0 MB`, F06 `1.5 GB`), Upload Date (`staff-photo-01.jpg` `01/07/26` s.d. `budi-avatar.jpg` `02/09/26`); kata kunci Search `photo`; Uploaded By `System`.
- Kemampuan teknis: membaca ID file hasil seeding (nilai tie-breaker sort pada TC-GS-FILEMGR-143, 148) lewat fixture BE (disediakan tim FE/BE; ID file tidak tampil di UI dan tidak tercantum di Tabel A2); membaca indikator panah sort header kolom; membaca info pagination.
- Cleanup: hook `after` menghapus indikator sort, mengosongkan Search dan Filter, dan mengembalikan halaman 1 (preferensi UI).

## Test Steps

### TC-GS-FILEMGR-143: Siklus sort 3 tahap kolom teks File Name dan File Format

1. Klik header File Name sekali
2. Verifikasi urutan Ascending baris pertama sampai keenam: `alex-photo.jpeg`, `big-banner.png`, `budi-avatar.jpg`, `dewi-kartika.jpg`, `maya-wijaya.jpg`, `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg` (tidak membedakan huruf besar-kecil)
3. Klik header File Name lagi
4. Verifikasi baris pertama `staff-photo-25.jpg` (Descending)
5. Klik header File Name sekali lagi
6. Verifikasi indikator sort File Name hilang
7. Verifikasi urutan kembali default Upload Date terbaru (`budi-avatar.jpg` pertama)
8. Klik header File Format sekali
9. Verifikasi baris pertama `alex-photo.jpeg` (JPEG) dan baris kedua adalah baris JPG dengan ID file terkecil (tie-break ID searah sort, bukan Upload Date)
10. Klik header File Format lagi
11. Verifikasi tiga baris pertama berurutan `siti-profile.png`, `rudi-hartono.png`, `big-banner.png` (PNG; tie-break ID searah sort Descending: ID terbesar lebih dulu)
12. Klik header File Format sekali lagi (indikator sort hilang)

### TC-GS-FILEMGR-144: Siklus sort User Name dan Uploaded By berdasarkan nama lengkap

13. Klik header User Name sekali
14. Verifikasi `dewi-kartika.jpg` berada di atas `staff-photo-01.jpg` (`Dewi Kartika` sebelum `Dewi Kusuma` menurut nama lengkap walau tampilan sama `Dewi K`)
15. Klik header User Name lagi
16. Verifikasi `staff-photo-01.jpg` berada di atas `dewi-kartika.jpg`
17. Klik header User Name sekali lagi
18. Verifikasi indikator sort User Name hilang
19. Verifikasi urutan kembali default
20. Klik header Uploaded By sekali
21. Verifikasi `rudi-hartono.png` (`Sinta Maharani`) berada di atas `siti-profile.png` (`System`)
22. Klik header Uploaded By lagi
23. Verifikasi `siti-profile.png` berada di atas `rudi-hartono.png`
24. Klik header Uploaded By sekali lagi (indikator sort hilang)

### TC-GS-FILEMGR-145: Siklus sort kolom Size berdasarkan nilai byte

25. Klik header Size sekali
26. Verifikasi `dewi-kartika.jpg` (`1.0 KB`) pertama dan `staff-photo-01.jpg` (`200.0 KB`) kedua (Ascending)
27. Klik header Size lagi
28. Verifikasi berurutan `big-banner.png` (`1.5 GB`), `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg` (`3.0 MB`), `budi-avatar.jpg` (`2.4 MB`) (Descending menurut nilai byte, bukan teks `1.5 GB` dan `3.0 MB`)
29. Klik header Size sekali lagi
30. Verifikasi indikator sort Size hilang
31. Verifikasi urutan kembali default

### TC-GS-FILEMGR-146: Siklus sort kolom Upload Date

32. Klik header Upload Date sekali
33. Verifikasi baris pertama `staff-photo-01.jpg` (Oldest First)
34. Klik header Upload Date lagi
35. Verifikasi baris pertama `budi-avatar.jpg` (Newest First)
36. Klik header Upload Date sekali lagi
37. Verifikasi indikator sort Upload Date hilang
38. Verifikasi urutan kembali default Newest First

### TC-GS-FILEMGR-147: Berpindah kolom sort mereset kolom sebelumnya dan mempertahankan Search dan Filter

39. Ketik Search `photo`, tekan Enter
40. Klik ikon Filter di toolbar
41. Pilih `System` pada `Uploaded By`
42. Klik `[Apply]`
43. Klik header File Name sekali
44. Klik header Size sekali
45. Verifikasi kolom File Name netral (tanpa panah)
46. Verifikasi Size Ascending aktif
47. Verifikasi kata kunci `photo` tetap aktif di Search
48. Verifikasi filter Uploaded By `System` tetap aktif
49. Verifikasi tabel memuat 25 baris `staff-photo-` terurut Size Ascending
50. Klik `[Clear Field]`
51. Klik `[Apply]`
52. Klik ikon Filter untuk menutup panel
53. Klik `(←)` pada kotak Search

### TC-GS-FILEMGR-148: Urutan baris dengan nilai sort sama deterministik antar halaman

54. Klik header File Format sekali
55. Catat nama file seluruh baris halaman 1, 2, 3, dan 4
56. Verifikasi seluruh 33 baris muncul tepat satu kali di empat halaman (tidak ada baris ganda atau terlewat)
57. Verifikasi baris berformat JPG berurutan ID file searah sort (Ascending: ID terkecil lebih dulu), bukan menurut Upload Date
58. Klik header File Format lagi
59. Klik header File Format sekali lagi (indikator sort hilang)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC mengikuti sumber (143, 144, 145, 146, 147, 148).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 dan langkah 24 (klik ketiga yang menghapus indikator sort sebelum TC berikutnya; TC sumber menutup siklus 3 tahap pada TC-GS-FILEMGR-145 dan 146 sendiri), langkah 50 (pemulihan Filter dan Search), serta langkah 58 (pemulihan indikator sort; hook `after` menjadi cadangan). Indikator sort Size dari TC-GS-FILEMGR-147 hilang karena klik header File Format pada TC-GS-FILEMGR-148 mereset kolom sebelumnya (perilaku yang diasersi TC-GS-FILEMGR-147). Langkah "Catat nama file seluruh baris halaman 1, 2, 3, dan 4" adalah aksi baca (pindah halaman berurutan) dan menjadi dasar `Verifikasi` sesudahnya.
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 59 langkah): enam TC memakai header kolom tabel utama yang sama pada dataset Tabel A2, hanya membaca, satu akun, satu topik (Sort); tiap TC mengakhiri siklus dengan klik ketiga sehingga urutan awal TC berikutnya default dan tidak bergantung pada hasil asersi sebelumnya.
- Temuan untuk QA:
  - TC-GS-FILEMGR-143 butir d dan e, TC-GS-FILEMGR-148 butir b: tie-breaker memakai ID file yang tidak tampil di UI dan tidak ditentukan di Tabel A2. Bila ID mengikuti urutan seeding atau Upload Date, "ID searah sort" dan "Upload Date" tidak terbedakan; butir e (PNG Descending: `siti-profile.png`, `rudi-hartono.png`, `big-banner.png`) menyiratkan ID terbesar = Upload Date terbaru, sehingga ID terkecil JPG = `staff-photo-01.jpg`. Spec membaca ID dari fixture BE dan mengasersi urutan menurut ID tanpa menyebut baris JPG pertama; perlu konfirmasi QA tentang ID seeding.
  - TC-GS-FILEMGR-144: posisi baris pada Descending dan pada Uploaded By dapat berada di halaman berbeda (dataset 33 baris, ukuran halaman 10); spec mengasersi urutan relatif kedua baris, dibaca lintas halaman bila perlu.
  - TC-GS-FILEMGR-147: TC tidak menyebut urutan baris selain Size Ascending; spec mengasersi 25 baris `staff-photo-` terurut Size Ascending (`staff-photo-01.jpg` pertama).
  - Seeding Tabel A2 dan reset dataset antar spec tidak punya mekanisme tertulis di TC (lihat spec 031).
