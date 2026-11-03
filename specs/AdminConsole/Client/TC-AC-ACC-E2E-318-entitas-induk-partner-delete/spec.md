---
id: TC-AC-ACC-E2E-318-entitas-induk-partner-delete
title: "Client Derived Saat Entitas Induk Partner Di-Delete: Tidak Diblokir, Menjadi Direct, Dapat Diedit, Default User Bersama Tetap Ada, dan Jejak Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1001
  - TC-AC-ACC-1002
  - TC-AC-ACC-444
coverage:
  web: automated
---

# Client Derived Saat Entitas Induk Partner Di-Delete: Tidak Diblokir, Menjadi Direct, Dapat Diedit, Default User Bersama Tetap Ada, dan Jejak Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-1001: P-FX15-1 dan C-FX15-1 -> `CV Mitra Hapus Bawah Distributor {runId}-317` (Partner di bawah Distributor PT Distribusi Nusantara, Group Cabang Menteng; Client Code `FX15-001`, Company Email `fx15-001@qwertysystem.net`, PIC Name `Hendra Kusuma`, Industry `Retail`; Group Area Jakarta pada view Principal; FAMS Active).
  - TC-AC-ACC-1002: P-FX15-2 dan C-FX15-2 -> `CV Mitra Hapus Mandiri {runId}-317` (Partner langsung di bawah Principal; Group Cabang Bekasi; Client Code `FX15-002`, Company Email `fx15-002@qwertysystem.net`, PIC Name `Maya Anggraini`, Industry `Logistics`; FAMS Active).
  - TC-AC-ACC-444: P-FX15-5 dan C-FX15-8 -> `CV Mitra Hapus Default User {runId}-317` (Partner langsung di bawah Principal; Default User bersama email `fx15-008@qwertysystem.net`; Group Cabang Bekasi; FAMS Active).
- Kemampuan teknis: kemampuan membaca Activity Log (Admin Console > Activity Log) dan System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log); baseline hitungan baris log dicatat sebelum aksi dengan Search nama bersuffix (S-12). Tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Delete entitas induk di bawah Distributor (TC-AC-ACC-1001)

1. Kembali ke List, klik sub-tab Active, ketik Search `CV Mitra Hapus Bawah Distributor {runId}-317`, tekan Enter, klik Company Name `CV Mitra Hapus Bawah Distributor {runId}-317`, dan catat badge Derived, Client Code, Company Email, PIC Name, Industry, dan Group pada Detail
2. Verifikasi badge `Derived`
3. Verifikasi Client Code `FX15-001`
4. Verifikasi Group `Area Jakarta` (hasil resolusi Anchor Distributor pada view Principal)
5. Buka Admin Console > Partner, ketik Search `CV Mitra Hapus Bawah Distributor {runId}-317`, tekan Enter, buka `⋯` baris itu → Delete, lalu klik `[Delete]` pada dialog Delete Partner
6. Verifikasi toast `Success, partner has been deleted.` tanpa dialog blok `Cannot Delete Partner` (Client Derived)
7. Buka Admin Console > Client, klik sub-tab Active, ketik Search `CV Mitra Hapus Bawah Distributor {runId}-317`, tekan Enter
8. Verifikasi baris `CV Mitra Hapus Bawah Distributor {runId}-317` tampil di sub-tab Active tanpa badge `Derived`
9. Verifikasi Managed By `PT Distribusi Nusantara (Direct)` (relasi Distributor-langsung)
10. Verifikasi Group `Area Jakarta`
11. Verifikasi sel FAMS `Active`
12. Verifikasi Client Code `FX15-001`
13. Klik Company Name `CV Mitra Hapus Bawah Distributor {runId}-317`
14. Verifikasi header tanpa badge `Derived from [nama]`
15. Verifikasi Company Name, Company Email, PIC Name, dan Industry sama dengan nilai yang dicatat
16. Kembali ke List lalu buka `⋯` baris `CV Mitra Hapus Bawah Distributor {runId}-317`
17. Verifikasi menu `⋯` memuat `Detail | Edit | Change Partner | Suspend`
18. Klik Edit, ubah Company Name menjadi `CV Mitra Hapus Bawah Distributor {runId}-317 Ubah`, lalu klik `[Save]`
19. Verifikasi field Company Name dapat diedit
20. Verifikasi toast `Success, client has been updated.`
21. Verifikasi baris tampil dengan Company Name `CV Mitra Hapus Bawah Distributor {runId}-317 Ubah`
22. Kembali ke List, klik `[Changelog]` di toolbar, ketik Search `CV Mitra Hapus Bawah Distributor {runId}-317` di Search modal, tekan Enter
23. Verifikasi Modal Changelog Client memuat tepat satu baris, Action `Edit` (Field Company Name dari langkah edit)
24. Verifikasi tidak ada baris Action `Delete`, `Change Partner`, atau Action lain akibat Delete Partner
25. Buka Admin Console > Activity Log lalu cari baris dengan Object `Client` dan Name `CV Mitra Hapus Bawah Distributor {runId}-317`
26. Verifikasi Activity Log tidak memuat baris Object `Client` selain baris Action `Edit` dari langkah edit
27. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `CV Mitra Hapus Bawah Distributor {runId}-317`, tekan Enter
28. Verifikasi System Log akun aktor tidak memuat baris Object `Client` selain baris Action `Edit` dari langkah edit (jejak Delete Partner hanya berobjek Partner)

