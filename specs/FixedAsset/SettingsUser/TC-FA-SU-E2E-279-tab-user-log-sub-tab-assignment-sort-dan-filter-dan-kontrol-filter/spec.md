---
id: TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter
title: "Tab User Log sub-tab Assignment: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-846
  - TC-FA-SU-847
  - TC-FA-SU-848
  - TC-FA-SU-849
  - TC-FA-SU-850
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Handed over|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Handed over|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Handed over|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Handed over|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-846: Sort kelas teks: Transaction ID, Name

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Klik header Transaction ID satu kali
3. Verifikasi Transaction ID klik 1 ascending (↑), lima baris pertama: A-5, A-4, A-1, A-3, A-2
4. Klik header Transaction ID kedua kali
5. Verifikasi Transaction ID klik 2 descending (↓), lima baris pertama: A-2, A-1, A-3, A-4, A-5
6. Klik header Transaction ID ketiga kali
7. Verifikasi Transaction ID klik 3 netral kembali ke default, lima baris pertama: A-1, A-2, A-3, A-4, A-5
8. Klik header Name satu kali
9. Verifikasi Name klik 1 ascending (↑), lima baris pertama: A-4, A-2, A-5, A-1, A-3
10. Klik header Name kedua kali
11. Verifikasi Name klik 2 descending (↓), lima baris pertama: A-1, A-3, A-5, A-2, A-4
12. Klik header Name ketiga kali
13. Verifikasi Name klik 3 netral kembali ke default, lima baris pertama: A-1, A-2, A-3, A-4, A-5

### TC-FA-SU-847: Sort kelas user: PIC

14. Klik header PIC satu kali
15. Verifikasi PIC klik 1 ascending (↑), lima baris pertama: A-2, A-4, A-5, A-1, A-3
16. Klik header PIC kedua kali
17. Verifikasi PIC klik 2 descending (↓), lima baris pertama: A-1, A-3, A-2, A-4, A-5
18. Klik header PIC ketiga kali
19. Verifikasi PIC klik 3 netral kembali ke default, lima baris pertama: A-1, A-2, A-3, A-4, A-5

### TC-FA-SU-848: Guard kolom non-sortable: Activity

20. Hover header Activity
21. Klik header Activity
22. Verifikasi header Activity tidak memiliki icon sort dan klik header tidak mengubah urutan

### TC-FA-SU-849: Screening Filter Panel: field, label, placeholder, dan tombol

23. Klik icon Filter
24. Verifikasi panel terbuka di bawah Table Tools
25. Verifikasi ikon Filter menjadi gelap
26. Hover icon Filter
27. Verifikasi tooltip `Filter`
28. Verifikasi field pertama Date (date range picker, placeholder `Select date`)
29. Verifikasi field kedua Activity (multi-select searchable, placeholder `All activities`)
30. Verifikasi field ketiga PIC (multi-select searchable, placeholder `All PICs`)
31. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
32. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply
33. Klik icon Filter untuk menutup panel

### TC-FA-SU-850: Filter kelas date: Date

34. Klik icon Filter
35. Pilih rentang 05/05/26 sampai 12/05/26 pada Date
36. Klik `[Apply]`
37. Verifikasi rentang inklusif 05/05/26 sampai 12/05/26 menyisakan A-4, A-5 (2 baris)
38. Klik `[Clear Field]` lalu `[Apply]`
39. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Panel Filter tetap terbuka sesudah `[Apply]` dan baru tertutup bila icon Filter diklik (keputusan produk); karena itu `[Clear Field]` + `[Apply]` dijalankan tanpa mengklik icon Filter lagi. Langkah 39 (`Klik icon Filter untuk menutup panel`) adalah langkah penghubung yang menutup panel sebelum blok berikutnya (S-03, S-09).
- Spec ini berjumlah 39 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-846 dan TC-FA-SU-847: Expected hanya mendaftar lima baris pertama dari lima baris seed; spec mengasersi lima baris itu. Pada sort Name, A-1 dan A-3 berurutan sama di kedua arah (nilai Name keduanya tidak tertulis di Pre-setup TC); spec mengikuti TC. TC-FA-SU-848 Langkah Uji menyebut "tiap header kolom yang dicantumkan" padahal hanya Activity.
