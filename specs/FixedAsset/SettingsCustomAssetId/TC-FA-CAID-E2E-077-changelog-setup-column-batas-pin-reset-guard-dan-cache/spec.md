---
id: TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache
title: "Modal Changelog: Batas Pin, Reset to Default, Close, Guard Satu Kolom, dan Cache Independen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-209
  - TC-FA-CAID-210
  - TC-FA-CAID-211
  - TC-FA-CAID-212
  - TC-FA-CAID-213
coverage:
  web: automated
---

# Modal Changelog: Batas Pin, Reset to Default, Close, Guard Satu Kolom, dan Cache Independen

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
- Precondition TC-FA-CAID-209, TC-FA-CAID-210, TC-FA-CAID-211, TC-FA-CAID-212, TC-FA-CAID-213 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan tujuh entri log; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: drag and drop elemen daftar kolom pada Popup Setup Column; hover icon Pin dan checkbox untuk membaca tooltip; memperkecil lebar viewport sampai tabel Changelog dapat di-scroll horizontal (nilai lebar tidak ditentukan TC; dipilih spec "sampai scroll horizontal tersedia", lihat Temuan untuk QA); scroll horizontal tabel; menekan `Esc`; menghapus preferensi kolom Modal Changelog di browser (disediakan tim FE).
- Konfigurasi kolom Modal Changelog dimulai dari default (enam kolom tampil, tanpa pin); hook `before` menghapus preferensi kolom.
- Modal View Code List (TC-FA-CAID-213) dibuka dari tautan `[View Code List]` pada tab Custom Asset ID; kolom tab pertama `Group Name` dan `Code`.
- State global yang dipulihkan: preferensi kolom Modal Changelog dihapus (bukan `[Reset to Default]`) dan viewport dikembalikan ke bawaan di hook `after`.
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-209: Pin ke-4 dibatasi: icon Pin kolom lain disabled setelah tiga kolom di-pin

1. Klik tombol `[Changelog]` pada header kartu
2. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, lalu klik icon Pin pada `Date`, `Action`, dan `Field`
3. Hover icon Pin pada `Old Value`
4. Verifikasi icon Pin pada `Old Value`, `New Value`, dan `Modified By` berstatus disabled
5. Verifikasi tooltip berbunyi `Maximum 3 columns can be pinned at once. Unpin another column first.`

### TC-FA-CAID-210: Reset to Default pada Setup Column Changelog

6. Klik `[✕]` pada Popup Setup Column untuk menutup tanpa menyimpan
7. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, sembunyikan `Field`, pindahkan `Date` ke posisi terakhir, dan pin `Action`
8. Klik `[Reset to Default]`, lalu klik `[Save]`
9. Verifikasi keenam kolom tampil
10. Verifikasi urutan kolom default `Date | Action | Field | Old Value | New Value | Modified By`
11. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
12. Scroll tabel secara horizontal
13. Verifikasi tidak ada kolom ter-pin
14. Pulihkan lebar viewport ke ukuran semula

### TC-FA-CAID-211: Menutup Popup Setup Column Changelog dengan close atau Esc membuang perubahan

15. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, hilangkan centang `Field`, lalu klik `[✕]`
16. Verifikasi jalur close: tabel tetap menampilkan keenam kolom dan perubahan tidak tersimpan
17. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, hilangkan centang `Field`, lalu tekan `Esc`
18. Verifikasi jalur Esc: tabel tetap menampilkan keenam kolom dan perubahan tidak tersimpan

### TC-FA-CAID-212: Guard satu kolom tersisa pada Setup Column Changelog

19. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, lalu hilangkan centang lima kolom sehingga hanya `Modified By` yang tercentang
20. Hover checkbox `Modified By`
21. Verifikasi checkbox `Modified By` disabled
22. Verifikasi checkbox `Modified By` tetap tercentang
23. Verifikasi tooltip `At least one column must remain visible.`
24. Klik `[✕]` pada Popup Setup Column untuk menutup tanpa menyimpan

### TC-FA-CAID-213: Cache Setup Column Changelog independen dari Code List

25. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, sembunyikan kolom `Field`, lalu klik `[Save]`
26. Klik `[✕]` pada Modal Changelog
27. Klik tautan `[View Code List]`
28. Verifikasi tabel Code List tetap menampilkan kolom `Group Name` dan `Code`; konfigurasi kolom Changelog tidak memengaruhinya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (209 sampai 213). TC-FA-CAID-213 di akhir karena menyimpan konfigurasi kolom. Modal Changelog dibuka di langkah 1 untuk TC-FA-CAID-209 sampai 212.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 6 dan 24 (menutup popup dengan perubahan yang tidak disimpan: tiga pin pada TC-FA-CAID-209 dan lima kolom tidak tercentang pada TC-FA-CAID-212), langkah 11 dan 14 (mengatur dan memulihkan viewport agar scroll horizontal teramati pada TC-FA-CAID-210; viewport diperkecil sesudah `[Save]` mengikuti Langkah TC), dan langkah 26 (menutup Modal Changelog sebelum membuka Modal View Code List). Langkah membuka popup digabung dalam langkah aksi pertama di popup. Pada TC-FA-CAID-211 `Verifikasi` jalur close dan jalur Esc (langkah 16 dan 18) dan pada TC-FA-CAID-213 (langkah 28) masing-masing memuat dua klausa Expected yang diamati dari satu keadaan tabel (kesimpulan "perubahan tidak tersimpan" atau "tidak memengaruhi" tidak teramati terpisah, S-03).
- Pembagian TC lintas spec: Setup Column screening dan kelas Date ada di spec 074; kelas teks pendek di spec 075; kelas nilai campuran di spec 076; Setup Column Modal View Code List (TC-FA-CAID-132 sampai 141) ada di spec 056 dan 057.
- Alasan satu dataset berada di beberapa spec: Sort (spec 073) dan Setup Column (spec 074 sampai 076 dan ini) memakai dataset Pre-setup No 15 (L1 sampai L7) yang sama. Spec 073 sampai 077 berjumlah 137 langkah (35, 36, 19, 19, dan 28), jauh di atas batas sekitar 35 langkah per spec (bagian 3 prinsip 13); tiap spec berdiri sendiri dan Setup Column dibagi menurut Anggota kelas kolom di TC sumber (Date, teks pendek, nilai campuran) serta batas pin, Reset to Default, close, guard, dan cache.
- Temuan untuk QA: (1) TC-FA-CAID-210 menulis "perkecil lebar viewport sehingga tabel dapat di-scroll horizontal" tanpa nilai lebar; spec memperkecil viewport sampai scroll horizontal tersedia (pilihan spec, lihat Prerequisites) dan lebar yang pasti perlu ditetapkan QA; tidak ada kolom yang membeku di kiri diamati lewat scroll pada viewport itu. (2) TC-FA-CAID-213 tidak menyebut tab Code List yang diamati; spec mengamati tab pertama yang terbuka (kolom `Group Name` dan `Code`). (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
