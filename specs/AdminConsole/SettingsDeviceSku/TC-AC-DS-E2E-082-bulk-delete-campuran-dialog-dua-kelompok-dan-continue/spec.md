---
id: TC-AC-DS-E2E-082-bulk-delete-campuran-dialog-dua-kelompok-dan-continue
title: "Bulk Delete Campuran: Dialog Dua Kelompok, Cancel, Esc, dan Continue Melewati SKU Berstok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-286
  - TC-AC-DS-287
  - TC-AC-DS-288
  - TC-AC-DS-555
coverage:
  web: automated
---

# Bulk Delete Campuran: Dialog Dua Kelompok, Cancel, Esc, dan Continue Melewati SKU Berstok

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: SKU seed dan inti yang dihapus atau ditambah stoknya oleh spec ini dibuat ulang atau dikembalikan ke stok 0 sesuai Pre-setup #29 dan #30. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-286: dialog dua kelompok

1. Centang checkbox baris `HHR-ARC-100`, `HHR-ARC-200`, dan `SEED-005`
2. Klik `Bulk Action`, lalu pilih `Delete`
3. Verifikasi judul dialog "Delete SKUs"
4. Verifikasi kelompok "The following will be deleted:" dengan bullet `HHR-ARC-200` dan `SEED-005`
5. Verifikasi kelompok "The following will be skipped (still have stock):" dengan bullet `HHR-ARC-100`
6. Verifikasi pertanyaan "Are you sure you want to continue?"
7. Verifikasi tombol `[Cancel]` dan `[Continue]`

### TC-AC-DS-288: Cancel mempertahankan seleksi

8. Klik `[Cancel]`
9. Hilangkan centang baris `SEED-005`
10. Klik `Bulk Action`, lalu pilih `Delete`
11. Klik `[Cancel]`
12. Verifikasi dialog tertutup
13. Verifikasi tidak ada toast
14. Verifikasi seleksi dua baris dan bar "2 SKUs selected" tetap ada
15. Verifikasi tidak ada SKU terhapus

### TC-AC-DS-555: Esc setara Cancel

16. Centang checkbox baris `SEED-005`
17. Klik `Bulk Action`, lalu pilih `Delete`
18. Tekan Esc
19. Verifikasi dialog tertutup seperti `[Cancel]`
20. Verifikasi tidak ada toast
21. Verifikasi tidak ada SKU terhapus
22. Verifikasi seleksi tiga baris dan bar "3 SKUs selected" tetap ada

### TC-AC-DS-287: Continue

23. Klik `Bulk Action`, lalu pilih `Delete`
24. Klik `[Continue]`
25. Verifikasi muncul toast sukses "Success, device SKU has been deleted. Some items were skipped (still have stock)."
26. Verifikasi baris `HHR-ARC-200` dan `SEED-005` hilang dari List
27. Verifikasi baris `HHR-ARC-100` tetap ada
28. Verifikasi bar bulk hilang
29. Verifikasi seleksi direset ke 0 termasuk SKU yang dilewati

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-288 dan TC-555 (membatalkan) mendahului TC-287 (menghapus) mengikuti S-10; urutan TC-288 sebelum TC-555 mengikuti kebutuhan seleksi dua baris lalu tiga baris. Langkah penghubung: `[Cancel]` setelah TC-286, menghilangkan dan mencentang kembali `SEED-005` mengatur seleksi antar blok (S-09).
- Temuan untuk QA: TC-286 memilih `SEED-005` yang berada di halaman 1 pada default sort SKU A-Z (Pre-setup #29 dan #30). Post Condition TC-287 (dua SKU terhapus; hanya dua entri Delete) tidak diasersi karena TC tidak memberi langkah observasinya.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
