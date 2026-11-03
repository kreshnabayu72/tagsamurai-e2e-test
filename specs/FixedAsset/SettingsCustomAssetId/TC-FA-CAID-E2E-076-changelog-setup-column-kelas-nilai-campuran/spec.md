---
id: TC-FA-CAID-E2E-076-changelog-setup-column-kelas-nilai-campuran
title: "Modal Changelog: Setup Column Kelas Nilai Campuran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-206
  - TC-FA-CAID-207
  - TC-FA-CAID-208
coverage:
  web: automated
---

# Modal Changelog: Setup Column Kelas Nilai Campuran

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
- Precondition TC-FA-CAID-206, TC-FA-CAID-207, TC-FA-CAID-208 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan tujuh entri log; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: drag and drop elemen daftar kolom pada Popup Setup Column; memperkecil lebar viewport sampai tabel Changelog dapat di-scroll horizontal (nilai lebar tidak ditentukan TC; dipilih spec "sampai scroll horizontal tersedia", lihat Temuan untuk QA); scroll horizontal tabel; menghapus preferensi kolom Modal Changelog di browser (disediakan tim FE).
- Konfigurasi kolom Modal Changelog dimulai dari default (enam kolom tampil, urutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, tanpa pin); hook `before` menghapus preferensi kolom. "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya preferensi tetap ada.
- State global yang dipulihkan: preferensi kolom Modal Changelog dihapus (bukan `[Reset to Default]`) dan viewport dikembalikan ke bawaan di hook `after`.
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-206: Setup Column Hide dan Unhide kelas nilai campuran pada Changelog

1. Klik tombol `[Changelog]` pada header kartu
2. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, hilangkan centang `Old Value` dan `New Value`, lalu klik `[Save]`
3. Muat ulang halaman (F5)
4. Klik tombol `[Changelog]` pada header kartu
5. Verifikasi setelah Save dan refresh: kolom `Date`, `Action`, `Field`, dan `Modified By` tetap tampil
6. Verifikasi setelah Save dan refresh: kolom `Old Value` dan `New Value` tersembunyi
7. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, centang kembali kolom `Old Value` dan `New Value`, lalu klik `[Save]`
8. Verifikasi setelah dicentang kembali dan Save: kolom `Old Value` dan `New Value` tampil lagi

### TC-FA-CAID-207: Setup Column Drag reorder kelas nilai campuran pada Changelog

9. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, seret kolom `New Value`, lalu `Old Value` masing-masing ke posisi paling kiri tabel, lalu klik `[Save]`
10. Muat ulang halaman (F5)
11. Klik tombol `[Changelog]` pada header kartu
12. Verifikasi setelah Save dan refresh: urutan kolom menjadi `Old Value | New Value | Date | Action | Field | Modified By`

### TC-FA-CAID-208: Setup Column Pin kelas nilai campuran pada Changelog

13. Klik header kolom `Actions (⋯)`, klik `Setup Column...`, klik icon Pin pada kolom `Old Value` dan `New Value`, lalu klik `[Save]`
14. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
15. Scroll tabel secara horizontal
16. Verifikasi kolom `Old Value` dan `New Value` ter-pin ke kiri
17. Verifikasi kolom `Old Value` dan `New Value` tetap di posisinya saat tabel di-scroll horizontal
18. Verifikasi kolom lain yang tidak ter-pin ikut bergeser saat tabel di-scroll horizontal
19. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (206, 207, 208): hide dipulihkan di dalam blok TC-FA-CAID-206; TC-FA-CAID-207 dan 208 menyimpan urutan dan pin berturut-turut pada konfigurasi yang sama. Modal Changelog dibuka di langkah 1 dan dibuka kembali sesudah tiap muat ulang halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 14 dan 19 (mengatur dan memulihkan viewport agar scroll horizontal teramati). Langkah membuka popup (klik header `Actions (⋯)` lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup karena `[Save]` menutup popup. Pada TC-FA-CAID-206 `Verifikasi` kolom lain tampil mendahului `Verifikasi` kolom tersembunyi sebagai anchor positif (bagian 8b butir 2); Expected TC memuat keduanya.
- Pembagian TC lintas spec: Setup Column screening dan kelas Date ada di spec 074; kelas teks pendek di spec 075; batas pin, Reset to Default, close, guard, dan cache di spec 077.
- Alasan satu dataset berada di beberapa spec: Sort (spec 073) dan Setup Column (spec 074, 075, ini, dan 077) memakai dataset Pre-setup No 15 (L1 sampai L7) yang sama. Spec 073 sampai 077 berjumlah 137 langkah (35, 36, 19, 19, dan 28), jauh di atas batas sekitar 35 langkah per spec (bagian 3 prinsip 13); tiap spec berdiri sendiri dan Setup Column dibagi menurut Anggota kelas kolom di TC sumber (Date, teks pendek, nilai campuran) serta batas pin, Reset to Default, close, guard, dan cache.
- Temuan untuk QA: (1) TC-FA-CAID-208 menulis "perkecil lebar viewport sehingga tabel dapat di-scroll horizontal" tanpa nilai lebar; spec memperkecil viewport sampai scroll horizontal tersedia (pilihan spec, lihat Prerequisites) dan lebar yang pasti perlu ditetapkan QA. (2) TC-FA-CAID-208 tidak menyebut urutan antara `Old Value` dan `New Value` setelah di-pin; spec hanya mengasersi keduanya ter-pin ke kiri. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
