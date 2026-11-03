---
id: TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date
title: "Modal Changelog: Setup Column Screening dan Kelas Date"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-198
  - TC-FA-CAID-199
  - TC-FA-CAID-200
  - TC-FA-CAID-201
  - TC-FA-CAID-202
coverage:
  web: automated
---

# Modal Changelog: Setup Column Screening dan Kelas Date

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CHANGELOG_TC_PASSWORD` (Total Control Company Changelog) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; kedua nama didaftarkan di tahap script.
- Data Pre-setup (hanya dibaca): No 15 Company Changelog; No 27 General Settings Company Changelog (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`). Data Dinamis: tidak ada. Nilai L1 sampai L7 adalah data Pre-setup tetap (bukan data Dinamis) sehingga tidak bersuffix `{runId}`; fixture modul Custom Asset ID untuk nilai ini dan teks UI belum ada; prasyarat tahap script yang disediakan tim FE/BE.
- Entri Changelog seed (Pre-setup No 15, urut Date terbaru di atas, pengguna Rina Putri `Rina P`, Sarah Johnson `Sarah J`, Budi Santoso `Budi S`):

| Id | Date | Action | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| L1 | `15/09/26, 14:25` | Edit | Separator | `Dash` | `Dot` | `Rina P` |
| L2 | `14/09/26, 11:30` | Edit | Status | `Inactive` | `Active` | `Sarah J` |
| L3 | `13/09/26, 09:15` | Edit | Status | `Active` | `Inactive` | `Budi S` |
| L4 | `12/09/26, 16:40` | Edit | Separator | `Slash` | `Dash` | `Sarah J` |
| L5 | `10/09/26, 10:02` | Create | Segments Formula | `—` | `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` | `Sarah J` |
| L6 | `10/09/26, 10:01` | Create | Separator | `—` | `Slash` | `Sarah J` |
| L7 | `10/09/26, 10:00` | Create | Status | `—` | `Active` | `Sarah J` |

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Company Changelog dikembalikan tim FE/BE ke keadaan awal (tujuh entri) sebelum tiap run (lihat `suite.md`); spec ini tidak menambah entri Changelog. Entri Changelog tidak bisa dihapus. Entri L1 sampai L7 dan General Settings No 27 dipakai sebagai precondition TC, tidak diasersi pada spec ini (S-11).
- Precondition TC-FA-CAID-198, TC-FA-CAID-199, TC-FA-CAID-200, TC-FA-CAID-201, TC-FA-CAID-202 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan tujuh entri log; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: hover header kolom untuk membaca tooltip; drag and drop elemen daftar kolom pada Popup Setup Column; memperkecil lebar viewport sampai tabel Changelog dapat di-scroll horizontal (nilai lebar tidak ditentukan TC; dipilih spec "sampai scroll horizontal tersedia", lihat Temuan untuk QA); scroll horizontal tabel; menghapus preferensi kolom Modal Changelog di browser (disediakan tim FE).
- Konfigurasi kolom Modal Changelog dimulai dari default (enam kolom tampil, urutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, tanpa pin); hook `before` menghapus preferensi kolom. "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya preferensi tetap ada.
- State global yang dipulihkan: preferensi kolom Modal Changelog dihapus (bukan `[Reset to Default]`) dan viewport dikembalikan ke bawaan di hook `after`.
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-198: Screening overlay Column Visibility pada Changelog

