---
id: TC-FA-CF-E2E-183-global-value-document-tidak-terdaftar-di-file-manager-dan-recycle-bin
title: "Global Value Document: Tidak Terdaftar di File Manager dan Tidak Masuk Recycle Bin Saat Diganti"
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FACF-LOGIC-12a"]
trace:
  "FACF-LOGIC-12a": [8, 12, 22, 26]
coverage:
  web: automated
---

# Global Value Document: Tidak Terdaftar di File Manager dan Tidak Masuk Recycle Bin Saat Diganti

## Prerequisites

- Mode: FE+BE (backend nyata).
- Sumber: spec ini diturunkan langsung dari PRD `fixed-asset/settings-custom-fields/PRD/settings-custom-fields.md` (aturan `FACF-LOGIC-12a`) dan hanya mengamati sisi UI yang teramati: daftar File Manager FAMS (tab Files dan modal Recycle Bin, `fixed-asset/file-manager/PRD/file-manager.md`). Belum ada TestCase untuk aturan ini sehingga `sourceTc` tidak ada dan `sourceRules` mengutip ID PRD (konvensi sumber PRD).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Aktor Total Control memiliki akses File Manager.
- Berkas uji (fixture berkas `Fixture.berkasUji`; berkas baru bernama unik agar Search File Manager tidak bertabrakan dengan berkas spec lain): `cf-global-183-a.pdf` dan `cf-global-183-b.pdf`.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-183`): `Global Doc FM {runId}-183` (Document, General, Global; berkas awal `cf-global-183-a.pdf`, lalu diganti `cf-global-183-b.pdf`).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-183` beserta berkasnya.
- Kemampuan teknis: pemilihan berkas lewat file picker.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]
2. Isi Field Name `Global Doc FM {runId}-183`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
3. Pilih berkas `cf-global-183-a.pdf`
4. Klik [Submit]
5. Verifikasi toast "Success, custom field has been created." tampil
6. Buka Settings > File Manager, tab Files
7. Ketik Search `cf-global-183`, tekan Enter
8. Verifikasi tabel menampilkan `No results found`
9. Klik `(←)` pada kotak Search
10. Klik tombol `Recycle Bin`
11. Ketik Search `cf-global-183`, tekan Enter
12. Verifikasi tabel modal Recycle Bin menampilkan `No results found`
13. Tutup modal Recycle Bin

### FACF-LOGIC-12a: File Global Value yang diganti dihapus permanen, bukan soft-delete

14. Buka Settings > Custom Fields, tab General
15. Klik row action `⋯` > `Edit` pada baris `Global Doc FM {runId}-183`
16. Verifikasi kontrol Value menampilkan nama file `cf-global-183-a.pdf` pre-filled
17. Pilih berkas `cf-global-183-b.pdf`
18. Klik `[Save]`
19. Verifikasi toast "Success, custom field has been updated." tampil
20. Buka Settings > File Manager, tab Files
21. Ketik Search `cf-global-183`, tekan Enter
22. Verifikasi tabel menampilkan `No results found`
23. Klik `(←)` pada kotak Search
24. Klik tombol `Recycle Bin`
25. Ketik Search `cf-global-183-a`, tekan Enter
26. Verifikasi tabel modal Recycle Bin menampilkan `No results found`
27. Klik `(←)` pada kotak Search
28. Tutup modal Recycle Bin

## Notes

- Sumber PRD, bukan TC. Spec ini hanya mengamati sisi File Manager (tidak terdaftar di tab Files, tidak ada di Recycle Bin). Penghapusan permanen file dari penyimpanan itu sendiri tidak teramati lewat UI karena kartu Storage Usage adalah snapshot berkala (`FAFM-LOGIC-06`); lihat halaman coverage.
- Asersi absence (`No results found`) didahului langkah anchor positif pada blok yang sama (toast sukses langkah 5 dan 19).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 dan 14 sampai 15 (menyiapkan data dan membuka form), langkah 6, 9 sampai 11, 13, 20, 23 sampai 25, 27, dan 28 (navigasi, membersihkan Search, dan menutup modal).
- Kaskade hapus field, ganti Data Type, Value Type kembali ke Specific, dan Asset Name keluar dari Scope memakai jalur penghapusan file yang sama dan tidak teramati di UI, sehingga tidak diotomasi (lihat halaman coverage).
- Temuan untuk QA:
  - Label tombol `Recycle Bin` dan placeholder Search mengikuti `file-manager.md` §4 (tombol bertooltip `Recycle Bin`, placeholder `Search file name, asset...`); PRD modul ini tidak mendefinisikannya.
