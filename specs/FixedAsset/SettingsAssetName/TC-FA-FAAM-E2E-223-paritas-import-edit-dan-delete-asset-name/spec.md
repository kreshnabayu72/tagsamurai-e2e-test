---
id: TC-FA-FAAM-E2E-223-paritas-import-edit-dan-delete-asset-name
title: "Paritas Import: Asset Name Hasil Import Dapat Di-Edit dan Dihapus Mengikuti Guard In-Use"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-604
  - TC-FA-FAAM-605
coverage:
  web: automated
---

# Paritas Import: Asset Name Hasil Import Dapat Di-Edit dan Dihapus Mengikuti Guard In-Use

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`, `FA_IMPORT_PASSWORD`.
- Data Pre-setup (Pre-setup No. 28b, dibuat lewat Import oleh aktor Import Data `importData_automated_{namaCompany}@qwertysystem.net`, Pre-setup No. 9, kredensial `Spectra.env.FA_IMPORT_PASSWORD`; dipakai di hook `before` untuk membentuk data, tidak diasersi): `Imported Used` (Total Asset 2; hanya menjadi target Delete yang diblokir guard, tidak diubah, Last Updated tidak berubah).
- Data Dinamis, di-seed lewat Import di hook `before`, nama bersuffix `{runId}-223` (Tabel Data Uji Dinamis No. 94 dan 95; Total Asset 0): `Imported Item 604 {runId}-223` dan `Imported Item 605 {runId}-223`.
- Kemampuan teknis: seed lewat jalur Import oleh aktor Import Data; Modal Changelog dan Search di dalamnya. Changelog adalah audit trail permanen sehingga entri dicari lewat Search atas nama bersuffix unik.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Imported Item 604 {runId}-223` dan sisa `Imported Item 605 {runId}-223` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-604 dan 605: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-604: Asset Name hasil Import dapat di-Edit sama dengan hasil Create manual

1. Ketik Search `Imported Item 604 {runId}-223`, tekan Enter
2. Klik `⋯` baris `Imported Item 604 {runId}-223` lalu `Edit`
3. Ubah Code menjadi `IMP604-2`
4. Ubah UoM menjadi `Pcs`
5. Klik `[Save]`
6. Verifikasi toast `Success, asset name has been updated.`
7. Klik icon Changelog
8. Ketik Search `Imported Item 604 {runId}-223`, tekan Enter
9. Verifikasi satu baris Edit Field `Code` untuk `Imported Item 604 {runId}-223`
10. Verifikasi satu baris Edit Field `UoM` untuk `Imported Item 604 {runId}-223`
11. Tutup Modal Changelog

### TC-FA-FAAM-605: Asset Name hasil Import dapat dihapus mengikuti guard in-use

12. Ganti isi kotak search dengan `Imported Item 605 {runId}-223`, tekan Enter
13. Klik `⋯` baris `Imported Item 605 {runId}-223` lalu `Delete`
14. Klik `[Delete]`
15. Ketik Search `Imported Item 605 {runId}-223`, tekan Enter
16. Verifikasi empty state `No results found`, sehingga `Imported Item 605 {runId}-223` terhapus
17. Ganti isi kotak search dengan `Imported Used`, tekan Enter
18. Klik `⋯` baris `Imported Used` lalu `Delete`
19. Verifikasi dialog blok `Cannot Delete Asset Name`
20. Tutup dialog blok

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search untuk menemukan baris target), langkah 7, 8, 11 (membuka, mencari, dan menutup Modal Changelog; S-12, S-14), langkah 12, 15, 17 (Search untuk menemukan baris target atau memuat ulang hasil), dan langkah 20 (menutup dialog).
- Urutan TC: TC-FA-FAAM-604 sebelum TC-FA-FAAM-605 (aksi menghapus data di akhir; S-10).
- Temuan untuk QA:
  - TC-FA-FAAM-604 menyebut "ubah Code dan UoM" tanpa nilai baru; spec memilih Code `IMP604-2` dan UoM `Pcs` (Pre-setup No. 24).
  - TC-FA-FAAM-605 butir a ("terhapus") tidak menyebut toast; spec memakai empty state `No results found` hasil Search sebagai anchor.
  - Teks dialog blok pada TC-FA-FAAM-605 butir b hanya disebut judulnya (`Cannot Delete Asset Name`); isi dialog tidak diasersi.
