---
id: TC-GS-HHR-E2E-034-edit-reader-power-penutupan-form-dan-unsaved-changes
title: "Edit Reader Power: Dialog Unsaved Changes (Cancel dan Leave), Klik Backdrop, dan Tutup Tanpa Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-134
  - TC-GS-HHR-135
  - TC-GS-HHR-136
  - TC-GS-HHR-450
coverage:
  web: automated
---

# Edit Reader Power: Dialog Unsaved Changes (Cancel dan Leave), Klik Backdrop, dan Tutup Tanpa Perubahan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec dijalankan pada Client A yang datanya dipakai spec lain; spec tidak menyimpan perubahan apa pun.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, Long Range, `30 dBm`). Nilai uji yang digeser namun tidak pernah disimpan: `25 dBm`. Seed Reader A bernama literal tanpa suffix (pengecualian S-12 Population Seed Reader A HHR) karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g) dan DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`; baris diidentifikasi lewat Serial Number.
- Cleanup: Seed Reader A tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: penggeseran slider ke nilai tertentu; input keyboard (`Esc`); klik pada area backdrop di luar dialog.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Form dirty: TC-GS-HHR-134 (X lalu Cancel)

1. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
2. Geser slider ke 25 dBm
3. Klik `[✕]`
4. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]`
5. Klik `[Cancel]`
6. Verifikasi dialog `Unsaved Changes` tertutup
7. Verifikasi Dialog Edit Reader Power tetap terbuka
8. Verifikasi slider tetap pada `25 dBm`

### TC-GS-HHR-450: Klik backdrop pada form dirty diabaikan

9. Klik area backdrop di luar dialog
10. Verifikasi Dialog Edit Reader Power tetap terbuka
11. Verifikasi slider tetap pada `25 dBm`
12. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-GS-HHR-135: Esc lalu Leave menutup tanpa menyimpan

13. Tekan `Esc`
14. Verifikasi dialog `Unsaved Changes` muncul dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]`
15. Klik `[Leave]`
16. Verifikasi Dialog Edit Reader Power tertutup
17. Verifikasi kolom `Reader Power` baris DD-01 tetap `30 dBm`
18. Verifikasi tidak ada toast

### TC-GS-HHR-136: Tutup tanpa perubahan tidak memunculkan dialog

19. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
20. Klik `[✕]`
21. Verifikasi dialog tertutup langsung
22. Verifikasi dialog `Unsaved Changes` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 134, 450, 135, 136. Urutan menyimpang dari urutan TC sumber dan mengikuti kondisi form: TC-GS-HHR-134, 450, dan 135 memakai satu pembukaan form dirty (`25 dBm`); TC-GS-HHR-136 menutup dalam keadaan bersih sehingga memakai form baru dan ditaruh terakhir (prinsip 6).
- Jumlah pembukaan dialog Edit Reader Power: 2 (langkah 1, 19); jumlah kejadian menutup: 2 (langkah 13 sampai 15, langkah 20). Langkah 5 (`[Cancel]`) hanya menutup dialog `Unsaved Changes`.
- Langkah 2 adalah aksi penggeseran slider (tanpa `Verifikasi`) yang membuat form dirty.
- Seluruh penutupan memakai `[✕]`, `Esc`, atau `[Leave]` (tanpa `[Cancel]` pada dialog Edit; `[Cancel]` hanya pada dialog `Unsaved Changes`).
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Spec 032, 033, dan 034 menguji dialog Edit Reader Power pada dataset Seed Reader A yang sama dan sengaja dipisah: gabungannya 118 langkah (50, 46, dan 22), jauh di atas sekitar 35 langkah, dan tiap spec membuka dialog sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Pembagian TC lintas spec: TC-GS-HHR-125 dan 129 sampai 132 ada di spec 032; TC-GS-HHR-126 sampai 128, 133, 451, dan 457 ada di spec 033; TC-GS-HHR-137 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-HHR-450 menulis Data Uji `DD-01` tanpa menyebut nilai awal; spec memakai nilai tersimpan `30 dBm` (Seed Reader A) dan pergeseran ke `25 dBm` seperti TC-GS-HHR-134.
  - Tidak ada Post Condition pada TC sumber spec ini.
