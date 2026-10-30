---
id: TC-GS-UOM-E2E-059-konflik-create-edit-dua-admin
title: "Konflik Create dan Edit Unit oleh Dua Admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-91
  - TC-GS-UOM-245
  - TC-GS-UOM-246
coverage:
  web: automated
---

# Konflik Create dan Edit Unit oleh Dua Admin

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Akun Sesi B (admin kedua): Total Control Client A kedua, `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); fixture disediakan tim FE.
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Hook `before` login keduanya dan membuka Global Settings > Master Reference > Measurement. Sesi B dipakai sebagai sesi UI pada TC-GS-UOM-245 dan TC-GS-UOM-246 (hasil di Sesi B diasersi); pada TC-GS-UOM-91 admin kedua hanya memicu perubahan state dan memakai sesi API (login API dengan `Spectra.env.GS_TC2_PASSWORD`). Hook `after` menutup konteks Sesi B.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), seluruhnya bebas relasi dan milik spec ini:
  - `Edit Bersama {runId}-059` / `eb`: di-seed lewat API di hook `before` (pengganti Liter pada TC-GS-UOM-245; target tulis tidak memakai baris Pre-setup, S-06).
  - `Pint {runId}-059` / `pt` (D-14): di-seed lewat API di hook `before`; dihapus admin kedua pada TC-GS-UOM-91.
  - `Bushel {runId}-059` / `bu` (D-18): dibuat spec lewat UI pada TC-GS-UOM-246 (nama `Bushel` diberi suffix, S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Edit Bersama {runId}-059`, `Bushel {runId}-059`, dan `Pint {runId}-059` bila masih ada.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; pemicu klik [Submit] hampir bersamaan di dua sesi; sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk Delete Measurement oleh admin kedua dengan menunggu hasil tersimpan.
- Tidak ada state global yang diubah.
- TC-GS-UOM-91, 245, 246: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-245: Dua admin mengedit unit yang sama, Save terakhir menimpa tanpa dialog konflik

1. [Sesi A] Ketik Search `Edit Bersama {runId}-059`, tekan Enter, klik `⋯` pada baris tersebut > Edit
2. [Sesi B] Ketik Search `Edit Bersama {runId}-059`, tekan Enter, klik `⋯` pada baris tersebut > Edit
3. [Sesi A] Ubah Symbol menjadi `la`, klik [Save]
4. [Sesi A] Verifikasi toast sukses: "Success, unit has been updated."
5. [Sesi A] Verifikasi tidak ada dialog konflik
6. [Sesi B] Ubah Symbol menjadi `lb`, klik [Save]
7. [Sesi B] Verifikasi toast sukses: "Success, unit has been updated."
8. [Sesi B] Verifikasi tidak ada dialog konflik
9. [Sesi A] Muat ulang halaman Measurement, ketik Search `Edit Bersama {runId}-059`, tekan Enter
10. [Sesi A] Verifikasi Symbol `Edit Bersama {runId}-059` bernilai `lb`

### TC-GS-UOM-246: Dua admin membuat unit dengan Unit Name sama bersamaan, yang kedua ditolak

11. [Sesi A] Klik [+ Unit], isi Unit Name `Bushel {runId}-059` dan Symbol `bu`
12. [Sesi B] Klik [+ Unit], isi Unit Name `Bushel {runId}-059` dan Symbol `bu`
13. Klik [Submit] di kedua sesi hampir bersamaan
14. Verifikasi tepat satu sesi menampilkan toast sukses: "Success, unit has been created."
15. Verifikasi sesi lainnya menampilkan error `Unit name already exists`
16. Verifikasi form Create di sesi yang menampilkan error tetap terbuka
17. Di sesi yang menampilkan error: klik `✕` pada form Create
18. Di sesi yang menampilkan error: Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
19. Di sesi yang menampilkan error: klik `[Leave]`

### TC-GS-UOM-91: Edit unit yang sudah dihapus admin lain

20. [Sesi A] Ganti isi kotak search dengan `Pint {runId}-059`, tekan Enter, klik `⋯` pada baris tersebut > Edit
21. [Sesi B, sesi API] Hapus `Pint {runId}-059` hingga tersimpan
22. [Sesi A] Ubah Symbol menjadi `pint`, klik [Save]
23. [Sesi A] Verifikasi toast: "This unit is no longer available."
24. [Sesi A] Verifikasi modal Edit tertutup otomatis
25. [Sesi A] Verifikasi tabel me-refresh sehingga `Pint {runId}-059` tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: multi-konteks (dua sesi admin), bagian 3 prinsip 13c.
- Urutan TC di spec berbeda dari urutan sumber: 245 (mengubah nilai), 246 (membuat data), lalu 91 yang unitnya dihapus admin kedua di akhir (prinsip 5). Data tiap TC independen.
- TC-GS-UOM-91 dan TC-GS-UOM-103/344/345/357/413 (record sudah dihapus admin lain) terbagi: TC-GS-UOM-91 di spec ini, TC-GS-UOM-103, 344, 345, 357, 413 di spec `TC-GS-UOM-E2E-060-konflik-delete-dua-admin`; resilience cek referensi/delete gagal (5xx, timeout) di spec 035.
- Langkah penghubung: langkah 1, 2, 9, dan 20 (Search baris target sebelum aksi baris; tabel memuat lebih dari satu halaman), langkah 9 (muat ulang Sesi A agar tabel menampilkan nilai terbaru dari server), langkah 17 sampai 19 (menutup form Create dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`, sebagai pembersihan state; S-08), langkah 21 (admin kedua menghapus lewat sesi API; "hingga tersimpan" menjadi penanda selesai).
- Langkah 5 dan 8 (tidak ada dialog konflik) berasal dari Expected c TC-GS-UOM-245 dan didahului toast sukses sebagai anchor positif di sesi yang sama.
- Langkah 25: "tabel me-refresh" diamati lewat hilangnya baris `Pint` setelah toast; refresh tidak punya indikator terpisah.
- Pemenang race TC-GS-UOM-246 tidak deterministik (sesi mana yang berhasil), sehingga langkah 14 sampai 19 merujuk "sesi yang menampilkan error" sesuai hasil langkah 15, bukan sesi tertentu.
- Temuan untuk QA:
  - Akun admin kedua (Admin A dan B pada TC-GS-UOM-245 dan 246, "Admin lain" pada TC-GS-UOM-91) tidak ada di Tabel Data Uji Pre-setup TC; spec memakai akun Total Control Client A kedua yang disediakan tim FE (S-13).
  - TC-GS-UOM-245 dan 246 menyebut target Liter dan `Bushel` (D-18) tanpa suffix; spec memakai unit milik spec bersuffix (S-06, S-12).
  - TC-GS-UOM-246 Expected "Satu sukses" tidak menyebut teks toast; spec memakai toast Create standar `Success, unit has been created.` dari TC-GS-UOM-36. Teks error `Unit name already exists` mengikuti TC.
  - TC-GS-UOM-246 Post Condition "Satu Bushel tersimpan (D-18)" dan TC-GS-UOM-245 Post Condition tidak punya langkah observasi di TC, sehingga tidak diasersi.
