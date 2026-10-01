---
id: TC-GS-USER-E2E-151-custom-field-dropdown-stale
title: Custom Field Dropdown yang stale ditolak saat Submit di Create dan Edit
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-610
coverage:
  web: automated
---

# Custom Field Dropdown yang stale ditolak saat Submit di Create dan Edit

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, sesi pertama (Admin A)
- Sesi kedua dengan akun Total Control lain di entity yang sama (Admin B)
- Custom Field "Contract Type" bertipe Dropdown aktif dengan value "Permanent" dan "Contract"
- Target Edit "Fajar Nugraha" adalah User Basic biasa
- Spec ini menghapus value "Contract" dari master Custom Field, jadi value itu dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Admin A: buka modal Create, isi field wajib, pilih "Contract Type" = "Contract"
2. Admin B: hapus value "Contract" dari Custom Field "Contract Type"
3. Admin A: klik `[Submit]`
4. Verifikasi inline error di bawah dropdown "This Contract Type no longer exists. Please select another." dan bukan toast generik
5. Verifikasi dropdown kosong kembali, opsi dimuat ulang tanpa "Contract", field lain tetap terisi, dan modal tetap terbuka
6. Ulangi untuk Edit: seed ulang value "Contract", buka Modal Edit "Fajar Nugraha", pilih "Contract", Admin B menghapus value itu lagi, lalu Admin A klik `[Save]` dan verifikasi hasil yang sama

## Notes

- Pasangan `TC-GS-USER-E2E` untuk D6 Position/Division (TC-88) dan multi-select (TC-461). Aturan `user.md` §6 dan §9.4.2 D6.
- Tidak ada user yang dibuat atau diubah karena Submit ditolak.
