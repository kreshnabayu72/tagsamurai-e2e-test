---
id: TC-FA-GRP-E2E-084-bulk-delete-campuran-dan-semua-terblok-dialog-continue-dan-blokir-total
title: "Bulk Delete: Dialog Campuran dengan [Continue] dan Toast Ringkasan, Campuran dengan User Ter-Scope, Semua Terblok, dan N=1 Terblok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-256
  - TC-FA-GRP-257
  - TC-FA-GRP-258
  - TC-FA-GRP-262
coverage:
  web: automated
---

# Bulk Delete: Dialog Campuran dengan [Continue] dan Toast Ringkasan, Campuran dengan User Ter-Scope, Semua Terblok, dan N=1 Terblok

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset): `Bulk E4` dan `Bulk E5` (TC-256), `Bulk U2` (tanpa aset, punya `User BU 2` ber-Group Role, email `userBu2+{runId}-084@qwertysystem.net`; TC-257).
- Data Pre-setup (Tabel A, No 9 dan 10; hanya dibaca, di-skip atau diblok guard dan tidak diubah): `Warehouse A` (beraset), `Del Transfer` (tujuan transfer belum tuntas), `Del Disposal` (tujuan disposal belum tuntas).
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### TC-FA-GRP-262: N=1 terblok collapse ke dialog blok single

1. Centang hanya `Warehouse A`
2. Buka Bulk Action, pilih `Delete`
3. Verifikasi dialog dengan title "Cannot Delete Group", isi "This group or its subgroups still hold assets. Transfer or dispose them first.", dan tombol [OK]
4. Klik [OK], lalu klik (X)

### TC-FA-GRP-258: Semua terblok, dialog blokir total

5. Centang `Warehouse A` dan `Del Transfer`
6. Buka Bulk Action, pilih `Delete`
7. Verifikasi dialog dengan title "Cannot Delete Groups", bullet `Warehouse A` dan `Del Transfer`, isi "These groups can't be deleted because they still hold assets or are used in an ongoing transfer or disposal transaction."
8. Verifikasi dialog hanya memuat tombol [OK]
9. Klik [OK]
10. Verifikasi `Warehouse A` dan `Del Transfer` tetap ada di tabel (tidak ada yang terhapus)
11. Verifikasi seleksi dan bar bulk action dipertahankan
12. Klik (X)

### TC-FA-GRP-257: Campuran dengan kelompok user ter-scope

13. Centang `Bulk U2` dan `Warehouse A`
14. Buka Bulk Action, pilih `Delete`
15. Verifikasi dialog campuran memuat kelompok "The following have users whose group roles will be removed:" berisi `Bulk U2`
16. Verifikasi kelompok skip aset "The following hold assets and will be skipped:" berisi `Warehouse A`
17. Klik [Cancel], lalu klik (X)

### TC-FA-GRP-256: Campuran, [Continue], dan toast ringkasan

18. Centang `Bulk E4`, `Bulk E5`, `Warehouse A`, `Del Transfer`, dan `Del Disposal`
19. Buka Bulk Action, pilih `Delete`
20. Verifikasi dialog `Delete Groups` dengan kelompok "The following will be deleted:" berisi `Bulk E4` dan `Bulk E5`, "The following hold assets and will be skipped:" berisi `Warehouse A`, "The following are the destination of an ongoing transfer and will be skipped:" berisi `Del Transfer`, "The following are being used for an ongoing disposal transaction and will be skipped:" berisi `Del Disposal`, isi "Are you sure you want to continue? This action cannot be undone.", tombol [Cancel] dan [Continue]
21. Verifikasi tiap group muncul tepat di satu kelompok
22. Klik [Continue]
23. Verifikasi toast "Success, group has been deleted. Some items were skipped."
24. Verifikasi `Bulk E4` dan `Bulk E5` terhapus dari tabel
25. Verifikasi `Warehouse A`, `Del Transfer`, dan `Del Disposal` tetap ada di tabel
26. Verifikasi bar bulk action hilang
27. Verifikasi seleksi direset ke 0 termasuk ketiga group yang di-skip

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4, 12, 17: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan: dialog blokir dan dialog yang dibatalkan lebih dulu (TC-262, TC-258, TC-257), Delete campuran yang menghapus data (TC-256) paling akhir (S-10).
- Temuan untuk QA:
  - TC-257 Expected hanya menyebut dua kelompok dialog campuran; spec mengasersi keduanya dan tidak menekan [Continue].
  - Teks kelompok dan kalimat penutup dialog pada TC-256 mengikuti kolom Expected; "Tiap group muncul tepat di satu kelompok" diasersi lewat isi dialog.
