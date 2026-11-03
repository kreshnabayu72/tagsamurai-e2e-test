---
id: TC-FA-CAID-E2E-072-changelog-filter-independen-kolom-tanpa-filter-dan-tanpa-hasil
title: "Modal Changelog: Filter Independen Column Visibility, Kolom Tanpa Filter, dan Filter Tanpa Hasil"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-190
  - TC-FA-CAID-191
  - TC-FA-CAID-229
coverage:
  web: automated
---

# Modal Changelog: Filter Independen Column Visibility, Kolom Tanpa Filter, dan Filter Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun disediakan tim FE/BE (Pre-setup No 15 hanya menyebut env var). Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
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

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Entri log audit lain pada Company Changelog tidak dihapus dan tidak diasersi (audit trail permanen, S-12); spec ini tidak menambah entri Changelog. Entri Changelog tidak bisa dihapus.
- Precondition TC-FA-CAID-190, TC-FA-CAID-191, TC-FA-CAID-229 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: menyembunyikan dan menampilkan kolom lewat overlay Column Visibility; memilih rentang tanggal pada date range picker Filter; membaca chip pada field Filter.
- State global yang dipulihkan: preferensi kolom Modal Changelog dihapus di hook `after` (TC-FA-CAID-190 menyembunyikan kolom `Field`).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-190: Filter independen dari Column Visibility

1. Klik tombol `[Changelog]` pada header kartu
2. Klik icon Filter, pilih `Separator` pada `Field`, klik `[Apply]`
3. Sembunyikan kolom `Field` lewat overlay Column Visibility
4. Klik icon Filter
5. Verifikasi field filter `Field` tetap ada di panel dengan chip `Separator`
6. Verifikasi tabel tetap tersaring menampilkan L1, L4, L6
7. Klik `[Clear Field]`, lalu klik `[Apply]`
8. Tampilkan kembali kolom `Field` lewat overlay Column Visibility

### TC-FA-CAID-191: Kolom Old Value dan New Value tidak memiliki filter

9. Klik icon Filter
10. Verifikasi panel memuat field `Date`, `Action`, `Field`, dan `Modified By`
11. Verifikasi tidak ada field `Old Value` maupun `New Value` di panel

### TC-FA-CAID-229: Filter tanpa hasil menampilkan empty state filter/search

12. Klik icon Filter untuk menutup panel
13. Klik icon Filter, pilih rentang `01/09/26` sampai `02/09/26` pada field `Date`, klik `[Apply]`
14. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-CAID-190, 191, 229. Alasan: TC-FA-CAID-190 mengubah visibilitas kolom dan memulihkannya di dalam blok; TC-FA-CAID-191 hanya mengamati panel; TC-FA-CAID-229 (hasil kosong) di akhir. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 7 (membersihkan Filter pada panel yang terbuka), langkah 8 (memulihkan kolom `Field`), dan langkah 12 (menutup panel yang masih terbuka dari TC-FA-CAID-191). Langkah "Klik icon Filter" sebelum memilih opsi membuka kembali panel yang ditutup `[Apply]`.
- Asersi memakai pola baris seed L1, L4, L6 milik Company Changelog (relatif terhadap audit trail, S-12); tidak ada asersi total entri absolut. Empty state pada TC-FA-CAID-229 adalah hasil Filter tanpa baris, sehingga rentang `01/09/26` sampai `02/09/26` harus lebih awal dari entri seed tertua (10/09/26, 10:00).
- Pembagian TC lintas spec: screening Filter Panel dan Filter fungsional (TC-FA-CAID-177 sampai 189) ada di spec 069, 070, dan 071.
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066 sampai 071 dan 079. Filter Modal Changelog tidak digabung ke satu spec dengan spec 069, 070, dan 071 karena gabungan langkah spec 069 (40), 070 (25), 071 (34), dan 072 (14) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell).
- Temuan untuk QA: (1) TC-FA-CAID-190 tidak menyebut pemulihan kolom `Field` sesudah asersi; spec menambah langkah penghubung 8 dan menghapus preferensi kolom di hook `after`. (2) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
