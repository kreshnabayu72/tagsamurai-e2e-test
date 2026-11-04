---
id: TC-AC-SU-E2E-103-tab-changelog-screening-dan-state
title: "Tab Changelog: Screening, Search Kosong, Tie-breaker Auto-Revert, Loading, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-368
  - TC-AC-SU-369
  - TC-AC-SU-370
  - TC-AC-SU-371
  - TC-AC-SU-373
  - TC-AC-SU-377
coverage:
  web: automated
---

# Tab Changelog: Screening, Search Kosong, Tie-breaker Auto-Revert, Loading, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE, dibaca dari Fixture `settingsUser`):
  - User A `Jane Smith {runId}-103` (email `janesmith+{runId}-103@qwertysystem.net`): Changelog berisi minimal entri `Assign`, `Edit`, `Remove`, `Activate` dengan satu entri Modified By `Admin U` (nama lengkap `Admin Utama`), ditambah pasangan entri `Edit` dan `Auto-Revert` (hasil satu edit CRUD pada target Total Control) dengan Date dan Modified By identik yang merupakan entri seeding terbaru.
  - User B `Rina Putri {runId}-103` (email `rinaputri+{runId}-103@qwertysystem.net`): tanpa entri Changelog (0 baris).
- Kemampuan teknis: Spectra.intercept untuk menahan respons request data tabel tab Changelog selama 3000 ms (TC-371; menahan respons hanya untuk mengamati Loading); kemampuan baca dan seed entri Changelog disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-368: Screening Tab Changelog

1. Ketik Search `Jane Smith {runId}-103`, tekan Enter
2. Klik Name `Jane Smith {runId}-103` untuk membuka Detail User
3. Klik tab `Changelog`
4. Verifikasi toolbar menampilkan `Search`, `Filter`, dan `Download`
5. Verifikasi toolbar tidak memuat icon Changelog terpisah
6. Verifikasi header kolom berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, `Column Visibility (⋯)`
7. Verifikasi kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By` sortable
8. Verifikasi header `Column Visibility (⋯)` unsortable, berfungsi sebagai overlay Column Visibility, dan tanpa row action
9. Verifikasi tidak ada kolom User Name
10. Verifikasi default sort Date Newest First (entri seeding terbaru berada di baris teratas)
11. Verifikasi footer menampilkan pagination standar

### TC-AC-SU-369: Modified By di Tab Changelog, hover menampilkan nama lengkap

12. Hover sel Modified By `Admin U`
13. Verifikasi tooltip menampilkan nama lengkap `Admin Utama`

### TC-AC-SU-373: Empty state hasil Search Tab Changelog tanpa kecocokan

14. Verifikasi sedikitnya satu baris data tampil pada tabel
15. Ketik Search `zzqx-tidak-ada`, tekan Enter
16. Verifikasi tabel menampilkan illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
17. Klik icon `(←)` pada kotak Search

### TC-AC-SU-377: Entri pemicu dan entri Auto-Revert bertimestamp sama

18. Verifikasi pada sort default (Newest First), entri `Auto-Revert` tampil di atas entri `Edit` pemicunya
19. Klik header `Date` satu kali (Oldest First)
20. Verifikasi entri `Edit` pemicu tampil di atas entri `Auto-Revert`
21. Klik header `Date` dua kali sampai kembali ke sort default Date Newest First

### TC-AC-SU-371: Loading state Tab Changelog

22. Pasang tahanan respons 3000 ms pada request data tabel tab Changelog
23. Muat ulang halaman Detail dengan F5
24. Klik tab `Changelog`
25. Verifikasi tabel menampilkan 5 skeleton rows sesuai layout kolom
26. Lepas tahanan respons setelah 3000 ms
27. Verifikasi baris data menggantikan skeleton rows
28. Lepas intercept request data tabel tab Changelog

### TC-AC-SU-370: Empty state Tab Changelog saat belum ada data

29. Buka Settings > User lewat sidebar
30. Ketik Search `Rina Putri {runId}-103`, tekan Enter
31. Klik Name `Rina Putri {runId}-103` untuk membuka Detail User
32. Klik tab `Changelog`
33. Verifikasi tabel menampilkan illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
34. Verifikasi pagination tidak menampilkan baris data

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah penghubung tanpa Verifikasi: tutup Search `(←)` (setelah TC-373), klik header `Date` dua kali ke sort default (setelah TC-377), lepas tahanan respons, muat ulang F5 sebelum klik tab pada TC-371 (agar request data tabel dikirim ulang dan dapat ditahan), dan kembali ke Settings > User lewat sidebar sebelum TC-370.
- Urutan blok mengikuti screening di awal dan empty state pada user B di akhir; TC-371 dan TC-370 memakai tab yang sama tetapi state data berbeda sehingga TC-370 memakai user kedua.
- Temuan untuk QA:
  - TC-370 meminta Jane Smith dengan 0 baris Changelog, sedangkan TC-368, 369, 373, dan 377 meminta Jane Smith dengan entri Changelog; satu user tidak dapat memenuhi keduanya. Spec memakai user B untuk TC-370. Tidak dinyatakan apakah proses seeding user sendiri menulis entri Changelog (yang membuat 0 baris tidak tercapai).
  - TC-371 tidak menyatakan cara memicu pemuatan ulang data tab; spec memakai F5 lalu klik tab (langkah penghubung).
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
