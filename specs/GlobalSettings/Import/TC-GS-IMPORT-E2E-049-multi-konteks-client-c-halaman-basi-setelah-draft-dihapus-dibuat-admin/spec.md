---
id: TC-GS-IMPORT-E2E-049-multi-konteks-client-c-halaman-basi-setelah-draft-dihapus-dibuat-admin
title: "Multi-Konteks Client C: Halaman Basi Setelah Draft Dihapus atau Dibuat Admin Lain, Confirm Mapping Append ke Draft yang Sudah Hilang"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-868@L738
  - TC-GS-IMPORT-873
  - TC-GS-IMPORT-874
coverage:
  web: automated
---

# Multi-Konteks Client C: Halaman Basi Setelah Draft Dihapus atau Dibuat Admin Lain, Confirm Mapping Append ke Draft yang Sudah Hilang

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun, password lewat env:
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; login UI di hook `before`; satu-satunya sesi UI yang diasersi.
  - Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC2_PASSWORD`; hanya memicu perubahan state lewat sesi API ("lewat fixture permintaan" pada TC): Discard Draft Brand atau unggah `brand-3.csv` dan konfirmasi pemetaan sampai draft tersimpan. Kemampuan sesi API ini disediakan tim FE/BE.
  - Password tidak ditulis di spec atau fixture.
- Data: `brand-3.csv` (header `Brand Name`; Acme Corp, Lenovo, Zebra Technologies) dan `brand-3b.csv` (Hitachi, Philips, Sony). Client C tanpa draft Tab Brand sebelum tiap TC (Kontrak Fixture R1).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk Total Control Client C.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client C direset lewat skrip fixture di akhir tiap blok (R1).

## Test Steps

### TC-GS-IMPORT-868 (baris L738): Confirm Mapping pada alur Append membuat draft baru bila draft tujuan sudah dihapus

1. Unggah `brand-3.csv` dan klik [Confirm Mapping] sehingga draft Brand 3 baris terbentuk
2. Unggah `brand-3b.csv`, pada dialog Confirm Append Draft klik [Append Records], dan biarkan Modal Column Mapping terbuka
3. Tunggu aksi selesai (permintaan mendapat respons)
4. Admin kedua Client C (sesi API): Discard Draft Brand hingga draft terhapus
5. Klik [Confirm Mapping]
6. Verifikasi modal tertutup
7. Verifikasi toast sukses: "Success, row has been added."
8. Verifikasi toast "This draft is no longer available." tidak muncul
9. Verifikasi Staging Table menampilkan draft baru berisi 3 baris `pending` bernomor 1 sampai 3: `Hitachi`, `Philips`, `Sony`
10. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-873: Upload pada halaman basi setelah draft dihapus admin lain

11. Muat ulang halaman Import > Brand
12. Unggah `brand-3.csv` dan klik [Confirm Mapping] sehingga draft Brand 3 baris terbentuk (jangan muat ulang halaman setelahnya)
13. Tunggu aksi selesai (Modal Column Mapping tertutup)
14. Admin kedua Client C (sesi API): Discard Draft Brand hingga draft terhapus
15. Klik [Upload File] dan pilih `brand-3b.csv`
16. Pada dialog Confirm Append Draft klik [Append Records]
17. Verifikasi Modal Column Mapping terbuka untuk `brand-3b.csv`
18. Verifikasi toast "This draft is no longer available." tidak muncul
19. Verifikasi unggahan tidak ditolak
20. Klik [Cancel] pada Modal Column Mapping

### TC-GS-IMPORT-874: Upload dari halaman basi saat draft sudah dibuat admin lain

21. Muat ulang halaman Import > Brand (belum ada draft; jangan muat ulang halaman setelahnya)
22. Tunggu aksi selesai (permintaan mendapat respons)
23. Admin kedua Client C (sesi API): unggah `brand-3.csv` dan konfirmasi pemetaan hingga draft Brand 3 baris tersimpan
24. Klik [Upload File] dan pilih `brand-3b.csv`
25. Verifikasi Modal Column Mapping terbuka langsung tanpa dialog Confirm Append Draft
26. Klik [Confirm Mapping] pada Modal Column Mapping
27. Verifikasi toast sukses: "Success, row has been added."
28. Verifikasi Staging Table menampilkan satu draft berisi 6 baris `pending` bernomor 1 sampai 6 (3 baris Admin kedua lalu `Hitachi`, `Philips`, `Sony`)
29. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Halaman Total Control yang basi menjadi objek asersi (kelas c, prinsip 13c). Admin kedua hanya memicu perubahan lewat sesi API (P-2); tidak ada sesi UI kedua.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 29 (reset Client C), langkah 11 dan 21 (muat ulang halaman Import > Brand sesudah reset, halaman tanpa draft), langkah 20 (menutup modal agar blok berikutnya mulai dari layar awal), langkah 4, 14, 23 (pemicu Admin kedua lewat sesi API; langkah 4, 14, dan 23 didahului "Tunggu aksi selesai" langkah 3, 13, dan 22). Langkah 3, 13, 22 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum Admin kedua memicu perubahan lewat sesi API; penanda langkah 3 dan 22 permintaan mendapat respons, langkah 13 Modal Column Mapping tertutup). Penanda langkah 3 dan 22 tidak ada di TC; halaman dimuat segar pada langkah 21 sebelum pemicu dan tidak dimuat ulang sesudahnya.
- Pembagian TC lintas spec: nomor TC-GS-IMPORT-868 dipakai dua baris; spec ini memuat baris di L738 (Confirm Mapping pada alur Append) dan spec 073 memuat baris di L1077 (Take Over Session).
- Temuan untuk QA:
  - ID ganda TC-GS-IMPORT-868 (L738 dan L1077), 869 (L937 dan L1078), 870 (L1020 dan L1079), 871 (L938 dan L1080) dengan isi berbeda; `sourceTc` dan `check-suite.py` tidak dapat membedakannya. Usulan: QA memberi nomor baru pada empat baris di L1077-L1080.
  - TC-GS-IMPORT-868 dan 873 menyebut dialog "Confirm Append Draft", sedangkan TC lain memberi judul dialog yang sama "Append to Draft"; spec memakai nama dialog sesuai TC sumber.
