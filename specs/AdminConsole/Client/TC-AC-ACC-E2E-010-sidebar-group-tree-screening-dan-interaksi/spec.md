---
id: TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi
title: "Sidebar Group Tree: Screening, Klik Node, Search Groups, Hierarchy Toggle, dan Collapse"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-27
  - TC-AC-ACC-28
  - TC-AC-ACC-29
  - TC-AC-ACC-30
  - TC-AC-ACC-31
  - TC-AC-ACC-32
coverage:
  web: automated
---

# Sidebar Group Tree: Screening, Klik Node, Search Groups, Hierarchy Toggle, dan Collapse

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Tree Group baseline delapan node (Hierarki Tabel A1). State collapse panel Sidebar Group Tree (persisten) dibuka kembali pada langkah spec; pilihan node dikembalikan ke `[All Groups]` dan sub-tab ke `Active` dalam spec.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-27: Screening Sidebar Group Tree

1. Amati panel kanan Sidebar Group Tree
2. Verifikasi header `Groups` tampil tanpa tombol close
3. Arahkan kursor ke floating handle di tepi panel
4. Verifikasi tooltip floating handle `Collapse Group Tree`
5. Verifikasi input `Search groups...` dan ikon hierarchy toggle tampil sejajar
6. Verifikasi opsi `[All Groups]` terpilih (highlight + teks bold)
7. Klik ikon hierarchy toggle (expand all)
8. Verifikasi tree menampilkan delapan node: `Regional Barat` > `Area Jakarta` > `Cabang Menteng`; `Regional Barat` > `Cabang Bekasi`; `Regional Barat` > `Cabang Kemang`; `Regional Timur` > `Area Surabaya` > `Cabang Rungkut`
9. Verifikasi tidak ada badge count per node

### TC-AC-ACC-30: Hierarchy toggle: expand semua level lalu collapse ke level 1

10. Klik ikon hierarchy toggle sampai tree collapse ke level 1 (keadaan awal)
11. Klik ikon hierarchy toggle
12. Verifikasi semua level tree ter-expand
13. Klik ikon hierarchy toggle sekali lagi
14. Verifikasi tree kembali collapse ke level 1

### TC-AC-ACC-28: Klik node Group memfilter tabel secara eksklusif dan hanya satu node aktif

15. Catat jumlah total baris sub-tab `Active` dengan `[All Groups]` terpilih (baseline)
16. Klik node `Area Surabaya`
17. Verifikasi node `Area Surabaya` aktif (highlight + teks bold)
18. Verifikasi `[All Groups]` tidak aktif
19. Verifikasi sedikitnya satu baris tampil pada tabel
20. Verifikasi tabel hanya memuat Client dengan Group `Area Surabaya` (`PT Timur Perkasa`)
21. Klik node `Area Jakarta`
22. Verifikasi hanya `Area Jakarta` aktif
23. Klik `[All Groups]`
24. Verifikasi hanya `[All Groups]` aktif
25. Verifikasi tidak ada filter Group (jumlah total baris sub-tab `Active` sama dengan baseline)
26. Verifikasi selalu tepat satu opsi aktif pada tree

### TC-AC-ACC-29: Search groups tanpa membedakan huruf besar-kecil dan meng-expand node

27. Klik ikon hierarchy toggle sampai tree collapse ke level 1
28. Ketik `menteng` pada input `Search groups...`
29. Verifikasi node `Cabang Menteng` ditemukan (case-insensitive)
30. Verifikasi tree meng-expand sampai node `Cabang Menteng`
31. Kosongkan input `Search groups...`

### TC-AC-ACC-32: Pilihan node dipertahankan saat pindah sub-tab bila masih valid

32. Klik node `Area Jakarta`
33. Klik sub-tab `Suspended`
34. Verifikasi node `Area Jakarta` tetap terpilih
35. Verifikasi sedikitnya satu baris tampil pada tabel `Suspended`
36. Verifikasi tabel `Suspended` terfilter Group tersebut (setiap baris pada halaman memiliki Group `Area Jakarta`)
37. Klik `[All Groups]` dan klik sub-tab `Active`

### TC-AC-ACC-31: Panel Sidebar Group Tree dapat di-collapse dan status collapse dipertahankan

38. Klik floating handle di tepi panel Sidebar Group Tree (tooltip `Collapse Group Tree`)
39. Verifikasi panel collapse
40. Arahkan kursor ke floating handle
41. Verifikasi floating handle ber-tooltip `Open Group Tree`
42. Verifikasi lebar tabel menyesuaikan
43. Muat ulang halaman (F5)
44. Verifikasi status collapse panel tetap setelah refresh
45. Klik floating handle `Open Group Tree` sampai panel terbuka kembali

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 10, 27, 31, 37, 45. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-27, 30, 28, 29, 32, 31 (semula 27 sampai 32); TC-AC-ACC-30 dipindah tepat sesudah 27 karena TC-27 langkah 2 sudah meng-expand seluruh level dan TC-30 butuh keadaan awal collapse; TC-AC-ACC-31 di akhir karena mengubah state persisten (collapse panel) yang dipulihkan sesudahnya.
- TC-AC-ACC-27 butir a: tooltip floating handle "Collapse Group Tree" / "Open Group Tree" diasersi untuk handle dalam keadaan panel terbuka (`Collapse Group Tree`); tooltip `Open Group Tree` diasersi pada TC-AC-ACC-31 (langkah 41) setelah panel collapse.
- Hitungan mutlak hanya untuk node Area Surabaya (populasi tertutup Tabel A3: Active 1, `PT Timur Perkasa`); node lain memakai baseline relatif atau asersi tiap baris.
- Pembagian TC lintas spec: tree per viewer dan per sub-tab (TC-AC-ACC-33, 34, 557) ada di spec 011; tree klik node Partner per viewer di spec 013, 015, dan 018.
- Ukuran spec (45 langkah, melewati sekitar 35 langkah): satu dataset (tree Group dan List), tanpa aksi tulis, dan tiap blok TC memulai dari keadaan eksplisit (collapse ke level 1, sub-tab Active) sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-28 dan 32: TC tidak menyatakan apakah memilih node Group memasukkan Client pada descendant node; asersi spec ditulis "hanya Client dengan Group node itu" mengikuti kalimat Expected.
  - TC-AC-ACC-32: Expected "tabel Suspended terfilter group tersebut" tidak menyebut Client mana yang tampil; spec mengasersi tiap baris halaman ber-Group `Area Jakarta`.
