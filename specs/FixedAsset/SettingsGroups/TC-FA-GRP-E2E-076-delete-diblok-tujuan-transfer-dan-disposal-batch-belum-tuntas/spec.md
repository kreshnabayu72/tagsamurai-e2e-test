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
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12). N1, N2, dan N3 dicatat pada langkah 16, 29, dan 42 (sebelum aksi TC-FA-GRP-233, 234, dan 235), saat Modal Changelog: Group masih terbuka sesudah pembacaan blok sebelumnya (S-12).

## Test Steps

### Baseline Changelog

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group

### TC-FA-GRP-232: Tujuan Transfer Waiting for Approval

5. Ketik Search `Del Transfer`, tekan Enter
6. Buka elipsis `⋯` baris `Del Transfer`, pilih `Delete`
7. Verifikasi dialog dengan title "Cannot Delete Group"
8. Verifikasi isi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
9. Verifikasi dialog hanya memuat tombol [OK]
10. Klik [OK]
11. Verifikasi dialog tertutup
12. Verifikasi `Del Transfer` tetap ada di tabel (tidak ada yang terhapus)
13. Verifikasi tidak ada toast yang tampil
14. Buka Modal Changelog: Group
15. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
16. Catat jumlah entri Modal Changelog: Group sebagai baseline N1 (jumlah total pada footer pagination)
17. Tutup Modal Changelog: Group

### TC-FA-GRP-233: Tujuan Transfer Waiting for Departure

18. Ganti isi kotak Search dengan `Del Transfer 2`, tekan Enter
19. Buka elipsis `⋯` baris `Del Transfer 2`, pilih `Delete`
20. Verifikasi dialog dengan title "Cannot Delete Group"
21. Verifikasi isi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
22. Verifikasi dialog hanya memuat tombol [OK]
23. Klik [OK]
24. Verifikasi dialog tertutup
25. Verifikasi `Del Transfer 2` tetap ada di tabel (tidak ada yang terhapus)
26. Verifikasi tidak ada toast yang tampil
27. Buka Modal Changelog: Group
28. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N1
29. Catat jumlah entri Modal Changelog: Group sebagai baseline N2 (jumlah total pada footer pagination)
30. Tutup Modal Changelog: Group

### TC-FA-GRP-234: Descendant tujuan Transfer In Transfer Process

31. Ganti isi kotak Search dengan `Del Transfer 3`, tekan Enter
32. Buka elipsis `⋯` baris `Del Transfer 3`, pilih `Delete`
33. Verifikasi dialog dengan title "Cannot Delete Group"
34. Verifikasi isi dialog "This group is the destination of an ongoing transfer. Wait for it to complete or be canceled first."
35. Verifikasi dialog hanya memuat tombol [OK]
36. Klik [OK]
37. Verifikasi dialog tertutup
38. Verifikasi `Del Transfer 3` tetap ada di tabel (tidak ada yang terhapus)
39. Verifikasi tidak ada toast yang tampil
40. Buka Modal Changelog: Group
41. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N2
42. Catat jumlah entri Modal Changelog: Group sebagai baseline N3 (jumlah total pada footer pagination)
43. Tutup Modal Changelog: Group

### TC-FA-GRP-235: Tujuan Disposal Batch In Disposal Process

44. Ganti isi kotak Search dengan `Del Disposal`, tekan Enter
45. Buka elipsis `⋯` baris `Del Disposal`, pilih `Delete`
46. Verifikasi dialog dengan title "Cannot Delete Group"
47. Verifikasi isi dialog "This group is being used for an ongoing disposal transaction. Wait for it to complete or be canceled first."
48. Verifikasi dialog hanya memuat tombol [OK]
49. Klik [OK]
50. Verifikasi dialog tertutup
51. Verifikasi `Del Disposal` tetap ada di tabel (tidak ada yang terhapus)
52. Verifikasi tidak ada toast yang tampil
53. Buka Modal Changelog: Group
54. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N3
55. Tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 14, 17, 27, 30, 40, 43, 53, 55: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 5, 18, 31, 44 (Ketik atau ganti isi kotak Search dengan `Del Transfer`, `Del Transfer 2`, `Del Transfer 3`, dan `Del Disposal`, tekan Enter) menemukan baris yang dibuka elipsisnya; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: seluruh TC memblokir sehingga tidak ada aksi yang menghapus data; kondisi data berbeda per blok (prinsip 12).
- Klausa "tanpa toast & log" tiap blok diasersi dengan baseline jumlah entri (langkah 13/15, 26/28, 39/41, 52/54); anchor positif: langkah 2 (entri lain tampil) dan node tetap ada (langkah 12, 25, 38, 51). Butir `P-1`: seeding transaksi berat (Pre-setup No 10) membuat asersi log tetap berada di spec ini dengan baseline.
- Spec berisi lebih dari 35 langkah (empat blok blokir). Alasan: seluruhnya satu kelas dan satu topik (Delete diblok transaksi belum tuntas), tiap blok berdiri sendiri dengan data transaksi berbeda, dan empat blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13.
- Temuan untuk QA:
  - TC-232 sampai TC-235 menyebut "tanpa toast & log" tanpa menyebut surface log; spec memakai Modal Changelog: Group.
