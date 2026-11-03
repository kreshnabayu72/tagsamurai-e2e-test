---
id: TC-AC-ACHA-E2E-043-download-fungsional
title: "Download Fungsional pada List Device Allocation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-357
  - TC-AC-ACHA-358
  - TC-AC-ACHA-359
  - TC-AC-ACHA-362
  - TC-AC-ACHA-363
coverage:
  web: automated
---

# Download Fungsional pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (nama env tercantum di daftar env var `suite.md`, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-11: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Kemampuan teknis (disediakan tim FE): browser mengunduh berkas ke folder uji yang dikosongkan sebelum tiap unduhan; membuka berkas unduhan CSV dan XLSX untuk membaca nama berkas, baris header, jumlah baris, dan isi sel. Nama berkas unduhan `Device-Allocation.csv` dan `Device-Allocation.xlsx`.
- State yang diubah: Search, Filter, Sort, dan visibilitas kolom Client dikembalikan ke default di akhir tiap TC terkait.
- Preferensi kolom tabel (Setup Column) tersimpan di browser; hook `after` suite menghapusnya (kemampuan disediakan tim FE, didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-357: Download mengekspor seluruh baris, bukan satu halaman

1. Klik ikon Download
2. Verifikasi overlay menawarkan `Download as CSV` dan `Download as XLSX`
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas `Device-Allocation.csv` terunduh
6. Buka berkas CSV
7. Verifikasi berkas memuat seluruh 30 baris data (bukan hanya halaman aktif)
8. Verifikasi berkas memuat sembilan kolom yang sedang tampil: Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated
9. Verifikasi kolom Allocated By ditulis `[First Name] [Last Initial]` sama dengan tampilan tabel (mis. `Andi W`)

### TC-AC-ACHA-358: Download mengikuti Search dan Filter aktif

10. Ketik Search `Budi`, tekan Enter
11. Klik ikon Filter
12. Pilih Status `Completed`, klik `[Apply]`
13. Tutup Filter Panel (klik ikon Filter)
14. Klik ikon Download
15. Klik `Download as XLSX`
16. Verifikasi berkas `Device-Allocation.xlsx` terunduh
17. Buka berkas XLSX
18. Verifikasi berkas hanya memuat 3 baris yang cocok dengan Search `Budi` dan Filter Status `Completed`
19. Klik `(←)` pada kotak Search
20. Klik ikon Filter
21. Klik `[Clear Field]`, klik `[Apply]`
22. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-359: Kolom tersembunyi tidak ikut diekspor

23. Klik ikon `⋯` pada header kolom terakhir
24. Hilangkan centang kolom Client di overlay Column Visibility
25. Tutup overlay Column Visibility
26. Klik ikon Download
27. Klik `Download as CSV`
28. Verifikasi tidak ada toast atau peringatan tambahan
29. Verifikasi berkas `Device-Allocation.csv` terunduh
30. Buka berkas CSV
31. Verifikasi berkas pertama tidak memuat kolom Client
32. Klik ikon `⋯` pada header kolom terakhir
33. Centang kembali kolom Client di overlay Column Visibility
34. Tutup overlay Column Visibility
35. Klik ikon Download
36. Klik `Download as CSV`
37. Buka berkas CSV
38. Verifikasi berkas kedua memuat kolom Client lagi

### TC-AC-ACHA-363: Urutan baris berkas mengikuti Sort aktif

39. Klik header kolom Quantity sekali (ascending)
40. Klik ikon Download
41. Klik `Download as CSV`
42. Buka berkas CSV
43. Verifikasi urutan baris berkas sama dengan urutan tabel: tiga baris pertama `HALC-20260906-00002`, `HALC-20260907-00003`, `HALC-20260905-00001`
44. Klik header kolom Quantity dua kali hingga netral

### TC-AC-ACHA-362: Download dengan nol baris

45. Ketik Search `zzzzqqqq`, tekan Enter
46. Verifikasi tampil `No results found`
47. Verifikasi tombol Download tetap aktif
48. Klik ikon Download
49. Klik `Download as CSV`
50. Verifikasi tidak ada toast
51. Buka berkas CSV
52. Verifikasi berkas hanya memuat baris header kolom yang tampil
53. Klik `(←)` pada kotak Search

## Notes

- Ukuran spec (di atas 35 langkah): lima TC Download fungsional satu topik memakai satu dataset; tiap Expected (nama berkas, header, jumlah baris, toast) menjadi `Verifikasi` sendiri (S-01).
- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-7). Seluruh TC primer spec ini (TC-AC-ACHA-357, 358, 359, 362, 363) dikerjakan di sini. Isi sel berkas CSV dan XLSX (kelas f) ada di spec 044; TC-AC-ACHA-364 (kegagalan Download) ada di spec 058 dan TC-AC-ACHA-365 (di atas 5.000 baris) di spec 045.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): pembukaan berkas unduhan; penutupan Filter Panel dengan klik ikon Filter (langkah 13 dan 22); pembersihan Search, Filter, dan sort di akhir TC; penyembunyian dan penampilan kolom Client lewat overlay Column Visibility. Asersi absence toast ditaruh segera sesudah pemicu (klik pilihan format) dan sebelum asersi berkas terunduh; pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas (bagian 8b butir 11).
- Anchor absence (bagian 8b butir 2): asersi kolom Client tidak ada pada berkas pertama (langkah 31) didahului `Verifikasi` berkas terunduh (langkah 29) sebagai anchor positif bahwa unduhan selesai.
- Penyimpangan urutan (S-10): TC-AC-ACHA-363 ditaruh sebelum TC-AC-ACHA-362 (bukan menurut nomor TC) karena TC-AC-ACHA-362 memakai Search tanpa hasil dan menjadi blok terakhir, sehingga Sort pada TC-AC-ACHA-363 diuji pada dataset 30 baris penuh.
- Asersi tambahan (S-03): pada TC-AC-ACHA-362 `Verifikasi` `No results found` sebagai anchor positif bahwa tabel kosong sebelum Download.
- Temuan untuk QA:
  - TC-AC-ACHA-357 butir b (kolom Allocated By ditulis `[First Name] [Last Initial]`) dan TC-AC-ACHA-363 (urutan Allocation ID dalam isi berkas) adalah asersi isi sel berkas (kelas f, konvensi bagian 3 prinsip 13f), bukan nama berkas, header, atau jumlah baris. Penempatan awalnya di spec fungsional ini; keputusan sudah diambil: dua klausa itu diterima tetap di spec ini (tidak dipindah ke spec 044) dan dicatat di sini.
  - TC-AC-ACHA-358 Expected "dari semua halaman" tidak teruji oleh data: 3 baris hasil `Budi` Completed muat pada satu halaman (Page size 10).
  - TC-AC-ACHA-357 langkah uji kedua ("Amati opsi lalu pilih `Download as CSV`") tidak menyebut tempat berkas diunduh; spec bergantung pada kemampuan membaca berkas unduhan (disediakan tim FE).
