---
id: TC-AC-SU-E2E-122-tab-user-log-search-siklus-dan-per-kolom
title: "Tab User Log: Siklus Search Box dan Search per Kolom Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-434
  - TC-AC-SU-435
coverage:
  web: automated
---

# Tab User Log: Siklus Search Box dan Search per Kolom Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-122` (email `janesmith+{runId}-122@qwertysystem.net`) dengan 3 sesi Admin Console: (1) Activity `Session`, Note `Session started`, IP Address `203.0.113.10`, Device / Browser `Chrome on Windows`; (2) Note `Session ended`, IP Address `203.0.113.10`, Device / Browser `Chrome on Windows`; (3) Note `Session started`, IP Address `198.51.100.7`, Device / Browser `Firefox on Windows`. Keyword `203.0.113` memuat sesi (1) dan (2) saja.

| Search per kolom | Keyword huruf kecil | Keyword huruf kapital | Nilai yang cocok |
|---|---|---|---|
| Activity | `sess` | `SESS` | `Session` |
| Note | `ended` | `ENDED` | `Session ended` |
| IP Address | `203.0` | `203.0` | `203.0.113.10` |
| Device / Browser | `chrome` | `CHROME` | `Chrome on Windows` |

- Kemampuan teknis: kemampuan seed sesi User Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-434: Siklus interaksi Search box Tab User Log

1. Ketik Search `Jane Smith {runId}-122`, tekan Enter
2. Klik Name `Jane Smith {runId}-122`
3. Klik tab `User Log`
4. Hover icon Search
5. Verifikasi tooltip `Search` tampil
6. Klik icon Search
7. Verifikasi input Search melebar
8. Verifikasi kursor auto-focus di input Search
9. Verifikasi placeholder input Search `Search note, IP address, or device...`
10. Catat jumlah baris tabel User Log
11. Ketik `203.0.113` di input Search tanpa menekan Enter
12. Verifikasi icon `(✕)` muncul
13. Verifikasi tabel belum tersaring (jumlah baris sama dengan jumlah yang dicatat sebelum mengetik)
14. Tekan Enter
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi setiap baris yang tampil memuat `203.0.113`
17. Klik icon `(✕)`
18. Verifikasi input Search kosong
19. Verifikasi search bar tetap terbuka
20. Verifikasi tabel tetap menampilkan hasil search terakhir
21. Tekan Enter pada input kosong
22. Verifikasi tabel kembali menampilkan semua data (jumlah baris sama dengan jumlah yang dicatat)
23. Ketik Search `203.0.113`, tekan Enter
24. Klik icon `(←)`
25. Verifikasi search bar collapse ke icon
26. Verifikasi keyword Search kosong
27. Verifikasi tabel langsung kembali menampilkan semua data

### TC-AC-SU-435: Search Tab User Log per kolom kelas teks

28. Untuk setiap baris tabel "Search per kolom" di Prerequisites, lakukan langkah 29 sampai 33
29. Ketik Search keyword huruf kecil pada baris tabel 'Search per kolom', tekan Enter
30. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
31. Ganti isi kotak Search dengan keyword huruf kapital pada baris tabel yang sama, tekan Enter
32. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
33. Klik icon `(←)` pada kotak Search

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah Search per kolom diulang per baris tabel 'Search per kolom': langkah 29 sampai 33 (4 kolom, tiap kolom dua keyword). Tiap iterasi diakhiri klik `(←)` yang menutup dan mengosongkan Search sehingga iterasi berikutnya mulai dari kotak kosong (langkah penghubung).
- Temuan untuk QA:
  - TC-435 kolom `IP Address` memakai keyword `203.0` untuk 'huruf kecil' dan 'huruf kapital' sekaligus (angka tidak berkapitalisasi); spec mengulang keyword yang sama untuk kedua iterasi.
  - Search diterapkan pada seluruh kolom searchable, sehingga keyword seperti `sess` juga dapat cocok dengan kolom `Note` (`Session started`); TC tidak menyatakan apakah hasil hanya dari kolom yang disebut. Spec hanya mengasersi bahwa baris yang memuat nilai kolom itu tampil.
  - Cara men-seed sesi User Log (Date, Note, IP Address, user agent, asal Admin Console atau Global Settings, user pemilik sesi) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (33 langkah nominal, sekitar 48 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
