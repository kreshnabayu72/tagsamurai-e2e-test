---
id: TC-AC-SU-E2E-106-tab-changelog-search-kolom-non-searchable-dan-hidden
title: "Tab Changelog: Search Kolom Non-searchable dan Kolom Hidden"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-380
  - TC-AC-SU-381
coverage:
  web: automated
---

# Tab Changelog: Search Kolom Non-searchable dan Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-106` (email `janesmith+{runId}-106@qwertysystem.net`) dengan 2 entri Changelog: (1) Date `12 Jun 2026`, Action `Edit`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Admin U`; (2) Action `Assign`, Field `Manage group`, Old Value `Inactive`, New Value `Assigned`, Modified By `Budi S`. Nilai `12 Jun 2026` tidak muncul di kolom searchable mana pun dan nilai `Manage group` hanya ada di kolom `Field`.
- Kemampuan teknis: kemampuan seed entri Changelog dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-380: Kolom non-searchable tidak ikut dicari

1. Cari `Jane Smith {runId}-106` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Verifikasi sedikitnya satu baris data tampil pada tabel
4. Ketik Search `12 Jun 2026`, tekan Enter
5. Verifikasi tabel menampilkan empty state `No results found`
6. Klik icon `(←)` pada kotak Search
7. Klik icon Filter
8. Verifikasi Filter Panel memuat field `Date`
9. Klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-381: Kolom yang di-hide tidak ikut dicari lalu kembali searchable saat di-unhide

10. Klik header `⋯`, hilangkan centang kolom `Field` pada overlay Column Visibility
11. Verifikasi kolom `Field` tidak tampil pada tabel
12. Ketik Search `Manage group`, tekan Enter
13. Verifikasi tabel menampilkan empty state `No results found`
14. Klik icon `(←)` pada kotak Search
15. Klik header `⋯`, centang kembali kolom `Field` pada overlay Column Visibility
16. Verifikasi kolom `Field` tampil pada tabel
17. Ketik Search `Manage group`, tekan Enter
18. Verifikasi baris yang memuat `Manage group` tampil
19. Klik icon `(←)` pada kotak Search

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Klik `(←)` setelah tiap Search adalah langkah penghubung yang mengosongkan Search (S-09). Klik icon Filter, Verifikasi field `Date`, lalu menutup panel mengasersi Expected b TC-380 (penyaringan kolom Date hanya lewat Filter Panel) dan diturunkan dari TC-382 yang menyatakan `Date` ada di Filter Panel Tab Changelog.
- Temuan untuk QA:
  - Expected b TC-380 ('hanya tersedia lewat Filter Panel (bila Filterable)') bersifat penjelasan bersyarat dan tidak memiliki hasil teramati sendiri; spec mengasersinya lewat keberadaan field `Date` di Filter Panel.
  - Keyword `12 Jun 2026` ditulis lengkap tahun empat digit, sedangkan format tampil Date mengikuti Date Format General Settings (nilainya tidak tertulis di TC). Bila format menampilkan tahun dua digit, tidak adanya kecocokan terjadi dengan alasan yang berbeda dari 'kolom non-searchable'.
  - TC-381 menyebut 'hide kolom Field' lewat header `⋯` tanpa menyatakan kontrol yang diklik; spec memakai checkbox kolom pada overlay Column Visibility (sesuai TC-392).
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
