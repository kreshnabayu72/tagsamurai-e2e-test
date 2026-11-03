---
id: TC-AC-ACAL-E2E-039-download-nama-berkas-header-cakupan-baris-filter-dan-kolom-hidden
title: "Download: Nama Berkas, Header, Cakupan Baris, Mengikuti Filter, Kolom Hidden, dan Hasil Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-121
  - TC-AC-ACAL-122
  - TC-AC-ACAL-123
  - TC-AC-ACAL-124
  - TC-AC-ACAL-125
  - TC-AC-ACAL-126
  - TC-AC-ACAL-128
coverage:
  web: automated
---

# Download: Nama Berkas, Header, Cakupan Baris, Mengikuti Filter, Kolom Hidden, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas log-terbatas khusus spec ini (`Fixture.activityLog.akunLog039`, disediakan tim FE; email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), kredensial `Spectra.env.AC_LIMITLOG_TC_PASSWORD` (nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Entitas ini dipakai hanya oleh spec ini karena TC-AC-ACAL-122 dan TC-AC-ACAL-124 mengasersi seluruh baris pada log append-only (jumlah dibaca dari footer sebagai Z, bukan angka mutlak); entitas segar disediakan tim FE/BE sebelum run. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook `before`/`after` spec ini menyetel dan memulihkan flag seen untuk akun `akunLog039` dan halaman Admin Console > Activity Log (kemampuan disediakan tim FE/BE).
- Data Dinamis (bersuffix `{runId}-039`), disediakan lewat seed BE di entitas `akunLog039` (mekanisme seeding log tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE):
  - Tab Session: 35 entri Session dalam scope sesuai TC (seeding; Z dibaca dari footer `Showing X–Y of Z entries` tab Session sebelum Download pada langkah 7, termasuk baris sesi akun aktor hook `before`; bagian 8b butir 10), sehingga Z lebih dari 10 (page size default 10) agar asersi "seluruh baris, bukan satu halaman" bermakna (TC-AC-ACAL-122 dan TC-AC-ACAL-124).
    - Entri Session yang di-seed memuat sedikitnya dua nilai Date yang berbeda, supaya asersi urutan Date terbaru di atas pada langkah 14 bermakna.
  - Tab User Action, empat entri (TC-AC-ACAL-125):
    - A1 Name `Mitra Zeta {runId}-039`, Object `Partner`, Action `Suspend`.
    - A2 Name `Mitra Alfa {runId}-039`, Object `Partner`, Action `Suspend`.
    - A3 Name `Mitra Gamma {runId}-039`, Object `Partner`, Action `Create` (cocok Search `Partner`, tidak cocok Filter Action `Suspend`).
    - A4 Name `Klien Suspend {runId}-039`, Object `Client`, Action `Suspend` (cocok Filter Action `Suspend`, tidak cocok Search `Partner`: tidak ada kolom Searchable lain yang memuat `Partner`).
  - Tab User Action: sedikitnya satu entri lain sehingga tabel tidak kosong pada TC-AC-ACAL-123.
- Kemampuan teknis (disediakan tim FE/BE):
  - Menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama sheet, baris header, jumlah dan urutan baris data). Nama berkas, nama kolom (header), dan jumlah baris adalah asersi fungsional (bagian 3 prinsip 13f). Berkas unduhan dihapus di hook `after`.
  - Mengamati ada atau tidaknya dialog, toast, dan peringatan segera setelah klik pilihan format.
- State global yang diubah dan dipulihkan: visibilitas dan urutan kolom Setup Column tab Session (dipulihkan di langkah 43 dan 49; hook `after` suite menghapus preferensi kolom sebagai cadangan); Search, Filter, dan Sort tab Session dan tab User Action (dibersihkan di langkah 22 dan 36). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-121: Overlay Download kedua tab

1. Klik icon Download di tab Session
2. Verifikasi overlay `Download as CSV` / `Download as XLSX` tampil di tab Session
3. Tekan Esc untuk menutup overlay
4. Klik tab "User Action", klik icon Download
5. Verifikasi overlay `Download as CSV` / `Download as XLSX` tampil di tab User Action
6. Tekan Esc untuk menutup overlay

