---
id: TC-AC-ACTS-E2E-149-state-tenant-distributor-suspended-aksi-tulis-ditolak-dan-plan-gating-tidak-ada
title: "State Tenant: Distributor Suspended (Aksi Tulis Ditolak Server, Import GPS, Delete Scan dan Bulk, Aksi Sistem Tanpa Aktor Tidak Diblokir) dan Plan Gating Tidak Ada"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-138
  - TC-AC-ACTS-736
  - TC-AC-ACTS-758
  - TC-AC-ACTS-760
  - TC-AC-ACTS-837
coverage:
  web: automated
---

# State Tenant: Distributor Suspended (Aksi Tulis Ditolak Server, Import GPS, Delete Scan dan Bulk, Aksi Sistem Tanpa Aktor Tidak Diblokir) dan Plan Gating Tidak Ada

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Suspended (Pre-setup #20) `distributorSuspended_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_SUSP_PASSWORD`.
- Akun aktor kedua (Ganti akun): Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Distributor Suspended; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- State global: status Suspended entitas Distributor dan plan tier diatur lewat fixture BE sebelum blok TC terkait dan dipulihkan ke nilai awal di hook `after` spec ini (R-08); suite berjalan serial (`parallel: false`).
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12) dan SKU GPS `GPS-TRACK-CORE-G3` (#15). Unit milik spec (di-seed idempoten, dipulihkan fixture BE): unit Available milik Distributor Suspended (U1, U2); Subject Activation Collision pending dari Client di bawah entitas Distributor itu beserta unit Waiting for Approval (TC-AC-ACTS-758). Identifier untuk Preview GPS TC-AC-ACTS-760: dua IMEI baru dari Data Dinamis #2 (`356938035643809` dan `356938035643810`).
- Tabel Tier plan untuk TC-AC-ACTS-736, tiap tier mendaftarkan satu TAG RFID baru yang belum terdaftar (EPC baru per tier, disediakan simulator):

| Tier plan | TAG baru |
|---|---|
| Starter | EPC baru tier 1 |
| Growth | EPC baru tier 2 |
| Professional | EPC baru tier 3 |
| Enterprise | EPC baru tier 4 |

- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pemicu event Delete TAG dari Global Settings (Client menghapus tag Waiting di registri) disediakan tim FE/BE (TC-AC-ACTS-758); aktor dan mekanismenya tidak disebut di TC, PRD, atau LLD.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).

## Test Steps

### TC-AC-ACTS-138: Distributor Suspended, aksi tulis ditolak server dan baca tetap berjalan

1. Atur status entitas Distributor menjadi Suspended lewat fixture BE, lalu muat ulang halaman
2. Klik `[Add Stock]` pada SKU `RFID-ASSET-CORE-R5`, scan satu TAG baru, klik `[Stop]`, lalu klik `[Submit]`
3. Verifikasi Submit ditolak server (403) dengan toast error `Changes can't be saved while this workspace is suspended or expired.`
4. Verifikasi tidak ada data tersimpan dan UI di-refresh tanpa redirect
5. Buka Detail SKU `RFID-ASSET-CORE-R5`, klik (⋯) pada unit Available, klik `Delete`, lalu klik `[Delete]`
6. Verifikasi Delete ditolak server (403) dengan toast error `Changes can't be saved while this workspace is suspended or expired.`
7. Verifikasi unit tidak terhapus dan UI di-refresh tanpa redirect
8. Klik `[Audit TAG]`, klik `[Start Scan]`, scan satu unit, klik `[Stop]`, lalu klik `[Submit]`
9. Verifikasi Audit Submit ditolak server (403) dengan toast error `Changes can't be saved while this workspace is suspended or expired.`
10. Verifikasi tidak ada perubahan status unit dan UI di-refresh tanpa redirect
11. Buka Stock List
12. Verifikasi Stock List dapat dibuka
13. Buka Detail SKU `RFID-ASSET-CORE-R5`
14. Verifikasi Detail SKU dapat dibuka
15. Klik Download pada Tab Available
16. Verifikasi Download dapat dibuka dan menghasilkan berkas
17. Klik `[Event Log]`
18. Verifikasi modal Event Log dapat dibuka
19. Tutup modal Event Log

### TC-AC-ACTS-760: Import GPS, Distributor Suspended, Submit ditolak server dan baca tetap berjalan

20. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), isi Preview dengan 2 baris OK
21. Klik `[Submit]`
22. Verifikasi Submit ditolak server (403) dengan toast error `Changes can't be saved while this workspace is suspended or expired.`
23. Verifikasi tidak ada unit tersimpan dan UI di-refresh tanpa redirect
24. Buka Stock List
25. Verifikasi Stock List tetap dapat dibuka

### TC-AC-ACTS-837: Distributor Suspended, aksi hapus (scan dan Bulk) ditolak server

26. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
27. Klik `[Delete by Scan]`, scan U1, klik `[Stop]`
28. Verifikasi aksi Delete by Scan ditolak server dengan toast error `Changes can't be saved while this workspace is suspended or expired.`
29. Centang U1 dan U2, pilih Bulk Action > `Delete`, klik `[Delete]`
30. Verifikasi aksi Bulk Delete ditolak server dengan toast error `Changes can't be saved while this workspace is suspended or expired.`
31. Verifikasi UI di-refresh tanpa redirect dan U1 dan U2 tidak terhapus

### TC-AC-ACTS-758: Aksi sistem tanpa aktor (Duplicate Canceled) tidak diblokir saat entitas Suspended

32. Ganti akun: Logout, lalu login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)
33. Buka Activity Log (filter Object `TAG Stock`) dan catat baseline jumlah entri `Duplicate Canceled`
34. Kirim event Delete TAG dari Global Settings (Client menghapus tag Waiting di registri) hingga event diproses
35. Buka Approvals > TAG Stock > Tab History
36. Verifikasi Subject ditandai Canceled
37. Verifikasi unit Waiting for Approval terkait dihapus
38. Buka Activity Log
39. Verifikasi jumlah entri `Duplicate Canceled` naik tepat 1 dari baseline langkah 33
40. Verifikasi entri `Duplicate Canceled` teratas (urutan default `Date` terbaru) tercatat dengan Modified By `System`

### TC-AC-ACTS-736: Plan Gating tidak ada, perilaku Add Stock identik lintas semua tier plan

41. Atur plan tier sesuai baris tabel Tier plan (mulai Starter) lewat fixture BE, lalu muat ulang halaman
42. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`
43. Scan 1 TAG baru sesuai baris tabel
44. Klik `[Stop]`
45. Klik `[Submit]`
46. Verifikasi toast sukses `Success, TAG has been registered.`
47. Verifikasi tidak ada gating, upsell, atau limit berbeda pada halaman Add Stock
48. Untuk setiap baris tabel Tier plan berikutnya (Growth, Professional, Enterprise) ulangi langkah 41 sampai 47
49. Pulihkan plan tier ke nilai awal lewat fixture BE

## Notes

- Alasan di atas smell ~35 langkah: blok 138 sampai 837 berkelas h (Suspended) dengan satu akun dan dataset, blok 758 dan 736 sesudah Ganti akun berkelas h dan plan tier; TC-AC-ACTS-736 mengulang langkah 41 sampai 47 untuk empat tier (8b butir 7; parameter ada di tabel Prerequisites, ekspansi 4 kali tujuh langkah). Tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal.
- Langkah penghubung (S-03): langkah 1 (menyetel status Suspended), pembukaan dan penutupan modal, navigasi, dan pemulihan plan tier di langkah terakhir. Urutan TC: 138, 760, 837, 758, 736; blok 758 dan 736 sesudah Ganti akun.
- Cara baca entri audit trail baru (S-12, S-14): jumlah entri dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-758 selisih satu entri `Duplicate Canceled` setelah event Delete TAG diproses.
- Temuan untuk QA:
  - Langkah Uji TC-AC-ACTS-138 nomor 1 menyebut "Klik `[Add Stock]` pada SKU lalu Submit" tanpa menyebut TAG yang discan; spec men-scan satu TAG baru (simulator).
  - TC-AC-ACTS-758 dan 736 dijalankan sebagai Total Control walau TC-AC-ACTS-758 berprecondition entitas Distributor Suspended; Pre-setup #1 dipakai untuk melihat hasil di Approvals (Tab History) dan Activity Log.
  - TC-AC-ACTS-736 menyebut "1 TAG baru per tier" tanpa identifier; spec memakai EPC baru per tier yang disediakan simulator (identifier tetap tidak dapat dipakai ulang antar tier).
  - TC-AC-ACTS-758 tidak menyebut aktor Client dan mekanisme event Delete TAG; spec memakai pemicu yang disediakan tim FE/BE.
  - TC-AC-ACTS-736 "UI identik lintas tier" dibandingkan terhadap tier yang diuji berurutan; TC tidak menyebut elemen yang dibandingkan.
