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
- Data Dinamis (Client A, disiapkan lewat skrip fixture oleh langkah 1):
  - D-09: draft Brand 13 baris (D-01 ditambah baris #13 `error` dengan Brand Name 121 karakter, nilai sumber Brand pertama tabel D-41) dengan badge saran AI pada sel Brand Name baris #13.
  - D-11: layanan AI mock deterministik mode normal (D-40, tabel D-41 dan D-42) disiapkan oleh langkah 1; dikembalikan ke normal oleh hook `after`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Langkah "Buka menu Import dari sidebar" mengikuti TC dan memuat ulang halaman.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: seluruh permintaan ditolak sehingga draft tidak berubah; hook `beforeEach` suite memulihkan draft dasar Client A; draft D-09 disiapkan oleh langkah 1.

## Test Steps

### TC-GS-IMPORT-42: AI Accept lewat permintaan langsung

1. Siapkan lewat skrip fixture draft Brand D-09 pada Client A (13 baris, baris #13 `error` dengan badge saran AI pada sel Brand Name) dan layanan AI mock deterministik mode normal (D-40), lalu muat ulang halaman Import > Brand
2. Ambil pengenal baris tetap `Row #` 13 dari respons pembacaan Staging Table dengan token akun Import data (Read Only) Client A
3. Kirim permintaan Accept saran AI untuk sel Brand Name baris #13 langsung ke server dengan token akun Import data (Read Only) Client A
4. Verifikasi server menolak permintaan dengan 403 Forbidden
5. Buka menu Import dari sidebar dengan akun yang sama
6. Klik halaman 2 pada Pagination
7. Verifikasi Staging Metric Cards Errors 1
8. Verifikasi baris #13 tetap berstatus `error`
9. Verifikasi sel Brand Name baris #13 masih berisi 121 karakter
10. Verifikasi badge saran AI pada sel Brand Name baris #13 masih tampil

### TC-GS-IMPORT-602: Delete All Rows lewat permintaan langsung

11. Kirim permintaan Delete All Rows untuk kategori pesan "Brand Name: Max. 120 characters" langsung ke server dengan token akun Import data (Read Only) Client A
12. Verifikasi server menolak permintaan dengan 403 Forbidden
13. Buka menu Import dari sidebar dengan akun yang sama
14. Verifikasi Staging Metric Cards Total Rows 13
15. Verifikasi Staging Metric Cards Errors 1

### TC-GS-IMPORT-603: AI Dismiss lewat permintaan langsung

16. Ambil pengenal baris tetap `Row #` 13 dari respons pembacaan Staging Table halaman 2 dengan token akun Import data (Read Only) Client A
17. Kirim permintaan Dismiss saran AI untuk sel Brand Name baris #13 langsung ke server dengan token akun Import data (Read Only) Client A
18. Verifikasi server menolak permintaan dengan 403 Forbidden
19. Buka menu Import dari sidebar dengan akun yang sama
20. Klik halaman 2 pada Pagination
21. Verifikasi Staging Metric Cards Errors 1
22. Verifikasi baris #13 tetap berstatus `error`
23. Verifikasi badge saran AI pada sel Brand Name baris #13 masih tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a). Asersi pada langkah permintaan langsung hanya status respons dan state data; perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (seed draft D-09 dan mock AI, K-7), langkah 2, 16 (mengambil pengenal baris), langkah 5, 13, 19 (muat ulang halaman Import), langkah 6 dan 20 (pindah ke halaman 2 agar baris #13 terbaca).
- Temuan untuk QA:
  - Mekanisme token sesi per akun tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-602 tidak membuka halaman 2 sehingga hanya Metric Cards yang diasersi; Post Condition "draft tetap 13 baris dengan 1 baris error" setara dengan Expected b.
