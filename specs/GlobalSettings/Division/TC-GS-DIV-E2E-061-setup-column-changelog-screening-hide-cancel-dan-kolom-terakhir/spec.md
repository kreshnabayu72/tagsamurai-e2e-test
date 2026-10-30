---
id: TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir
title: "Setup Column Modal Changelog: Screening, Hide/Unhide, Tutup dengan X, dan Kolom Visible Terakhir"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-213
  - TC-GS-DIV-214
  - TC-GS-DIV-215
  - TC-GS-DIV-219
  - TC-GS-DIV-220
coverage:
  web: automated
---

# Setup Column Modal Changelog: Screening, Hide/Unhide, Tutup dengan X, dan Kolom Visible Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`): Division `Log Div {runId}-061` dibuat oleh Sari Dewi (entri Changelog Action Create oleh `Sari D`), agar riwayat Changelog terisi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division `Log Div {runId}-061`; pulihkan konfigurasi kolom Modal Changelog ke default lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel Changelog. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6) dan Division milik spec ini (1) (disediakan tim FE).
- Konfigurasi kolom tersimpan di `localStorage` browser dengan key unik per tabel (PRD division.md §4.2e; prd-conventions.md §9.3). Hook `before` mengosongkan konfigurasi kolom Modal Changelog sehingga spec mulai dari default (7 kolom tampil). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Kemampuan teknis: hover checkbox disabled untuk membaca tooltip; membaca dan menghapus key `localStorage` browser.
- Precondition TC-GS-DIV-213, 214, 215, 219, 220: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite serial (`parallel: false`) karena konfigurasi kolom disimpan di browser yang sama dengan spec lain.
- State global yang dipulihkan: konfigurasi kolom Changelog (default 7 kolom tampil, tanpa pin) dipulihkan di hook `after`.

## Test Steps

### TC-GS-DIV-213: Screening Overlay Column Visibility Modal Changelog

