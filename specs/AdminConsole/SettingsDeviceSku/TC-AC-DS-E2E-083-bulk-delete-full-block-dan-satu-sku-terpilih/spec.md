---
id: TC-AC-DS-E2E-083-bulk-delete-full-block-dan-satu-sku-terpilih
title: "Bulk Delete Full-block dan Satu SKU Terpilih: Dialog Blok, OK, Esc, dan Dialog Single"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-285
  - TC-AC-DS-289
  - TC-AC-DS-290
  - TC-AC-DS-291
  - TC-AC-DS-556
coverage:
  web: automated
---

# Bulk Delete Full-block dan Satu SKU Terpilih: Dialog Blok, OK, Esc, dan Dialog Single

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- SKU berstok: `HHR-ARC-100` (120), `SFR-VEL-4P` (36), `TAG-ARC-USR` (500); SKU stok 0: `SEED-004`.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: tidak ada data tersimpan yang berubah (spec hanya membuka dan menutup dialog). Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-289: dialog blok full-block

1. Atur jumlah data per halaman menjadi 100
2. Centang checkbox baris `HHR-ARC-100`
3. Pindah ke halaman 2
4. Centang checkbox baris `SFR-VEL-4P` dan `TAG-ARC-USR`
5. Klik `Bulk Action`, lalu pilih `Delete`
6. Verifikasi judul dialog blok "Cannot Delete SKUs"
7. Verifikasi bullet `HHR-ARC-100`, `SFR-VEL-4P`, dan `TAG-ARC-USR` dalam list yang dapat di-scroll
8. Verifikasi body "These SKUs still have stock. Remove all stock before deleting."
9. Verifikasi hanya satu tombol `[OK]`, tanpa tahap konfirmasi Yes/No
10. Verifikasi tidak ada toast

### TC-AC-DS-290: OK mempertahankan seleksi

11. Klik `[OK]`
12. Hilangkan centang baris `TAG-ARC-USR`
13. Klik `Bulk Action`, lalu pilih `Delete`
14. Klik `[OK]`
15. Verifikasi dialog tertutup
16. Verifikasi tidak ada toast
17. Verifikasi seleksi dua baris dan bar "2 SKUs selected" tetap ada

### TC-AC-DS-556: Esc setara OK

18. Klik `Bulk Action`, lalu pilih `Delete`
19. Tekan Esc
20. Verifikasi dialog tertutup seperti `[OK]`
21. Verifikasi tidak ada toast
22. Verifikasi seleksi dua baris dan bar bulk tetap ada
23. Verifikasi tidak ada SKU terhapus

### TC-AC-DS-291: satu SKU berstok terpilih

24. Hilangkan centang baris `SFR-VEL-4P`
25. Klik `Bulk Action`, lalu pilih `Delete`
26. Verifikasi dialog blok tunggal dengan judul "Cannot Delete SKU", bullet `HHR-ARC-100`, dan body "This SKU still has stock. Remove all stock before deleting."
27. Verifikasi hanya satu tombol `[OK]`
28. Klik `[OK]`

### TC-AC-DS-285: satu SKU stok 0 terpilih

29. Klik ikon `(✕)` pada bar
30. Pindah ke halaman 1
31. Centang checkbox baris `SEED-004`
32. Klik `Bulk Action`, lalu pilih `Delete`
33. Verifikasi dialog tunggal dengan judul "Delete SKU" (bentuk tunggal), bullet `SEED-004`, dan body "Are you sure you want to delete it? This action cannot be undone."
34. Verifikasi tombol `[Cancel]` dan `[Delete]`
35. Verifikasi bukan dialog bulk dua kelompok
36. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas sekitar 35 langkah (bagian 3, prinsip 13): semua blok memakai satu kelas harness (dialog Bulk Delete pada data seed yang sama), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihannya berasal dari pemecahan Expected per klausa (S-01) dan pembersihan seleksi antar blok (S-09). Langkah: 36.
- Penyimpangan urutan: TC-290 dan TC-556 memakai dua SKU (`HHR-ARC-100`, `SFR-VEL-4P`) yang diturunkan dari seleksi tiga SKU TC-289 dengan menghilangkan centang `TAG-ARC-USR`; TC-291 dan TC-285 menyusul. Atur 100 baris per halaman (langkah 1) dan pindah ke halaman 2 menjadikan `SFR-VEL-4P` dan `TAG-ARC-USR` (di luar halaman 1 pada default sort SKU A-Z) dapat dicentang tanpa Search; seleksi dipertahankan antar halaman (TC-280).
- Langkah penghubung: `[OK]` dan ikon `(✕)` serta `[Cancel]` menutup dialog dan membersihkan seleksi antar blok (S-09).
- Temuan untuk QA: TC-289 sampai TC-291 dan TC-556 tidak menyebut cara menjangkau `SFR-VEL-4P` dan `TAG-ARC-USR` yang tidak berada di halaman 1. Post Condition TC-285 sampai TC-291 dan TC-556 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
