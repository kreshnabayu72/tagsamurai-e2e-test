---
id: TC-AC-DN-E2E-052-create-tutup-form-dirty-dan-unsaved-changes
title: "Create Device Name: Menutup Form Dirty, Dialog Unsaved Changes (Cancel, Leave, Esc)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-117
  - TC-AC-DN-121
  - TC-AC-DN-118
  - TC-AC-DN-119
  - TC-AC-DN-120
coverage:
  web: automated
---

# Create Device Name: Menutup Form Dirty, Dialog Unsaved Changes (Cancel, Leave, Esc)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`.
- Data Dinamis: nama yang diketik `Draft Gateway {runId}-052`; tidak ada [Submit] sehingga tidak ada record yang dibuat dan tidak ada cleanup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-117: Menutup form yang sudah diisi lewat icon close memunculkan dialog Unsaved Changes

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `Draft Gateway {runId}-052` pada field Device Name
3. Klik icon close `[✕]` pada popup
4. Verifikasi dialog Unsaved Changes tampil dengan Body "You have unsaved changes. Are you sure you want to leave?"
5. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
6. Verifikasi popup form Create tetap terbuka di belakang dialog
7. Verifikasi isian Device Name `Draft Gateway {runId}-052` dipertahankan

### TC-AC-DN-121: Esc pada dialog Unsaved Changes setara tombol Cancel

8. Tekan tombol `Esc`
9. Verifikasi dialog Unsaved Changes tertutup
10. Verifikasi popup form Create tetap terbuka dengan Device Name `Draft Gateway {runId}-052` dipertahankan

### TC-AC-DN-118: Menutup form yang sudah diisi dengan Esc memunculkan dialog Unsaved Changes

11. Klik field Measurement lalu pilih `Meter`
12. Tekan tombol `Esc`
13. Verifikasi dialog Unsaved Changes tampil dengan Body "You have unsaved changes. Are you sure you want to leave?"
14. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`

### TC-AC-DN-119: Tombol Cancel mempertahankan form dan isiannya

15. Klik `[Cancel]` pada dialog
16. Verifikasi dialog tertutup
17. Verifikasi popup form Create tetap terbuka dengan Device Name `Draft Gateway {runId}-052` dipertahankan
18. Verifikasi Measurement `Meter` dipertahankan

### TC-AC-DN-120: Tombol Leave menutup form tanpa menyimpan

19. Klik icon close `[✕]` pada popup
20. Verifikasi dialog Unsaved Changes tampil
21. Klik `[Leave]` pada dialog
22. Verifikasi dialog tertutup
23. Verifikasi popup form Create tertutup
24. Verifikasi tidak ada toast
25. Ketik Search `Draft Gateway {runId}-052`, tekan Enter
26. Verifikasi List tidak memuat baris `Draft Gateway {runId}-052` (empty state "No results found" tampil)

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. TC-AC-DN-117, TC-AC-DN-118, TC-AC-DN-119, dan TC-AC-DN-121 bertanda FE Test "UI Only"; TC-AC-DN-120 "Need API".
- Penyimpangan urutan (S-05 dan S-10): urutan TC diatur supaya satu popup yang sama dipakai tanpa dibuka ulang (prinsip 13, "Halaman yang sama dipakai berulang"). TC-AC-DN-121 (Esc pada dialog) dijalankan tepat setelah TC-AC-DN-117 karena dialog dari TC-AC-DN-117 sudah terbuka dan harus ditutup; TC-AC-DN-118 menyusul sebagai Esc pada form dirty; TC-AC-DN-119 memakai dialog dari TC-AC-DN-118 (bukan dari icon close seperti langkah TC), dan TC-AC-DN-120 terakhir karena menutup popup (S-10).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 11 (memilih Measurement `Meter` yang dibutuhkan Expected TC-AC-DN-119 sebelum dialog dibuka; TC-AC-DN-118 hanya mensyaratkan form terisi sehingga tetap terpenuhi) dan langkah 25 (Search untuk memeriksa baris target, R-16; hasil kosong "No results found" menjadi anchor positif asersi absence pada langkah 26).
- Langkah 20 mengasersi dialog tampil sebagai bagian S-08 (✕, verifikasi dialog, `[Leave]`).
- Temuan untuk QA:
  - Post Condition TC-AC-DN-120 ("Tidak ada record baru tersimpan") tidak punya langkah observasi di TC; Expected b (List tidak memuat `Draft Gateway`) diasersi lewat Search pada langkah 25 dan 26.
  - TC-AC-DN-119 dan TC-AC-DN-120 mengisi Measurement `Meter`, sedangkan TC-AC-DN-117 dan TC-AC-DN-118 tidak; keadaan Measurement tidak diasersi pada TC-AC-DN-117, TC-AC-DN-118, dan TC-AC-DN-121.
