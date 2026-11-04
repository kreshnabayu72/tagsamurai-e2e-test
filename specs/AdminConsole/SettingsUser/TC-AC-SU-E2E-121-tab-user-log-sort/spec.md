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

1. Ketik Search `Jane Smith {runId}-121`, tekan Enter
2. Klik Name `Jane Smith {runId}-121`
3. Klik tab `User Log`
4. Verifikasi tabel menampilkan sedikitnya dua baris data uji
5. Klik header `Date` untuk pertama kalinya
6. Verifikasi urutan baris Oldest First
7. Verifikasi ikon sort `↑` tampil
8. Klik header `Date` untuk kedua kalinya
9. Verifikasi urutan baris Newest First
10. Verifikasi ikon sort `↓` tampil
11. Klik header `Date` untuk ketiga kalinya
12. Verifikasi urutan baris kembali ke sort default (Date Newest First)

### TC-AC-SU-433: Header kolom teks Tab User Log sortable 3-state

13. Untuk setiap baris tabel "Kolom sort dengan nilai distinct" di Prerequisites, lakukan langkah 14 sampai 21
14. Klik header kolom pada baris tabel 'Kolom sort dengan nilai distinct'
15. Verifikasi urutan baris A–Z menurut nilai distinct kolom itu
16. Verifikasi ikon sort `↑` tampil
17. Klik header kolom yang sama untuk kedua kalinya
18. Verifikasi urutan baris Z–A menurut nilai distinct kolom itu
19. Verifikasi ikon sort `↓` tampil
20. Klik header kolom yang sama untuk ketiga kalinya
21. Verifikasi urutan baris kembali ke sort default (Date Newest First)
22. Klik header `Device / Browser` untuk pertama kalinya
23. Verifikasi urutan baris A–Z menurut nilai distinct kolom `Device / Browser`
24. Verifikasi ikon sort `↑` tampil
25. Verifikasi nilai `—` berada di akhir
26. Klik header `Device / Browser` untuk kedua kalinya
27. Verifikasi urutan baris Z–A menurut nilai distinct kolom `Device / Browser`
28. Verifikasi ikon sort `↓` tampil
29. Verifikasi nilai `—` berada di awal
30. Klik header `Device / Browser` untuk ketiga kalinya
31. Verifikasi urutan baris kembali ke sort default (Date Newest First)
32. Untuk setiap baris tabel "Kolom sort tanpa nilai distinct" di Prerequisites, lakukan langkah 33 sampai 38
33. Klik header kolom pada baris tabel 'Kolom sort tanpa nilai distinct'
34. Verifikasi ikon sort `↑` tampil
35. Klik header kolom yang sama untuk kedua kalinya
36. Verifikasi ikon sort `↓` tampil
37. Klik header kolom yang sama untuk ketiga kalinya
38. Verifikasi urutan baris kembali ke sort default (Date Newest First)

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Klik header kolom diulang per baris tabel: langkah 14 sampai 21 (2 kolom dengan nilai distinct) dan langkah 33 sampai 38 (2 kolom tanpa nilai distinct). Klik ketiga tiap kolom mengembalikan sort ke default sehingga kolom berikutnya mulai dari keadaan yang sama (S-09).
- Temuan untuk QA:
  - Kolom `Activity` (semua `Session`) dan `Status` (semua `—`) pada TC-425 tidak memiliki dua nilai distinct, sehingga urutan A–Z dan Z–A tidak dapat diasersi (S-14, S-11); untuk keduanya spec hanya mengasersi ikon sort dan kembali ke default.
  - TC-432 klik 2 (Newest First) dan klik 3 (kembali ke default Date Newest First) menghasilkan urutan baris yang sama; pembeda keadaan header pada klik 3 tidak dinyatakan.
  - Cara men-seed sesi User Log (Date, Note, IP Address, user agent, asal Admin Console atau Global Settings, user pemilik sesi) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (38 langkah nominal, sekitar 52 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
