---
id: TC-FA-SU-E2E-189-tab-non-login-user-setup-column-bagian-2
title: "Tab Non-Login User: Setup Column (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-563
  - TC-FA-SU-564
  - TC-FA-SU-565
coverage:
  web: automated
---

# Tab Non-Login User: Setup Column (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Custom Field Shift (Pre-setup #31, `FaUserMain`): Gudang Cabang Bekasi `Morning`, Kendaraan Operasional B 1234 XY `Night`, Mesin Fotokopi Lt.3 `Morning`, Printer Lantai 5 `Night`, Ruang Meeting Anggrek `Morning`; kolom curated Shift muncul setelah ditampilkan lewat Setup Column.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Tabel parameter "Putaran pin Non-Login User" (putaran 1 ditulis eksplisit pada langkah awal TC-FA-SU-563; batas maksimum 3 kolom per putaran):

| Putaran | Kolom |
|---|---|
| Putaran 2 | `Position`, `Division`, `Active` |
| Putaran 3 | `Last Update` |
- Tabel parameter "Urutan drag kolom curated" (urutan awal: `Temporary User`, `Temporary Until`, `Shift`):

| No | Kolom yang di-drag | Arah (satu posisi) | Urutan kolom sesudah drag |
|---|---|---|---|
| 1 | `Shift` | atas | `Temporary User`, `Shift`, `Temporary Until` |
| 2 | `Temporary User` | bawah | `Shift`, `Temporary User`, `Temporary Until` |
| 3 | `Temporary Until` | atas | `Shift`, `Temporary Until`, `Temporary User` |

## Test Steps

1. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-563: Pin dan unpin Setup Column kelas Hideable

2. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
3. Klik icon Pin pada kolom `Name`, `Email`, `Employee ID` (satu klik per kolom)
4. Hover icon Pin kolom `Position`
5. Verifikasi icon Pin kolom `Position` disabled sesudah tiga kolom di-pin
6. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
7. Klik `[Save]`
8. Scroll tabel secara horizontal
9. Verifikasi kolom `Name`, `Email`, `Employee ID` membeku di kiri saat tabel di-scroll horizontal
10. Tekan F5
11. Verifikasi kolom `Name`, `Email`, `Employee ID` tetap membeku di kiri setelah refresh
12. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
13. Klik icon Pin (unpin) pada kolom `Name`, `Email`, `Employee ID`
14. Klik `[Save]`
15. Verifikasi kolom `Name`, `Email`, `Employee ID` dilepas dan tidak lagi membeku
16. Untuk setiap baris tabel "Putaran pin Non-Login User" (langkah 16 sampai 26): klik header kolom Actions (⋯), lalu klik `Setup Column...`
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

### TC-FA-SU-564: Ceklis dan unceklis Setup Column kelas Curated

27. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
28. Centang kolom `Temporary User`, `Temporary Until`, dan `Shift` pada daftar Setup Column
29. Verifikasi Live Preview menampilkan kolom `Temporary User`, `Temporary Until`, dan `Shift`
30. Klik `[Save]`
31. Verifikasi tabel menampilkan kolom `Temporary User`, `Temporary Until`, dan `Shift`
32. Tekan F5
33. Verifikasi tabel tetap menampilkan kolom `Temporary User`, `Temporary Until`, dan `Shift` setelah refresh
34. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
35. Hilangkan centang kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`, `Temporary User`, `Temporary Until` pada daftar Setup Column (satu per satu)
36. Hover checkbox kolom Shift
37. Verifikasi checkbox kolom Shift disabled sebagai satu-satunya kolom visible
38. Verifikasi tooltip `At least one column must remain visible.`
39. Klik ✕ pada popup Setup Column

### TC-FA-SU-565: Geser (drag reorder) Setup Column kelas Curated

40. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
41. Untuk setiap baris tabel "Urutan drag kolom curated" (langkah 41 sampai 42): drag kolom baris itu satu posisi sesuai kolom "Arah" baris itu
42. Verifikasi urutan Live Preview sama dengan kolom "Urutan kolom sesudah drag" baris itu
43. Klik `[Save]`
44. Verifikasi urutan kolom tabel sama dengan kolom "Urutan kolom sesudah drag" baris terakhir
45. Tekan F5
46. Verifikasi urutan kolom tabel tetap sama dengan baris terakhir tabel parameter setelah refresh

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; membuka Setup Column, `[Save]`, dan unpin pada tiap putaran pin (mengosongkan kuota 3 pin untuk putaran berikutnya, S-09); `✕` menutup popup Setup Column tanpa menyimpan uncheck sembilan kolom pada TC-FA-SU-564.
- Langkah uncheck sembilan kolom pada TC-FA-SU-564 ditambahkan sebagai langkah menuju keadaan Expected d (satu-satunya kolom visible, S-14); TC-FA-SU-565 bergantung pada kolom curated yang sudah ditampilkan TC-FA-SU-564 dalam spec yang sama.
- Verifikasi pin per putaran memuat daftar tiga kolom yang disebut utuh dalam satu butir.
- Langkah berulang per baris tabel parameter: tabel "Putaran pin Non-Login User" pada langkah 16 sampai 26 (2 iterasi); tabel "Urutan drag kolom curated" pada langkah 41 sampai 42 (3 iterasi).
- Jumlah langkah: 46 tertulis, 61 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (61 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-563 langkah 3 meminta pin pada ketujuh kolom sedangkan Expected h membatasi maksimum 3 kolom; spec mem-pin dalam putaran tiga kolom dan melepasnya sebelum putaran berikutnya.
  - TC-FA-SU-563 langkah 5 hanya meng-unpin satu kolom; spec meng-unpin seluruh kolom putaran supaya kuota pin kembali.
  - TC-FA-SU-564 Expected d (kolom terakhir tidak dapat di-uncheck) tidak punya langkah menuju keadaannya; spec menambah langkah uncheck sembilan kolom lain tanpa menyimpan.
  - TC-FA-SU-565 tidak menyebut arah drag; arah per kolom ditetapkan di tabel parameter (S-15).
