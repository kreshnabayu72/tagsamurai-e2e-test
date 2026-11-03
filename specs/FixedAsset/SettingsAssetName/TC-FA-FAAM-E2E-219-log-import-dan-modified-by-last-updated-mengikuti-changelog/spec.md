---
id: TC-FA-FAAM-E2E-219-log-import-dan-modified-by-last-updated-mengikuti-changelog
title: "Pencatatan: Asset Name Hasil Import Action Create dan Modified By-Last Updated Mengikuti Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-578
  - TC-FA-FAAM-584
coverage:
  web: automated
---

# Pencatatan: Asset Name Hasil Import Action Create dan Modified By-Last Updated Mengikuti Changelog

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor pertama: Total Control (Sarah Johnson, `Sarah J` pada kolom Modified By menurut TC) `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor kedua (ganti akun eksplisit di langkah 11): David Kurniawan, pemegang Role Total Control; email tidak tertulis di Pre-setup TC dan disediakan tim FE. Kredensial `Spectra.env.FA_DAVID_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo).
- Env var: `FA_TC_PASSWORD`, `FA_DAVID_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 28 (aktor Changelog contoh Sarah Johnson dan David Kurniawan), No. 25 (Label).
- Data Dinamis, di-seed lewat API di hook `before`:
  - `Imported Item 578 {runId}-219` (Tabel Data Uji Dinamis No. 93; fixture No. 28b, Total Asset 0) dibuat lewat Import Tab Asset Name oleh aktor Import Data (`importData_automated_{namaCompany}@qwertysystem.net`, Tabel Pre-setup No. 9, kredensial `Spectra.env.FA_IMPORT_PASSWORD`; dipakai di hook `before`, tidak diasersi).
  - `Edit Target Item 584 {runId}-219` (Code `ETI584`; Tabel Dinamis No. 51): salinan fixture 13d, Total Asset 0, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`, Default Label `Rename Label 584 {runId}-219` (fixture 25b).
  - Hasil edit Code TC-FA-FAAM-584: `MLU1`; hasil rename label: `Renamed Label 584 {runId}-219`.
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; seed lewat Import oleh aktor Import Data. Changelog adalah audit trail permanen sehingga entri dicari lewat Search atas nama bersuffix unik.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini dan label lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-578 dan 584: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-578: Asset Name hasil Import dicatat Action Create tanpa penanda asal

1. Ketik Search `{runId}-219`, tekan Enter
2. Klik icon Changelog
3. Ketik Search `Imported Item 578 {runId}-219`, tekan Enter
4. Verifikasi baris Action `Create` untuk `Imported Item 578 {runId}-219`, Field `Asset Name`, Old `—`, New `Imported Item 578 {runId}-219`, Modified By aktor import
5. Verifikasi baris Create itu tidak memuat penanda asal
6. Tutup Modal Changelog

### TC-FA-FAAM-584: Modified By dan Last Updated mengikuti entri Changelog terbaru

7. Klik `⋯` baris `Edit Target Item 584 {runId}-219` lalu `Edit` sebagai Sarah Johnson
8. Ubah Code menjadi `MLU1`
9. Klik `[Save]`
10. Catat Last Updated baris `Edit Target Item 584 {runId}-219` sebagai waktu Edit Code
11. Logout lalu login sebagai David Kurniawan
12. Ketik Search `Edit Target Item 584 {runId}-219`, tekan Enter
13. Klik `⋯` baris `Edit Target Item 584 {runId}-219` lalu `Edit`
14. Klik `[Save]` tanpa perubahan
15. Kembali ke List Asset Name
16. Verifikasi Modified By baris `Edit Target Item 584 {runId}-219` tetap `Sarah J`
17. Verifikasi Last Updated baris itu tetap sama dengan waktu Edit Code pada langkah 10
18. Buka tab Labels
19. Ubah nama label `Rename Label 584 {runId}-219` menjadi `Renamed Label 584 {runId}-219`
20. Buka tab Asset Name
21. Ketik Search `Edit Target Item 584 {runId}-219`, tekan Enter
22. Verifikasi Modified By baris `Edit Target Item 584 {runId}-219` tetap `Sarah J`
23. Verifikasi Last Updated baris itu tetap sama dengan waktu Edit Code pada langkah 10

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search tabel utama), langkah 2 sampai 3 (membuka dan mencari di Modal Changelog; S-12, S-14), langkah 6 (menutup Modal Changelog), langkah 10 (mencatat waktu Edit Code), langkah 12 dan 21 (Search tabel utama untuk menemukan baris target; kotak search mengganti isi sebelumnya), langkah 15 (kembali ke List), dan langkah 18 serta 20 (pindah tab).
- Ganti akun eksplisit di langkah 11 (S-07); sesi dikembalikan ke akun default suite di hook `after`.
- Temuan untuk QA:
  - TC-FA-FAAM-584 menyebut Sarah Johnson dan David Kurniawan tanpa email dan tanpa menyatakan akun mana yang dipakai sesi Total Control default; spec mengasumsikan akun default suite adalah Sarah Johnson dan David Kurniawan adalah akun Total Control kedua yang disediakan tim FE.
  - TC-FA-FAAM-578 memakai Modified By "aktor import" tanpa nama; spec mengasersi baris memuat aktor import tanpa format nama.
  - TC-FA-FAAM-584 butir "Last Updated tetap waktu Edit Code" dibandingkan dengan nilai yang dicatat pada langkah 10 (ketelitian menit).
