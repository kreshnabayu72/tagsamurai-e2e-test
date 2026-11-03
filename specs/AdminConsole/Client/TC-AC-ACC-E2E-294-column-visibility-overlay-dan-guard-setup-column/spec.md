---
id: TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column
title: "Column Visibility Overlay dan Modal Setup Column Client List: Screening, Batas Pin, Penutupan Tanpa Simpan, Kolom Terakhir, Independensi Changelog, dan Reset to Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-406
  - TC-AC-ACC-687
  - TC-AC-ACC-696
  - TC-AC-ACC-695
  - TC-AC-ACC-694
  - TC-AC-ACC-697
  - TC-AC-ACC-408
  - TC-AC-ACC-407
coverage:
  web: automated
---

# Column Visibility Overlay dan Modal Setup Column Client List: Screening, Batas Pin, Penutupan Tanpa Simpan, Kolom Terakhir, Independensi Changelog, dan Reset to Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Kemampuan teknis: menghapus preferensi Setup Column di browser (disediakan tim FE); hook `after` memulihkan preferensi. Tidak butuh klien HTTP, intercept, atau jam server.
- Tabel Changelog Client dan List memakai cache preferensi kolom terpisah.

## Test Steps

### Screening Overlay Column Visibility (TC-AC-ACC-406)

1. Arahkan kursor ke header kolom Actions `(⋯)`
2. Verifikasi tooltip header kolom Actions `Column Visibility`
3. Klik header kolom Actions `(⋯)`
4. Verifikasi panel memuat checkbox dan handle drag untuk 17 kolom: Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated, Company Email, PIC Email, PIC Phone, Industry, Country, State, City
5. Verifikasi kolom Hideable tercentang dan enabled: Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated
6. Verifikasi kolom Curated tidak tercentang dan enabled: Company Email, PIC Email, PIC Phone, Industry, Country, State, City
7. Verifikasi item `Setup Column...` tampil di bagian bawah panel
8. Verifikasi kolom Checkbox dan Actions tidak tercantum sebagai baris panel

### Screening modal Setup Column (TC-AC-ACC-687)

9. Klik item `Setup Column...`
10. Verifikasi Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan ikon close `[✕]` di kanan atas
11. Verifikasi Body: 17 baris kolom (Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated, Company Email, PIC Email, PIC Phone, Industry, Country, State, City) masing-masing dengan checkbox, handle drag, dan ikon Pin
12. Verifikasi Body: 10 kolom Hideable tercentang dan 7 kolom Curated tidak tercentang
13. Verifikasi Body: tabel di balik modal menampilkan 10 kolom data bersama kolom Checkbox dan Actions
14. Verifikasi Body: kolom Checkbox dan Actions tidak tercantum sebagai baris modal
15. Verifikasi Footer: `[Reset to Default]` (teks, primary) dan `[Save]` (filled, success)
16. Verifikasi Footer: tidak ada tombol `[Cancel]`

### Kolom terakhir yang tampil disabled pada modal (TC-AC-ACC-696)

17. Hapus centang Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, dan Modified By satu per satu
18. Verifikasi hanya Last Updated yang tercentang
19. Verifikasi checkbox Last Updated tetap tampil namun disabled
20. Arahkan kursor ke checkbox Last Updated
21. Verifikasi tooltip checkbox Last Updated `At least one column must remain visible.`
22. Klik checkbox Last Updated
23. Verifikasi checkbox Last Updated tetap tercentang dan disabled
24. Verifikasi Last Updated tetap tampil di tabel di balik modal (tabel belum berubah sebelum [Save], D-065)
25. Centang Company Name
26. Verifikasi checkbox Last Updated enabled kembali
27. Klik `[✕]` untuk menutup modal tanpa menyimpan

### Menutup modal tanpa menyimpan (TC-AC-ACC-695)

28. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, hapus centang PIC Name, lalu klik `[✕]`
29. Verifikasi modal tertutup
30. Verifikasi kolom PIC Name tetap tampil di tabel (state tersimpan terakhir)
31. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, hapus centang PIC Name, lalu tekan Esc
32. Verifikasi modal tertutup
33. Verifikasi kolom PIC Name tetap tampil di tabel
34. Tekan F5
35. Verifikasi kolom PIC Name tetap tampil

### Pin keempat diblok (TC-AC-ACC-694)

36. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
37. Klik ikon Pin pada Company Name, Client Code, dan PIC Name
38. Arahkan kursor ke ikon Pin Managed By
39. Verifikasi ikon Pin Managed By disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
40. Klik ikon Pin Managed By
41. Verifikasi klik pada ikon Pin yang disabled tidak membekukan Managed By
42. Unpin PIC Name
43. Arahkan kursor ke ikon Pin Managed By
44. Verifikasi ikon Pin Managed By enabled kembali
45. Klik `[✕]` untuk menutup modal tanpa menyimpan

### Kolom terakhir yang tampil disabled pada overlay (TC-AC-ACC-697)

46. Klik header kolom Actions `(⋯)`
47. Hapus centang Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, dan Modified By satu per satu
48. Verifikasi hanya Last Updated yang tercentang dan tabel langsung hanya menampilkan kolom Last Updated
49. Verifikasi checkbox Last Updated tetap tampil namun disabled
50. Arahkan kursor ke checkbox Last Updated
51. Verifikasi tooltip checkbox Last Updated `At least one column must remain visible.`
52. Klik checkbox Last Updated
53. Verifikasi Last Updated tetap tampil di tabel
54. Centang Company Name
55. Verifikasi checkbox Last Updated enabled kembali
56. Klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]` (pemulihan konfigurasi kolom ke default)

### Pengaturan kolom List independen dari Changelog (TC-AC-ACC-408)

57. Klik `[Changelog]` di toolbar List dan catat kolom tabel modal Changelog: Client (baseline), lalu tutup modal
58. Klik header kolom Actions `(⋯)` lalu hapus centang kolom Group di List
59. Klik `[Changelog]` di toolbar List
60. Verifikasi kolom modal Changelog: Client tidak terpengaruh: sama dengan baseline
61. Tutup modal Changelog, lalu klik header kolom Actions `(⋯)` dan centang kolom Group kembali

### Reset to Default (TC-AC-ACC-407)

62. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
63. Hapus centang Group, centang Industry, seret Last Updated ke posisi pertama, klik ikon Pin pada PIC Name, lalu klik `[Save]`
64. Verifikasi tabel menampilkan konfigurasi kustom: Group hilang, Industry tampil, Last Updated paling kiri, PIC Name terpin
65. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, lalu klik `[Reset to Default]`
66. Verifikasi daftar kolom di popup: 10 kolom Hideable tercentang dengan urutan Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated
67. Verifikasi 7 kolom Curated tidak tercentang
68. Verifikasi tidak ada kolom terpin
69. Verifikasi tabel di balik modal masih menampilkan konfigurasi kustom langkah 63 (Group hilang, Industry tampil) sebelum [Save] (Reset baru berlaku setelah [Save], D-065)
70. Klik `[Save]`, lalu tekan F5
71. Verifikasi tabel tetap memakai konfigurasi default tersebut

## Notes

- Urutan TC disusun ulang (S-10): screening (406, 687) di awal, guard tanpa Save (696, 695, 694), lalu overlay yang langsung berlaku (697) beserta pemulihan Reset to Default, independensi Changelog (408), dan TC-AC-ACC-407 (menyimpan konfigurasi kustom) paling akhir karena mengubah preferensi yang tersimpan.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness dan satu dataset (Setup Column List), blok memulihkan state sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): `[✕]` penutup modal, `Setup Column...`/`[Reset to Default]`/`[Save]` pemulihan Post Condition, dan baseline kolom Changelog sebelum aksi (S-12).
- Keselarasan TC dan spec
  - TC-AC-ACC-696 dan 407: TC sudah diselaraskan pada 2026-11-03 sesuai `docs/spec-decisions.md` D-065 (tabel di balik popup tidak berubah sampai [Save]; menutup popup tanpa Save membuang perubahan); spec dan TC sama. langkah 24 mengasersi tabel belum berubah, langkah 69 mengasersi tabel masih kustom sebelum [Save], dan konfigurasi default diasersi setelah [Save] dan F5 (langkah 71). TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview. TC-AC-ACC-697 memakai panel Column Visibility (bukan popup) yang berlaku langsung dan tidak terdampak; TC-AC-ACC-695 sudah sesuai D-065. Sisa konflik hanya `prd-conventions.md` §9.3 (di luar scope suite, dilaporkan ke pemilik foundation).
  - TC-AC-ACC-408: Expected `Kolom modal Changelog tidak terpengaruh` tanpa daftar kolom; spec memakai baseline kolom modal yang dicatat sebelum aksi.
  - TC-AC-ACC-407: Expected butir (a) mengasersi tabel setelah [Save] dan Expected (b) preview setelah [Reset to Default]; spec menulis keduanya.
