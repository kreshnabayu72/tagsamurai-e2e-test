---
id: TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker
title: "Independensi Search, Filter, dan Sort, Pemulihan dari Empty State, serta Urutan Newest dan Oldest"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-211
  - TC-FA-NOTIF-212
  - TC-FA-NOTIF-213
  - TC-FA-NOTIF-217
  - TC-FA-NOTIF-218
coverage:
  web: automated
---

# Independensi Search, Filter, dan Sort, Pemulihan dari Empty State, serta Urutan Newest dan Oldest

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi dengan waktu menurun) milik akun aktor, dipulihkan fixture BE pemulih di hook `before` dan `after`. Spec hanya membaca data. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-211: Clear Filter tidak mereset Search dan Sort yang aktif

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Ketik Search `access`, tekan Enter
3. Klik toggle Sort hingga Sort `Oldest`
4. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
5. Klik `[Clear Field]`, lalu klik `[Apply]`
6. Verifikasi kotak Search tetap berisi `access`
7. Verifikasi Sort `Oldest` tetap aktif

### TC-FA-NOTIF-212: Clear Search tidak mereset Filter dan Sort yang aktif

8. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
9. Ketik Search `access`, tekan Enter
10. Klik toggle Sort hingga Sort `Oldest`
11. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
12. Klik `✕` pada Search, tekan Enter
13. Verifikasi indikator titik pada icon Filter tampil (Filter tetap aktif)
14. Verifikasi Sort `Oldest` tetap aktif

### TC-FA-NOTIF-213: Pemulihan dari empty state saat salah satu saringan dilepas

15. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
16. Ketik Search `repaired`, tekan Enter
17. Klik icon Filter, pilih Event Type `Missing Found`, lalu klik `[Apply]`
18. Verifikasi empty state tampil dengan Title `No results found`
19. Klik `✕` pada Search, tekan Enter
20. Verifikasi item `missing_found` tampil kembali pada list

### TC-FA-NOTIF-217: Sort default Newest dan toggle ke Oldest

21. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
22. Verifikasi Sort `Newest` aktif
23. Verifikasi list berurutan terbaru di atas
24. Klik toggle Sort
25. Verifikasi Sort `Oldest` aktif
26. Verifikasi list berurutan terlama di atas
27. Klik toggle Sort
28. Verifikasi Sort kembali `Newest`

### TC-FA-NOTIF-218: Sort tidak mereset Search dan Filter aktif

29. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
30. Ketik Search `access`, tekan Enter
31. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
32. Scroll sampai akhir list hingga seluruh item termuat, lalu catat urutan item hasil
33. Klik toggle Sort
34. Verifikasi kotak Search tetap berisi `access`
35. Verifikasi indikator titik pada icon Filter tampil (Filter tetap aktif)
36. Scroll sampai akhir list hingga seluruh item termuat
37. Verifikasi list memuat sedikitnya 2 item
38. Verifikasi urutan hasil berbalik terhadap urutan yang dicatat pada langkah 32
39. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular. Tie-breaker Sort (TC-219) ada di spec 115.
- Langkah penghubung (S-03): langkah 1, 8, 15, 21, 29, 39 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 32 dan 36 (memuat seluruh item dan mencatat urutan).
- Asersi tambahan di luar Expected TC (S-03): langkah 37 (anchor positif: sedikitnya 2 item agar pembalikan urutan pada langkah 38 bermakna, 8b butir 2).
- Seed N-01 sampai N-37 hanya dibaca; tidak ada keadaan yang dibawa antar spec.
- Spec ini di atas sekitar 35 langkah (39 langkah): kelima TC satu topik (independensi kontrol Search, Filter, dan Sort pada seed yang sama), tiap blok diawali reset lewat `[Show All]` dan berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-211 dan 212 tidak mengasersi bahwa hasil list tersaring sesuai Search dan Filter yang masih aktif; spec hanya mengasersi kontrol yang tetap aktif (kotak Search, indikator titik Filter, label Sort) sesuai Expected TC.
  - TC-218 menulis "urutan hasil berbalik" tanpa daftar hasil; spec membandingkan urutan sebelum dan sesudah toggle Sort.
  - TC-213 menyebut item yang tampil kembali hanya lewat nama event `missing_found` tanpa Title atau Body; spec menulis item itu sebagai event_type `missing_found` (langkah 20).
