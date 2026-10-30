---
id: TC-GS-FILEMGR-E2E-033-filter-nilai-size-upload-date-dan-logika-and-or
title: "Filter Tabel Utama: Multi-Select OR, Rentang Size, Rentang Upload Date, dan Logika AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-125
  - TC-GS-FILEMGR-126
  - TC-GS-FILEMGR-127
  - TC-GS-FILEMGR-128
coverage:
  web: automated
---

# Filter Tabel Utama: Multi-Select OR, Rentang Size, Rentang Upload Date, dan Logika AND

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data File Manager.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Tabel A2): 33 file aktif (F01 `budi-avatar.jpg` s.d. F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, F09-F33 `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), 4 halaman pada ukuran halaman 10, format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2 (tanpa sisa file, Recycle Bin, atau Changelog dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris dalam spec ini mengasumsikan dataset Tabel A2 segar tanpa sisa dari spec lain.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Data uji: File Format `JPEG`, `JPEG` + `PNG`, `PNG`; Uploaded By `System`; Size (KB) Min/Max `512`/`512`, `1`/`1`, `513`/`1023`, hanya Min `1024`, hanya Max `1`; Upload Date `01/09/26`-`02/09/26`, `02/09/26`-`02/09/26`, `01/09/26`-`01/09/26` (F01 `02/09/26 14:30`, F02 `01/09/26 09:00`). 1 KB = 1.024 byte (F03 524.288 byte = 512 KB, F04 1.024 byte = 1 KB, F07 1.048.576 byte = 1024 KB).
- Kemampuan teknis: mengisi field Min dan Max `Size (KB)`; memilih rentang pada date range picker `Upload Date` (selector disediakan tim FE); mengubah ukuran halaman tabel utama.
- Cleanup: hook `after` mengosongkan Filter dan mengembalikan ukuran halaman 10 (preferensi UI).

## Test Steps

### TC-GS-FILEMGR-125: Filter multi-select File Format dan Uploaded By dengan logika OR dalam satu field

1. Klik ikon Filter di toolbar
2. Pilih `JPEG` pada `File Format`
3. Klik `[Apply]`
4. Verifikasi tabel hanya memuat satu baris `alex-photo.jpeg`
5. Klik `[Clear Field]`
6. Klik `[Apply]`
7. Pilih `JPEG` dan `PNG` pada `File Format`
8. Klik `[Apply]`
9. Verifikasi tabel memuat tepat 4 baris: `alex-photo.jpeg`, `siti-profile.png`, `rudi-hartono.png`, `big-banner.png`
10. Klik `[Clear Field]`
11. Klik `[Apply]`
12. Pilih `System` pada `Uploaded By`
13. Klik `[Apply]`
14. Ubah ukuran halaman ke 50 supaya seluruh hasil tampil dalam satu halaman
15. Verifikasi tabel memuat tepat 28 baris: `siti-profile.png`, `dewi-kartika.jpg`, `big-banner.png`, dan `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`
16. Ubah ukuran halaman kembali ke 10

### TC-GS-FILEMGR-126: Filter rentang Size (KB) dengan batas inklusif

17. Klik `[Clear Field]`
18. Isi Min `512` dan Max `512` pada `Size (KB)`
19. Klik `[Apply]`
20. Verifikasi tabel hanya memuat satu baris `alex-photo.jpeg` (batas Min dan Max inklusif)
21. Klik `[Clear Field]`
22. Isi Min `1` dan Max `1` pada `Size (KB)`
23. Klik `[Apply]`
24. Verifikasi tabel hanya memuat satu baris `dewi-kartika.jpg`
25. Klik `[Clear Field]`
26. Isi Min `513` dan Max `1023` pada `Size (KB)`
27. Klik `[Apply]`
28. Verifikasi empty state `No results found` tampil
29. Klik `[Clear Field]`
30. Isi hanya Min `1024` pada `Size (KB)`
31. Klik `[Apply]`
32. Verifikasi tabel memuat tepat 6 baris: `maya-wijaya.jpg`, `rudi-hartono.png`, `siti-profile.png`, `budi-avatar.jpg`, `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, `big-banner.png`
33. Klik `[Clear Field]`
34. Isi hanya Max `1` pada `Size (KB)`
35. Klik `[Apply]`
36. Verifikasi tabel hanya memuat satu baris `dewi-kartika.jpg`

### TC-GS-FILEMGR-127: Filter rentang Upload Date dengan batas inklusif satu hari

37. Klik `[Clear Field]`
38. Pilih `Upload Date` `01/09/26` sampai `02/09/26` pada date range picker
39. Klik `[Apply]`
40. Verifikasi tabel memuat tepat 2 baris: `budi-avatar.jpg` dan `siti-profile.png`
41. Klik `[Clear Field]`
42. Pilih `Upload Date` `02/09/26` sampai `02/09/26` pada date range picker
43. Klik `[Apply]`
44. Verifikasi tabel hanya memuat satu baris `budi-avatar.jpg`
45. Klik `[Clear Field]`
46. Pilih `Upload Date` `01/09/26` sampai `01/09/26` pada date range picker
47. Klik `[Apply]`
48. Verifikasi tabel hanya memuat satu baris `siti-profile.png`

### TC-GS-FILEMGR-128: Kombinasi filter File Format dan Uploaded By dengan logika AND antar field

49. Klik `[Clear Field]`
50. Pilih `PNG` pada `File Format`
51. Pilih `System` pada `Uploaded By`
52. Klik `[Apply]`
53. Verifikasi tabel memuat tepat 2 baris: `siti-profile.png` dan `big-banner.png`
54. Verifikasi baris `rudi-hartono.png` (PNG, Uploaded By `Sinta Maharani`) tidak tampil
55. Klik `[Clear Field]`
56. Klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC mengikuti sumber (125, 126, 127, 128).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 dan langkah 16 (TC-GS-FILEMGR-125 butir c menyebut 28 baris, lebih dari ukuran halaman 10; ukuran halaman 50 dipakai supaya semua baris diperiksa dalam satu halaman dan dikembalikan ke 10), serta `[Clear Field]` dan `[Apply]` di antara blok dan di langkah 55 (pemulihan state Filter; hook `after` menjadi cadangan). Filter Panel tetap terbuka setelah `[Apply]` (TC-GS-FILEMGR-135 menutup panel secara eksplisit).
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 56 langkah): empat TC memakai Filter Panel dan dataset Tabel A2 yang sama, hanya membaca, dan tiap kasus diawali `[Clear Field]` sehingga hasil kasus sebelumnya tidak dipakai kasus berikutnya; kegagalan satu asersi hasil filter tidak membuat kasus lain kehilangan makna (soft assertion).
- Temuan untuk QA:
  - TC-GS-FILEMGR-127: interaksi date range picker (membuka kalender, memilih awal dan akhir) tidak didefinisikan di TC; ditulis "pilih ... pada date range picker" dan selector "disediakan tim FE".
  - TC-GS-FILEMGR-127: batas inklusif satu hari bergantung zona waktu pembanding (F01 `02/09/26 14:30`, F02 `01/09/26 09:00`); TC tidak menyebut zona waktu server dan klien. Spec mengikuti nilai tampil Tabel A2.
  - TC-GS-FILEMGR-126 butir d: TC menulis daftar enam baris berurutan menurut Size, bukan menurut urutan default tabel; spec mengasersi keanggotaan baris, bukan urutan.
  - TC-GS-FILEMGR-125 butir c: 28 baris melewati satu halaman (ukuran halaman 10); TC tidak menyebut cara memeriksa seluruh baris (lihat langkah penghubung langkah 14).
  - Seeding Tabel A2 dan reset dataset antar spec tidak punya mekanisme tertulis di TC (lihat spec 031).
