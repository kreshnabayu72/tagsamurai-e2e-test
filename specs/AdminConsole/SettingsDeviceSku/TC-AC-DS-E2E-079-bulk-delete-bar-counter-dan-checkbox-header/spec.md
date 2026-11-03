---
id: TC-AC-DS-E2E-079-bulk-delete-bar-counter-dan-checkbox-header
title: "Bulk Action Bar: Screening, Counter Realtime, Checkbox Header, dan Indeterminate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-272
  - TC-AC-DS-273
  - TC-AC-DS-274
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Counter Realtime, Checkbox Header, dan Indeterminate

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: tidak ada data tersimpan yang berubah (spec hanya memilih baris). Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-272: screening Bulk Action Bar

1. Centang checkbox baris `SEED-001`
2. Klik `Bulk Action`
3. Verifikasi bar bulk tampil di atas tabel, sejajar dengan Table Tools, dan rata kiri
4. Verifikasi elemen bar berurutan: tombol `Bulk Action`, teks "1 SKU selected", tombol "Select All (129 records)", dan ikon `(✕)`
5. Verifikasi overlay `Bulk Action` hanya memuat aksi `Delete`
6. Verifikasi checkbox header berstatus indeterminate
7. Tekan Esc untuk menutup overlay, lalu klik ikon `(✕)` pada bar

### TC-AC-DS-273: counter realtime dan ikon close

8. Centang checkbox baris `SEED-001`
9. Centang checkbox baris `SEED-002`
10. Verifikasi counter menampilkan "2 SKUs selected"
11. Hilangkan centang baris `SEED-002`
12. Verifikasi counter menampilkan "1 SKU selected"
13. Klik ikon `(✕)` pada bar
14. Verifikasi bar bulk hilang
15. Verifikasi baris `SEED-001` tidak tercentang

### TC-AC-DS-274: checkbox header dan indeterminate

16. Klik checkbox header
17. Verifikasi seluruh 10 baris halaman aktif tercentang
18. Verifikasi checkbox header berstatus checked
19. Verifikasi counter menampilkan "10 SKUs selected"
20. Hilangkan centang satu baris
21. Verifikasi checkbox header berstatus indeterminate
22. Verifikasi counter menampilkan "9 SKUs selected"
23. Klik checkbox header dua kali
24. Verifikasi semua baris tidak tercentang
25. Verifikasi bar bulk hilang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: menutup overlay `Bulk Action` dan membersihkan seleksi dengan ikon `(✕)` sesudah blok TC-272 (S-09); mulai TC-273 dengan seleksi bersih.
- Temuan untuk QA: TC-274 menyebut "Klik checkbox header lagi dua kali" dari keadaan indeterminate; spec mengasumsikan klik pertama memilih semua baris dan klik kedua membatalkan semuanya, sesuai Expected c. Post Condition TC-272 sampai TC-274 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
