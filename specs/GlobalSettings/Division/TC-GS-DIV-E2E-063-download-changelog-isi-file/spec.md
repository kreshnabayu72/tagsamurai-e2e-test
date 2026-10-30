---
id: TC-GS-DIV-E2E-063-download-changelog-isi-file
title: "Download Changelog: Isi File Tanpa dan Dengan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-221
  - TC-GS-DIV-222
coverage:
  web: automated
---

# Download Changelog: Isi File Tanpa dan Dengan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`, urutan sebagai berikut):
  - 11 Division pembantu `Log Exp {NN} {runId}-063` (NN = 01 sampai 11) dibuat oleh Sari Dewi (11 entri Action Create oleh `Sari D`, Old Value `—`), sehingga ekspor melebihi satu halaman (lebih dari 10 baris).
  - Division pembantu `Log Del Div {runId}-063` dibuat lalu dihapus oleh Sari Dewi (entri Action Delete, New Value `—`), dilakukan sesudah seeding lain; menjamin ada sedikitnya satu entri Delete untuk TC-GS-DIV-222.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API 11 Division `Log Exp {NN} {runId}-063`; hapus berkas unduhan. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6) dan Division milik spec ini (12, termasuk satu yang langsung dihapus) (disediakan tim FE).
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih; membaca isi berkas CSV dan XLSX (nama berkas, jumlah baris data, nilai kolom Action); membaca total entri Changelog Client A sebagai pembanding jumlah baris CSV (disediakan tim FE/BE; TC tidak menyebut cara).
- Precondition TC-GS-DIV-221, 222: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi (Create, Delete).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite serial (`parallel: false`) karena total entri Changelog Client A dibaca sebagai pembanding jumlah baris CSV.
- State global yang dipulihkan: tidak ada.

## Test Steps

### TC-GS-DIV-221: Download Changelog tanpa Search dan Filter mengekspor seluruh riwayat

1. Klik icon Changelog di Table Tools
2. Klik Download di modal, lalu klik `Download CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi file `Changelog-Division.csv` terunduh
5. Verifikasi file memuat seluruh riwayat (jumlah baris data sama dengan total entri Changelog)
6. Verifikasi jumlah baris data file lebih dari 10 (melebihi halaman yang tampil)

### TC-GS-DIV-222: Download Changelog dengan Filter aktif hanya mengekspor baris yang cocok

7. Klik icon Filter di modal
8. Pilih Action `Delete`, klik `[Apply]`
9. Klik Download di modal, lalu klik `Download XLSX`
10. Verifikasi file `Changelog-Division.xlsx` terunduh
11. Verifikasi file memuat sedikitnya satu baris Action `Delete`
12. Verifikasi file hanya memuat baris Action `Delete`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (221, 222): TC-GS-DIV-221 tanpa saringan lebih dulu, lalu TC-GS-DIV-222 dengan Filter aktif. Modal Changelog dibuka sekali di langkah 1.
- Isi berkas export dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f); kegagalan download Changelog (TC-GS-DIV-223) ada di spec 051.
- Verifikasi file memuat sedikitnya satu baris `Delete` (langkah 11) adalah asersi tambahan (S-03) agar "hanya memuat baris `Delete`" tidak lulus pada berkas kosong.
- Asersi pada TC-GS-DIV-222 memakai pola baris (semua baris data bernilai `Delete` pada kolom Action), sehingga entri dari run atau spec lain tidak memengaruhi hasil.
- Temuan untuk QA: (1) TC-GS-DIV-221 Expected b "memuat seluruh riwayat" tidak menyebut cara mengetahui total entri; spec membandingkan jumlah baris data berkas dengan total entri Changelog yang dibaca tim FE/BE. (2) TC-GS-DIV-222 tidak menyebut jumlah baris Delete yang diharapkan; spec hanya mengasersi bahwa semua baris data berkas bernilai `Delete`.
