---
id: TC-FA-SU-E2E-287-tab-user-log-sub-tab-session-sort-dan-filter-dan-kontrol-filter
title: "Tab User Log sub-tab Session: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-877
  - TC-FA-SU-878
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Sort dan Filter dan Kontrol Filter

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

## Test Steps

### TC-FA-SU-877: Sort kelas teks: Activity, Status, Note, IP Address, Device/Browser

1. Ketik Search `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu klik tab User Log, sub-tab Session
2. Klik header Activity satu kali
3. Verifikasi Activity klik 1 ascending (↑), lima baris pertama: S-1, S-2, S-3, S-4, S-5
4. Klik header Activity kedua kali
5. Verifikasi Activity klik 2 descending (↓), lima baris pertama: S-1, S-2, S-3, S-4, S-5
6. Klik header Activity ketiga kali
7. Verifikasi Activity klik 3 netral kembali ke default, lima baris pertama: S-1, S-2, S-3, S-4, S-5
8. Klik header Status satu kali
9. Verifikasi Status klik 1 ascending (↑), lima baris pertama: S-1, S-2, S-3, S-4, S-5
10. Klik header Status kedua kali
11. Verifikasi Status klik 2 descending (↓), lima baris pertama: S-1, S-2, S-3, S-4, S-5
12. Klik header Status ketiga kali
13. Verifikasi Status klik 3 netral kembali ke default, lima baris pertama: S-1, S-2, S-3, S-4, S-5
14. Klik header Note satu kali
15. Verifikasi Note klik 1 ascending (↑), lima baris pertama: S-2, S-4, S-6, S-8, S-1
16. Klik header Note kedua kali
17. Verifikasi Note klik 2 descending (↓), lima baris pertama: S-1, S-3, S-5, S-7, S-9
18. Klik header Note ketiga kali
19. Verifikasi Note klik 3 netral kembali ke default, lima baris pertama: S-1, S-2, S-3, S-4, S-5
20. Klik header IP Address satu kali
21. Verifikasi IP Address klik 1 ascending (↑), lima baris pertama: S-1, S-6, S-7, S-8, S-9
22. Klik header IP Address kedua kali
23. Verifikasi IP Address klik 2 descending (↓), lima baris pertama: S-2, S-3, S-4, S-5, S-1
24. Klik header IP Address ketiga kali
25. Verifikasi IP Address klik 3 netral kembali ke default, lima baris pertama: S-1, S-2, S-3, S-4, S-5
26. Klik header Device/Browser satu kali
27. Verifikasi Device/Browser klik 1 ascending (↑), lima baris pertama: S-2, S-3, S-1, S-6, S-7
28. Klik header Device/Browser kedua kali
29. Verifikasi Device/Browser klik 2 descending (↓), lima baris pertama: S-4, S-5, S-1, S-6, S-7
30. Klik header Device/Browser ketiga kali
31. Verifikasi Device/Browser klik 3 netral kembali ke default, lima baris pertama: S-1, S-2, S-3, S-4, S-5

### TC-FA-SU-878: Screening Filter Panel: field, label, placeholder, dan tombol

32. Klik icon Filter
33. Verifikasi panel terbuka di bawah Table Tools
34. Verifikasi ikon Filter menjadi gelap
35. Hover icon Filter
36. Verifikasi tooltip `Filter`
37. Verifikasi field Date (date range picker, placeholder `Select date`)
38. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
39. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply
40. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung tambahan (S-03, R-16, bagian 8b butir 13): langkah 1 mengetik Search `Budi Santoso` lalu Enter supaya baris Budi Santoso tampil di User List (25 baris) sebelum nama diklik.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-877: sort Activity dan Status tidak punya dua nilai distinct pada seed (Activity semua `Session`, Status semua `—`), sehingga urutan ascending, descending, dan default identik dan tidak membuktikan sort (S-11, S-14); spec mengikuti TC. Expected hanya mendaftar lima baris pertama dari sembilan baris. Urutan S-1 pada sort IP Address dan Device/Browser berada di tengah di kedua arah karena nilai kolomnya tidak tertulis di Pre-setup TC.