### Delete entitas induk langsung di bawah Principal (TC-AC-ACC-1002)

29. Buka Admin Console > Partner, ketik Search `CV Mitra Hapus Mandiri {runId}-317`, tekan Enter, buka `⋯` baris itu → Delete, lalu klik `[Delete]` pada dialog Delete Partner
30. Verifikasi toast `Success, partner has been deleted.`
31. Buka Admin Console > Client, klik sub-tab Active, ketik Search `CV Mitra Hapus Mandiri {runId}-317`, tekan Enter
32. Verifikasi baris `CV Mitra Hapus Mandiri {runId}-317` tampil di sub-tab Active tanpa badge `Derived`
33. Verifikasi Managed By `Direct`
34. Verifikasi Group `Cabang Bekasi`
35. Verifikasi sel FAMS `Active`
36. Verifikasi Client Code `FX15-002`
37. Klik Company Name `CV Mitra Hapus Mandiri {runId}-317`
38. Verifikasi header tanpa badge `Derived from [nama]`
39. Verifikasi Company Email `fx15-002@qwertysystem.net`, PIC Name `Maya Anggraini`, dan Industry `Logistics` tetap tampil
40. Kembali ke List lalu buka `⋯` baris `CV Mitra Hapus Mandiri {runId}-317`
41. Verifikasi menu `⋯` memuat `Detail | Edit | Change Partner | Suspend`
42. Klik Edit
43. Verifikasi form Edit memuat field Select Group (Client Direct) dengan nilai `Cabang Bekasi`
44. Verifikasi field Company Name dapat diedit
45. Tutup form Edit lewat `✕` (form tidak berubah, sehingga tidak ada dialog `Unsaved Changes`)
46. Kembali ke List, klik `[Changelog]` di toolbar, ketik Search `CV Mitra Hapus Mandiri {runId}-317` di Search modal, tekan Enter
47. Verifikasi Modal Changelog Client menampilkan empty state `No results found` untuk `CV Mitra Hapus Mandiri {runId}-317` (Delete Partner tidak menulis entri di sisi Client)
48. Buka Admin Console > Activity Log lalu cari baris dengan Object `Client` dan Name `CV Mitra Hapus Mandiri {runId}-317`
49. Verifikasi Activity Log tidak memuat baris Object `Client` dengan Name `CV Mitra Hapus Mandiri {runId}-317` (anchor: pencarian menampilkan empty state `No results found`)
50. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `CV Mitra Hapus Mandiri {runId}-317`, tekan Enter
51. Verifikasi System Log akun aktor tidak memuat baris Object `Client` dengan Name `CV Mitra Hapus Mandiri {runId}-317` (anchor: pencarian menampilkan empty state `No results found`)

### Default User bersama tidak ikut dihapus (TC-AC-ACC-444)

52. Buka Admin Console > Partner, ketik Search `CV Mitra Hapus Default User {runId}-317`, tekan Enter, buka `⋯` baris itu → Delete, lalu klik `[Delete]` pada dialog Delete Partner
53. Verifikasi toast `Success, partner has been deleted.`
54. Buka Global Settings tenant Client > User dan lihat Default User `CV Mitra Hapus Default User {runId}-317`
55. Verifikasi Default User dengan email `fx15-008@qwertysystem.net` tetap ada di daftar User (tidak ikut dihapus)

## Notes

- Kelas g (absence log) berada di spec ini dengan P-1 (state berat): asersi `tidak ada baris/entri` pada TC-AC-ACC-1001 dan 1002 bergantung pada aksi Delete Partner yang dibangun di spec ini; anchor positif memakai baris Action `Edit` atau empty state hasil Search pada surface yang sama (bagian 8b butir 2) dan nama bersuffix per run sebagai baseline (S-12). Tidak ada spec absence terpisah yang memuat aksi TC ini.
- Aksi Delete Partner menghabisi data; ketiga TC memakai Partner berbeda sehingga urutan di dalam spec tidak saling bergantung; TC-AC-ACC-444 (Delete tanpa pengamatan lanjut) paling akhir (prinsip 5).
- Spec melewati sekitar 35 langkah; alasan: semua blok satu topik (Delete entitas induk) dan satu kelas harness, data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi. Langkah 45 (tutup form Edit lewat `✕`) menghubungkan langkah 5 dan 6 TC-AC-ACC-1002.
- Temuan untuk QA
  - TC-AC-ACC-1002 langkah 5 (`Klik Edit`) dan langkah 6 (`Kembali ke List, klik [Changelog] ...`) tidak menyebut cara menutup form Edit; spec menutup lewat `✕` pada langkah 45 (form tidak berubah sehingga tidak ada dialog `Unsaved Changes`) sebelum `Kembali ke List`.
  - TC-AC-ACC-1001, 1002: Expected `System Log/Activity Log tidak memuat baris Object Client` tanpa pembanding positif yang disebut TC; spec memakai empty state Search atau baris `Edit` sebagai anchor.
  - TC-AC-ACC-444: Langkah `Buka Global Settings tenant Client > User` tidak menyebut cara masuk ke konteks tenant Client.
