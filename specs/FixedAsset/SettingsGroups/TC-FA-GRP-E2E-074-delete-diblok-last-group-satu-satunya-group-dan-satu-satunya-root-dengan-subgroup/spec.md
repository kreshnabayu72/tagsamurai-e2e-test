---
id: TC-FA-GRP-E2E-074-delete-diblok-last-group-satu-satunya-group-dan-satu-satunya-root-dengan-subgroup
title: "Delete Diblok: Last Group (Satu-Satunya Group dan Satu-Satunya Root dengan Subgroup)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-227
  - TC-FA-GRP-228
coverage:
  web: automated
---

# Delete Diblok: Last Group (Satu-Satunya Group dan Satu-Satunya Root dengan Subgroup)

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client khusus A (hanya `Only Group`; email dan `Spectra.env.FA_ONLYGROUP_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Akun ganti (langkah 16): Total Control client khusus B (hanya `Root One` dengan child `Child One`; `Spectra.env.FA_ROOTONE_TC_PASSWORD`, disediakan tim FE). Hook `after` mengembalikan sesi ke akun default suite.
- Data: kedua client khusus Pre-setup (disediakan tim FE); spec hanya membaca dan tidak mengubah (dialog blokir). `Only Group`, `Root One`, dan `Child One` memakai nama literal client khusus tanpa suffix karena data bukan milik spec.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group per client sebelum dan sesudah aksi (audit trail permanen; 8b butir 10). Baseline N0 (client A) dan N1 (client B) dicatat sebelum aksi pertama tiap blok (S-12).

## Test Steps

### TC-FA-GRP-227: Last group, satu-satunya group

1. Buka Modal Changelog: Group
2. Verifikasi judul Modal Changelog: Group tampil
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (boleh 0)
4. Tutup Modal Changelog: Group
5. Buka elipsis `⋯` baris `Only Group`, pilih `Delete`
6. Verifikasi dialog dengan title "Cannot Delete Group"
7. Verifikasi isi dialog "Deleting this group would leave you with no groups. Create another group before deleting this one."
8. Verifikasi dialog hanya memuat tombol [OK]
9. Klik [OK]
10. Verifikasi dialog tertutup
11. Verifikasi `Only Group` tetap ada di tabel (tidak ada yang terhapus)
12. Verifikasi tidak ada toast yang tampil
13. Buka Modal Changelog: Group
14. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
15. Tutup Modal Changelog: Group

### TC-FA-GRP-228: Last group, satu-satunya root dengan subgroup

16. Logout, lalu login sebagai Total Control client khusus B
17. Buka Fixed Asset > Settings > Groups
18. Buka Modal Changelog: Group
19. Verifikasi judul Modal Changelog: Group tampil
20. Catat jumlah entri Modal Changelog: Group sebagai baseline N1 (boleh 0)
21. Tutup Modal Changelog: Group
22. Buka elipsis `⋯` baris `Root One`, pilih `Delete`
23. Verifikasi dialog dengan title "Cannot Delete Group"
24. Verifikasi isi dialog "Deleting this group would leave you with no groups. Create another group before deleting this one."
25. Verifikasi dialog hanya memuat tombol [OK]
26. Klik [OK]
27. Verifikasi dialog tertutup
28. Verifikasi `Root One` tetap ada di tabel (tidak ada yang terhapus)
29. Verifikasi tidak ada toast yang tampil
30. Buka Modal Changelog: Group
31. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N1
32. Tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 13, 15 sampai 18, 20 dan 21, 30, 32: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Ganti akun ke client B ditulis eksplisit (langkah 16, S-07) karena kedua TC memakai client berbeda; akun pertama login di hook `before`.
- Klausa "tanpa toast & log" diasersi pada langkah 12 dan 14 (TC-227) serta 29 dan 31 (TC-228) dengan baseline jumlah entri; anchor positif: judul Modal Changelog tampil (langkah 2, 19) dan group tetap ada (langkah 11, 28). Baseline jumlah dipakai karena client khusus bisa belum punya entri Changelog (baseline nol sah, S-12). Prinsip 12 (blokir karena kondisi data).
- Temuan untuk QA:
  - Akun dan password Total Control client khusus tidak tertulis di Pre-setup TC; disediakan tim FE.
  - TC-227 dan TC-228 menyebut "tanpa toast & log" tanpa menyebut surface log; spec memakai Modal Changelog: Group.
