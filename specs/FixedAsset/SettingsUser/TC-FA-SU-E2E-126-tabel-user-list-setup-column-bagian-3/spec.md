---
id: TC-FA-SU-E2E-126-tabel-user-list-setup-column-bagian-3
title: "Tabel User List: Setup Column (Bagian 3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-356
  - TC-FA-SU-357
  - TC-FA-SU-358
coverage:
  web: automated
---

# Tabel User List: Setup Column (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Kolom Curated ditampilkan lewat Setup Column pada langkah 2 agar urutan dan pin teramati; arah geser tidak disebut TC dan ditetapkan pada tabel `Kolom Curated Geser`.
- Tabel lain yang punya Setup Column untuk TC-FA-SU-358 langkah 6 tidak disebut TC; spec memakai Sub-tab Borrowed Assets pada Detail Budi Santoso.
- Tabel `Kolom Curated Geser`:

| Kolom | Arah |
|---|---|
| Activation Status | kanan |
| Temporary User | kanan |
| Temporary Until | kanan |
| TAG | kanan |
| Shift | kiri |

- Tabel `Kolom Curated Pin`:

| Kolom |
|---|
| Activation Status |
| Temporary User |
| Temporary Until |
| TAG |
| Shift |

- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-356: Geser kelas Curated

1. Klik header kolom Actions (⋯), klik `Setup Column...`
2. Centang `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Shift`, klik `[Save]`
3. Klik header kolom Actions (⋯), klik `Setup Column...`
4. Untuk setiap baris tabel `Kolom Curated Geser` di Prerequisites (langkah 5 sampai 6):
5. Seret kolom `<Kolom>` satu posisi ke <Arah>
6. Verifikasi urutan kolom `<Kolom>` pada Live Preview berubah satu posisi
7. Klik `[Save]`
8. Untuk setiap baris tabel `Kolom Curated Geser` di Prerequisites (langkah 9):
9. Verifikasi urutan kolom `<Kolom>` pada tabel berubah satu posisi
10. Tekan F5
11. Untuk setiap baris tabel `Kolom Curated Geser` di Prerequisites (langkah 12):
12. Verifikasi urutan kolom `<Kolom>` bertahan setelah F5

### TC-FA-SU-357: Pin dan unpin kelas Curated

13. Untuk setiap baris tabel `Kolom Curated Pin` di Prerequisites (langkah 14 sampai 22):
14. Klik header kolom Actions (⋯), klik `Setup Column...`
15. Klik icon Pin pada kolom `<Kolom>`
16. Klik `[Save]`, scroll tabel secara horizontal
17. Verifikasi kolom `<Kolom>` membeku di kiri saat tabel di-scroll horizontal
18. Tekan F5, scroll tabel secara horizontal
19. Verifikasi kolom `<Kolom>` tetap membeku setelah F5
20. Klik header kolom Actions (⋯), klik `Setup Column...`
21. Unpin kolom `<Kolom>`, klik `[Save]`
22. Verifikasi kolom `<Kolom>` terlepas dan ikut ter-scroll
23. Klik header kolom Actions (⋯), klik `Setup Column...`
24. Klik icon Pin pada kolom `Activation Status`, `Temporary User`, dan `Temporary Until`
25. Hover icon Pin kolom `TAG`
26. Verifikasi icon Pin kolom `TAG` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
27. Klik `[✕]` pada Setup Column

### TC-FA-SU-358: Reset to Default, Discard, dan independensi cache

28. Klik header kolom Actions (⋯), klik `Setup Column...`
29. Hapus centang `Email`, seret kolom `Name` satu posisi ke kanan, dan klik icon Pin pada kolom `Active`
30. Klik `[Reset to Default]`
31. Verifikasi preview kembali ke default modul untuk visibility, urutan, dan pin
32. Klik `[Save]`
33. Verifikasi tabel memakai konfigurasi default modul setelah `[Save]`
34. Klik header kolom Actions (⋯), klik `Setup Column...`
35. Hapus centang `Email`, klik `[✕]`
36. Verifikasi perubahan dibuang dan tabel memakai konfigurasi tersimpan terakhir (kolom `Email` tampil)
37. Klik header kolom Actions (⋯), klik `Setup Column...`
38. Hapus centang `Email`, tekan Esc
39. Verifikasi perubahan dibuang dan tabel memakai konfigurasi tersimpan terakhir (kolom `Email` tampil)
40. Hapus centang `Email` pada Setup Column User List, klik `[Save]`
41. Buka Detail Budi Santoso, buka Tab Responsibilities, Sub-tab Borrowed Assets
42. Verifikasi konfigurasi kolom tabel Sub-tab Borrowed Assets tidak terpengaruh perubahan konfigurasi tabel User List

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1, 3, 23, 28, 34, 37 (membuka Setup Column), 2 (menampilkan kolom curated), 27 (menutup tanpa menyimpan), serta 40 dan 41 (menyiapkan perbandingan dengan tabel lain).
- Langkah yang diulang: langkah 5 sampai 6, langkah 9, langkah 12 (geser lima kolom) dan langkah 14 sampai 22 (pin satu per satu), dengan parameter pada tabel Prerequisites.
- Temuan untuk QA (S-15): (1) TC-FA-SU-358 langkah 6 tidak menyebut tabel lain; Sub-tab Borrowed Assets dipakai, dan perbandingan memerlukan konfigurasi User List non-default sehingga langkah 40 ditambahkan. (2) Post Condition TC-FA-SU-358 (preferensi kembali ke default setelah Reset to Default dan Save) tidak punya langkah observasi tersendiri selain Expected a.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 5 sampai 6, langkah 14 sampai 22) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman. Tiga TC Setup Column pada surface yang sama, dengan cache preferensi yang dibersihkan oleh hook.
