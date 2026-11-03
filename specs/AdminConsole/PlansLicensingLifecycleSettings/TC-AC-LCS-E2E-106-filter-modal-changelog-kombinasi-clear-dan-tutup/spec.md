---
id: TC-AC-LCS-E2E-106-filter-modal-changelog-kombinasi-clear-dan-tutup
title: "Filter Modal Changelog: Kombinasi AND, Tanpa Hasil, Clear Field, dan Tutup Tanpa Apply"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-395
  - TC-AC-LCS-396
  - TC-AC-LCS-397
  - TC-AC-LCS-398
coverage:
  web: automated
---

# Filter Modal Changelog: Kombinasi AND, Tanpa Hasil, Clear Field, dan Tutup Tanpa Apply

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

### TC-AC-LCS-395: Kombinasi filter Modified By dan Field menghasilkan irisan (AND)

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Klik icon Filter, pilih `Sarah Thompson` pada `Modified By` dan `Grace Period Duration` pada `Field`, klik `[Apply]`
3. Verifikasi footer `1–3 of 3`
4. Verifikasi baris 1: `23 May 26` jam `10:00`, Edit, Grace Period Duration, 115, 118, Sarah T
5. Verifikasi baris 2: `14 May 26` jam `10:00`, Edit, Grace Period Duration, 70, 73, Sarah T
6. Verifikasi baris 3: `05 May 26` jam `10:00`, Edit, Grace Period Duration, 25, 28, Sarah T

### TC-AC-LCS-396: Filter tanpa baris yang cocok menampilkan empty state filtered

7. Klik `[Clear Field]`, klik `[Apply]`
8. Pilih rentang `01 Jun 26` sampai `30 Jun 26` pada `Date`, klik `[Apply]`
9. Verifikasi empty state filtered: Illustration, Title "No results found", Description "Try adjusting your search or filter."

### TC-AC-LCS-397: Clear Field pada Filter Panel mengosongkan field filter dan Apply mengembalikan semua baris

10. Klik `[Clear Field]`, klik `[Apply]`
11. Pilih `John Doe` pada `Modified By`, klik `[Apply]`
12. Klik `[Clear Field]`
13. Verifikasi field `Modified By` kosong (placeholder "All users")
14. Verifikasi tidak ada dialog yang tampil
15. Klik `[Apply]`
16. Verifikasi footer `1–10 of 27`

### TC-AC-LCS-398: Menutup panel Filter tanpa Apply membuang perubahan yang belum di-Apply

17. Pilih `John Doe` pada `Modified By`, klik `[Apply]`
18. Ubah pilihan `Modified By` menjadi `Sarah Thompson` tanpa Apply
19. Klik icon Filter untuk menutup panel
20. Verifikasi tabel tetap menampilkan hasil filter `John Doe` (footer `1–9 of 9`)
21. Klik icon Filter untuk membuka panel lagi
22. Verifikasi panel menampilkan `John Doe` (nilai ter-Apply terakhir)
23. Verifikasi panel tidak menampilkan `Sarah Thompson` pada `Modified By`
24. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: klik `[Clear Field]` lalu `[Apply]` antar TC membersihkan filter TC sebelumnya dan langkah terakhir memulihkan filter modal (S-09); panel Filter tetap terbuka sesudah `[Apply]` (TC-AC-LCS-397 mengamati panel sesudah `[Apply]`), sehingga "Klik icon Filter" dilakukan sekali pada TC pertama.
- Temuan untuk QA:
  - TC-AC-LCS-397: Expected bernomor "Langkah 2" untuk field `Modified By` kosong dan "Langkah 3" untuk footer `1–10 of 27`, padahal `[Clear Field]` adalah Langkah Uji 3 dan `[Apply]` adalah Langkah Uji 4; spec mengikuti urutan state yang diamati.
  - TC-AC-LCS-398: Expected butir a bernomor "Langkah 2" (tabel tetap menampilkan hasil filter) dan butir b "Langkah 3" (panel menampilkan `John Doe`) padahal pembukaan panel kembali adalah Langkah Uji 4; spec mengikuti urutan state yang diamati.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