1. Klik tombol `[Changelog]` pada header kartu
2. Hover header kolom `Actions (⋯)`
3. Verifikasi tooltip `Column Visibility` tampil pada header `Actions (⋯)`
4. Klik header kolom `Actions (⋯)`
5. Verifikasi overlay memuat enam kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` dengan checkbox tercentang
6. Verifikasi keenam kolom pada overlay memiliki drag handle
7. Verifikasi overlay memuat item `Setup Column...`

### TC-FA-CAID-199: Screening Popup Setup Column pada Changelog (3 zona)

8. Klik item `Setup Column...`
9. Verifikasi Zona Header: Title `Setup Column`
10. Verifikasi Zona Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi Zona Header: tombol close `[✕]`
12. Verifikasi Zona Body: enam kolom tercentang
13. Verifikasi Zona Body: enam kolom memiliki drag handle
14. Verifikasi Zona Body: enam kolom memiliki icon Pin
15. Verifikasi Zona Body: Live Preview
16. Verifikasi Zona Footer: `[Reset to Default]` dan `[Save]`
17. Verifikasi Zona Footer: tidak ada `[Cancel]`

### TC-FA-CAID-200: Setup Column Hide dan Unhide kelas Date pada Changelog

18. Hilangkan centang `Date`, klik `[Save]`
19. Muat ulang halaman (F5)
20. Klik tombol `[Changelog]` pada header kartu
21. Verifikasi setelah Save dan refresh: kolom `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By` tetap tampil
22. Verifikasi setelah Save dan refresh: kolom `Date` tersembunyi
23. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, centang kembali kolom `Date`, lalu klik `[Save]`
24. Verifikasi setelah dicentang kembali dan Save: kolom `Date` tampil lagi

### TC-FA-CAID-201: Setup Column Drag reorder kelas Date pada Changelog

25. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, seret kolom `Date` ke posisi paling kanan tabel (setelah `Modified By`), lalu klik `[Save]`
26. Muat ulang halaman (F5)
27. Klik tombol `[Changelog]` pada header kartu
28. Verifikasi setelah Save dan refresh: kolom `Date` berada di posisi paling kanan
29. Verifikasi setelah Save dan refresh: urutan kolom menjadi `Action | Field | Old Value | New Value | Modified By | Date`

### TC-FA-CAID-202: Setup Column Pin kelas Date pada Changelog

30. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, klik icon Pin pada kolom `Date`, lalu klik `[Save]`
31. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
32. Scroll tabel secara horizontal
33. Verifikasi kolom `Date` ter-pin ke kiri
34. Verifikasi kolom `Date` tetap di posisinya saat tabel di-scroll horizontal
35. Verifikasi kolom lain yang tidak ter-pin ikut bergeser saat tabel di-scroll horizontal
36. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (198 sampai 202). Screening (198, 199) lebih dulu; TC-FA-CAID-200 (hide, lalu dipulihkan di blok yang sama), 201, dan 202 menyimpan konfigurasi. Modal Changelog dibuka di langkah 1 dan dibuka kembali sesudah tiap muat ulang halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 31 dan 36 (mengatur dan memulihkan viewport agar scroll horizontal teramati). Langkah membuka popup (klik header `Actions (⋯)` lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup karena `[Save]` menutup popup. Pada TC-FA-CAID-200 `Verifikasi` kolom lain tampil mendahului `Verifikasi` kolom `Date` tersembunyi sebagai anchor positif (bagian 8b butir 2); Expected TC memuat keduanya.
- TC-FA-CAID-199 dan 200 memakai popup yang dibuka sekali pada langkah pertama TC-FA-CAID-199; langkah hilangkan centang `Date` TC-FA-CAID-200 dijalankan pada popup yang masih terbuka.
- Pembagian TC lintas spec: Setup Column kelas teks pendek ada di spec 075; kelas nilai campuran di spec 076; batas pin, Reset to Default, close, guard satu kolom, dan cache independen di spec 077; Setup Column Modal View Code List ada di spec 056 dan 057.
- Spec mencapai sekitar 35 langkah (36 langkah) karena TC-FA-CAID-199 memuat tiga zona dengan satu `Verifikasi` per klausa (S-01); semua blok satu kelas harness (Setup Column Modal Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena konfigurasi dikembalikan di dalam blok atau dihapus di hook `after`.
- Alasan satu dataset berada di beberapa spec: Sort (spec 073) dan Setup Column (spec ini dan 075 sampai 077) memakai dataset Pre-setup No 15 (L1 sampai L7) yang sama. Spec 073 sampai 077 berjumlah 137 langkah (35, 36, 19, 19, dan 28), jauh di atas batas sekitar 35 langkah per spec (bagian 3 prinsip 13); tiap spec berdiri sendiri dan Setup Column dibagi menurut Anggota kelas kolom di TC sumber (Date, teks pendek, nilai campuran) serta batas pin, Reset to Default, close, guard, dan cache.
- Temuan untuk QA: (1) TC-FA-CAID-202 menulis "perkecil lebar viewport sehingga tabel dapat di-scroll horizontal" tanpa nilai lebar; spec memperkecil viewport sampai scroll horizontal tersedia (pilihan spec, lihat Prerequisites) dan lebar yang pasti perlu ditetapkan QA. (2) TC-FA-CAID-202 tidak menyebut bahwa kolom `Date` yang di-pin berada di posisi paling kanan sebelum di-pin (sesudah TC-FA-CAID-201 tersimpan) maupun posisi akhirnya terhadap kolom lain; spec hanya mengasersi ter-pin ke kiri, tetap saat scroll, dan kolom lain bergeser. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
