---
id: TC-FA-SU-E2E-178-sub-tab-pending-tasks-setup-column-bagian-2
title: "Sub-tab Pending Tasks: Setup Column (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-528
  - TC-FA-SU-529
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Setup Column (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Tabel parameter "Putaran pin Pending Tasks" (putaran 1 ditulis eksplisit pada langkah awal; batas maksimum 3 kolom per putaran):

| Putaran | Kolom |
|---|---|
| Putaran 2 | `Group`, `PIC`, `Total Asset` |
| Putaran 3 | `Request Date`, `Last Updated` |
- Tabel lain yang punya Setup Column: Sub-tab Assigned Assets (dibuka pada TC-FA-SU-529).

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-528: Pin dan unpin Setup Column kelas Hideable

2. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
3. Klik icon Pin pada kolom `Transaction ID`, `Transaction`, `Status` (satu klik per kolom)
4. Hover icon Pin kolom `Group`
5. Verifikasi icon Pin kolom `Group` disabled sesudah tiga kolom di-pin
6. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
7. Klik `[Save]`
8. Scroll tabel secara horizontal
9. Verifikasi kolom `Transaction ID`, `Transaction`, `Status` membeku di kiri saat tabel di-scroll horizontal
10. Tekan F5
11. Verifikasi kolom `Transaction ID`, `Transaction`, `Status` tetap membeku di kiri setelah refresh
12. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
13. Klik icon Pin (unpin) pada kolom `Transaction ID`, `Transaction`, `Status`
14. Klik `[Save]`
15. Verifikasi kolom `Transaction ID`, `Transaction`, `Status` dilepas dan tidak lagi membeku
16. Untuk setiap baris tabel "Putaran pin Pending Tasks" (langkah 16 sampai 26): klik header kolom Actions (⋯), lalu klik `Setup Column...`
17. Klik icon Pin pada kolom putaran itu (satu klik per kolom)
18. Klik `[Save]`
19. Scroll tabel secara horizontal
20. Verifikasi kolom putaran itu membeku di kiri saat tabel di-scroll horizontal
21. Tekan F5
22. Verifikasi kolom putaran itu tetap membeku di kiri setelah refresh
23. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
24. Klik icon Pin (unpin) pada kolom putaran itu
25. Klik `[Save]`
26. Verifikasi kolom putaran itu dilepas dan tidak lagi membeku

### TC-FA-SU-529: Reset to Default, Discard (✕ atau Esc), dan independensi cache

27. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
28. Hilangkan centang kolom Group
29. Drag kolom Status satu posisi ke atas
30. Klik icon Pin pada kolom Transaction ID
31. Klik `[Reset to Default]`
32. Verifikasi Live Preview kembali ke default modul untuk visibilitas, urutan, dan pin
33. Klik `[Save]`
34. Verifikasi tabel memakai konfigurasi default (visibilitas, urutan, dan pin)
35. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
36. Hilangkan centang kolom Group
37. Klik ✕ pada popup Setup Column
38. Verifikasi tabel masih menampilkan kolom Group sesuai konfigurasi tersimpan terakhir
39. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
40. Verifikasi kolom Group tercentang pada daftar Setup Column dan Live Preview (perubahan dibuang)
41. Hilangkan centang kolom Group
42. Tekan Esc
43. Verifikasi tabel masih menampilkan kolom Group sesuai konfigurasi tersimpan terakhir
44. Klik Sub-tab Assigned Assets
45. Verifikasi konfigurasi kolom Sub-tab Assigned Assets tidak terpengaruh perubahan pada tabel ini (tetap default)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13); membuka Setup Column, `[Save]`, dan unpin pada tiap putaran pin (mengosongkan kuota 3 pin untuk putaran berikutnya, S-09).
- Verifikasi pin per putaran memuat daftar tiga kolom yang disebut utuh dalam satu butir.
- Langkah berulang per baris tabel parameter: tabel "Putaran pin Pending Tasks" pada langkah 16 sampai 26 (2 iterasi).
- Jumlah langkah: 45 tertulis, 56 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (56 langkah). Seluruh blok berada pada satu surface (satu sub-tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-528 langkah 3 meminta pin pada kedelapan kolom sedangkan Expected i membatasi maksimum 3 kolom; spec mem-pin dalam putaran tiga kolom dan melepasnya sebelum putaran berikutnya.
  - TC-FA-SU-528 langkah 5 hanya meng-unpin satu kolom; spec meng-unpin seluruh kolom putaran supaya kuota pin kembali.
  - TC-FA-SU-529 langkah 6 tidak menyebut tabel lain yang dibandingkan; spec memakai Sub-tab Assigned Assets. Perubahan sebelum Reset to Default tidak disimpan sehingga konfigurasi tersimpan tabel ini sama dengan default pada saat perbandingan.
  - TC-FA-SU-529 langkah 2 tidak menyebut pengaturan yang diubah; spec memakai uncheck Group, drag Status satu posisi ke atas, dan pin Transaction ID.