### TC-AC-ACAL-122 dan TC-AC-ACAL-124: Download CSV tab Session, nama berkas, tanpa toast sukses, dan seluruh baris

7. Klik tab "Session", lalu baca Z dari footer (`Showing X–Y of Z entries`) sebagai jumlah entri sebelum Download
8. Klik icon Download, lalu klik `Download as CSV`
9. Verifikasi tidak ada dialog konfirmasi
10. Verifikasi tidak ada toast sukses
11. Verifikasi berkas `Activity-Log-Session.csv` terunduh langsung
12. Buka isi berkas yang terunduh
13. Verifikasi jumlah baris data berkas sama dengan Z dari footer (seluruh baris, bukan satu halaman berisi 10 baris)
14. Verifikasi baris data berkas terurut Date terbaru di atas (descending)

### TC-AC-ACAL-128: Download dengan hasil kosong

15. Ketik Search `zzz`, tekan Enter
16. Verifikasi `"No results found"` tampil di tab Session
17. Klik icon Download, lalu klik `Download as CSV`
18. Verifikasi tidak ada toast error
19. Verifikasi berkas `Activity-Log-Session.csv` terunduh
20. Buka isi berkas yang terunduh
21. Verifikasi berkas hanya berisi baris header (tanpa baris data)
22. Klik `(←)` pada kotak Search

### TC-AC-ACAL-123: Download XLSX tab User Action, nama berkas, nama sheet, dan header

23. Klik tab "User Action", klik icon Download, lalu klik `Download as XLSX`
24. Verifikasi tidak ada toast sukses
25. Verifikasi berkas `Activity-Log-User-Action.xlsx` terunduh
26. Buka isi berkas yang terunduh
27. Verifikasi nama sheet berkas `Activity-Log-User-Action`
28. Verifikasi baris header berkas berisi nama kolom data seperti di tabel tab User Action dengan urutan yang sama

### TC-AC-ACAL-125: Download mengikuti Search, Filter, dan Sort

29. Ketik Search `Partner`, tekan Enter
30. Klik icon Filter, buka dropdown Action, centang `Suspend`, klik [Apply]
31. Klik icon sort pada header kolom Name sekali (ascending)
32. Verifikasi sedikitnya dua baris tampil di tabel tab User Action
33. Klik icon Download, klik `Download as XLSX`, lalu buka isi berkas yang terunduh
34. Verifikasi baris data berkas sama dengan baris yang tampil di tabel (Search `Partner` dan Filter Action `Suspend`)
35. Verifikasi baris data berkas terurut Name ascending
36. Klik icon sort pada header kolom Name hingga netral, klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

### TC-AC-ACAL-126: Download tidak menyertakan kolom hidden dan menyertakannya kembali setelah unhide

