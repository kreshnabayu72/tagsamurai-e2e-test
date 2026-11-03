---
id: TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas
title: "Modal Changelog: Search Modified By, Kolom Date, Trim, Empty State, dan Visibilitas Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-171
  - TC-FA-CAID-172
  - TC-FA-CAID-173
  - TC-FA-CAID-174
  - TC-FA-CAID-175
  - TC-FA-CAID-176
coverage:
  web: automated
---

# Modal Changelog: Search Modified By, Kolom Date, Trim, Empty State, dan Visibilitas Kolom

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
- Precondition TC-FA-CAID-171, TC-FA-CAID-172, TC-FA-CAID-173, TC-FA-CAID-174, TC-FA-CAID-175, TC-FA-CAID-176 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: mengetik di kotak Search Modal Changelog; menyembunyikan dan menampilkan kolom lewat overlay Column Visibility; mendeteksi dialog `alert` browser (TC-FA-CAID-176).
- State global yang dipulihkan: preferensi kolom Modal Changelog dihapus di hook `after` (TC-FA-CAID-175 menyembunyikan kolom `Field`).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-171: Search kolom Modified By mencocokkan nama lengkap user

1. Klik tombol `[Changelog]` pada header kartu
2. Ketik Search `santoso`, tekan Enter
3. Verifikasi `santoso` menemukan baris L3 yang tampil sebagai `Budi S`
4. Ganti isi kotak search dengan `rina`, tekan Enter
5. Verifikasi `rina` menemukan baris L1 yang tampil sebagai `Rina P`
6. Ganti isi kotak search dengan `johnson`, tekan Enter
7. Verifikasi `johnson` menemukan baris L2, L4, L5, L6, L7 yang tampil sebagai `Sarah J`

### TC-FA-CAID-172: Kolom Date tidak dapat dicari lewat Search

8. Ganti isi kotak search dengan `15/09/26`, tekan Enter
9. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-FA-CAID-173: Query Search Changelog di-trim saat Enter

10. Ganti isi kotak search dengan `  edit  ` (spasi awal dan akhir), tekan Enter
11. Verifikasi tabel menampilkan baris L1, L2, L3, L4 seperti keyword `edit`
12. Verifikasi isi input di layar tidak berubah: tetap `  edit  ` dengan spasi awal dan akhir

### TC-FA-CAID-174: Search Changelog tanpa hasil menampilkan empty state filter/search

13. Ganti isi kotak search dengan `zzzzz`, tekan Enter
14. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-FA-CAID-175: Search Changelog terikat visibilitas kolom: Field yang disembunyikan tidak dicari

15. Klik icon `(←)` pada kotak Search
16. Sembunyikan kolom `Field` lewat overlay Column Visibility
17. Ketik Search `segments`, tekan Enter
18. Verifikasi saat kolom `Field` disembunyikan, `segments` tidak menemukan baris: tampil Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
19. Tampilkan kembali kolom `Field` lewat overlay Column Visibility
20. Ganti isi kotak search dengan `segments`, tekan Enter
21. Verifikasi setelah kolom `Field` ditampilkan kembali, `segments` menemukan baris L5

### TC-FA-CAID-176: Kata kunci Search Changelog diperlakukan sebagai teks biasa

22. Ganti isi kotak search dengan `<img src=x onerror=alert(1)>`, tekan Enter
23. Verifikasi tidak ada skrip yang dijalankan: tidak ada dialog `alert` browser
24. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (171 sampai 176). TC-FA-CAID-175 (menyembunyikan kolom) berada sebelum TC-FA-CAID-176 dan state kolom dipulihkan di dalam TC itu sendiri. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 (menutup input Search dan mereset tabel sebelum Search berikutnya, S-09). Langkah menyembunyikan dan menampilkan kolom `Field` adalah langkah TC-FA-CAID-175.
- Empty state `No results found` diasersi sebagai satu `Verifikasi` (ilustrasi, judul, dan deskripsi disebut utuh dalam satu butir Expected TC, S-01). Untuk TC-FA-CAID-172 dan 174 empty state itu sekaligus menjadi anchor positif asersi ketiadaan baris (bagian 8b butir 2).
- Pembagian TC lintas spec: siklus Search, placeholder, kelas enum, dan nilai campuran (TC-FA-CAID-167 sampai 170) ada di spec 067.
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066, 067, 069 sampai 072, dan 079. Search Modal Changelog tidak digabung ke satu spec dengan spec 067 karena gabungan langkah spec 067 (35) dan 068 (24) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell).
- Temuan untuk QA: (1) TC-FA-CAID-172 Expected menyebut kolom Date "disaring lewat Filter Panel" sebagai penjelasan tanpa langkah observasi; spec hanya mengasersi empty state, penyaringan Date lewat Filter diuji di spec 069. (2) TC-FA-CAID-176 Expected "tidak ada skrip yang dijalankan" tidak menyebut cara mengamati; spec memakai tidak adanya dialog `alert` browser. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
