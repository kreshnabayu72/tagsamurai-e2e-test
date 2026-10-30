---
id: TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes
title: "Edit Alias Name: Dialog Unsaved Changes (Cancel dan Leave), Klik Backdrop, Tutup Tanpa Perubahan, dan Nilai Dikembalikan Tidak Dirty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-115
  - TC-GS-HHR-116
  - TC-GS-HHR-117
  - TC-GS-HHR-118
  - TC-GS-HHR-119
coverage:
  web: automated
---

# Edit Alias Name: Dialog Unsaved Changes (Cancel dan Leave), Klik Backdrop, Tutup Tanpa Perubahan, dan Nilai Dikembalikan Tidak Dirty

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec dijalankan pada Client A yang datanya dipakai spec lain; spec tidak menyimpan perubahan apa pun.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Spec memakai DD-01 (Serial Number `SN-HHR-00101`, Alias Name `—`) dan DD-02 (`Gudang Reader - 1`, Serial Number `SN-HHR-00102`, Alias Name `Reader Gudang 02`). Nilai uji yang diketik namun tidak pernah disimpan: `Reader Dock 01` dan `Reader Gudang 03`. Seed Reader A bernama literal tanpa suffix (pengecualian S-12 Population Seed Reader A HHR) karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number.
- Cleanup: Seed Reader A tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: input keyboard (`Esc`); klik pada area backdrop di luar dialog.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Form dirty: TC-GS-HHR-115 (X lalu Cancel)

1. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
2. Isi `Alias Name` dengan `Reader Dock 01`
3. Klik `[✕]`
4. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]`
5. Klik `[Cancel]`
6. Verifikasi dialog `Unsaved Changes` tertutup
7. Verifikasi Dialog Edit Alias Name tetap terbuka
8. Verifikasi input `Alias Name` berisi `Reader Dock 01`

### TC-GS-HHR-119: Klik backdrop pada form dirty diabaikan

9. Klik area backdrop di luar dialog
10. Verifikasi Dialog Edit Alias Name tetap terbuka
11. Verifikasi input `Alias Name` tetap berisi `Reader Dock 01`
12. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-GS-HHR-116: Esc lalu Leave menutup tanpa menyimpan

13. Tekan `Esc`
14. Verifikasi dialog `Unsaved Changes` muncul dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]`
15. Klik `[Leave]`
16. Verifikasi Dialog Edit Alias Name tertutup
17. Verifikasi tidak ada toast
18. Verifikasi kolom `Alias Name` baris DD-01 tetap `—`

### TC-GS-HHR-117: Tutup tanpa perubahan tidak memunculkan dialog

19. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
20. Klik `[✕]`
21. Verifikasi dialog tertutup langsung
22. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-GS-HHR-118: Alias diubah lalu dikembalikan identik dianggap clean

23. Klik `⋯` pada baris DD-02 (`Gudang Reader - 1`), pilih `Edit Alias Name`
24. Ubah `Alias Name` menjadi `Reader Gudang 03`
25. Ketik ulang `Reader Gudang 02` pada `Alias Name`
26. Klik `[✕]`
27. Verifikasi dialog tertutup langsung
28. Verifikasi dialog `Unsaved Changes` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 115, 119, 116, 117, 118. Urutan menyimpang dari urutan TC sumber dan mengikuti kondisi form: TC-GS-HHR-115, 119, dan 116 memakai satu pembukaan form dirty (`Reader Dock 01`); TC-GS-HHR-117 dan 118 menutup dalam keadaan bersih sehingga memakai form baru masing-masing dan ditaruh terakhir (prinsip 6). TC-GS-HHR-118 menguji pengembalian nilai itu sendiri, sehingga memakai form sendiri.
- Jumlah pembukaan dialog Edit Alias Name: 3 (langkah 1, 19, 23); jumlah kejadian menutup: 3 (langkah 13 sampai 15, langkah 20, langkah 26). Langkah 5 (`[Cancel]`) hanya menutup dialog `Unsaved Changes`.
- Langkah 2, 24, dan 25 adalah aksi pengisian (tanpa `Verifikasi`) yang membuat form dirty atau mengembalikannya.
- Seluruh penutupan memakai `[✕]`, `Esc`, atau `[Leave]` (tanpa `[Cancel]` pada dialog Edit; `[Cancel]` hanya pada dialog `Unsaved Changes`).
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Spec 029, 030, dan 031 menguji dialog Edit Alias Name pada dataset Seed Reader A yang sama dan sengaja dipisah: gabungannya 163 langkah (61, 74, dan 28), jauh di atas sekitar 35 langkah, dan tiap spec membuka dialog sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Pembagian TC lintas spec: TC-GS-HHR-103, 109 sampai 114, dan 462 ada di spec 029; TC-GS-HHR-104 sampai 108, 120, 123, dan 124 ada di spec 030.
- Temuan untuk QA:
  - TC-GS-HHR-119 tidak menyebut cara mengisi `Alias Name`; spec memakai nilai `Reader Dock 01` seperti TC-GS-HHR-115 dan 116 (form dirty yang sama).
  - Tidak ada Post Condition pada TC sumber spec ini.
