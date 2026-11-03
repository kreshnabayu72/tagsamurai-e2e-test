---
id: TC-AC-DS-E2E-081-bulk-delete-homogen-dialog-cancel-esc-dan-berhasil
title: "Bulk Delete Homogen: Dialog dengan Daftar Scroll, Cancel, Esc, Klik Ganda, dan Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-281
  - TC-AC-DS-282
  - TC-AC-DS-283
  - TC-AC-DS-284
  - TC-AC-DS-297
coverage:
  web: automated
---

# Bulk Delete Homogen: Dialog dengan Daftar Scroll, Cancel, Esc, Klik Ganda, dan Berhasil

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


### TC-AC-DS-281: dialog dengan daftar scroll

1. Ketik Search `SEED`, tekan Enter
2. Atur jumlah data per halaman menjadi 25
3. Klik checkbox header
4. Klik `Bulk Action`, lalu pilih `Delete`
5. Verifikasi judul dialog "Delete SKUs"
6. Verifikasi 25 bullet SKU (`SEED-001` sampai `SEED-025`) tampil lengkap dalam container yang dapat di-scroll, tanpa teks ringkasan yang menyingkat daftar
7. Verifikasi body "Are you sure you want to delete them? This action cannot be undone."
8. Verifikasi tombol `[Cancel]` dan `[Delete]`
9. Klik `[Cancel]`
10. Klik ikon `(✕)` pada bar

### TC-AC-DS-282: Cancel mempertahankan seleksi

11. Centang checkbox baris `SEED-001`, `SEED-002`, dan `SEED-003`
12. Klik `Bulk Action`, lalu pilih `Delete`
13. Klik `[Cancel]`
14. Verifikasi dialog tertutup
15. Verifikasi tidak ada toast
16. Verifikasi seleksi tiga baris dan bar "3 SKUs selected" tetap ada
17. Verifikasi tidak ada SKU terhapus

### TC-AC-DS-283: Esc setara Cancel

18. Hilangkan centang baris `SEED-003`
19. Klik `Bulk Action`, lalu pilih `Delete`
20. Tekan Esc
21. Verifikasi dialog tertutup seperti `[Cancel]`
22. Verifikasi tidak ada SKU terhapus
23. Verifikasi seleksi dan bar bulk tetap ada

### TC-AC-DS-284: Bulk Delete berhasil

24. Centang checkbox baris `SEED-003`
25. Klik `Bulk Action`, lalu pilih `Delete`
26. Klik `[Delete]`
27. Verifikasi muncul toast sukses "Success, device SKU has been deleted."
28. Verifikasi dialog tertutup
29. Verifikasi baris `SEED-001`, `SEED-002`, dan `SEED-003` hilang dari List
30. Verifikasi bar bulk hilang
31. Verifikasi seleksi direset ke 0

### TC-AC-DS-297: klik ganda Delete pada dialog Bulk

32. Centang checkbox baris `SEED-014` dan `SEED-015`
33. Klik `Bulk Action`, lalu pilih `Delete`
34. Tunggu toast lama hilang otomatis
35. Klik `[Delete]` dua kali dengan cepat
36. Verifikasi tombol `[Delete]` disabled setelah klik pertama
37. Verifikasi hanya satu toast sukses "Success, device SKU has been deleted." yang tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas sekitar 35 langkah (bagian 3, prinsip 13): semua blok memakai satu kelas harness (dialog Bulk Delete pada data seed yang sama), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihannya berasal dari pemecahan Expected per klausa (S-01) dan pembersihan seleksi antar blok (S-09). Langkah: 37.
- Langkah penghubung: Search `SEED` pada langkah 1 dan 25 baris per halaman membuat `SEED-001` sampai `SEED-025` tampil bersama di halaman 1; ikon `(✕)` pada bar, menghilangkan centang `SEED-003`, dan memilih kembali `SEED-003` mengatur seleksi antar blok (S-09).
- Penyimpangan urutan: TC-297 (aksi menghapus data) dijalankan paling akhir bersama TC-284 (S-10).
- Temuan untuk QA: TC-281 mengharapkan 25 bullet `SEED-001` sampai `SEED-025`; urutan bullet mengikuti default sort SKU A-Z. Post Condition TC-284 dan TC-297 (SKU terhapus permanen; entri Delete per SKU tiap surface log) tidak diasersi karena TC tidak memberi langkah observasinya.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
