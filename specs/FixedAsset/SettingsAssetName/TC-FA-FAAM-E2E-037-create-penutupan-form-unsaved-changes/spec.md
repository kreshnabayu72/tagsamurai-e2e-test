---
id: TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes
title: "Create: Penutupan Form Bersih dan Terisi, Dialog Unsaved Changes, Leave, Cancel, dan Esc"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-71
  - TC-FA-FAAM-72
  - TC-FA-FAAM-73
  - TC-FA-FAAM-74
  - TC-FA-FAAM-75
coverage:
  web: automated
---

# Create: Penutupan Form Bersih dan Terisi, Dialog Unsaved Changes, Leave, Cancel, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis: Asset Name `Leave Item {runId}-037` hanya diketik dan tidak tersimpan; keberadaannya dicari di List sebagai asersi absence.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Leave Item {runId}-037` bila masih ada.

## Test Steps

### TC-FA-FAAM-71: Menutup Popup Create yang bersih tidak memunculkan Unsaved Changes

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Klik `[✕]`
3. Verifikasi Modal langsung tertutup (cara `[✕]`)
4. Verifikasi Dialog `Unsaved Changes` tidak muncul (cara `[✕]`)
5. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
6. Tekan Esc
7. Verifikasi Modal langsung tertutup (cara Esc)
8. Verifikasi Dialog `Unsaved Changes` tidak muncul (cara Esc)

### TC-FA-FAAM-72: Menutup Popup Create yang terisi memunculkan dialog Unsaved Changes

9. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
10. Isi Asset Name `Dirty Item`
11. Klik `[✕]`
12. Verifikasi Dialog tampil dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` serta `[Leave]`

### TC-FA-FAAM-75: Cancel pada Unsaved Changes mempertahankan form dan input

13. Klik `[Cancel]`
14. Verifikasi Dialog tertutup
15. Verifikasi Modal tetap terbuka
16. Verifikasi Asset Name masih `Dirty Item`

### TC-FA-FAAM-73: Esc pada Popup Create terisi memunculkan Unsaved Changes dan Esc pada dialog setara Cancel

17. Tekan Esc
18. Verifikasi Dialog `Unsaved Changes` tampil
19. Tekan Esc lagi pada dialog
20. Verifikasi Dialog tertutup
21. Verifikasi User tetap di form dengan input `Dirty Item`

### TC-FA-FAAM-74: Leave pada Unsaved Changes menutup form tanpa menyimpan

22. Ganti isi Asset Name dengan `Leave Item {runId}-037`
23. Klik `[✕]`
24. Verifikasi Dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
25. Klik `[Leave]`
26. Verifikasi Modal tertutup
27. Ketik Search `Leave Item {runId}-037`, tekan Enter
28. Verifikasi Empty state `No results found` tampil (baris `Leave Item {runId}-037` tidak ada di List)
29. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Urutan TC dalam spec (S-10): penutupan bersih (TC-FA-FAAM-71), dialog muncul (TC-FA-FAAM-72), Cancel (TC-FA-FAAM-75), Esc (TC-FA-FAAM-73), dan Leave (TC-FA-FAAM-74) paling akhir karena Leave menutup form; jumlah buka form tidak melebihi jumlah kejadian menutup.
- TC-FA-FAAM-74 mengganti isi Asset Name `Dirty Item` dengan `Leave Item {runId}-037` karena form sama dilanjutkan; dialog `Unsaved Changes` diasersi sesuai S-08 sebelum `[Leave]`.
- Search pada langkah akhir adalah langkah penghubung dan memakai empty state `No results found` sebagai anchor positif absence (bagian 8b butir 2).
