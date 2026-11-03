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

1. Ketik Search `Warehouse A`, tekan Enter
2. Centang hanya `Warehouse A`
3. Buka Bulk Action, pilih `Delete`
4. Verifikasi dialog dengan title "Cannot Delete Group", isi "This group or its subgroups still hold assets. Transfer or dispose them first.", dan tombol [OK]
5. Klik [OK], lalu klik (X)

### TC-FA-GRP-258: Semua terblok, dialog blokir total

6. Centang `Warehouse A`
7. Ganti isi kotak Search dengan `Del Transfer`, tekan Enter
8. Centang `Del Transfer`
9. Buka Bulk Action, pilih `Delete`
10. Verifikasi dialog dengan title "Cannot Delete Groups", bullet `Warehouse A` dan `Del Transfer`, isi "These groups can't be deleted because they still hold assets or are used in an ongoing transfer or disposal transaction."
11. Verifikasi dialog hanya memuat tombol [OK]
12. Klik [OK]
13. Verifikasi `Del Transfer` tetap ada di tabel (tidak ada yang terhapus)
14. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
15. Verifikasi `Warehouse A` tetap ada di tabel
16. Verifikasi seleksi dan bar bulk action dipertahankan
17. Klik (X)

### TC-FA-GRP-257: Campuran dengan kelompok user ter-scope

18. Centang `Warehouse A`
19. Ganti isi kotak Search dengan `Bulk U2`, tekan Enter
20. Centang `Bulk U2`
21. Buka Bulk Action, pilih `Delete`
22. Verifikasi dialog campuran memuat kelompok "The following have users whose group roles will be removed:" berisi `Bulk U2`
23. Verifikasi kelompok skip aset "The following hold assets and will be skipped:" berisi `Warehouse A`
24. Klik [Cancel], lalu klik (X)

### TC-FA-GRP-256: Campuran, [Continue], dan toast ringkasan

25. Ganti isi kotak Search dengan `{runId}-084`, tekan Enter
26. Centang `Bulk E4` dan `Bulk E5`
27. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
28. Centang `Warehouse A`
29. Ganti isi kotak Search dengan `Del Transfer`, tekan Enter
30. Centang `Del Transfer`
31. Ganti isi kotak Search dengan `Del Disposal`, tekan Enter
32. Centang `Del Disposal`
33. Buka Bulk Action, pilih `Delete`
34. Verifikasi dialog `Delete Groups` dengan kelompok "The following will be deleted:" berisi `Bulk E4` dan `Bulk E5`, "The following hold assets and will be skipped:" berisi `Warehouse A`, "The following are the destination of an ongoing transfer and will be skipped:" berisi `Del Transfer`, "The following are being used for an ongoing disposal transaction and will be skipped:" berisi `Del Disposal`, isi "Are you sure you want to continue? This action cannot be undone.", tombol [Cancel] dan [Continue]
35. Verifikasi tiap group muncul tepat di satu kelompok
36. Klik [Continue]
37. Verifikasi toast "Success, group has been deleted. Some items were skipped."
38. Ganti isi kotak Search dengan `{runId}-084`, tekan Enter
39. Verifikasi `Bulk E4` dan `Bulk E5` terhapus dari tabel
40. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
41. Verifikasi `Warehouse A` tetap ada di tabel
42. Ganti isi kotak Search dengan `Del Transfer`, tekan Enter
43. Verifikasi `Del Transfer` tetap ada di tabel
44. Ganti isi kotak Search dengan `Del Disposal`, tekan Enter
45. Verifikasi `Del Disposal` tetap ada di tabel
46. Verifikasi bar bulk action hilang
47. Verifikasi seleksi direset ke 0 termasuk ketiga group yang di-skip

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 5, 17, 24: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 1 (Ketik Search `Warehouse A`, tekan Enter) dan langkah Ganti isi kotak Search lain (7, 14, 19, 25, 27, 29, 31, 38, 40, 42, 44) menemukan satu baris per Search: group seed spec ini lewat `{runId}-084` (tiga baris, satu halaman) dan group Pre-setup lewat namanya; centang dipertahankan saat Search berganti (TC-FA-GRP-251 dan 426); client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: dialog blokir dan dialog yang dibatalkan lebih dulu (TC-262, TC-258, TC-257), Delete campuran yang menghapus data (TC-256) paling akhir (S-10).
- Spec berisi lebih dari 35 langkah. Alasan: empat TC Bulk Delete (blokir total, campuran, dan dialog batal) satu keluarga dan satu kelas (fungsional) dengan dataset seed milik spec dan Pre-setup, tiap blok berdiri sendiri; tambahan langkah berasal dari Search baris target (R-16), bukan asersi baru (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-257 Expected hanya menyebut dua kelompok dialog campuran; spec mengasersi keduanya dan tidak menekan [Continue].
  - Teks kelompok dan kalimat penutup dialog pada TC-256 mengikuti kolom Expected; "Tiap group muncul tepat di satu kelompok" diasersi lewat isi dialog.
