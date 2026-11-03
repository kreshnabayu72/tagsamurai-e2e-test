---
id: TC-AC-SU-E2E-121-tab-user-log-sort
title: "Tab User Log: Sort 3-state Kolom Tanggal dan Kolom Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-432
  - TC-AC-SU-433
coverage:
  web: automated
---

# Tab User Log: Sort 3-state Kolom Tanggal dan Kolom Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-121` (email `janesmith+{runId}-121@qwertysystem.net`) dengan 3 sesi Admin Console (Date berbeda, satu halaman):

| Sesi | Note | IP Address | Device / Browser |
|---|---|---|---|
| S1 | Session started | 203.0.113.10 | Chrome on Windows |
| S2 | Session ended | 203.0.113.11 | Firefox on Windows |
| S3 | Session started | 203.0.113.12 | — (user agent tidak dikenali) |

| Kolom sort dengan nilai distinct | Urutan A–Z nilai distinct |
|---|---|
| Note | Session ended, Session started |
| IP Address | 203.0.113.10, 203.0.113.11, 203.0.113.12 |

- Nilai distinct `Device / Browser` urut A–Z: Chrome on Windows, Firefox on Windows, `—` (di akhir saat ascending dan di awal saat descending).

| Kolom sort tanpa nilai distinct |
|---|
| Activity |
| Status |

- Kemampuan teknis: kemampuan seed sesi User Log dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-432: Sort 3-state kelas tanggal

1. Cari `Jane Smith {runId}-121` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `User Log`
3. Klik header `Date` untuk pertama kalinya
4. Verifikasi urutan baris Oldest First
5. Verifikasi ikon sort `↑` tampil
6. Klik header `Date` untuk kedua kalinya
7. Verifikasi urutan baris Newest First
8. Verifikasi ikon sort `↓` tampil
9. Klik header `Date` untuk ketiga kalinya
10. Verifikasi urutan baris kembali ke sort default (Date Newest First)

### TC-AC-SU-433: Header kolom teks Tab User Log sortable 3-state

11. Klik header kolom pada baris tabel 'Kolom sort dengan nilai distinct'
12. Verifikasi urutan baris A–Z menurut nilai distinct kolom itu
13. Verifikasi ikon sort `↑` tampil
14. Klik header kolom yang sama untuk kedua kalinya
15. Verifikasi urutan baris Z–A menurut nilai distinct kolom itu
16. Verifikasi ikon sort `↓` tampil
17. Klik header kolom yang sama untuk ketiga kalinya
18. Verifikasi urutan baris kembali ke sort default (Date Newest First)
19. Klik header `Device / Browser` untuk pertama kalinya
20. Verifikasi urutan baris A–Z menurut nilai distinct kolom `Device / Browser`
21. Verifikasi ikon sort `↑` tampil
22. Verifikasi nilai `—` berada di akhir
23. Klik header `Device / Browser` untuk kedua kalinya
24. Verifikasi urutan baris Z–A menurut nilai distinct kolom `Device / Browser`
25. Verifikasi ikon sort `↓` tampil
26. Verifikasi nilai `—` berada di awal
27. Klik header `Device / Browser` untuk ketiga kalinya
28. Verifikasi urutan baris kembali ke sort default (Date Newest First)
29. Klik header kolom pada baris tabel 'Kolom sort tanpa nilai distinct'
30. Verifikasi ikon sort `↑` tampil
31. Klik header kolom yang sama untuk kedua kalinya
32. Verifikasi ikon sort `↓` tampil
33. Klik header kolom yang sama untuk ketiga kalinya
34. Verifikasi urutan baris kembali ke sort default (Date Newest First)

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Klik header kolom diulang per baris tabel: langkah 11 sampai 18 (2 kolom dengan nilai distinct) dan langkah 29 sampai 34 (2 kolom tanpa nilai distinct). Klik ketiga tiap kolom mengembalikan sort ke default sehingga kolom berikutnya mulai dari keadaan yang sama (S-09).
- Temuan untuk QA:
  - Kolom `Activity` (semua `Session`) dan `Status` (semua `—`) pada TC-425 tidak memiliki dua nilai distinct, sehingga urutan A–Z dan Z–A tidak dapat diasersi (S-14, S-11); untuk keduanya spec hanya mengasersi ikon sort dan kembali ke default.
  - TC-432 klik 2 (Newest First) dan klik 3 (kembali ke default Date Newest First) menghasilkan urutan baris yang sama; pembeda keadaan header pada klik 3 tidak dinyatakan.
  - Cara men-seed sesi User Log (Date, Note, IP Address, user agent, asal Admin Console atau Global Settings, user pemilik sesi) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (34 langkah nominal, sekitar 48 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
