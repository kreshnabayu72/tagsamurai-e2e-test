---
id: TC-AC-DN-E2E-053-create-tutup-form-bersih-backdrop-dan-reload
title: "Create Device Name: Backdrop, Navigasi In-app, Reload, dan Menutup Form Bersih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-123
  - TC-AC-DN-124
  - TC-AC-DN-125
  - TC-AC-DN-115
  - TC-AC-DN-116
  - TC-AC-DN-122
  - TC-AC-DN-126
coverage:
  web: automated
---

# Create Device Name: Backdrop, Navigasi In-app, Reload, dan Menutup Form Bersih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`.
- Data Dinamis: nama yang diketik `Draft Gateway {runId}-053`; tidak ada [Submit] sehingga tidak ada record yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: menangani dialog `beforeunload` bawaan browser (mengamati dan membatalkan reload) untuk TC-AC-DN-125; disediakan tim FE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-123: Klik backdrop pada form yang sudah diisi tidak menutup popup

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `Draft Gateway {runId}-053` pada field Device Name
3. Klik area gelap di luar popup
4. Verifikasi popup form Create tetap terbuka dengan Device Name `Draft Gateway {runId}-053` dipertahankan
5. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-DN-124: Navigasi in-app saat form terisi memunculkan dialog Unsaved Changes

6. Klik salah satu item sidebar menuju halaman lain di aplikasi
7. Verifikasi perubahan halaman dicegat dan dialog Unsaved Changes tampil dengan Body "You have unsaved changes. Are you sure you want to leave?"
8. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
9. Verifikasi halaman `Settings > Device > Device Name` tetap tampil sebelum user memilih
10. Verifikasi popup form Create tetap tampil sebelum user memilih
11. Klik `[Cancel]` pada dialog

### TC-AC-DN-125: Reload saat form terisi memunculkan konfirmasi bawaan browser

12. Tekan `F5` untuk memuat ulang halaman
13. Verifikasi konfirmasi bawaan browser (beforeunload) tampil sebelum halaman dimuat ulang
14. Batalkan reload pada konfirmasi bawaan browser sehingga tetap di halaman
15. Klik icon close `[✕]` pada popup
16. Verifikasi dialog Unsaved Changes tampil
17. Klik `[Leave]` pada dialog

### TC-AC-DN-115: Menutup form yang belum diisi lewat icon close

18. Klik tombol `+ Device Name` pada toolbar
19. Klik icon close `[✕]` pada popup
20. Verifikasi popup form tertutup langsung
21. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-DN-116: Menutup form yang belum diisi dengan tombol Esc

22. Klik tombol `+ Device Name` pada toolbar
23. Tekan tombol `Esc`
24. Verifikasi popup form tertutup langsung
25. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-DN-122: Klik backdrop pada form yang kosong tidak menutup popup

26. Klik tombol `+ Device Name` pada toolbar
27. Klik area gelap di luar popup
28. Verifikasi popup form Create tetap terbuka
29. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-DN-126: Reload saat form kosong tidak memunculkan konfirmasi bawaan browser

30. Tekan `F5` untuk memuat ulang halaman
31. Verifikasi List Device Name tampil setelah halaman dimuat ulang
32. Verifikasi tidak ada konfirmasi bawaan browser sebelum halaman dimuat ulang

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Ketujuh TC bertanda FE Test "UI Only" dan tanpa [Submit]; tidak ada record yang dibuat.
- Urutan (S-10): kasus form terisi (TC-AC-DN-123, TC-AC-DN-124, TC-AC-DN-125) dijalankan lebih dulu pada satu pembukaan popup, lalu kasus form bersih. Jumlah pembukaan popup (langkah 1, 18, 22, 26) sama dengan jumlah kejadian menutup (langkah 17, 19, 23, dan reload pada langkah 30).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 11 (`[Cancel]` menutup dialog navigasi sebelum TC berikutnya), langkah 14 (membatalkan reload bawaan browser), serta langkah 15 sampai 17 (menutup form dirty secara deterministik: icon close, verifikasi dialog Unsaved Changes, `[Leave]`, S-08 dan S-09).
- Pemilihan item sidebar pada langkah 6 mengikuti TC ("breadcrumb atau item sidebar menuju halaman lain"); spec memakai item sidebar.
- Langkah 5, 21, 25, 29, dan 32 adalah asersi absence; anchor positifnya adalah popup yang tampil (langkah 4 dan 28), popup yang tertutup (langkah 20 dan 24), atau List yang tampil (langkah 31) (bagian 8b butir 2 dan R-21).
- Temuan untuk QA:
  - TC-AC-DN-124 tidak menyebut item sidebar tujuan; spec memakai item sidebar apa pun menuju halaman lain.
  - TC-AC-DN-126 tidak menyebut state popup setelah reload; spec mengasersi List Device Name tampil sebagai bukti halaman dimuat ulang.
