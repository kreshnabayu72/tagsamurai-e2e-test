---
id: TC-AC-LCS-E2E-098-search-modal-changelog-reveal-dan-siklus
title: "Search Modal Changelog: Reveal Search Box, Siklus Interaksi, dan Panah Penutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-372
  - TC-AC-LCS-373
  - TC-AC-LCS-374
coverage:
  web: automated
---

# Search Modal Changelog: Reveal Search Box, Siklus Interaksi, dan Panah Penutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-372: Reveal search box: hover icon Search menampilkan tooltip dan klik membuka input dengan fokus kursor

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Hover icon Search di toolbar modal
3. Verifikasi tooltip "Search" tampil
4. Klik icon Search
5. Verifikasi input pencarian terbuka
6. Verifikasi kursor langsung fokus di input
7. Verifikasi placeholder input "Search field, modified by..."

### TC-AC-LCS-373: Siklus interaksi Search: ketik tidak memfilter, Enter memfilter, icon × menghapus teks tanpa mereset tabel, Enter pada input kosong mereset

8. Ketik `Grace` pada input Search tanpa menekan Enter
9. Verifikasi icon × muncul di dalam input
10. Verifikasi footer tetap `1–10 of 27`
11. Tekan Enter
12. Verifikasi footer `1–3 of 3`
13. Verifikasi baris Field Grace Period Duration dengan tanggal `23 May 26`, `14 May 26`, dan `05 May 26`
14. Klik icon × pada input
15. Verifikasi input kosong
16. Verifikasi tabel tetap menampilkan hasil `Grace` (`1–3 of 3`)
17. Tekan Enter pada input kosong
18. Verifikasi footer `1–10 of 27`

### TC-AC-LCS-374: Klik icon panah penutup pada search box menutup input dan mereset hasil

19. Ketik Search `Grace`, tekan Enter
20. Klik icon panah tutup pada input pencarian
21. Verifikasi search box tertutup kembali menjadi icon Search
22. Verifikasi footer `1–10 of 27`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: tidak ada selain langkah TC; ketiga TC berurutan dalam satu pembukaan modal dan state Search dari TC sebelumnya sudah bersih (input kosong) saat TC berikutnya dimulai (S-09).
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
