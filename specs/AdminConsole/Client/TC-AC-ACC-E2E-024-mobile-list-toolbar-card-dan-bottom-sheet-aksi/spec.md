---
id: TC-AC-ACC-E2E-024-mobile-list-toolbar-card-dan-bottom-sheet-aksi
title: "Mobile List Client: Toolbar, Card List, dan Bottom Sheet Aksi per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-862
  - TC-AC-ACC-417
  - TC-AC-ACC-863
coverage:
  mobile: automated
---

# Mobile List Client: Toolbar, Card List, dan Bottom Sheet Aksi per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama (Total Control, A-01) di aplikasi Android dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01).
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Platform: aplikasi native Android (PRD §4.6 List (Card)); tampilan berupa Card List dan bottom sheet. Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang, serta kemampuan mengetuk, menggeser horizontal, dan mengetik di aplikasi.
- Ketiga TC bertanda `Manual Only (b)` di sumber; menurut bagian 2 konvensi hambatan teknis bukan alasan keluar dari spec, sehingga kebutuhan perangkat ditulis di sini dan tim FE menyiapkan environment-nya.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-862: Mobile List: sub-tab dapat digeser horizontal, toolbar mobile, dan CTA + New Client

1. Buka halaman Client di aplikasi Android
2. Geser sub-tab secara horizontal
3. Verifikasi sub-tab `Active`, `Suspended`, dan `Archived` tampil di atas daftar card
4. Verifikasi sub-tab dapat digeser horizontal
5. Lihat toolbar mobile
6. Verifikasi toolbar mobile menampilkan ikon pencarian dan ikon `⋯`
7. Ketuk ikon `⋯` pada toolbar mobile
8. Verifikasi ikon `⋯` membuka menu berisi `Filter` dan `Download`
9. Verifikasi ikon `Changelog` tampil di header halaman, bukan di menu `⋯`
10. Verifikasi CTA `[+ New Client]` tampil di bawah toolbar dan di atas daftar card
11. Tutup menu `⋯`

### TC-AC-ACC-417: Mobile List: tabel diganti Card List

12. Ketuk ikon Search, ketik Search `PT Sejahtera Abadi`, lalu submit
13. Lihat card `PT Sejahtera Abadi`
14. Verifikasi baris 1 card: `PT Sejahtera Abadi` (tebal) dan badge status `Active`
15. Verifikasi baris 2 card: `SJA-001` (muted) | `Managed By: CV Mitra Sejati`
16. Geser badge produk pada card secara horizontal
17. Verifikasi baris 3 card: `FAMS: Active`, `SAMS: Active`, `SIEM: Active` sebagai satu badge per produk
18. Verifikasi baris 3 card dapat digeser horizontal
19. Verifikasi baris 4 card: `Group: ` diikuti badge severity primary bertuliskan `Area ..karta` (nama Group 12 karakter, lebih dari 10 karakter di mobile sehingga dipotong 5 huruf pertama + `..` + 5 huruf terakhir)
20. Verifikasi ikon `⋯` tampil pada card
21. Ketuk chip `Group` di atas sub-tab
22. Verifikasi chip `Group` membuka bottom sheet tree picker
23. Tutup bottom sheet tree picker dan hapus isi Search

### TC-AC-ACC-863: Mobile List: bottom sheet aksi card per sub-tab Active, Suspended, dan Archived

24. Ketik Search `PT Sejahtera Abadi` pada sub-tab `Active`, lalu submit
25. Ketuk `⋯` pada card `PT Sejahtera Abadi`
26. Verifikasi bottom sheet `Active` memuat `Detail`, `Edit`, `Change Partner`, dan `Suspend`
27. Verifikasi `Unsuspend` dan `Delete` tidak tampil pada bottom sheet `Active`
28. Tutup bottom sheet
29. Ketuk sub-tab `Suspended`
30. Ketik Search `PT Wahana Nusantara`, lalu submit
31. Ketuk `⋯` pada card `PT Wahana Nusantara`
32. Verifikasi bottom sheet `Suspended` memuat `Detail` dan `Unsuspend`
33. Verifikasi `Edit`, `Change Partner`, `Suspend`, dan `Delete` tidak tampil pada bottom sheet `Suspended`
34. Tutup bottom sheet
35. Ketuk sub-tab `Archived`
36. Ketik Search `PT Karya Abadi`, lalu submit
37. Ketuk `⋯` pada card `PT Karya Abadi`
38. Verifikasi bottom sheet `Archived` memuat `Detail`, `Edit`, dan `Delete`
39. Verifikasi `Change Partner`, `Suspend`, dan `Unsuspend` tidak tampil pada bottom sheet `Archived`
40. Tutup bottom sheet dan hapus isi Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 11, 23, 24, 30, 36, 40. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-862, 417, 863 (semula 417, 862, 863); screening toolbar didahulukan, lalu isi card, lalu aksi.
- Asersi absence menu pada bottom sheet memakai item menu yang tampil pada `Verifikasi` tepat sebelumnya sebagai anchor positif pada surface yang sama (bagian 8b butir 2).
- TC-AC-ACC-863 langkah 'Tutup bottom sheet' ditulis sebagai langkah TC (langkah 2 dan 4 TC); Search dipakai untuk menemukan card target karena daftar berpaginasi dan populasi fixture A3 menambah card.
- Ukuran spec (40 langkah, melewati sekitar 35 langkah): semua blok satu kelas (aplikasi Android, satu akun, tanpa aksi tulis) dan tiap blok TC dimulai dari state eksplisit (halaman Client, Search, atau sub-tab dipilih di awal blok) sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-417, 862, 863: kolom Automation `Manual Only — (b) aplikasi native Android`; spec ditulis sebagai `coverage.mobile: automated` mengikuti bagian 2 konvensi (hambatan teknis bukan alasan keluar). Bila tim FE tidak dapat menyiapkan perangkat, spec ditandai `coverage.mobile: unsupported`.
  - TC-AC-ACC-417: judul menyebut "tabel diganti Card List" tetapi Expected tidak memuat klausa itu; spec tidak menambah `Verifikasi` untuk klausa judul.
