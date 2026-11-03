---
id: TC-FA-RP-E2E-114-auto-revert-total-control-3
title: "Auto-Revert Total Control (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-393
  - TC-FA-RP-1137
coverage:
  web: automated
---

# Auto-Revert Total Control (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor kedua (langkah 11 dan 12, ganti akun eksplisit): Manage global user & role dengan Update (Hendra Wijaya, Pre-setup #6) `murGlobal_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MUR_GLOBAL_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Pelaku kedua pada TC-FA-RP-393 hanya memicu perubahan state dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, seluruh Global Role CRUD penuh; baris Group Role eksplisit `Manage files` Read di `Data Center`), #15 (Ahmad Fauzi, Standard), #6, #18.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca nilai tersimpan checkbox Create (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: tingkat akses Total Control Rina Wulandari dilepas (TC-FA-RP-1137) dan Ahmad Fauzi dijadikan Total Control (TC-FA-RP-393). Hook `after` memulihkan Pre-setup #3 dan #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage accounting`

### TC-FA-RP-1137: Confirm auto-revert Total Control lewat edit CRUD, penugasan Group Role dipertahankan

3. Hapus centang Delete pada baris Rina Wulandari
4. Klik `[Remove]` pada dialog
5. Verifikasi toast sukses `Success, permissions have been updated. Rina Wulandari is no longer Total Control.`
6. Kembali ke Tab `System`
7. Buka Detail Role Group Role `Manage files`
8. Klik node `Data Center` pada Sidebar Group Tree
9. Ketik Search `Rina Wulandari`, tekan Enter
10. Verifikasi baris Rina Wulandari tetap ada di Detail Role `Manage files` pada `Data Center`

### TC-FA-RP-393: Status target berubah antara render dan submit, aktor non-Total Control ditolak

11. Logout dari akun Total Control
12. Login sebagai Manage global user & role dengan Update (Hendra Wijaya)
13. Klik Tab `System`
14. Buka Detail Role `Manage accounting`
15. Tetapkan Ahmad Fauzi sebagai Total Control lewat sesi API hingga tersimpan
16. Centang Create pada baris Ahmad Fauzi
17. Verifikasi toast error `You don't have permission to edit.`
18. Verifikasi cell Create baris Ahmad Fauzi kembali ke nilai tersimpan
19. Verifikasi tidak ada perubahan tersimpan pada Create baris Ahmad Fauzi lewat kemampuan baca

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 1137, 393 agar ganti akun eksplisit (langkah 11 dan 12) hanya sekali.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6 (kembali ke Tab `System`), langkah 9 (Search untuk menemukan baris target, R-16).
- Pada TC-FA-RP-393 Sesi 2 hanya memicu state dan memakai sesi API (langkah 15, "hingga tersimpan"); langkah TC "Sesi 1 melihat checkbox Ahmad Fauzi Enabled" terpenuhi oleh langkah 14 dan tidak diasersi. TC sumber menyebut `Manual Only (d) dua sesi paralel`.
- Temuan untuk QA:
  - TC-FA-RP-393 butir b menulis "tidak ada perubahan tersimpan" tanpa indikator UI; spec memakai kemampuan baca (langkah 19).
  - TC-FA-RP-393 menyebut Hendra Wijaya mengedit Detail Role `Manage accounting`; TC tidak memuat precondition bahwa Manage global user & role memberi akses buka Detail Role itu, spec mengikuti TC.
  - TC-FA-RP-1137 menyebut "Detail Role Group Role `Manage files`" tanpa menyebut langkah membuka daftar Group Role; spec memakai langkah buka Detail Role seperti TC lain.
