---
id: TC-FA-GRP-E2E-076-delete-diblok-tujuan-transfer-dan-disposal-batch-belum-tuntas
title: "Delete Diblok: Tujuan Transfer Waiting for Approval/Departure/In Transfer Process dan Tujuan Disposal Batch In Disposal Process"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-232
  - TC-FA-GRP-233
  - TC-FA-GRP-234
  - TC-FA-GRP-235
coverage:
  web: automated
---

# Delete Diblok: Tujuan Transfer Waiting for Approval/Departure/In Transfer Process dan Tujuan Disposal Batch In Disposal Process

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Pre-setup (Tabel A, No 10; hanya dibaca, dialog blokir tidak mengubah apa pun): `Del Transfer` (tujuan transfer Waiting for Approval), `Del Transfer 2` (tujuan transfer Waiting for Departure), `Del Transfer 3` dengan child yang menjadi tujuan transfer In Transfer Process, dan `Del Disposal` (Disposal Group tujuan batch In Disposal Process). Status transaksi tetap tidak tuntas selama spec berjalan.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group sebelum dan sesudah aksi (audit trail permanen, tidak dapat diturunkan dari seeding; 8b butir 10) lewat fixture BE atau pembacaan UI.
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12).

## Test Steps

### Baseline Changelog

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group

### TC-FA-GRP-232: Tujuan Transfer Waiting for Approval

5. Buka elipsis `⋯` baris `Del Transfer`, pilih `Delete`
6. Verifikasi dialog dengan title "Cannot Delete Group"
7. Verifikasi isi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
8. Verifikasi dialog hanya memuat tombol [OK]
9. Klik [OK]
10. Verifikasi dialog tertutup
11. Verifikasi `Del Transfer` tetap ada di tabel (tidak ada yang terhapus)
12. Verifikasi tidak ada toast yang tampil
13. Buka Modal Changelog: Group
14. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
15. Tutup Modal Changelog: Group

### TC-FA-GRP-233: Tujuan Transfer Waiting for Departure

16. Buka elipsis `⋯` baris `Del Transfer 2`, pilih `Delete`
17. Verifikasi dialog dengan title "Cannot Delete Group"
18. Verifikasi isi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
19. Verifikasi dialog hanya memuat tombol [OK]
20. Klik [OK]
21. Verifikasi dialog tertutup
22. Verifikasi `Del Transfer 2` tetap ada di tabel (tidak ada yang terhapus)
23. Verifikasi tidak ada toast yang tampil
24. Buka Modal Changelog: Group
25. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
26. Tutup Modal Changelog: Group

### TC-FA-GRP-234: Descendant tujuan Transfer In Transfer Process

27. Buka elipsis `⋯` baris `Del Transfer 3`, pilih `Delete`
28. Verifikasi dialog dengan title "Cannot Delete Group"
29. Verifikasi isi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
30. Verifikasi dialog hanya memuat tombol [OK]
31. Klik [OK]
32. Verifikasi dialog tertutup
33. Verifikasi `Del Transfer 3` tetap ada di tabel (tidak ada yang terhapus)
34. Verifikasi tidak ada toast yang tampil
35. Buka Modal Changelog: Group
36. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
37. Tutup Modal Changelog: Group

### TC-FA-GRP-235: Tujuan Disposal Batch In Disposal Process

38. Buka elipsis `⋯` baris `Del Disposal`, pilih `Delete`
39. Verifikasi dialog dengan title "Cannot Delete Group"
40. Verifikasi isi dialog "This group is being used for an ongoing disposal transaction. Wait for it to complete or be canceled first."
41. Verifikasi dialog hanya memuat tombol [OK]
42. Klik [OK]
43. Verifikasi dialog tertutup
44. Verifikasi `Del Disposal` tetap ada di tabel (tidak ada yang terhapus)
45. Verifikasi tidak ada toast yang tampil
46. Buka Modal Changelog: Group
47. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
48. Tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 13, 15, 24, 26, 35, 37, 46, 48: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan: seluruh TC memblokir sehingga tidak ada aksi yang menghapus data; kondisi data berbeda per blok (prinsip 12).
- Klausa "tanpa toast & log" tiap blok diasersi dengan baseline jumlah entri (langkah 12/14, 23/25, 34/36, 45/47); anchor positif: langkah 2 (entri lain tampil) dan node tetap ada (langkah 11, 22, 33, 44). Butir `P-1`: seeding transaksi berat (Pre-setup No 10) membuat asersi log tetap berada di spec ini dengan baseline.
- Spec berisi lebih dari 35 langkah (empat blok blokir). Alasan: seluruhnya satu kelas dan satu topik (Delete diblok transaksi belum tuntas), tiap blok berdiri sendiri dengan data transaksi berbeda, dan empat blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13.
- Temuan untuk QA:
  - TC-232 sampai TC-235 menyebut "tanpa toast & log" tanpa menyebut surface log; spec memakai Modal Changelog: Group.
