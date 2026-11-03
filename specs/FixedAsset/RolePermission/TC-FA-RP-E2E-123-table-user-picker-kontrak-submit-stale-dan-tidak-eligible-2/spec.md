---
id: TC-FA-RP-E2E-123-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-2
title: "Table User Picker: kontrak submit stale dan tidak eligible (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-417
  - TC-FA-RP-418
  - TC-FA-RP-419
coverage:
  web: automated
---

# Table User Picker: kontrak submit stale dan tidak eligible (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Sesi 2 pada TC sumber hanya memicu perubahan state (meng-Assign Total Control, menghapus identitas, mengganti nama pengguna) dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE. TC sumber menyebut `Manual Only (d) dua sesi paralel`; Sesi 2 bukan objek asersi.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso, Dimas Pranata). Kolam #15 disiapkan ulang lewat seeding API di awal tiap TC (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: meng-Assign Total Control, menghapus identitas, mengganti nama pengguna, dan membaca tingkat akses serta ID user lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: identitas Ahmad Fauzi dihapus, nama Ahmad Fauzi diganti menjadi `Ahmad Fauzi Rahman`, tingkat akses Total Control Budi Santoso dan Ahmad Fauzi ditetapkan. Hook `after` memulihkan kolam Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-417: Submit Assign, dua user tidak lagi eligible memakai bentuk jamak

1. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
2. Klik `[+ Assign]` di Tab `Total Control`
3. Centang Ahmad Fauzi dan Budi Santoso
4. Tetapkan Total Control kepada Ahmad Fauzi dan Budi Santoso lewat sesi API hingga tersimpan
5. Klik `[Assign]`
6. Verifikasi alert inline `Ahmad Fauzi and Budi Santoso are no longer eligible. Please select another.`
7. Klik `[Cancel]`

### TC-FA-RP-418: Submit Assign, campuran stale dan tidak eligible menampilkan alert stale lebih dulu

8. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
9. Klik `[+ Assign]` di Tab `Total Control`
10. Centang Ahmad Fauzi, Budi Santoso, dan Dimas Pranata
11. Hapus identitas Ahmad Fauzi dan tetapkan Total Control kepada Budi Santoso lewat sesi API hingga tersimpan
12. Klik `[Assign]`
13. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
14. Verifikasi centangan Ahmad Fauzi dan Budi Santoso auto-clear
15. Verifikasi Dimas Pranata tetap tercentang
16. Verifikasi tidak ada penugasan Total Control dibuat untuk Dimas Pranata lewat kemampuan baca
17. Klik `[Cancel]`

### TC-FA-RP-419: Rename user antara load picker dan submit bukan error

18. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
19. Klik `[+ Assign]` di Tab `Total Control`
20. Centang Ahmad Fauzi
21. Ganti nama Ahmad Fauzi menjadi `Ahmad Fauzi Rahman` lewat sesi API hingga tersimpan
22. Klik `[Assign]`
23. Verifikasi toast sukses `Success, Total Control has been assigned.`
24. Verifikasi baris tampil dengan nama terbaru `Ahmad Fauzi Rahman`
25. Verifikasi baris itu memakai ID user yang sama dengan ID Ahmad Fauzi sebelum diganti nama lewat kemampuan baca

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, dan 18 (menyiapkan kolam pengguna per TC lewat sesi API, Pre-setup #32), langkah 7 dan 17 (menutup popup Assign dengan `[Cancel]`).
- Pada TC-FA-RP-419 langkah 21 hanya memicu state dan memakai sesi API; langkah 24 dan 25 mengasersi tampilan baris pada sesi aktor.
- Temuan untuk QA:
  - TC-FA-RP-418 butir b menyebut centangan Ahmad Fauzi dan Budi Santoso auto-clear tanpa menjelaskan mengapa centangan user yang tidak eligible ikut auto-clear padahal alert hanya menyebut user stale; spec mengikuti TC.
  - TC-FA-RP-419 butir b ("ID user yang sama") tidak menyebut tempat ID teramati di UI; spec memakai kemampuan baca (langkah 25).
  - TC-FA-RP-418 menyebut Expected tidak ada penugasan dibuat, tetapi tidak menyatakan untuk user mana; spec mengasersi Dimas Pranata (langkah 16).
