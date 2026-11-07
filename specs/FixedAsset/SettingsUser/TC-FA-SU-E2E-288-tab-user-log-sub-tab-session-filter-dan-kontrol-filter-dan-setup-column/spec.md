---
id: TC-FA-SU-E2E-288-tab-user-log-sub-tab-session-filter-dan-kontrol-filter-dan-setup-column
title: "Tab User Log sub-tab Session: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-879
  - TC-FA-SU-880
  - TC-FA-SU-881
  - TC-FA-SU-882
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Filter dan Kontrol Filter dan Setup Column

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
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-879: Filter kelas date: Date

1. Ketik Search `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu klik tab User Log, sub-tab Session
2. Klik icon Filter
3. Pilih rentang 12/07/26 sampai 13/07/26 pada Date
4. Klik `[Apply]`
5. Verifikasi rentang inklusif 12/07/26 sampai 13/07/26 menyisakan S-6, S-7, S-8, S-9 (4 baris)
6. Klik `[Clear Field]` lalu `[Apply]`
7. Klik icon Filter untuk menutup panel

### TC-FA-SU-880: Perilaku Filter Panel: tutup tanpa Apply, indikator titik, dan nilai kosong

8. Klik icon Filter, pilih rentang 12/07/26 sampai 13/07/26 pada Date tanpa `[Apply]`
9. Klik di luar panel Filter
10. Klik icon Filter
11. Verifikasi panel yang dibuka lagi menampilkan nilai ter-Apply terakhir (field Date kosong)
12. Verifikasi tabel tidak berubah
13. Pilih rentang 12/07/26 sampai 13/07/26 pada Date, klik `[Apply]`
14. Klik icon Filter untuk menutup panel
15. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
16. Klik icon Filter untuk membuka panel
17. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
18. Klik `[Clear Field]`, lalu klik `[Apply]`
19. Verifikasi badge titik hilang
20. Pilih rentang 12/07/26 sampai 13/07/26 pada Date, klik `[Apply]`
21. Klik header kolom Column Visibility (⋯), hilangkan centang Date, tekan Esc
22. Verifikasi field Date pada Filter Panel tidak hilang
23. Verifikasi filter Date yang ter-Apply tetap berlaku
24. Klik `[Clear Field]`, lalu klik `[Apply]`
25. Klik header kolom Column Visibility (⋯), centang kembali Date, tekan Esc
26. Klik icon Filter untuk menutup panel

### TC-FA-SU-881: Screening Overlay Column Visibility

27. Klik header kolom Actions (⋯)
28. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
29. Verifikasi daftar kolom berurutan Date, Activity, Status, Note, IP Address, Device/Browser
30. Verifikasi tiap kolom memiliki checkbox Hideable terpilih dan enabled serta drag handle
31. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-882: Screening Popup Setup Column dan Preview Table

32. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
33. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
34. Verifikasi body: daftar kolom Date, Activity, Status, Note, IP Address, Device/Browser dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
35. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
36. Klik ✕ untuk menutup popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung tambahan (S-03, R-16, bagian 8b butir 13): langkah 1 mengetik Search `Budi Santoso` lalu Enter supaya baris Budi Santoso tampil di User List (25 baris) sebelum nama diklik.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Panel Filter tetap terbuka sesudah `[Apply]` dan baru tertutup bila icon Filter diklik (keputusan produk); karena itu `[Clear Field]` + `[Apply]` dijalankan tanpa mengklik icon Filter lagi. Langkah 7, 14 dan 26 (`Klik icon Filter untuk menutup panel`) adalah langkah penghubung yang menutup panel sebelum blok berikutnya (S-03, S-09).
- Spec ini berjumlah 36 langkah dan melewati sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01) dan langkah penutupan panel Filter, bukan dari pengulangan.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-880: Expected c (dropdown filter tidak memiliki opsi nilai kosong) tidak berlaku pada sub-tab Session karena Filter Panel hanya punya field Date tanpa dropdown; spec tidak mengasersinya. TC-FA-SU-879: nilai Date menyisakan 4 baris (S-6, S-7, S-8, S-9) mengikuti TC.
