---
id: TC-AC-SU-E2E-114-tab-system-log-sort
title: "Tab System Log: Sort 3-state Kolom Tanggal dan Kolom Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-409
  - TC-AC-SU-410
coverage:
  web: automated
---

# Tab System Log: Sort 3-state Kolom Tanggal dan Kolom Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-114` (email `janesmith+{runId}-114@qwertysystem.net`) sebagai aktor dengan 4 entri System Log (Date berbeda, urutan seeding R1 tertua sampai R4 terbaru; satu halaman):

| Entri | Action | Object | Name | Field | Old Value | New Value |
|---|---|---|---|---|---|---|
| R1 | Deactivate | User | John Doe {runId}-114 | Status | Active | Inactive |
| R2 | Resend Activation Email | User | Sarah Lee {runId}-114 | Activation Email | — | — |
| R3 | Assign | Total Control | Rina Putri {runId}-114 | Access Level | Inactive | Active |
| R4 | Edit | Global Role | Dewi Lestari {runId}-114 | Manage group — Update | Read | Update |

| Kolom sort teks | Urutan A–Z nilai distinct |
|---|---|
| Action | Assign, Deactivate, Edit, Resend Activation Email |
| Object | Global Role, Total Control, User |
| Name | Dewi Lestari, John Doe, Rina Putri, Sarah Lee (bersuffix) |
| Field | Access Level, Activation Email, Manage group — Update, Status |

- Kemampuan teknis: kemampuan seed entri System Log dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-409: Sort 3-state kelas tanggal

1. Ketik Search `Jane Smith {runId}-114`, tekan Enter
2. Klik Name `Jane Smith {runId}-114`
3. Klik tab `System Log`
4. Verifikasi tabel menampilkan sedikitnya dua baris data uji
5. Klik header `Date` untuk pertama kalinya
6. Verifikasi urutan baris Oldest First
7. Verifikasi ikon sort `↑` tampil
8. Klik header `Date` untuk kedua kalinya
9. Verifikasi urutan baris Newest First
10. Verifikasi ikon sort `↓` tampil
11. Klik header `Date` untuk ketiga kalinya
12. Verifikasi urutan baris kembali ke sort default (Date Newest First)

### TC-AC-SU-410: Header kolom teks Tab System Log sortable 3-state

13. Untuk setiap baris tabel "Kolom sort teks" di Prerequisites, lakukan langkah 14 sampai 21
14. Klik header kolom pada baris tabel 'Kolom sort teks'
15. Verifikasi urutan baris A–Z menurut nilai distinct kolom itu
16. Verifikasi ikon sort `↑` tampil
17. Klik header kolom yang sama untuk kedua kalinya
18. Verifikasi urutan baris Z–A menurut nilai distinct kolom itu
19. Verifikasi ikon sort `↓` tampil
20. Klik header kolom yang sama untuk ketiga kalinya
21. Verifikasi urutan baris kembali ke sort default (Date Newest First)
22. Klik header `Old Value` untuk pertama kalinya
23. Verifikasi nilai kosong `—` berada di akhir saat ascending
24. Klik header `Old Value` untuk kedua kalinya
25. Verifikasi nilai kosong `—` berada di awal saat descending
26. Klik header `Old Value` untuk ketiga kalinya
27. Verifikasi urutan baris kembali ke sort default (Date Newest First)

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Klik header kolom diulang per baris tabel 'Kolom sort teks': langkah 14 sampai 21 (4 kolom). Klik ketiga tiap kolom mengembalikan sort ke default sehingga kolom berikutnya mulai dari keadaan yang sama (S-09).
- Temuan untuk QA:
  - TC-409 klik 2 (Newest First) dan klik 3 (kembali ke default Date Newest First) menghasilkan urutan baris yang sama; pembeda keadaan header (ikon sort) pada klik 3 tidak dinyatakan. Spec hanya mengasersi urutan baris pada klik 3.
  - TC-410 butir b mengasersi urutan kolom `Old Value` hanya untuk nilai kosong `—`; tidak dinyatakan urutan nilai lain, sehingga spec tidak mengasersinya.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (27 langkah nominal, sekitar 51 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
