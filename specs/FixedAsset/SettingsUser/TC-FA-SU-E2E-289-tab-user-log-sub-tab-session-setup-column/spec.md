---
id: TC-FA-SU-E2E-289-tab-user-log-sub-tab-session-setup-column
title: "Tab User Log sub-tab Session: Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-883
  - TC-FA-SU-884
coverage:
  web: automated
---

# Tab User Log sub-tab Session: Setup Column

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
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Status, Note, IP Address, Device/Browser.
- Tabel "Drag Setup Column" (parameter langkah berulang TC-FA-SU-884; baris diproses berurutan dari urutan awal Date, Activity, Status, Note, IP Address, Device/Browser; "kiri" atau "kanan" berarti satu posisi; arah dan urutan ditetapkan spec supaya drag antarkolom tidak saling membatalkan, lihat Temuan untuk QA). Kolom "posisi akhir" adalah posisi kolom sesudah seluruh baris dijalankan:
  - Activity, kiri, urutan sesudah drag: Activity, Date, Status, Note, IP Address, Device/Browser, posisi akhir 1
  - Date, kanan, urutan sesudah drag: Activity, Status, Date, Note, IP Address, Device/Browser, posisi akhir 2
  - Status, kanan, urutan sesudah drag: Activity, Date, Status, Note, IP Address, Device/Browser, posisi akhir 6
  - Note, kiri, urutan sesudah drag: Activity, Date, Note, Status, IP Address, Device/Browser, posisi akhir 3
  - IP Address, kiri, urutan sesudah drag: Activity, Date, Note, IP Address, Status, Device/Browser, posisi akhir 4
  - Device/Browser, kiri, urutan sesudah drag: Activity, Date, Note, IP Address, Device/Browser, Status, posisi akhir 5
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-883: Ceklis dan unceklis Setup Column kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter, klik nama Budi Santoso, lalu klik tab User Log, sub-tab Session
2. Buka Setup Column
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Device/Browser (langkah 4 sampai 5):
4. Hilangkan centang kolom tersebut pada daftar Setup Column
5. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
6. Hover checkbox kolom Device/Browser pada daftar Setup Column
7. Verifikasi checkbox kolom Device/Browser disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
8. Klik `[Save]`
9. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Device/Browser (langkah 10):
10. Verifikasi kolom tersebut tidak tampil di tabel
11. Klik F5
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Device/Browser (langkah 13):
13. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
14. Buka Setup Column, centang kembali seluruh kolom selain Device/Browser, lalu hilangkan centang kolom Device/Browser
15. Verifikasi perubahan kolom Device/Browser tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi kolom Device/Browser tidak tampil di tabel
18. Klik F5
19. Verifikasi kolom Device/Browser tetap tidak tampil di tabel setelah refresh (F5)
20. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-884: Geser (drag reorder) Setup Column kelas Hideable (default tampil)

21. Buka Setup Column
22. Untuk setiap baris tabel "Drag Setup Column" secara berurutan (langkah 23 sampai 24):
23. Drag kolom pada baris tersebut satu posisi ke arah pada tabel
24. Verifikasi urutan Live Preview sama dengan "urutan sesudah drag" pada baris tersebut
25. Klik `[Save]`
26. Untuk setiap baris tabel "Drag Setup Column" (langkah 27):
27. Verifikasi posisi kolom pada baris tersebut di tabel sama dengan "posisi akhir" pada baris tersebut
28. Klik F5
29. Untuk setiap baris tabel "Drag Setup Column" (langkah 30):
30. Verifikasi posisi kolom pada baris tersebut di tabel tetap sama dengan "posisi akhir" setelah refresh (F5)
31. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung tambahan (S-03, R-16, bagian 8b butir 13): langkah 1 mengetik Search `Budi Santoso` lalu Enter supaya baris Budi Santoso tampil di User List (25 baris) sebelum nama diklik.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan: Hover checkbox kolom Device/Browser (langkah 6) sebelum `Verifikasi` tooltip, supaya tooltip muncul.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 5 kali, satu iterasi per kolom di tabel Prerequisites; langkah 10 dijalankan 5 kali, satu iterasi per kolom di tabel Prerequisites; langkah 13 dijalankan 5 kali, satu iterasi per kolom di tabel Prerequisites; langkah 23 sampai 24 dijalankan 6 kali, satu iterasi per baris tabel "Drag Setup Column"; langkah 27 dijalankan 6 kali, satu iterasi per baris tabel "Drag Setup Column"; langkah 30 dijalankan 6 kali, satu iterasi per baris tabel "Drag Setup Column".
- Spec ini berjumlah 67 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- TC-FA-SU-885 (pin dan unpin sub-tab Session) ada di spec 294; TC-FA-SU-886 ada di spec 290.
- Temuan untuk QA (S-15): (1) Post Condition preferensi kolom tersimpan per perangkat (atau kembali ke default) tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan. Spec ini menyimpan konfigurasi Setup Column di browser; `suite.md` belum mencantumkan daftar spec yang menyimpan konfigurasi kolom (bagian 4 konvensi), sehingga perlu ditambahkan tim FE. (2) TC-FA-SU-883: TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji lima kolom pertama bersamaan lalu kolom Device/Browser terpisah setelah kolom lain dicentang kembali. TC-FA-SU-884: TC tidak menyebut arah drag dan urutan; spec menetapkan arah (kiri atau kanan, satu posisi) dan urutan drag per kolom lewat tabel "Drag Setup Column" supaya drag kumulatif tidak saling membatalkan dan posisi akhir tiap kolom berbeda dari posisi awalnya; usulan perubahan TC: sebutkan arah dan posisi akhir.
