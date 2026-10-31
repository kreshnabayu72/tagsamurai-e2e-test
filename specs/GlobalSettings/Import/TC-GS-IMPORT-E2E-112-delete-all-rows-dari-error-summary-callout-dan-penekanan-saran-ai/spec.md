---
id: TC-GS-IMPORT-E2E-112-delete-all-rows-dari-error-summary-callout-dan-penekanan-saran-ai
title: "Delete All Rows dari Error Summary Callout dan penekanan saran AI dihapus oleh Remove dan Discard Draft"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-274
  - TC-GS-IMPORT-275
  - TC-GS-IMPORT-279
  - TC-GS-IMPORT-285
coverage:
  web: automated
---

# Delete All Rows dari Error Summary Callout dan penekanan saran AI dihapus oleh Remove dan Discard Draft

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global (mock AI, hook umur draft) dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Penghapus kategori kedua (hanya memicu perubahan state, P-2): sesi API dengan akun Total Control Client A yang sama pada konteks terpisah; klien HTTP disediakan tim FE/BE.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Layanan AI: mock tetap mode normal (D-40, tabel D-41 dan D-42; saran untuk Brand Name 121 karakter pertama D-41: `Samsung Electronics Indonesia`); disediakan tim FE/BE.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12), dibuat ulang lewat skrip fixture sebelum tiap blok (Kontrak Fixture R2): D-09 (Draft Brand 13 baris Client A: D-01 ditambah baris #13 `error` dengan Brand Name 121 karakter nilai sumber Brand pertama tabel D-41, yaitu `PT Samsung Electronics Indonesia Manufacturing and Distribution Company for Consumer Electronics and Home Appliances Prod`, sehingga badge saran AI tampil); berkas `brand-overlength.csv`: header `Brand Name`; 1 baris data berisi nilai sumber yang sama (121 karakter). D-76 varian 1 (hook umur draft): `created_at` job dimundurkan 25 jam untuk TC-285 sehingga Unsaved Banner tampil (hanya pemicu banner).
- Kemampuan teknis: skrip seed D-09 dan hook umur draft D-76 (`created_at` atau jam server), mock AI, sesi API penghapus kategori kedua (disediakan tim FE/BE).
- State global: jam server atau `created_at` draft diubah oleh D-76; hook `after` memulihkan jam server, mode mock AI normal, dan draft ke D-01.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01, mode mock AI ke normal, dan jam server.

## Test Steps

### TC-GS-IMPORT-279: Remove baris menghapus penekanan saran AI

1. Seed draft D-09 di Client A lewat skrip fixture, lalu muat ulang halaman Import > Brand
2. Klik tombol halaman 2 pada paginator
3. Klik `[Dismiss]` pada badge saran AI di sel Brand Name baris #13
4. Klik `⋯` pada baris #13, pilih `Remove`
5. Klik `[Delete]`
6. Klik `[Upload File]` dan pilih berkas `brand-overlength.csv` pada file picker
7. Klik `[Append Records]` pada dialog "Append to Draft"
8. Klik `[Confirm Mapping]`
9. Klik tombol halaman 2 pada paginator
10. Verifikasi baris #13 berstatus `error`
11. Verifikasi badge `AI suggestion: 'Samsung Electronics Indonesia'?` tampil pada sel Brand Name baris #13

### TC-GS-IMPORT-275: Delete All Rows dari halaman basi pada kategori yang sudah kosong

12. Tunggu toast lama hilang otomatis; seed ulang draft D-09 di Client A lewat skrip fixture, lalu muat ulang halaman Import > Brand
13. Verifikasi baris pesan "Brand Name: Max. 120 characters" tampil di Error Summary Callout
14. Penghapus kategori kedua menghapus seluruh baris kategori "Brand Name: Max. 120 characters" lewat sesi API hingga tersimpan
15. Pada halaman yang belum dimuat ulang: klik `[Delete All Rows]` pada baris pesan yang sama
16. Verifikasi tidak ada dialog yang tampil
17. Verifikasi tidak ada toast error
18. Verifikasi Staging Metric Cards: Total Rows 12 dan Errors 0 (tidak ada baris lain terhapus)

### TC-GS-IMPORT-274: Delete All Rows menghapus seluruh baris kategori tanpa dialog

19. Tunggu toast lama hilang otomatis; seed ulang draft D-09 di Client A lewat skrip fixture, lalu muat ulang halaman Import > Brand
20. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
21. Verifikasi tidak ada dialog konfirmasi
22. Verifikasi muncul toast sukses: "Success, row has been deleted."
23. Verifikasi baris #13 terhapus: Total Rows 12 dan Errors 0
24. Verifikasi baris pesan "Brand Name: Max. 120 characters" hilang dari Error Summary Callout

### TC-GS-IMPORT-285: Discard Draft menghapus penekanan saran AI (paling akhir)

25. Tunggu toast lama hilang otomatis; seed ulang draft D-09 di Client A lewat skrip fixture, mundurkan `created_at` draft 25 jam (hook umur draft D-76 varian 1), lalu muat ulang halaman Import > Brand
26. Klik tombol halaman 2 pada paginator
27. Klik `[Dismiss]` pada badge saran AI di sel Brand Name baris #13
28. Klik `[Discard]` pada Unsaved Banner
29. Klik `[Discard Draft]`
30. Verifikasi Dropzone tampil
31. Verifikasi Unsaved Banner tidak tampil
32. Klik `[Upload File]` dan pilih berkas `brand-overlength.csv` pada file picker
33. Verifikasi dialog Append to Draft tidak tampil
34. Verifikasi Modal Column Mapping terbuka
35. Klik `[Confirm Mapping]`
36. Verifikasi draft berisi 1 baris `error` (hanya baris dari berkas)
37. Verifikasi badge `AI suggestion: 'Samsung Electronics Indonesia'?` tampil pada sel Brand Name

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (mock AI mode normal default dan hook umur draft hanya pemicu); penghapus kategori kedua hanya pemicu (P-2, sesi API).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-279, TC-275, TC-274, lalu TC-285 (menghapus draft) paling akhir; tiap blok menyiapkan D-09 sendiri (Kontrak Fixture R2, "dibuat ulang per TC").
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 12, 19, 25 menyiapkan D-09; langkah 14 menjalankan Langkah 2 sampai 3 TC-275 (Tab 2 menghapus kategori) sebagai sesi API (P-2).
- Spec berisi 37 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (penghapusan baris error dan saran AI), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-258 sampai 260 (Remove) ada di spec 108.
- Temuan untuk QA:
  - Post Condition semua TC kosong; tidak ada yang diasersi.
  - TC-GS-IMPORT-285 Dependensi D-76 varian 1 hanya sebagai pemicu Unsaved Banner; mekanisme (fixture timestamp atau jam server) disediakan tim FE/BE (S-13).
