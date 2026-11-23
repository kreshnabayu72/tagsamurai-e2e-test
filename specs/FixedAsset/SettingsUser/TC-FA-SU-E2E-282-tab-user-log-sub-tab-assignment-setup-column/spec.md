---
id: TC-FA-SU-E2E-282-tab-user-log-sub-tab-assignment-setup-column
title: "Tab User Log sub-tab Assignment: Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-859
  - TC-FA-SU-860
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Setup Column

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
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Transaction ID, Name, PIC.
- Tabel "Urutan Drag Setup Column" (parameter langkah berulang; dijalankan berurutan dari baris pertama, tiap baris drag satu posisi tanpa `[Save]` di antaranya sehingga efeknya kumulatif; posisi 1 = paling atas pada daftar Setup Column dan paling kiri pada tabel; urutan semula pada tabel "Kolom Setup Column Hideable"): (1) Activity ke atas, urutan sesudahnya Activity, Date, Transaction ID, Name, PIC; (2) Date ke bawah, urutan sesudahnya Activity, Transaction ID, Date, Name, PIC; (3) Name ke atas, urutan sesudahnya Activity, Transaction ID, Name, Date, PIC; (4) Transaction ID ke bawah, urutan sesudahnya Activity, Name, Transaction ID, Date, PIC; (5) PIC ke atas, urutan sesudahnya Activity, Name, Transaction ID, PIC, Date. Posisi akhir sesudah baris (5): Activity 1, Name 2, Transaction ID 3, PIC 4, Date 5.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-859: Ceklis dan unceklis Setup Column kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Buka Setup Column
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain PIC (langkah 4 sampai 5):
4. Hilangkan centang kolom tersebut pada daftar Setup Column
5. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
6. Hover checkbox kolom PIC pada daftar Setup Column
7. Verifikasi checkbox kolom PIC disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
8. Klik `[Save]`
9. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain PIC (langkah 10):
10. Verifikasi kolom tersebut tidak tampil di tabel
11. Klik F5
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain PIC (langkah 13):
13. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
14. Buka Setup Column, centang kembali seluruh kolom selain PIC, lalu hilangkan centang kolom PIC
15. Verifikasi perubahan kolom PIC tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi kolom PIC tidak tampil di tabel
18. Klik F5
19. Verifikasi kolom PIC tetap tidak tampil di tabel setelah refresh (F5)
20. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-860: Geser (drag reorder) Setup Column kelas Hideable (default tampil)

21. Buka Setup Column
22. Untuk setiap baris pada tabel "Urutan Drag Setup Column" secara berurutan (langkah 23 sampai 24):
23. Drag kolom pada baris tersebut satu posisi ke arah (atas atau bawah) yang tertulis pada tabel
24. Verifikasi urutan Live Preview berubah
25. Klik `[Save]`
26. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 27):
27. Verifikasi posisi kolom tersebut pada tabel berubah (menempati posisi akhir pada tabel)
28. Klik F5
29. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 30):
30. Verifikasi posisi kolom tersebut pada tabel tetap berubah (menempati posisi akhir pada tabel) setelah refresh (F5)
31. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Langkah penghubung tambahan: Hover checkbox kolom PIC (langkah 6) sebelum `Verifikasi` tooltip, supaya tooltip muncul.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 4 kali, satu iterasi per kolom di tabel Prerequisites; langkah 10 dijalankan 4 kali, satu iterasi per kolom di tabel Prerequisites; langkah 13 dijalankan 4 kali, satu iterasi per kolom di tabel Prerequisites; langkah 23 sampai 24 dijalankan 5 kali, satu iterasi per baris di tabel "Urutan Drag Setup Column"; langkah 27 dijalankan 5 kali, satu iterasi per baris di tabel "Urutan Drag Setup Column"; langkah 30 dijalankan 5 kali, satu iterasi per baris di tabel "Urutan Drag Setup Column".
- Spec ini berjumlah 59 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- TC-FA-SU-861 (pin dan unpin sub-tab Assignment) ada di spec 293; TC-FA-SU-862 ada di spec 283.
- Temuan untuk QA (S-15): (1) TC-FA-SU-859: TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji empat kolom pertama bersamaan lalu kolom PIC terpisah setelah kolom lain dicentang kembali. TC-FA-SU-860: TC tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan menetapkan sendiri urutan, arah, dan posisi akhir tiap kolom pada tabel "Urutan Drag Setup Column" di Prerequisites, karena drag berurutan tanpa `[Save]` bersifat kumulatif sehingga arah yang tidak ditentukan membuat posisi akhir tidak deterministik; arah dan posisi akhir itu pilihan spec, bukan ketentuan TC. Post Condition preferensi kolom tersimpan per perangkat (atau kembali ke default) tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan. Spec ini menyimpan konfigurasi Setup Column di browser; `suite.md` belum mencantumkan daftar spec yang menyimpan konfigurasi kolom (bagian 4 konvensi), sehingga perlu ditambahkan tim FE.
