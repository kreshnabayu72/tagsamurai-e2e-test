---
id: TC-GS-IMPORT-E2E-045-defense-in-depth-ai-accept-delete-all-rows-dan-ai-dismiss-langsung
title: "Defense-in-depth: AI Accept, Delete All Rows, dan AI Dismiss Langsung Ditolak 403 untuk Import data (Read Only)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-42
  - TC-GS-IMPORT-602
  - TC-GS-IMPORT-603
coverage:
  web: automated
---

# Defense-in-depth: AI Accept, Delete All Rows, dan AI Dismiss Langsung Ditolak 403 untuk Import data (Read Only)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Klien HTTP: spec mengirim permintaan langsung ke server dengan token sesi akun yang diuji. Token diperoleh lewat login API yang disediakan tim FE/BE (mekanisme tidak tertulis di TC, PRD, atau LLD).
- Akun: Import data (Read Only) Client A (Tono Hartono) `importRead_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_IMPORTRO_PASSWORD`; login UI di hook `before`, hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC):
  - D-09: draft Brand 13 baris (D-01 ditambah baris #13 `error` dengan Brand Name 121 karakter, nilai sumber Brand pertama tabel D-41) dengan badge saran AI pada sel Brand Name baris #13.
  - D-11: layanan AI mock deterministik mode normal (D-40, tabel D-41 dan D-42) disiapkan sebelum spec; dikembalikan ke normal sesudah spec.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Langkah "Buka menu Import dari sidebar" mengikuti TC dan memuat ulang halaman.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: seluruh permintaan ditolak sehingga draft tidak berubah; hook `beforeEach` suite memulihkan draft D-09.

## Test Steps

### TC-GS-IMPORT-42: AI Accept lewat permintaan langsung

1. Ambil pengenal baris tetap `Row #` 13 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
2. Kirim permintaan Accept saran AI untuk sel Brand Name baris #13 langsung ke server dengan token akun Import data (Read Only) Client A
3. Verifikasi server menolak permintaan dengan 403 Forbidden
4. Buka menu Import dari sidebar dengan akun yang sama
5. Klik halaman 2 pada Pagination
6. Verifikasi Staging Metric Cards Errors 1
7. Verifikasi baris #13 tetap berstatus `error`
8. Verifikasi sel Brand Name baris #13 masih berisi 121 karakter
9. Verifikasi badge saran AI pada sel Brand Name baris #13 masih tampil

### TC-GS-IMPORT-602: Delete All Rows lewat permintaan langsung

10. Kirim permintaan Delete All Rows untuk kategori pesan "Brand Name: Max. 120 characters" langsung ke server dengan token akun Import data (Read Only) Client A
11. Verifikasi server menolak permintaan dengan 403 Forbidden
12. Buka menu Import dari sidebar dengan akun yang sama
13. Verifikasi Staging Metric Cards Total Rows 13
14. Verifikasi Staging Metric Cards Errors 1

### TC-GS-IMPORT-603: AI Dismiss lewat permintaan langsung

15. Ambil pengenal baris tetap `Row #` 13 dari respons pembacaan Staging Table halaman 2 dengan token akun Import data (Read Only) Client A
16. Kirim permintaan Dismiss saran AI untuk sel Brand Name baris #13 langsung ke server dengan token akun Import data (Read Only) Client A
17. Verifikasi server menolak permintaan dengan 403 Forbidden
18. Buka menu Import dari sidebar dengan akun yang sama
19. Klik halaman 2 pada Pagination
20. Verifikasi Staging Metric Cards Errors 1
21. Verifikasi baris #13 tetap berstatus `error`
22. Verifikasi badge saran AI pada sel Brand Name baris #13 masih tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a). Asersi pada langkah permintaan langsung hanya status respons dan state data; perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 15 (mengambil pengenal baris), langkah 4, 12, 18 (muat ulang halaman Import), langkah 5 dan 19 (pindah ke halaman 2 agar baris #13 terbaca).
- Temuan untuk QA:
  - Mekanisme token sesi per akun tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-602 tidak membuka halaman 2 sehingga hanya Metric Cards yang diasersi; Post Condition "draft tetap 13 baris dengan 1 baris error" setara dengan Expected b.
