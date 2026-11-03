---
id: TC-FA-RP-E2E-304-require-approval-prasyarat-aktivasi-dicek-ulang-approver-terakhir-dilepas
title: "Require Approval Transaction Role: prasyarat aktivasi dicek ulang saat approver terakhir dilepas admin lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-354
coverage:
  web: automated
---

# Require Approval Transaction Role: prasyarat aktivasi dicek ulang saat approver terakhir dilepas admin lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, kredensial `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Pelaku kedua (Sesi 2 yang melepas Approver) memakai sesi API akun Total Control `Company Isolated` yang sama; kemampuan sesi API disediakan tim BE/FE dan token tidak dihitung sebagai sesi web.
- Data Pre-setup: #35 `Company Isolated` (pohon group sama dengan Pre-setup #18; Approver Pandu Wijaya satu-satunya Approver sub-tab `Disposal` pada `IT Infrastructure`; tanpa Group Manager; Require Approval OFF di semua node).
- Kemampuan teknis: membaca nilai tersimpan Require Approval node dan sub-tab (disediakan tim FE/BE, tanpa endpoint karangan).
- State yang diubah dan pemulihannya: penugasan Approver Pandu Wijaya pada `IT Infrastructure` sub-tab `Disposal` dilepas spec ini; hook `after` memulihkannya (Pre-setup #35) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-354: Prasyarat aktivasi dicek ulang dalam transaksi, approver terakhir dilepas admin lain

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` pada Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Lepas Approver Pandu Wijaya dari node `IT Infrastructure` sub-tab `Disposal` lewat sesi API hingga terhapus
5. Aktifkan toggle `Require Approval for Disposal`
6. Verifikasi dialog `Cannot Require Approval` tampil
7. Verifikasi toggle `Require Approval for Disposal` kembali OFF
8. Klik `[OK]` pada dialog
9. Verifikasi nilai tersimpan Require Approval sub-tab `Disposal` pada `IT Infrastructure` tetap OFF lewat kemampuan baca

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 menutup dialog blok. Langkah 4 menjalankan "Sesi 2 meng-Remove Pandu Wijaya" lewat sesi API karena Sesi 2 hanya memicu state dan tidak diasersi.
- TC sumber menyebut `Manual Only (d) dua sesi paralel`; Sesi 2 hanya pemicu state sehingga spec ini memakai sesi API.
- Pembagian TC lintas spec: TC-FA-RP-345, 347 ada di spec 303; TC-FA-RP-337, 343, 344, 346 ada di spec 104; TC-FA-RP-348, 349, 355, 360 ada di spec 105; TC-FA-RP-350 ada di spec 296. Aktor spec ini berada di tenant `Company Isolated`, sedangkan spec lain pada kelompok ini memakai Company Alpha.
- Temuan untuk QA:
  - Email akun Total Control `Company Isolated` tidak tertulis di Pre-setup #1 sampai #11 maupun #35; akun disediakan tim FE.
  - Expected TC-FA-RP-354 hanya menyebut judul dialog `Cannot Require Approval`; teks isi dialog tidak diasersi karena tidak ditulis di TC ini.
  - Expected b (tidak ada perubahan Require Approval tersimpan) tidak punya cara cek di UI; spec memakai kemampuan baca nilai tersimpan yang disediakan tim FE/BE (langkah 9).
