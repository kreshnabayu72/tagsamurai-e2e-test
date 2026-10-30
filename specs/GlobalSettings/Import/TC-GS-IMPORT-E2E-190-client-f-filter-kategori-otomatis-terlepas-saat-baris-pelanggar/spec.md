---
id: TC-GS-IMPORT-E2E-190-client-f-filter-kategori-otomatis-terlepas-saat-baris-pelanggar
title: "Client F: filter kategori otomatis terlepas saat baris pelanggar terakhir hilang, dan kartu Active berhitung 0 setelah admin kedua menghapus (race pemicu)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-466
  - TC-GS-IMPORT-471
coverage:
  web: automated
---

# Client F: filter kategori otomatis terlepas saat baris pelanggar terakhir hilang, dan kartu Active berhitung 0 setelah admin kedua menghapus (race pemicu)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client F (Hendra Wijaya) `totalControl_automated_qaTeam6@qwertysystem.net`, password `Spectra.env.GS_CLIENTF_TC_PASSWORD` (TC tidak menyebut password per akun, lihat Temuan untuk QA).
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client F (Qori Fadillah) `totalControlSecond_automated_qaTeam6@qwertysystem.net`, password `Spectra.env.GS_CLIENTF_TC2_PASSWORD` (nama env baru). Sesi API menghapus Row # 5 dan Row # 6 untuk TC-GS-IMPORT-466; klien HTTP disediakan tim FE/BE, endpoint hapus baris mengikuti kontrak modul (tidak ditulis di TC; lihat Temuan untuk QA).
- Layar awal: hook `beforeEach` membuka Import > Brand Client F.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-10: draft Brand campuran Client F (5 `pending`, 3 `error`, 2 `duplicate`; Row # 5 `Samsung` dan Row # 6 `Pioneer` duplicate; Row # 7 nama 121 karakter, Row # 8 `Rocket 🚀`, Row # 9 `Star ⭐`), disiapkan lewat skrip seed. D-10 dibuat ulang sebelum tiap TC (hook langkah penghubung memanggil skrip seed): sebelum TC-GS-IMPORT-471 dan sebelum TC-GS-IMPORT-466. TC-GS-IMPORT-471 dijalankan lebih dulu karena penomoran ulang Row # 7 dan 8 bergantung pada Row # 5 dan 6 `duplicate` masih ada.
- Cleanup (hook `after`): draft Brand Client F dibuang lewat skrip reset (Post Condition TC: D-10 dipulihkan).
- Kemampuan teknis: skrip seed D-10, sesi API Admin kedua Client F.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Filter kategori terlepas otomatis (TC-GS-IMPORT-471)

1. Klik `[View Data]` pada baris pesan `Brand Name: Max. 120 characters` (kategori yang hanya punya 1 baris, Row # 7)
2. Verifikasi chip "Showing rows with: Brand Name: Max. 120 characters" tampil
3. Verifikasi tabel memuat 1 baris
4. Klik row action `⋯` pada Row # 7 lalu Remove
5. Klik `[Delete]` pada Dialog Delete Row
6. Verifikasi muncul toast sukses: "Success, row has been deleted."
7. Verifikasi chip filter kategori terlepas otomatis
8. Verifikasi kartu Errors tetap Active
9. Verifikasi tabel menampilkan 2 baris `error` yang tersisa (Row # 7 dan 8 setelah penomoran ulang)
10. Verifikasi baris pesan `Brand Name: Max. 120 characters` hilang dari Callout
11. Verifikasi baris pesan `Brand name contains invalid characters` dengan badge "2 rows" tetap tampil
12. Pulihkan D-10 (buat ulang draft Brand campuran Client F lewat skrip seed), lalu muat ulang halaman Import > Brand

### Kartu Active berhitung 0 (race) (TC-GS-IMPORT-466)

13. Klik kartu Duplicates
14. Admin kedua Client F (sesi API) menghapus Row # 5 dan Row # 6 (kedua baris duplicate) dari Staging Table hingga tersimpan
15. Tekan `F5` pada halaman admin pertama
16. Verifikasi kartu Duplicates tetap Active dengan angka `0`
17. Verifikasi tabel menampilkan empty state dengan Title "No results found"
18. Verifikasi empty state memuat Description "There are no rows matching this status anymore."
19. Klik kartu Total Rows
20. Verifikasi tabel menampilkan 8 baris (5 `pending` dan 3 `error`)
21. Verifikasi kartu Total Rows Active
22. Pulihkan D-10 (buat ulang draft Brand campuran Client F lewat skrip seed)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- P-2: Admin kedua Client F hanya memicu perubahan state (menghapus baris) lewat sesi API; hasil diasersi hanya di sesi admin pertama, sehingga spec ini tetap fungsional (bukan kelas c).
- Urutan TC-471 sebelum TC-466 mengikuti catatan Data Dinamis (penomoran ulang Row #); langkah 12 dan 22 memulihkan D-10 (Post Condition TC).
- Langkah 12 memuat ulang halaman setelah seed ulang agar tabel memuat draft baru (langkah penghubung, S-03).
- Temuan untuk QA:
  - TC-GS-IMPORT-466 langkah 2 ("Admin kedua ... menghapus Row # 5 dan Row # 6") tidak menyebut mekanisme penghapusan; spec memakai sesi API Admin kedua sesuai aturan pelaku kedua (P-2) dan kontrak endpoint disediakan tim FE/BE, bukan dikarang di spec.
  - TC-GS-IMPORT-466 Post Condition ("Draft Brand pada Client F dipulihkan") ditulis sebagai langkah pemulihan, tanpa asersi.
  - TC-GS-IMPORT-471 Post Condition dipulihkan dengan cara yang sama.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
