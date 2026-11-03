---
id: TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif
title: Sub-tab Addon dengan lisensi nonaktif dan aktif
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-462
  - TC-FA-RP-463
  - TC-FA-RP-464
  - TC-FA-RP-465
  - TC-FA-RP-466
  - TC-FA-RP-467
coverage:
  web: automated
---

# Sub-tab Addon dengan lisensi nonaktif dan aktif

## Prerequisites

- Mode: FE+BE
- Akun (akun disediakan tim FE; email tidak tertulis di Pre-setup TC):

| Urutan | Akun | Pre-setup | Env password |
|---|---|---|---|
| 1 (hook `before`) | Total Control pada `Client Addon Off` (lisensi Addon Audit, Maintenance, dan Tracking tidak aktif) | #31 | `Spectra.env.FA_ADDON_OFF_TC_PASSWORD` |
| 2 | Total Control pada `Client Addon On` (ketiga lisensi aktif) | #31 | `Spectra.env.FA_ADDON_ON_TC_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup: #18 (pohon Group, node `IT Infrastructure`), #31 (dua client Addon), #19 (seed Role Transaksi pada `IT Infrastructure`, dipakai sebagai precondition TC 466 dan 467, tidak diasersi).
- Spec ini tidak mengubah data; tidak ada pemulihan selain sesi.

## Test Steps

### Lisensi Addon nonaktif (Client Addon Off)

1. Buka Tab Transaction Role, lalu klik node `IT Infrastructure` di Sidebar Group Tree.
2. Verifikasi sub-tab `Audit` tampil bergaya disabled namun dapat dipilih.
3. Klik sub-tab `Audit`.
4. Verifikasi area konten hanya berisi banner `This feature requires the Audit add-on. Upgrade your license to use it.` dengan CTA `[View License]` (pola `This feature requires the [Addon Name] add-on. Upgrade your license to use it.` dengan `[Addon Name]` = `Audit`).
5. Verifikasi tidak ada data penugasan, tidak ada kartu Approval Rule, dan tidak ada aksi tulis.
6. Verifikasi sub-tab `Repair Ticketing` tampil bergaya disabled namun dapat dipilih.
7. Klik sub-tab `Repair Ticketing`.
8. Verifikasi area konten sub-tab `Repair Ticketing` hanya berisi banner `This feature requires the Maintenance add-on. Upgrade your license to use it.` dengan CTA `[View License]`.
9. Verifikasi tidak ada data penugasan, tidak ada kartu Approval Rule, dan tidak ada aksi tulis pada sub-tab `Repair Ticketing`.
10. Verifikasi sub-tab `Maintenance Routine` tampil bergaya disabled namun dapat dipilih.
11. Klik sub-tab `Maintenance Routine`.
12. Verifikasi area konten hanya berisi banner `This feature requires the Maintenance add-on. Upgrade your license to use it.` dengan CTA `[View License]`.
13. Verifikasi tidak ada data penugasan, tidak ada kartu Approval Rule, dan tidak ada aksi tulis.
14. Verifikasi sub-tab `Tracking` tampil bergaya disabled namun dapat dipilih.
15. Klik sub-tab `Tracking`.
16. Verifikasi area konten hanya berisi banner `This feature requires the Tracking add-on. Upgrade your license to use it.` dengan CTA `[View License]`.
17. Verifikasi tidak ada data penugasan, tidak ada kartu Approval Rule, dan tidak ada aksi tulis.

### Sub-tab inti tetap normal

18. Klik sub-tab `Borrowing & Assignment`.
19. Verifikasi kartu Approval Rule dan section role tampil normal tanpa banner.
20. Klik sub-tab `Missing`.
21. Verifikasi kartu Approval Rule dan section role tampil normal tanpa banner.

### CTA View License

22. Klik sub-tab `Audit`.
23. Klik `[View License]`.
24. Verifikasi menu License terbuka.

### Lisensi Addon aktif (Client Addon On)

25. Ganti akun: logout, lalu login sebagai Total Control pada `Client Addon On`.
26. Buka Fixed Asset > Settings > Role & Permission > Transaction Role, lalu klik node `IT Infrastructure` di Sidebar Group Tree.
27. Klik sub-tab `Audit`.
28. Verifikasi kartu Approval Rule dan section role tampil normal tanpa banner pada sub-tab `Audit`.
29. Klik sub-tab `Repair Ticketing`.
30. Verifikasi kartu Approval Rule dan section role tampil normal tanpa banner pada sub-tab `Repair Ticketing`.
31. Klik sub-tab `Tracking`.
32. Verifikasi kartu Approval Rule dan section role tampil normal tanpa banner pada sub-tab `Tracking`.
33. Klik sub-tab `Maintenance Routine`.
34. Verifikasi kartu Approval Rule dan section role tampil normal tanpa banner pada sub-tab `Maintenance Routine`.

## Notes

- Urutan TC berubah: TC 466 dijalankan sebelum TC 465 dan TC 467 paling akhir. TC 465 membuka menu License (meninggalkan halaman), sehingga dijalankan terakhir dalam blok `Client Addon Off`; TC 467 butuh ganti akun ke `Client Addon On`.
- Langkah penghubung (S-03): 1, 22, 25, 26, dan 27 sampai 33 yang berupa klik sub-tab sebagai aksi tanpa Verifikasi sendiri. Langkah 22 membuka sub-tab `Audit` sebagai precondition TC 465.
- Expected d TC 462 (pola copy PRD dengan `[Addon Name]` = `Audit`) digabung ke langkah 4 karena teks banner literal sudah memuat pola itu; langkah 4 menjadi satu `Verifikasi` elemen banner beserta CTA (S-01, elemen komposit).
- Langkah 5, 9, 13, dan 17 adalah asersi absence di area konten; pembanding positifnya banner pada langkah 4, 8, 12, dan 16.
- Temuan untuk QA:
  - Seluruh TC memakai `Client Addon Off` atau `Client Addon On` (Pre-setup #31); email akun Total Control kedua client itu tidak tertulis di Pre-setup TC dan disediakan tim FE.
