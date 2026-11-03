---
id: TC-AC-SG-E2E-066-isi-file-export-sel-numerik-xlsx-full-path-kolom-group-dan-snapshot-path-changelog
title: "Isi File Export: Sel Numerik XLSX, Full Path Kolom Group, dan Snapshot Path Changelog"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-233
  - TC-AC-SG-236
  - TC-AC-SG-395
  - TC-AC-SG-396
coverage:
  web: automated
---

# Isi File Export: Sel Numerik XLSX, Full Path Kolom Group, dan Snapshot Path Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before` spec ini: akun pertama; halaman dibuka hook `beforeEach` suite):

| Blok TC | Akun | Pre-setup | Email | Password |
|---|---|---|---|---|
| TC-233, TC-236 | Total Control entitas Principal (`Budi Santoso`) | #1, #16 | `totalControlGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-395 | Total Control entitas `Distributor Changelog` | #42 | `totalControlChangelog_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_CHANGELOG_PASSWORD` |
| TC-396 | Total Control entitas `Distributor Race` (akun A) | #32 | `totalControlRaceA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_RACEA_PASSWORD` |

- Hook `after` spec ini memulihkan sesi ke akun default spec (Total Control entitas Principal).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite untuk setiap akun UI suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): `Pohon Uji Utama` entitas Principal (Pre-setup #16), node `All Groups` terpilih, 14 group; `Room 301` berada di bawah `Floor 1` di bawah `Branch 1` di bawah `Region A`. `Distributor Changelog` (Pre-setup #42): seed Changelog Group memuat entri Delete untuk group `Branch 4` yang sudah tidak ada dengan snapshot path `Region B > Branch 4`.
- Data milik spec untuk TC-AC-SG-396 (`Distributor Race`, Pre-setup #32; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari Data Uji TC), di-seed di hook `before` bersuffix per run (S-06, S-12):

| Nama TC | Nama spec | Keterangan |
|---|---|---|
| `Race Induk` | `Race Induk {runId}-066` | node level 1 tanpa entitas, di-seed di `Distributor Race`; target Add Subgroup dan Edit |
| `Anak Snapshot` | `Anak Snapshot {runId}-066` | dibuat spec sebagai subgroup `Race Induk {runId}-066` |
| `Race Induk Baru` | `Race Induk Baru {runId}-066` | nama hasil rename `Race Induk {runId}-066` |

- Hook `before` dan `after` spec ini memulihkan pohon `Distributor Race` ke baseline Pre-setup #32 (menghapus node milik spec) lewat Fixture BE. Entri Changelog Create dan Edit yang dibuat blok TC-396 tidak dapat dihapus (audit trail permanen); entri dikenali lewat nama bersuffix unik (baseline nol, S-12). Efek pada Last Updated dan Modified By node milik spec tidak memengaruhi baseline Pre-setup.
- Kemampuan teknis (kelas f, binary buffer): membaca isi berkas CSV dan XLSX hasil unduhan (nama berkas, nilai dan tipe sel) disediakan tim FE; Fixture BE untuk baseline `Pohon Uji Utama`, pohon `Distributor Race`, dan seed Changelog `Distributor Changelog` disediakan tim FE/BE (lihat `suite.md`).
- Kelima kolom data Group List tampil secara default; preferensi kolom di browser bersih.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-233: Download XLSX menulis angka sebagai sel numerik

1. Klik ikon Download pada toolbar
2. Klik `Download as XLSX`
3. Verifikasi berkas terunduh bernama `Groups.xlsx`
4. Verifikasi kolom Total User dan Total Member bertipe sel angka (bukan teks)

### TC-AC-SG-236: Kolom Group pada file export berisi full path

5. Klik ikon Download pada toolbar
6. Klik `Download as CSV`
7. Verifikasi sel Group baris `Room 301` berisi `Region A > Branch 1 > Floor 1 > Room 301` (full path), bukan nama leaf saja

### TC-AC-SG-395: Hover dan export Group Name Changelog untuk group yang sudah dihapus memakai snapshot full path

8. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Changelog` (`totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_SG_CHANGELOG_PASSWORD`)
9. Buka `Settings > Group` lewat sidebar navigasi
10. Klik ikon Changelog pada toolbar
11. Ketik Search `Branch 4` pada Modal `Changelog: Group`, tekan Enter
12. Hover nilai Group Name pada baris Delete `Branch 4`
13. Verifikasi tooltip menampilkan snapshot full path `Region B > Branch 4` walau group `Branch 4` sudah tidak ada
14. Klik ikon Download di toolbar modal
15. Klik `Download as CSV`
16. Verifikasi sel Group Name baris Delete `Branch 4` pada berkas CSV bernilai `Region B > Branch 4`

### TC-AC-SG-396: Rename group sesudah entri Changelog ditulis tidak mengubah snapshot full path entri lama

17. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Race` (`totalControlRaceA_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_SG_RACEA_PASSWORD`)
18. Buka `Settings > Group` lewat sidebar navigasi
19. Klik ikon `⋯` pada node `Race Induk {runId}-066` di sidebar, lalu klik `+ Add Subgroup`
20. Ketik `Anak Snapshot {runId}-066` pada field nama group
21. Klik `[Submit]`
22. Tunggu aksi selesai (popup tertutup)
23. Klik ikon `⋯` pada node `Race Induk {runId}-066` di sidebar, lalu klik `Edit`
24. Ubah nama menjadi `Race Induk Baru {runId}-066`
25. Klik `[Save]`
26. Tunggu aksi selesai (popup tertutup)
27. Klik ikon Changelog pada toolbar
28. Ketik Search `Anak Snapshot {runId}-066` pada Modal `Changelog: Group`, tekan Enter
29. Hover nilai Group Name pada baris Create `Anak Snapshot {runId}-066`
30. Verifikasi tooltip entri Create menampilkan `Race Induk {runId}-066 > Anak Snapshot {runId}-066` (snapshot saat entri ditulis)
31. Verifikasi tooltip tidak menampilkan `Race Induk Baru {runId}-066 > Anak Snapshot {runId}-066`
32. Klik ikon Download di toolbar modal
33. Klik `Download as CSV`
34. Verifikasi sel Group Name baris Create `Anak Snapshot {runId}-066` pada berkas CSV bernilai `Race Induk {runId}-066 > Anak Snapshot {runId}-066`
35. Ganti isi kotak search modal dengan `Race Induk Baru {runId}-066`, tekan Enter
36. Verifikasi entri Edit tercatat Old Value `Race Induk {runId}-066` dan New Value `Race Induk Baru {runId}-066`

## Notes

- Langkah penghubung (S-03): langkah 9 dan 18 (membuka halaman sesudah ganti akun; hook `beforeEach` suite hanya membuka halaman untuk akun pertama), langkah 11, 28, dan 35 (Search di modal untuk menemukan baris target, R-16 dan S-14), langkah 22 dan 26 (menunggu popup tertutup setelah `[Submit]` dan `[Save]` sebelum Changelog dibaca, R-04 dan bagian 8b butir 8).
- Spec ini 36 langkah, di atas smell sekitar 35 langkah. Alasan: empat blok TC tentang isi file export dan snapshot path pada satu halaman; tiap blok memakai data dan akun sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan langkah ganti akun serta membuka halaman tidak dapat digabung.
- Ganti akun pada langkah 8 dan 17 adalah langkah eksplisit (S-07); akun pertama login di hook `before`.
- Nama group TC-AC-SG-396 (`Race Induk`, `Anak Snapshot`, `Race Induk Baru`) memakai suffix `{runId}-066` pada node milik spec dan teks asersi dibentuk dari nilai bersuffix yang sama (S-06, S-12); hook baseline tidak menghapus entri Changelog.
- Langkah 31 (absence teks) didahului langkah 30 yang membuktikan tooltip menampilkan teks snapshot (8b butir 2).
- Temuan untuk QA:
  - TC-AC-SG-396: TC menyebut "Total Control entitas Distributor Race" tanpa memilih akun A atau B; spec memakai akun A (`totalControlRaceA`).
  - TC-AC-SG-396: Expected c (entri Edit Old Value dan New Value) tidak memiliki langkah observasi di kolom Langkah Uji; spec menambah langkah 35 (Search entri Edit) berdasarkan Expected.
  - TC-AC-SG-395 dan TC-AC-SG-396: TC tidak menyebut nama kolom Changelog untuk jenis aksi (Create, Edit, Delete); baris target dikenali lewat Search dan teks Group Name.
  - TC-AC-SG-233: TC tidak menyebut baris atau sel yang dibaca tipenya; spec mengasersi tipe sel kolom Total User dan Total Member secara keseluruhan.
