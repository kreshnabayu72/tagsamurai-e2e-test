---
id: TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair
title: "User Detail: Sub-section User TAG (Screening, Penolakan Scan TAG-NEW-0001, TAG-4F7K2XQ9, dan TAG-OBJ-0001, Re-pair, Unpair, dan Scan TAG-USR-0001 Berhasil)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-313
  - TC-GS-USER-314
  - TC-GS-USER-315
  - TC-GS-USER-316
  - TC-GS-USER-317
  - TC-GS-USER-318
  - TC-GS-USER-319
  - TC-GS-USER-321
coverage:
  web: automated
---

# User Detail: Sub-section User TAG (Screening, Penolakan Scan TAG-NEW-0001, TAG-4F7K2XQ9, dan TAG-OBJ-0001, Re-pair, Unpair, dan Scan TAG-USR-0001 Berhasil)

## Prerequisites

- Mode: FE+BE (kelas harness d: simulasi scan TAG pada RFID reader).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup):
  - John Doe (No. 18, Activated, TAG `TAG-4F7K2XQ9`): dibaca di TC-GS-USER-314 dan TC-GS-USER-317, lalu diubah di TC-GS-USER-319 dan TC-GS-USER-321 (re-pair dan Unpair). Perubahan ini tidak dapat diganti user seed, karena `TAG-4F7K2XQ9` hanya terpasang pada John Doe. Hook `after` memulihkan John Doe ke `TAG-4F7K2XQ9`; Last Updated dan Modified By John Doe tidak dapat dipulihkan dan berubah.
  - TAG uji (No. 25): `TAG-USR-0001` (user, aktif, bebas), `TAG-4F7K2XQ9` (dipasang John Doe), `TAG-OBJ-0001` (object), `TAG-NEW-0001` (belum diaktivasi).
- Data Dinamis, di-seed lewat API di hook `before` (HK1) dan dibersihkan di hook `after`: `Dewi Lestari {runId}-057`, Email `dewilestari+{runId}-057@qwertysystem.net`, Activated, Division `Finance`, Access `Fixed Asset`, tanpa TAG.
- Kemampuan teknis, disediakan tim FE:
  - Simulasi RFID reader tersambung dan simulasi scan TAG pada tombol `Scan TAG` (HK7); TC tidak menyebut mekanismenya.
  - Memasang dan melepas TAG pada user lewat API untuk pemulihan di hook `after`; TC tidak menyebut mekanismenya.
- State global yang diubah: status paired TAG-USR-0001 dan TAG-4F7K2XQ9 di TAG Registry. Suite berjalan serial (`parallel: false`, lihat `suite.md`). Hook `after`, yang tetap berjalan walau spec gagal di tengah: lepas `TAG-USR-0001` dari user mana pun, pasang `TAG-4F7K2XQ9` kembali ke John Doe, lalu hapus `Dewi Lestari {runId}-057`.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-313: Screening sub-section User TAG tanpa TAG

3. Klik Name `Dewi Lestari {runId}-057` di User List
4. Verifikasi sub-section User TAG menampilkan Badge `Unverified` (warning), teks `No TAG paired`, dan Button `Scan TAG`

### TC-GS-USER-314: Screening sub-section User TAG dengan TAG terpasang

5. Kembali ke User List dengan klik Back
6. Klik Name `John Doe` di User List
7. Verifikasi sub-section User TAG menampilkan Badge `Verified` (success), `TAG-4F7K2XQ9`, Button `Scan TAG`, dan Button `Unpair`

### TC-GS-USER-316: Scan TAG-NEW-0001 dari Detail ditolak dan badge tidak berubah

8. Kembali ke User List dengan klik Back
9. Klik Name `Dewi Lestari {runId}-057` di User List
10. Klik `Scan TAG`
11. Simulasikan scan `TAG-NEW-0001`
12. Verifikasi toast error: "This TAG hasn't been activated yet. Please contact Admin."
13. Verifikasi Badge tetap `Unverified`

### TC-GS-USER-317: Scan TAG-4F7K2XQ9 dari Detail ditolak dan badge tidak berubah

14. Klik `Scan TAG`
15. Simulasikan scan `TAG-4F7K2XQ9`
16. Verifikasi toast error: "Error, RFID TAG is already paired to another user."
17. Verifikasi Badge tetap `Unverified`

### TC-GS-USER-318: Scan TAG-OBJ-0001 dari Detail ditolak dan badge tidak berubah

