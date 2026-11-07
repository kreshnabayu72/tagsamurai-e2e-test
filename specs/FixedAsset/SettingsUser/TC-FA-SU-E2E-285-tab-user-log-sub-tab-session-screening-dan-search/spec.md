---
id: TC-FA-SU-E2E-285-tab-user-log-sub-tab-session-screening-dan-search
title: "Tab User Log sub-tab Session: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-871
  - TC-FA-SU-872
  - TC-FA-SU-1045
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Session Budi Santoso (Pre-setup #30, 9 baris; urutan default Date descending). Label baris = `Date|Note` (kolom Activity bernilai `Session`, kolom Status bernilai `—`); alias dipakai langkah:
  - S-1: `16/07/26 08:12|Session started`
  - S-2: `15/07/26 20:30|Session ended`
  - S-3: `15/07/26 08:00|Session started`
  - S-4: `14/07/26 08:40|Session ended`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-5: `14/07/26 08:05|Session started`, IP Address `192.0.2.40`, Device/Browser memuat `Safari`
  - S-6: `13/07/26 17:05|Session ended`
  - S-7: `13/07/26 08:10|Session started`
  - S-8: `12/07/26 17:15|Session ended`
  - S-9: `12/07/26 08:02|Session started`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log, kecuali satu baris Session dengan User-Agent yang tidak dapat diparse (TC-FA-SU-1045) yang disiapkan lewat seed API dan dihapus di hook `after`.
- Kemampuan teknis (disediakan tim BE/FE): menyiapkan baris Session ber-User-Agent yang tidak dapat diparse lewat seed API untuk Budi Santoso. Mekanismenya tidak disebut TC, PRD, atau LLD (lihat Temuan untuk QA).

## Test Steps

### TC-FA-SU-871: Screening Table Tools, kolom, dan default sort

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Session
2. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil rata kanan
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Hover icon Filter
6. Verifikasi tooltip `Filter`
7. Hover icon Download
8. Verifikasi tooltip `Download`
9. Klik icon Search
10. Verifikasi placeholder Search `Search note, IP address, or device...`
11. Klik icon ←
12. Verifikasi kolom `Date (sortable) | Activity (sortable) | Status (sortable) | Note (sortable) | IP Address (sortable) | Device/Browser (sortable) | Column Visibility (⋯)`
13. Klik header kolom Column Visibility (⋯)
14. Verifikasi overlay Column Visibility tampil
15. Verifikasi sedikitnya satu baris tampil pada tabel
16. Verifikasi sel body kolom Column Visibility (⋯) pada setiap baris kosong tanpa row action
17. Tekan Esc untuk menutup overlay
18. Verifikasi default sort Date descending, lima baris pertama: S-1, S-2, S-3, S-4, S-5
19. Verifikasi footer pagination 10 data per halaman
20. Klik dropdown page size
21. Verifikasi pilihan page size 10, 25, 50, 100
22. Tekan Esc untuk menutup dropdown page size

### TC-FA-SU-872: Search kelas teks: kolom Activity, Status, Note, IP Address, Device/Browser

23. Ketik Search `Session` (kolom Activity), tekan Enter
24. Verifikasi keyword `Session` (kolom Activity) menyisakan 9 baris, termasuk S-1, S-2, S-3, S-4, S-5, S-6
25. Kosongkan isi kotak search, tekan Enter
26. Ketik Search `—` (kolom Status), tekan Enter
27. Verifikasi keyword `—` (kolom Status) menyisakan 9 baris, termasuk S-1, S-2, S-3, S-4, S-5, S-6
28. Kosongkan isi kotak search, tekan Enter
29. Ketik Search `ended` (kolom Note), tekan Enter
30. Verifikasi keyword `ended` (kolom Note) menyisakan S-2, S-4, S-6, S-8 (4 baris)
31. Kosongkan isi kotak search, tekan Enter
32. Ketik Search `192.0.2.40` (kolom IP Address), tekan Enter
33. Verifikasi keyword `192.0.2.40` (kolom IP Address) menyisakan S-4, S-5 (2 baris)
34. Kosongkan isi kotak search, tekan Enter
35. Ketik Search `Safari` (kolom Device/Browser), tekan Enter
36. Verifikasi keyword `Safari` (kolom Device/Browser) menyisakan S-4, S-5 (2 baris)
37. Kosongkan isi kotak search, tekan Enter
38. Klik icon ←

### TC-FA-SU-1045: Kolom Device/Browser: format [Browser] on [OS] dan tanda — bila tidak terparse

39. Verifikasi nilai Device/Browser tampil berformat `[Browser] on [OS]`: `Chrome on Windows 11`, `Chrome on Android`, `Safari on iOS`
40. Siapkan baris Session dengan User-Agent yang tidak dapat diparse lewat seed API hingga tersimpan, lalu muat ulang sub-tab Session
41. Verifikasi baris dengan User-Agent yang tidak dapat diparse menampilkan `—` pada kolom Device/Browser

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Langkah 15 (`Verifikasi sedikitnya satu baris tampil pada tabel`) adalah asersi tambahan di luar Expected TC dan dicatat di sini (S-03): pembanding generik sebelum asersi universal "setiap baris" pada kolom Column Visibility (bagian 8b butir 2).
- Langkah 20 (`Klik dropdown page size`) dan langkah 22 (`Tekan Esc untuk menutup dropdown page size`) mengikuti Langkah Uji TC (klik dropdown page size, amati pilihan, tutup dengan Esc) sehingga pilihan page size diasersi saat dropdown terbuka.
- Spec ini berjumlah 41 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-872: Expected a dan b mendaftar enam dari sembilan baris dengan "(9 baris)"; spec mengasersi 9 baris yang memuat enam baris tertulis (total absolut seed, S-12). TC-FA-SU-1045: TC tidak memetakan nilai `Chrome on Windows 11`, `Chrome on Android`, `Safari on iOS` ke baris seed tertentu dan mekanisme menyiapkan baris dengan User-Agent yang tidak dapat diparse tidak disebut TC, PRD, atau LLD (R-19); spec menandainya sebagai kemampuan seed API yang disediakan tim BE/FE dan menjalankannya sebagai baris terakhir spec. (3) Label baris Session `Date|Note` disimpulkan dari TC-FA-SU-872 dan 877 (keyword `ended` hanya mencocokkan baris `Session ended` pada kolom Note); TC tidak menyatakan format label secara eksplisit.
