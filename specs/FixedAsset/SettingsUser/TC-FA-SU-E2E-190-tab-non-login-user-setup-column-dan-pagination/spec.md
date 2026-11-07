---
id: TC-FA-SU-E2E-190-tab-non-login-user-setup-column-dan-pagination
title: "Tab Non-Login User: Setup Column dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-566
  - TC-FA-SU-567
  - TC-FA-SU-568
coverage:
  web: automated
---

# Tab Non-Login User: Setup Column dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Custom Field Shift (Pre-setup #31, `FaUserMain`): Gudang Cabang Bekasi `Morning`, Kendaraan Operasional B 1234 XY `Night`, Mesin Fotokopi Lt.3 `Morning`, Printer Lantai 5 `Night`, Ruang Meeting Anggrek `Morning`; kolom curated Shift muncul setelah ditampilkan lewat Setup Column.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Tabel lain yang punya Setup Column: Sub-tab Pending Tasks pada Tab Responsibilities (dibuka pada TC-FA-SU-567).
- Tabel parameter "Nomor halaman tidak valid":

| Input |
|---|
| `0` |
| `-1` |
| `999` |
| `abc` |

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-566: Pin dan unpin Setup Column kelas Curated

2. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
3. Centang kolom `Temporary User`, `Temporary Until`, dan `Shift` pada daftar Setup Column
4. Klik `[Save]`
5. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
6. Klik icon Pin pada kolom `Temporary User`, `Temporary Until`, `Shift` (satu klik per kolom)
7. Hover icon Pin kolom `Name`
8. Verifikasi icon Pin kolom `Name` disabled sesudah tiga kolom di-pin
9. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
10. Klik `[Save]`
11. Scroll tabel secara horizontal
12. Verifikasi kolom `Temporary User`, `Temporary Until`, `Shift` membeku di kiri saat tabel di-scroll horizontal
13. Tekan F5
14. Verifikasi kolom `Temporary User`, `Temporary Until`, `Shift` tetap membeku di kiri setelah refresh
15. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
16. Klik icon Pin (unpin) pada kolom `Temporary User`, `Temporary Until`, `Shift`
17. Klik `[Save]`
18. Verifikasi kolom `Temporary User`, `Temporary Until`, `Shift` dilepas dan tidak lagi membeku

### TC-FA-SU-567: Reset to Default, Discard (✕ atau Esc), dan independensi cache

19. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
20. Hilangkan centang kolom Division
21. Drag kolom Email satu posisi ke atas
22. Klik icon Pin pada kolom Name
23. Klik `[Reset to Default]`
24. Verifikasi Live Preview kembali ke default modul untuk visibilitas, urutan, dan pin
25. Klik `[Save]`
26. Verifikasi tabel memakai konfigurasi default (visibilitas, urutan, dan pin)
27. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
28. Hilangkan centang kolom Division
29. Klik ✕ pada popup Setup Column
30. Verifikasi tabel masih menampilkan kolom Division sesuai konfigurasi tersimpan terakhir
31. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
32. Verifikasi kolom Division tercentang pada daftar Setup Column dan Live Preview (perubahan dibuang)
33. Hilangkan centang kolom Division
34. Tekan Esc
35. Verifikasi tabel masih menampilkan kolom Division sesuai konfigurasi tersimpan terakhir
36. Buka Tab Responsibilities > Sub-tab Pending Tasks
37. Verifikasi konfigurasi kolom Sub-tab Pending Tasks tidak terpengaruh perubahan pada tabel ini (tetap default)

### TC-FA-SU-568: Pagination: page size, navigasi, dan kasus tepi

38. Klik Tab Non-Login User
39. Verifikasi footer pagination menampilkan default 10 baris per halaman
40. Klik dropdown page size
41. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
42. Tekan Esc
43. Untuk setiap baris tabel "Nomor halaman tidak valid" (langkah 43 sampai 44): isi nomor halaman input baris itu, tekan Enter
44. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
45. Ganti page size ke 25
46. Ganti page size ke 10
47. Verifikasi tabel menampilkan halaman 1 setelah page size diganti
48. Klik header Name satu kali
49. Verifikasi tabel menampilkan halaman 1 setelah sort diganti
50. Ketik Search `Printer`, tekan Enter
51. Verifikasi tabel menampilkan halaman 1 setelah Search mengubah hasil (`Printer Lantai 5`)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13); menampilkan kolom curated lewat Setup Column sebelum pin (kolom curated default tersembunyi); `Klik Tab Non-Login User` kembali dari tabel lain sebelum TC-FA-SU-568; langkah 40 (membuka dropdown page size) dan 42 (menutupnya dengan Esc).
- Verifikasi pin memuat daftar tiga kolom yang disebut utuh dalam satu butir.
- Langkah berulang per baris tabel parameter: tabel "Nomor halaman tidak valid" pada langkah 43 sampai 44 (4 iterasi).
- Jumlah langkah: 51 tertulis, 57 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (57 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-566 Expected d menyebut icon Pin kolom lain disabled setelah tiga kolom di-pin tanpa menyebut kolom pembanding; spec memakai `Name`.
  - TC-FA-SU-567 langkah 6 tidak menyebut tabel lain yang dibandingkan; spec memakai Sub-tab Pending Tasks. Perubahan sebelum Reset to Default tidak disimpan sehingga konfigurasi tersimpan tabel ini sama dengan default pada saat perbandingan.
  - TC-FA-SU-567 langkah 2 tidak menyebut pengaturan yang diubah; spec memakai uncheck Division, drag Email satu posisi ke atas, dan pin Name.
  - TC-FA-SU-568 Expected e adalah catatan fixture (satu halaman data) tanpa perilaku UI untuk diasersi.
