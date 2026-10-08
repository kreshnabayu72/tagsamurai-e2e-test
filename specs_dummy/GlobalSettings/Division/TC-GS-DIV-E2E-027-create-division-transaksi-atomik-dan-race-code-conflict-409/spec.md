---
id: TC-GS-DIV-E2E-027-create-division-transaksi-atomik-dan-race-code-conflict-409
title: "Transaksi DB Atomik Form Create dan Penanganan Race Condition Auto-Generate Code 409 dengan Auto-Retry Sekali"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-79
  - TC-GS-DIV-80
coverage:
  web: automated
---

# Transaksi DB Atomik Form Create dan Penanganan Race Condition Auto-Generate Code 409 dengan Auto-Retry Sekali

## Prerequisites

- Login sebagai Role: Total Control
- Dual context / background injection untuk simulasi konflik keunikan auto-generate code 409
- User berada di Global Settings > User > Division
- Code `QRT` belum dipakai Division lain
- Code `QRT` sudah dipakai

## Test Steps

### Dua Create bersamaan menghasilkan kandidat Code identik: yang kedua retry sekali dan berhasil (TC-GS-DIV-79)

1. Admin A dan Admin B membuka modal Create Division
2. Admin A mengisi Name `Quality Review Team`, Admin B mengisi Name `Quality Resource Team`, keduanya Code kosong
3. Admin A dan Admin B menekan `[Submit]` bersamaan
4. Verifikasi Kedua Create berhasil dengan toast sukses: `Success, division has been created.`
5. Verifikasi Salah satu Division memiliki Code `QRT` dan yang lain `QRT2` (retry otomatis sekali dengan suffix berikutnya)
6. Verifikasi Tidak ada pesan error ke Admin yang kalah

### Retry otomatis Code bentrok lagi diperlakukan sebagai kegagalan biasa (TC-GS-DIV-80)

7. Admin A mengisi Name `Quality Resource Team`, Code kosong, lalu menekan `[Submit]`
8. Saat retry otomatis pertama Admin A dibuat bentrok lagi (Code `QRT2` dipakai Admin lain di waktu yang sama)
9. Verifikasi Create Admin A gagal setelah retry otomatis sekali; tidak ada retry ketiga
10. Verifikasi Muncul toast error: `Error, failed to create division.`
11. Verifikasi Modal tetap terbuka dengan input dipertahankan, user dapat klik `[Submit]` lagi

## Notes

- Memvalidasi eksekusi atomik pembuatan record dan penanganan otomatis race duplicate code via auto-retry satu kali di server dengan kandidat suffix berikutnya (PRD §9.2 [F-DIV-09] langkah 7, §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-79, TC-GS-DIV-80.
