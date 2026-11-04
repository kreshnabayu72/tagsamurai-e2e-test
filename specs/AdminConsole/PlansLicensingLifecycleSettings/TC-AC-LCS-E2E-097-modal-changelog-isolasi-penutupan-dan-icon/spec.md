---
id: TC-AC-LCS-E2E-097-modal-changelog-isolasi-penutupan-dan-icon
title: "Modal Changelog: Isolasi Riwayat per Tab, Penutupan Modal, dan Icon Changelog Membuka Tab Aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-369
  - TC-AC-LCS-370
  - TC-AC-LCS-371
coverage:
  web: automated
---

# Modal Changelog: Isolasi Riwayat per Tab, Penutupan Modal, dan Icon Changelog Membuka Tab Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menimpa atau mengosongkan riwayat Changelog per tab, idempotent (Lampiran A-15; dinyatakan di `suite.md`).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab Trial Settings, Free Plan Settings, dan Recycle Bin lewat Fixture BE; hook `after` mengembalikan dataset ke keadaan awal.
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-369: Modal Changelog tab Trial Settings dan tab Free Plan Settings hanya memuat riwayat tab masing-masing

1. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
2. Verifikasi seluruh 3 baris (sedikitnya satu baris tampil) bernilai Field dari tab Trial Settings (Max Trial Duration atau Require Approval for Trial Activation)
3. Verifikasi tidak ada baris Free Plan Duration
4. Verifikasi tidak ada kolom Tab pada modal Trial Settings
5. Tutup modal dengan `[✕]`
6. Klik tab Free Plan Settings
7. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
8. Verifikasi seluruh 3 baris (sedikitnya satu baris tampil) bernilai Field Free Plan Duration
9. Verifikasi tidak ada baris Max Trial Duration
10. Verifikasi tidak ada kolom Tab pada modal Free Plan Settings
11. Tutup modal dengan `[✕]`

### TC-AC-LCS-370: Penutupan modal Changelog: [✕] dan Esc menutup, klik backdrop diabaikan

12. Klik tab Client Lifecycle
13. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
14. Klik area backdrop di luar modal
15. Verifikasi modal tetap terbuka
16. Klik `[✕]`
17. Verifikasi modal tertutup
18. Verifikasi panel tab Client Lifecycle tampil
19. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle (buka modal lagi)
20. Tekan Esc
21. Verifikasi modal tertutup

### TC-AC-LCS-371: Icon Changelog membuka riwayat tab yang sedang aktif

22. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
23. Verifikasi Title "Changelog: Lifecycle Settings > Client Lifecycle"
24. Verifikasi footer `1–10 of 27`
25. Tutup modal dengan `[✕]`
26. Klik tab Recycle Bin
27. Klik icon Changelog di pojok kanan atas panel tab Recycle Bin
28. Verifikasi Title "Changelog: Lifecycle Settings > Recycle Bin"
29. Verifikasi footer `1–3 of 3`
30. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: menutup modal dengan `[✕]` dan berpindah tab antar TC; pembukaan modal kedua pada TC-AC-LCS-370 adalah langkah TC itu sendiri.
- Pengecualian A-15: total absolut `1–10 of 27` dan `1–3 of 3` diasersi karena riwayat tab ditimpa lewat Fixture BE di hook `before` sebelum modal dibuka; hook `after` mengembalikan dataset Changelog.
- Dataset kecil Trial Settings, Free Plan Settings, dan Recycle Bin dipakai TC-AC-LCS-369 dan TC-AC-LCS-371; Dataset L dipakai TC-AC-LCS-370 dan TC-AC-LCS-371.
