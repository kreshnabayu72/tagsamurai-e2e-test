---
id: TC-AC-SU-E2E-125-detail-user-pagination-dan-retensi-state-lintas-tab
title: "Detail User: Pagination Empat Tab dan Retensi Search atau Filter Lintas Tab"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-441
  - TC-AC-SU-442
coverage:
  web: automated
---

# Detail User: Pagination Empat Tab dan Retensi Search atau Filter Lintas Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- Data seeding (Fixture BE): user `Jane Smith {runId}-125` (email `janesmith+{runId}-125@qwertysystem.net`) dengan 30 baris pada masing-masing tab Responsibilities, Changelog, System Log, dan User Log. Tab Responsibilities berisi 30 baris Pending Approval Device Allocation ber-ID `HALC-2026-NNNN` (NNNN hasil seeding). Tab Changelog berisi 20 entri Action `Assign` (memuat keyword Search `Assign`) dan 10 entri Action lain (tidak memuat keyword). System Log (user sebagai aktor) berisi 20 entri Action `Deactivate` ber-Object `User` dan 10 entri dengan Action dan Object lain. User Log berisi sesi ber-IP prefix `203.0.113`.

| Tab uji | Keyword Search |
|---|---|
| `Responsibilities (30)` | `HALC-2026` (prefix kolom ID seluruh 30 baris seeding) |
| Changelog | `Assign` |
| System Log | `Deactivate` (Action pada 20 entri seeding) |
| User Log | `203.0.113` (prefix IP Address seluruh sesi seeding) |

- Kemampuan teknis: kemampuan seed baris Responsibilities, Changelog, System Log, dan User Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus.

## Test Steps

### TC-AC-SU-441: Pagination Tab Responsibilities, Changelog, System Log, User Log

1. Ketik Search `Jane Smith {runId}-125`, tekan Enter
2. Klik Name `Jane Smith {runId}-125`
3. Untuk setiap baris tabel "Tab uji" di Prerequisites, lakukan langkah 4 sampai 14
4. Klik tab pada baris tabel 'Tab uji'
5. Verifikasi tab menampilkan 10 baris secara default
6. Klik halaman 2
7. Verifikasi halaman 2 menampilkan baris ke-11 sampai ke-20
8. Ubah page size menjadi 25
9. Verifikasi tab menampilkan 25 baris
10. Klik halaman 2
11. Ketik Search keyword pada kolom 'Keyword Search' baris tabel itu, tekan Enter
12. Verifikasi tab kembali ke halaman 1
13. Klik icon `(←)` pada kotak Search
14. Ubah page size kembali menjadi 10

### TC-AC-SU-442: Pindah tab Detail tidak me-reset search atau filter tab lain

15. Klik tab `Changelog`
16. Ketik Search `Assign`, tekan Enter
17. Klik tab `System Log`
18. Klik icon Filter
19. Pilih `User` di field `Object`
20. Klik `[Apply]`
21. Klik tab `Changelog`
22. Verifikasi keyword Search `Assign` tetap terisi pada Tab Changelog
23. Verifikasi sedikitnya satu baris tampil pada Tab Changelog
24. Verifikasi Tab Changelog menampilkan hasil Search `Assign` (setiap baris yang tampil memuat `Assign`)
25. Klik tab `System Log`
26. Verifikasi badge titik pada icon Filter masih tampil pada Tab System Log
27. Verifikasi sedikitnya satu baris tampil pada Tab System Log
28. Verifikasi Tab System Log masih menampilkan filter Object `User` (setiap baris yang tampil memiliki Object `User`)
29. Klik icon Filter
30. Klik `[Clear Field]`, lalu klik `[Apply]`
31. Klik tab `Changelog`
32. Klik icon `(←)` pada kotak Search

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah per tab diulang per baris tabel 'Tab uji': langkah 4 sampai 14 (4 tab). Klik halaman 2 setelah mengubah page size menjadi 25, serta mengubah page size kembali menjadi 10 dan klik `(←)`, adalah langkah penghubung (halaman 2 dibutuhkan agar Search dijalankan dari halaman selain halaman 1; page size dikembalikan agar tab berikutnya mulai dari 10 baris).
- Pada TC-442 klik `[Clear Field]` lalu `[Apply]` dan klik `(←)` di akhir spec adalah langkah penghubung yang mengosongkan state (S-09).
- Temuan untuk QA:
  - TC-441 tidak menyebut keyword Search per tab; spec memakai nilai seeding. Kolom dan keyword Search tab Responsibilities tidak dinyatakan di TC ini; spec memakai prefix ID seeding `HALC-2026`.
  - TC-441 tidak menyatakan halaman yang aktif saat Search dijalankan setelah page size diubah; spec menambahkan klik halaman 2 sebelum Search agar 'kembali ke halaman 1' dapat diamati.
  - TC-441 butir a menyebut 'default 10 baris' dan 'halaman 2 = baris 11–20' tanpa menyatakan apakah page size bertahan antar tab; spec mengembalikan page size ke 10 pada akhir tiap iterasi.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (32 langkah nominal, sekitar 65 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
