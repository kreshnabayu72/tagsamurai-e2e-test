---
id: TC-FA-CAID-E2E-079-changelog-download-nama-header-dan-hasil-kosong
title: "Modal Changelog: Download Overlay, Hasil Kosong, dan Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-220
  - TC-FA-CAID-224
  - TC-FA-CAID-225
coverage:
  web: automated
---

# Modal Changelog: Download Overlay, Hasil Kosong, dan Kolom Tersembunyi

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

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Entri log audit lain pada Company Changelog tidak dihapus dan tidak diasersi (audit trail permanen, S-12); spec ini tidak menambah entri Changelog. Seluruh entri seed L1 sampai L7 dan General Settings No 27 dipakai sebagai precondition TC, tidak diasersi (spec hanya mengasersi tooltip, opsi overlay, baris header, dan kolom berkas). Entri Changelog tidak bisa dihapus.
- Precondition TC-FA-CAID-220, TC-FA-CAID-224, TC-FA-CAID-225 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis (kelas binary buffer hanya untuk nama berkas, header, dan jumlah baris; isi sel ada di spec 059): menangkap berkas unduhan browser ke direktori bersih; membaca baris header dan jumlah baris berkas CSV; hover icon Download untuk membaca tooltip; menyembunyikan kolom lewat overlay Column Visibility.
- State global yang dipulihkan: berkas unduhan dihapus dan preferensi kolom Modal Changelog dihapus di hook `after` (TC-FA-CAID-225 menyembunyikan kolom).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-220: Overlay Download Changelog dan tooltip

1. Klik tombol `[Changelog]` pada header kartu
2. Hover icon Download
3. Verifikasi tooltip `Download` tampil
4. Klik icon Download
5. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`

### TC-FA-CAID-224: Download Changelog dengan hasil kosong berisi header saja

6. Klik icon Download untuk menutup overlay
7. Ketik Search `zzzzz`, tekan Enter
8. Verifikasi tombol Download tetap aktif
9. Klik Download, lalu klik `Download as CSV`
10. Verifikasi tidak ada toast
11. Verifikasi berkas hasil unduhan hanya berisi baris header

### TC-FA-CAID-225: Kolom Changelog yang disembunyikan tidak ikut diekspor

12. Klik icon `(←)` pada kotak Search
13. Sembunyikan kolom `Field` dan `Old Value` lewat overlay Column Visibility
14. Klik Download, lalu klik `Download as CSV`
15. Verifikasi berkas hanya berisi kolom `Date`, `Action`, `New Value`, dan `Modified By`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (220, 224, 225): TC-FA-CAID-225 di akhir karena menyembunyikan kolom. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 6 (menutup overlay Download dari TC-FA-CAID-220) dan langkah 12 (menutup Search dan mereset tabel sebelum TC-FA-CAID-225).
- Pada TC-FA-CAID-224 `Verifikasi` tidak ada toast diletakkan segera setelah pemicu Download dan sebelum `Verifikasi` berkas (bagian 8b butir 11); berkas yang terunduh menjadi anchor positif.
- Pembagian TC lintas spec: nama berkas dan isi sel CSV/XLSX Changelog (TC-FA-CAID-221, 222) ada di spec 059; Download mengikuti Search dan Filter serta di atas 5.000 baris (TC-FA-CAID-223, 227) ada di spec 080; Download sukses tanpa toast dan gagal dengan toast error (TC-FA-CAID-226) ada di spec 062.
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066 sampai 072. Download Modal Changelog tidak digabung ke spec tersebut karena gabungan langkah spec 066 sampai 072 dan 079 (jauh di atas 35 langkah) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell); harness penangkapan berkas unduhan hanya dipakai spec Download.
- Temuan untuk QA: (1) TC-FA-CAID-224 Expected "berkas hanya berisi baris header" tidak menyebut nama berkas; spec tidak mengasersi nama berkas. (2) TC-FA-CAID-225 tidak menyebut apakah penyembunyian kolom lewat overlay Column Visibility tersimpan; spec mengikuti TC dan menghapus preferensi kolom di hook `after`. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