18. Klik `Scan TAG`
19. Simulasikan scan `TAG-OBJ-0001`
20. Verifikasi toast error: "Error, the scanned TAG is object TAG."
21. Verifikasi Badge tetap `Unverified`

### TC-GS-USER-319: Re-pair dari Detail mengganti TAG lama

22. Kembali ke User List dengan klik Back
23. Klik Name `John Doe` di User List
24. Klik `Scan TAG`
25. Simulasikan scan `TAG-USR-0001`
26. Verifikasi toast sukses: "Success, TAG has been paired."
27. Verifikasi TAG ID tampil `TAG-USR-0001`

### TC-GS-USER-321: Unpair TAG dari Detail, dialog lalu instan

28. Klik `Unpair`
29. Verifikasi dialog Title `Unpair TAG`
30. Verifikasi body dialog `• John Doe` / `This will unpair the TAG from this user.` / `Are you sure you want to unpair it?`
31. Verifikasi tombol dialog `[Cancel]` dan `[Unpair]`
32. Klik `[Unpair]`
33. Verifikasi toast sukses: "Success, TAG has been unpaired."
34. Verifikasi Badge `Unverified` dan teks `No TAG paired`

### TC-GS-USER-315: Scan TAG dari Detail langsung tersimpan dengan toast sendiri

35. Kembali ke User List dengan klik Back
36. Klik Name `Dewi Lestari {runId}-057` di User List
37. Klik `Scan TAG`
38. Simulasikan scan `TAG-USR-0001`
39. Verifikasi toast sukses: "Success, TAG has been paired."
40. Verifikasi Badge `Verified`, `TAG-USR-0001`, dan Button `Unpair` tampil tanpa langkah Save

## Notes

- Mode: FE+BE (kelas harness d). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (40 langkah). Alasan: seluruh blok satu kelas harness (d, simulasi scan TAG) dan satu layar (sub-section User TAG di User Detail); state TAG dibangun berurutan dari blok ke blok (`TAG-4F7K2XQ9` dan `TAG-USR-0001` bergiliran terpasang), sehingga sebagian besar langkah hanyalah buka Detail dan klik `Scan TAG` yang berulang.
- Urutan TC sumber diubah: screening (TC-GS-USER-313, 314) di awal; penolakan scan (TC-GS-USER-316, 317, 318) sebelum aksi sukses dan sebelum `TAG-4F7K2XQ9` dibebaskan; TC-GS-USER-319 (re-pair John Doe ke `TAG-USR-0001`, membebaskan `TAG-4F7K2XQ9`) lalu TC-GS-USER-321 (Unpair John Doe, membebaskan `TAG-USR-0001`) lalu TC-GS-USER-315 (scan `TAG-USR-0001` pada `Dewi Lestari {runId}-057`), karena TC-GS-USER-315 membutuhkan `TAG-USR-0001` bebas. Aksi Unpair (TC-GS-USER-321) tidak di akhir karena itu.
- TC-GS-USER-316, 317, dan 318 dijalankan berurutan pada satu pembukaan Detail `Dewi Lestari {runId}-057` (tanpa buka ulang, karena tidak ada perubahan state); `Scan TAG` diklik ulang di tiap TC.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): pembukaan layar, Back ke User List, dan klik `Scan TAG` serta simulasi scan sebagai pemicu.
- Temuan untuk QA:
  - TC-GS-USER-315, 316, 317, 318, 319: precondition "RFID reader tersambung" tidak menyebut cara membuat reader tersambung; disediakan tim FE.
  - TC-GS-USER-315: Post Condition (TAG Registry status paired; Hardware > Handheld > Detail Tab Usage Event Type `Pair TAG` bila reader tersambung) tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-319 dan 321: target John Doe adalah data Pre-setup yang mengubah TAG-nya; hanya ada satu TAG bebas (`TAG-USR-0001`) dan satu TAG terpasang (`TAG-4F7K2XQ9`) di Tabel Pre-setup, sehingga re-pair user seed tidak dapat disiapkan tanpa TAG tambahan. Spec memulihkan John Doe di hook `after`.
  - TC-GS-USER-319: Expected hanya menyebut TAG ID tampil `TAG-USR-0001`; pembebasan `TAG-4F7K2XQ9` dari John Doe tidak diasersi di TC.
  - TC-GS-USER-315: Expected b menyebut "tanpa perlu Save"; spec mengasersi state `Verified` langsung tampil tanpa langkah Save.
