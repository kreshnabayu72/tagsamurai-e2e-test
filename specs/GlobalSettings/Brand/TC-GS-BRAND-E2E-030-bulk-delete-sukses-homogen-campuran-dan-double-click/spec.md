---
id: TC-GS-BRAND-E2E-030-bulk-delete-sukses-homogen-campuran-dan-double-click
title: "Bulk Delete Berhasil: Homogen, Campuran, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-116
  - TC-GS-BRAND-118
  - TC-GS-BRAND-125
coverage:
  web: automated
---

# Bulk Delete Berhasil: Homogen, Campuran, dan Klik Ganda

## Prerequisites

- Mode: FE+BE. Spec menghapus data (aksi destruktif), sehingga dijalankan sesudah spec lain selesai (suite `parallel: false`).
- Akun: Total Control Client A, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A: Zenith Corp (FAMS: Drill, 1 asset name; in-use, dilewati saat Bulk Delete campuran dan tidak berubah).
- Seeding (lewat API di hook `before`, milik spec ini karena brand-nya dihapus spec):
  - Brand bebas relasi milik spec ini (setara brand Population D-01 tetapi bersuffix, karena spec menghapusnya): `Iris Optics {runId}-030`, `Juniper Labs {runId}-030`, `Keystone Mfg {runId}-030`, `Harbor Tech {runId}-030`, dan `Linear Dynamics {runId}-030`.
  - D-25 bebas relasi: `Wisp Co {runId}-030` dan `Yew Co {runId}-030` (dependensi TC-GS-BRAND-124 dipenuhi lewat seeding).
- Suite berjalan serial pada Client A. Spec ini tidak memakai nama literal Population D-01 sehingga tidak menghapus atau mengubah brand D-01 milik spec lain. Dengan 12 brand Pre-setup, paling banyak 12 brand D-01 dari spec lain, dan 7 brand spec ini, total paling banyak 31 brand sehingga seluruhnya tampil pada satu halaman dengan page size 50.
- Opsi page size 50 tersedia pada paginasi tabel.
- Cleanup: hook `after` menghapus brand seeding yang masih tersisa (jalur gagal) lewat API tanpa berasumsi seeding berhasil penuh, dan memulihkan page size (10) serta seleksi tabel ke default.
- Kemampuan teknis: klik ganda cepat (dua klik berurutan dalam waktu sangat singkat) pada tombol dialog; pemantauan request jaringan untuk menghitung request Delete yang terkirim; membuka Modal Changelog Brand dari icon `[Changelog]` toolbar.
- TC-GS-BRAND-116: `Iris Optics {runId}-030`, `Juniper Labs {runId}-030`, `Keystone Mfg {runId}-030` bebas relasi (3 brand).
- TC-GS-BRAND-118: `Harbor Tech {runId}-030` dan `Linear Dynamics {runId}-030` bebas relasi; Zenith Corp in-use.
- TC-GS-BRAND-125: D-25 tersedia.

## Test Steps

### TC-GS-BRAND-116: Bulk Delete homogen berhasil

1. Ubah page size tabel menjadi 50
2. Centang `Iris Optics {runId}-030`, `Juniper Labs {runId}-030`, dan `Keystone Mfg {runId}-030`
3. Klik `Bulk Action` > `Delete`
4. Klik [Delete]
5. Verifikasi toast sukses: "Success, brand has been deleted."
6. Verifikasi `Iris Optics {runId}-030`, `Juniper Labs {runId}-030`, dan `Keystone Mfg {runId}-030` hilang dari tabel
7. Verifikasi Bulk Action Bar hilang
8. Verifikasi seleksi 0

### TC-GS-BRAND-118: Bulk Delete campuran menghapus yang bebas dan melewati yang in-use

9. Centang `Harbor Tech {runId}-030`, `Linear Dynamics {runId}-030`, dan Zenith Corp
10. Klik `Bulk Action` > `Delete`
11. Klik [Continue]
12. Verifikasi toast sukses: "Success, brand has been deleted. Some items were skipped."
13. Verifikasi `Harbor Tech {runId}-030` dan `Linear Dynamics {runId}-030` hilang dari tabel
14. Verifikasi Zenith Corp tetap ada di tabel
15. Verifikasi Bulk Action Bar hilang
16. Verifikasi seleksi 0

### TC-GS-BRAND-125: Klik ganda Delete pada dialog bulk hanya memproses satu request

17. Centang `Wisp Co {runId}-030` dan `Yew Co {runId}-030`
18. Klik `Bulk Action` > `Delete`
19. Klik [Delete] dua kali cepat
20. Verifikasi hanya satu toast sukses: "Success, brand has been deleted."
21. Verifikasi hanya satu request Delete terkirim ke server
22. Verifikasi `Wisp Co {runId}-030` dan `Yew Co {runId}-030` hilang dari tabel
23. Klik icon `[Changelog]` pada toolbar tabel untuk membuka Modal Changelog Brand
24. Search `Wisp Co {runId}-030` di Modal Changelog
25. Verifikasi satu entri Action Delete untuk `Wisp Co {runId}-030`
26. Search `Yew Co {runId}-030` di Modal Changelog
27. Verifikasi satu entri Action Delete untuk `Yew Co {runId}-030`
28. Tutup Modal Changelog Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Dialog yang dikonfirmasi pada langkah 4 adalah Dialog 4 (homogen, [Delete]); langkah 11 memakai Dialog 3 (campuran, [Continue]); langkah 19 memakai Dialog 4 untuk dua brand bebas relasi.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (page size 50 supaya seluruh brand yang dicentang, termasuk Zenith Corp, berada pada satu halaman), 23, 24, 26 (membuka Modal Changelog Brand dan Search nama brand untuk menemukan entri yang diasersi pada Expected Result b TC-GS-BRAND-125) dan 28 (menutup Modal Changelog).
- Langkah 25 dan 27 menegaskan tepat satu entri Delete per brand (hitungan entri ada, bukan absence log). Asersi "tidak ada entri log" tidak dimuat di spec ini; asersi absence berada di spec kelas absence.
- Aksi dialog yang hanya dibatalkan atau diblokir diuji di spec `TC-GS-BRAND-E2E-029-bulk-delete-dialog-screening-cancel-dan-blokir`.
- Aksi menghapus data ditaruh di dalam satu spec dengan urutan homogen, campuran, lalu klik ganda; tidak ada TC sumber yang memakai brand TC lain, sehingga urutan sumber (116, 118, 125) dipertahankan.
