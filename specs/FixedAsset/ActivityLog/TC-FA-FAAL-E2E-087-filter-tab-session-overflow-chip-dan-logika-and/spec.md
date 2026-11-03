---
id: TC-FA-FAAL-E2E-087-filter-tab-session-overflow-chip-dan-logika-and
title: "Filter Tab Session: Overflow Chip +N more dan Logika AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-88
  - TC-FA-FAAL-89
coverage:
  web: automated
---

# Filter Tab Session: Overflow Chip +N more dan Logika AND

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11), seperti tabel di bawah. Opsi field User: `Budi Santoso`, `Dewi Lestari`, `Hendra Pratama`, `Jane Smith`, `John Dalton`, `John Davis`, `John Doe`, `Mike Tan`, `Siti Nurbaya` (sembilan opsi, dipakai pada langkah 3). Spec hanya membaca dan tidak mengubah data.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

| Baris | User (nama lengkap) | Employee ID | Position | Division | Note | Tanggal (Asia/Jakarta) |
|---|---|---|---|---|---|---|
| SS-01 | John Doe | EMP001 | Staff | Marketing | Session started | 14/07/26 08:05 |
| SS-02 | John Doe | EMP001 | Staff | Marketing | Session ended | 14/07/26 09:30 |
| SS-03 | Siti Nurbaya (tampil `Siti N`) | EMP002 | Manager | Finance | Concurrent limit reached | 14/07/26 10:00 |
| SS-04 | Mike Tan | EMP003 | Staff | Operations | Logged out by admin | 14/07/26 14:00 |
| SS-05 | Jane Smith | kosong | kosong | Finance | Session started | 15/07/26 08:00 |
| SS-06 | Budi Santoso (tampil `Budi S`) | EMP004 | Supervisor | Operations | Session started | 15/07/26 09:00 |
| SS-07 | Dewi Lestari | EMP005 | Staff | Marketing | Session started | 15/07/26 10:00 |
| SS-08 | Hendra Pratama (pengguna pertama) | EMP006 | Staff | Marketing | Session started | 15/07/26 11:00 |
| SS-09 | Hendra Pratama (pengguna kedua) | EMP007 | Manager | Finance | Session started | 15/07/26 12:00 |
| SS-10 | John Dalton | EMP008 | Staff | Operations | Session started | 16/07/26 08:00 |
| SS-11 | John Davis | EMP009 | Supervisor | Finance | Session ended | 16/07/26 09:00 |

## Test Steps

### TC-FA-FAAL-88: Overflow chip diringkas menjadi +N more

1. Klik icon Filter
2. Buka dropdown User
3. Centang kesembilan opsi User satu per satu: `Budi Santoso`, `Dewi Lestari`, `Hendra Pratama`, `Jane Smith`, `John Dalton`, `John Davis`, `John Doe`, `Mike Tan`, `Siti Nurbaya`
4. Tutup dropdown User
5. Verifikasi chip yang muat tampil dan sisanya diringkas menjadi satu chip `+N more`; jumlah chip tampil ditambah N sama dengan 9
6. Verifikasi field User tidak melebar keluar panel
7. Verifikasi field User tidak digulir horizontal

### TC-FA-FAAL-89: Dua field filter berbeda memakai logika AND

8. Klik `[Clear Field]`
9. Pilih `Finance` pada field Division
10. Pilih `Session started` pada field Note
11. Klik `[Apply]`
12. Verifikasi hanya SS-05 dan SS-09 tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 1, 4, 8 (membuka Filter Panel, menutup dropdown, mengosongkan field sebelum TC berikutnya).
- Langkah 3 menulis sembilan klik centang sebagai satu langkah berulang (teks biasa); dihitung sembilan klik pada ambang ukuran (12 langkah nominal, 20 dengan ekspansi).
- Temuan untuk QA:
  - TC sumber tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`. Spec mengikuti pola TC-FA-FAAL-77 (`[Clear Field]` dan `[Apply]` berurutan tanpa membuka ulang panel).
  - TC-FA-FAAL-88 tidak menyebut cara memilih seluruh sembilan opsi (tidak ada `Select All` yang disebut); spec mencentang satu per satu.
  - TC-FA-FAAL-88 Expected a ("jumlah chip tampil ditambah N sama dengan 9") tidak menyebut jumlah chip yang muat; spec mengasersi jumlah total saja.