37. Klik tab "Session", klik `⋯` pada header kolom Actions, hilangkan centang kolom IP Address dan Device / Browser di overlay Column Visibility
38. Klik icon Download, lalu klik `Download as CSV`
39. Verifikasi tidak ada toast atau peringatan
40. Buka isi berkas yang terunduh
41. Verifikasi berkas memuat kolom Date
42. Verifikasi berkas tanpa kolom IP Address dan Device / Browser
43. Klik `⋯` pada header kolom Actions, centang kembali kolom IP Address dan Device / Browser di overlay Column Visibility
44. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
45. Verifikasi berkas kembali memuat kolom IP Address dan Device / Browser
46. Buka Popup Setup Column dari overlay Column Visibility, drag kolom Device / Browser ke posisi sebelum IP Address, lalu klik [Save]
47. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
48. Verifikasi urutan kolom berkas sama dengan urutan tampilan tabel (Device / Browser sebelum IP Address)
49. Buka Popup Setup Column dari overlay Column Visibility, klik [Reset to Default], lalu klik [Save]

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 121, 122 dan 124, 128, 123, 125, 126 (kasus yang mengubah Setup Column di akhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (49 langkah). Alasan: seluruh blok satu kelas harness (fungsional Download; nama berkas, header, dan jumlah baris adalah asersi fungsional menurut prinsip 13f), memakai satu dataset (entitas log-terbatas milik spec), dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna. Isi sel berkas (kelas f) ada di spec lain.
- TC-AC-ACAL-122 dan TC-AC-ACAL-124 berbagi satu unduhan CSV tab Session (langkah 8 sampai 14) karena Langkah Uji TC-AC-ACAL-124 ("Tab Session, Download > CSV") identik dengan TC-AC-ACAL-122 dan Precondition-nya sama (35 entri, page size 10).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 dan 6 (menutup overlay Download dengan Esc), langkah 7 (membaca Z dari footer sebelum Download; bagian 8b butir 10), langkah 12, 20, 26, 33, 40, 44, dan 47 (membuka isi berkas yang terunduh), langkah 22 dan 36 (pemulihan Search, Filter, dan Sort; S-09), langkah 43 dan 49 (pemulihan Setup Column; langkah 49 melaksanakan Post Condition TC-AC-ACAL-126 `[Reset to Default]` dan `[Save]` supaya tersimpan).
- Absence state sementara (bagian 8b butir 11 dan 5): dialog dan toast diasersi segera setelah pemicu (klik pilihan format) dan sebelum asersi berkas (langkah 9, 10, 18, 24, 39); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas (langkah 11, 19, 25, 41). Langkah 42 (tanpa kolom) memakai langkah 41 sebagai anchor positif berkas yang sama.
- Langkah 13 mengasersi jumlah baris data berkas sama dengan Z yang dibaca dari footer pada langkah 7 (bukan angka absolut audit trail hidup); entitas khusus spec menjamin hanya spec ini menambah baris.
- Asersi di luar Expected TC (S-03): langkah 16 (`"No results found"` tampil) adalah anchor positif untuk asersi berkas kosong (bagian 8b butir 2); langkah 32 (sedikitnya dua baris tampil) membuktikan Search `Partner` dan Filter Action `Suspend` menyisakan lebih dari satu baris sebelum Sort diasersi.
- Isi sel berkas: asersi nilai sel per baris adalah kelas f dan ada di spec 040. Spec ini terutama mengasersi nama berkas, nama sheet, header, jumlah baris, dan kolom yang ada; pengecualian: langkah 14 (urutan Date terbaru di atas), 34 (baris data berkas sama dengan baris tabel), dan 35 (urutan Name ascending) mengasersi isi sel berkas (nilai Date dan Name per baris) karena Expected TC-AC-ACAL-124 dan TC-AC-ACAL-125 mensyaratkan isi sel berkas.
- Temuan untuk QA:
  - Judul TC-AC-ACAL-121 menyebut "dan tooltip" tetapi Expected hanya overlay; tooltip `Download` (PRD §4.2) tidak diasersi karena tidak ada di Expected.
  - TC-AC-ACAL-121 tidak menyebut cara menutup overlay Download; spec memakai Esc sebagai langkah penghubung.
  - TC-AC-ACAL-122, 124, dan 128 menyebut entitas dan jumlah entri tanpa menyebut akun; akun entitas log-terbatas tidak ada di Pre-setup TC. Mekanisme seed entri log (35 entri Session, entri User Action untuk TC-AC-ACAL-125) tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-AC-ACAL-123 menulis "nama kolom seperti di tabel"; spec memakai kolom data tanpa kolom `Actions` (⋯), yang bukan kolom berisi data (PRD §4.1).
  - TC-AC-ACAL-125 tidak menyebut data yang dipakai; spec memakai A1 sampai A4 supaya Search, Filter, dan Sort sama-sama bermakna. Klik pertama ikon sort memberi ascending (PRD FI-09).
  - TC-AC-ACAL-126 langkah 3 menyebut "Popup Setup Column" tanpa menyebut kontrol pembukanya; spec membukanya dari overlay Column Visibility pada header `⋯`. Hide kolom di langkah 1 TC diasumsikan lewat overlay Column Visibility (TC-AC-ACAL-01).
  - Post Condition TC-AC-ACAL-126 (urutan kolom dikembalikan ke default) dijalankan sebagai langkah pemulihan 49; Post Condition lain bernilai `-` dan tidak diasersi.
  - Kolom Tipe TC-AC-ACAL-128 `Edge Case` tidak ada di legenda pemetaan konvensi; diperlakukan sebagai Edge, sedangkan `caseType` spec Positive mengikuti alur dominan.
