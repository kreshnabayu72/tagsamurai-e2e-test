---
id: TC-FA-TDC-E2E-239-restore-default-classes-hasil-nilai-class-sama-dengan-seed
title: "Restore Default Classes: Nilai Class Hasil Restore Sama dengan Nilai Seed"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-324
sourceRules: ["§4.1.5#r1", "§4.1.5#r2", "§4.1.5#r3", "§4.1.5#r4", "§4.1.5#r5", "§4.1.5#r6", "§4.1.5#r7", "§4.1.5#p1", "§4.1.2#r10", "§4.1.2#r11", "ST-08", "FATDC-LOGIC-03b"]
smoke: []
dependsOn: []
trace:
  "§4.1.5#r1": 5
  "§4.1.5#r2": 6
  "§4.1.5#r3": 7
  "§4.1.5#r4": 8
  "§4.1.5#r5": 9
  "§4.1.5#r6": 10
  "§4.1.5#r7": 11
  "§4.1.5#p1": 13
  "§4.1.2#r10": 13
  "§4.1.2#r11": 13
  "ST-08": 16
  "FATDC-LOGIC-03b": 16
coverage:
  web: automated
---

# Restore Default Classes: Nilai Class Hasil Restore Sama dengan Nilai Seed

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Data: tabel Tax Depreciation Class tanpa class sama sekali: di hook `before` seluruh class company uji dihapus lewat seeding API (company yang disediakan tim FE khusus automation) sebelum `beforeEach` membuka halaman, sehingga Empty State tampil. Hook `after` memulihkan tujuh class seed bawaan lewat seeding API (`suite.md`).
- Master Data Count Limit tidak membatasi tujuh class.
- Nilai seed mengikuti PRD §4.1.5 sebagaimana tertulis di Expected TC-324.
- Kemampuan teknis: mengosongkan seluruh class dan memulihkan tujuh class seed lewat API.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-324: Nilai class hasil Restore sama dengan nilai seed

1. Klik `Restore default classes`
2. Klik `[Restore]`
3. Tunggu aksi selesai
4. Baca tujuh baris tabel
5. Verifikasi NB-1: "Bukan bangunan – Kelompok 1", Non-building, 4, 25%, 50%, "Straight Line · Declining Balance"
6. Verifikasi NB-2: "Bukan bangunan – Kelompok 2", Non-building, 8, 12.5%, 25%, "Straight Line · Declining Balance"
7. Verifikasi NB-3: "Bukan bangunan – Kelompok 3", Non-building, 16, 6.25%, 12.5%, "Straight Line · Declining Balance"
8. Verifikasi NB-4: "Bukan bangunan – Kelompok 4", Non-building, 20, 5%, 10%, "Straight Line · Declining Balance"
9. Verifikasi BLD-P: "Bangunan permanen", Building, 20, 5%, "—", "Straight Line"
10. Verifikasi BLD-NP: "Bangunan tidak permanen", Building, 10, 10%, "—", "Straight Line"
11. Verifikasi LAND: "Tanah", Land, "—", "—", "—", "—"
12. Klik link Class Code `NB-1` pada tabel
13. Verifikasi Drawer Edit `NB-1`: Regulation Reference "UU HPP 7/2021; PMK 72/2023", Effective From "—", Last Posted Tax Year "—"
14. Klik `[×]` pada header Drawer
15. Klik link Class Code `LAND` pada tabel
16. Verifikasi Drawer Edit `LAND`: Useful Life dan Allowed Methods kosong Disabled
17. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 3 ("Tunggu aksi selesai", 8b.8; hasil `[Restore]` diasersi lewat isi tabel pada langkah 5 sampai 11), langkah 4 ("Baca" tanpa asersi), langkah 14 dan 17 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Baris diidentifikasi lewat Class Code seed (tabel hanya berisi tujuh baris pada satu halaman, sehingga dibuka tanpa Search).
- Kolom pada langkah 5 sampai 11 berurutan: Class Name, Asset Type, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods.
- Tidak ada Post Condition pada TC-324.
- Temuan untuk QA:
  - TC-324 butir a sampai g menyebut tujuh nilai tanpa nama kolom; urutan kolom di atas mengikuti kolom tabel pada TC-2.
  - Email akun Total Control tidak tertulis di TC.