1. Klik icon Changelog di Table Tools
2. Klik header kolom Actions (⋯)
3. Verifikasi overlay memuat 7 kolom berurutan `Date`, `Action`, `Division Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi ketujuh kolom pada overlay tercentang
5. Verifikasi ketujuh kolom pada overlay memiliki drag handle
6. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-DIV-214: Screening Popup Setup Column Modal Changelog

7. Klik item `Setup Column...` pada overlay
8. Verifikasi bagian Header: Title `Setup Column`
9. Verifikasi bagian Header: Subtitle `Manage column visibility, reorder, and freeze columns.`
10. Verifikasi bagian Header: icon close `[✕]`
11. Verifikasi bagian Body: daftar 7 kolom tercentang
12. Verifikasi bagian Body: ketujuh kolom memiliki drag handle
13. Verifikasi bagian Body: ketujuh kolom memiliki icon pin
14. Verifikasi bagian Body: Preview tabel Changelog
15. Verifikasi bagian Footer: `[Reset to Default]` dan `[Save]`
16. Klik `[✕]` untuk menutup popup tanpa perubahan

### TC-GS-DIV-220: Setup Column Modal Changelog: kolom visible terakhir tidak dapat di-uncheck

17. Klik header Actions (⋯), lalu klik `Setup Column...`
18. Hilangkan centang enam kolom: `Action`, `Division Name`, `Field`, `Old Value`, `New Value`, `Modified By` (tersisa `Date`)
19. Hover checkbox `Date`
20. Verifikasi checkbox `Date` disabled
21. Verifikasi Tooltip `At least one column must remain visible.`
22. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-DIV-219: Setup Column Modal Changelog: X membuang perubahan

23. Klik header Actions (⋯), lalu klik `Setup Column...`
24. Hilangkan centang `Field`
25. Klik `[✕]`
26. Verifikasi kolom `Field` tetap tampil

### TC-GS-DIV-215: Setup Column Modal Changelog: hide dan unhide tiap kolom lalu Save

27. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Date` (kolom lain tetap tercentang), lalu klik `[Save]`
28. Verifikasi kolom `Date` tidak tampil di tabel
29. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Date`, lalu klik `[Save]`
30. Verifikasi kolom `Date` tampil kembali di tabel
31. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Action` (kolom lain tetap tercentang), lalu klik `[Save]`
32. Verifikasi kolom `Action` tidak tampil di tabel
33. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Action`, lalu klik `[Save]`
34. Verifikasi kolom `Action` tampil kembali di tabel
35. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Division Name` (kolom lain tetap tercentang), lalu klik `[Save]`
36. Verifikasi kolom `Division Name` tidak tampil di tabel
37. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Division Name`, lalu klik `[Save]`
38. Verifikasi kolom `Division Name` tampil kembali di tabel
39. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Field` (kolom lain tetap tercentang), lalu klik `[Save]`
40. Verifikasi kolom `Field` tidak tampil di tabel
41. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Field`, lalu klik `[Save]`
42. Verifikasi kolom `Field` tampil kembali di tabel
43. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Old Value` (kolom lain tetap tercentang), lalu klik `[Save]`
44. Verifikasi kolom `Old Value` tidak tampil di tabel
45. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Old Value`, lalu klik `[Save]`
46. Verifikasi kolom `Old Value` tampil kembali di tabel
47. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `New Value` (kolom lain tetap tercentang), lalu klik `[Save]`
48. Verifikasi kolom `New Value` tidak tampil di tabel
49. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `New Value`, lalu klik `[Save]`
50. Verifikasi kolom `New Value` tampil kembali di tabel
51. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Modified By` (kolom lain tetap tercentang), lalu klik `[Save]`
52. Verifikasi kolom `Modified By` tidak tampil di tabel
53. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`
54. Verifikasi kolom `Modified By` tampil kembali di tabel
55. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Modified By` (kolom lain tetap tercentang), lalu klik `[Save]`
56. Muat ulang halaman (F5)
57. Klik icon Changelog di Table Tools
58. Verifikasi Modal Changelog termuat dengan sedikitnya satu baris
59. Verifikasi kolom `Modified By` tetap tidak tampil setelah muat ulang halaman
60. Klik header Actions (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-213, 214, 220, 219, 215. Alasan: dua TC screening (213, 214) di awal; TC-GS-DIV-220 (guard, dibatalkan) dan TC-GS-DIV-219 (X membuang perubahan) sebelum TC-GS-DIV-215 yang menyimpan dan memulihkan konfigurasi (bagian 3 konvensi: aksi yang menyimpan di akhir); TC-GS-DIV-215 berakhir dengan muat ulang halaman lalu pemulihan konfigurasi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 (menutup popup setelah screening), langkah 56 dan 57 (muat ulang halaman lalu klik icon Changelog untuk membuka kembali Modal Changelog yang tertutup oleh muat ulang), langkah 22 (menutup popup TC-GS-DIV-220 tanpa menyimpan, sehingga enam kolom yang di-uncheck dibuang), langkah 60 (mengembalikan `Modified By` ke tampil setelah muat ulang halaman, pemulihan konfigurasi default), dan langkah untuk membuka popup (klik header Actions (⋯) lalu `Setup Column...`) yang digabung dalam langkah aksi TC-GS-DIV-215.
- Langkah 58 (Modal Changelog termuat dengan sedikitnya satu baris sesudah muat ulang halaman) adalah anchor positif untuk asersi ketiadaan kolom `Modified By` pada langkah 59 (S-03, bagian 8b butir 2); Expected TC-GS-DIV-215 tidak memuatnya.
- TC-GS-DIV-215 mengunci tiap kolom dengan langkah "hilangkan centang, `[Save]`, lihat tabel, buka kembali popup, centang kembali"; `[Save]` di langkah centang kembali mengembalikan konfigurasi ke default sebelum kolom berikutnya.
- Pembagian TC Setup Column Changelog: reorder, pin, dan reset ada di spec 062; isolasi konfigurasi kolom tabel Division dan Modal Changelog (TC-GS-DIV-179 dan 234) ada di spec 049.
- Spec melewati sekitar 35 langkah (60 langkah) karena TC-GS-DIV-215 menguji tujuh kolom, masing-masing empat langkah (hide, `Verifikasi` hilang, unhide, `Verifikasi` tampil) sesuai butir Expected a sampai g (S-01); semua blok satu kelas harness (Setup Column Modal Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena konfigurasi dikembalikan ke default di akhir tiap kolom.
- Temuan untuk QA: (1) TC-GS-DIV-214 Expected tidak menyebut tidak adanya `[Cancel]`; spec tidak mengasersinya. Popup Setup Column tidak memiliki `[Cancel]` (prd-conventions.md §24.1).
