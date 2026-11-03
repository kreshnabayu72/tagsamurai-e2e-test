---
id: TC-AC-PF-E2E-219-resilience-push-update-dan-save-global-settings-5xx-dan
title: "Resilience: Push Update dan Save Global Settings Gagal 5xx dan Tanpa Respons"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-280
  - TC-AC-PF-299
  - TC-AC-PF-720
  - TC-AC-PF-721
coverage:
  web: automated
---

# Resilience: Push Update dan Save Global Settings Gagal 5xx dan Tanpa Respons

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan P (Pre-setup #28; custom plan `Paket Push` v3 dengan `PT Push Dua` Active v2, serta `Paket Push Susp` dan `Paket Push Exp`); nilai Global FAMS Settings tersimpan `5` (Max custom fields per asset name) dan `2` (Max depreciation methods (Multi Depreciation tier)).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum aksi pertama): Plan Version `PT Push Dua` (`v2`), jumlah entri Changelog Custom (`N_log_custom`), dan nilai Max custom fields per asset name (`5`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: `Paket Push`, `PT Push Dua`, dan nilai Global FAMS Settings Pre-setup menjadi target aksi tulis yang digagalkan intercept; spec tidak mengubah data itu karena seluruh request gagal. Pemulihan Dataset dan nilai Global Settings lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Push Update dan Save Global FAMS Settings (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC): (a) respons server error 5xx dan (b) respons tidak pernah diterima FE. Intercept dilepas segera setelah pemicu (S-09). Penanganan dialog `beforeunload` pada F5 saat form dirty (konfirmasi dialog), disediakan tim FE (S-08). Fixture BE untuk membaca Plan Version, nilai Global Settings, dan jumlah entri Changelog serta memulihkan Dataset; sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-280: Push Update gagal 5xx: toast error, dialog dapat diulang manual, versi client tidak berubah

1. Klik tab Custom
2. Ketik Search `Paket Push`, tekan Enter
3. Klik teks `Paket Push` pada kolom Plan Name sehingga Plan Detail terbuka
4. Klik Tab Assigned Clients
5. Buka Overlay Row Action `PT Push Dua` → klik `Push Update`
6. Pasang intercept: respons Push Update dijawab server error
7. Klik `[Push Update]`
8. Lepas intercept
9. Verifikasi toast error: "Error, failed to push plan update."
10. Verifikasi tombol `[Push Update]` aktif kembali untuk retry manual
11. Verifikasi (dibaca lewat fixture BE) Plan Version `PT Push Dua` tetap `v2`
12. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom sama dengan `N_log_custom`

### TC-AC-PF-721: Push Update tanpa respons (timeout atau jaringan terputus): toast Connection problem, dialog tetap terbuka

13. Dismiss toast error
14. Pasang intercept: respons Push Update tidak pernah diterima FE
15. Klik `[Push Update]` dan tunggu sampai FE menampilkan kegagalan
16. Lepas intercept
17. Verifikasi muncul toast error: "Connection problem. Please try again."
18. Verifikasi dialog `Push Plan Update` tetap terbuka
19. Verifikasi tombol `[Push Update]` aktif kembali untuk retry manual
20. Klik `[Cancel]` pada dialog `Push Plan Update`

### TC-AC-PF-299: Save Global Settings gagal 5xx: form tetap terbuka, input dipertahankan, nilai lama tidak berubah

21. Klik segmen Breadcrumb `Plans & Features`
22. Klik tab Global Settings
23. Ubah Max custom fields per asset name menjadi `8`
24. Pasang intercept: respons Save Global FAMS Settings dijawab server error
25. Klik `[Save]`
26. Lepas intercept
27. Verifikasi muncul toast error: "Error, failed to save global FAMS settings."
28. Verifikasi input Max custom fields per asset name tetap `8`
29. Verifikasi tombol `[Save]` aktif kembali
30. Tekan F5 dan konfirmasi dialog `beforeunload`
31. Verifikasi setelah refresh nilai tersimpan Max custom fields per asset name tetap `5`

### TC-AC-PF-720: Save Global Settings tanpa respons (timeout atau jaringan terputus): toast Connection problem, input dipertahankan

32. Ubah Max custom fields per asset name menjadi `9`
33. Pasang intercept: respons Save Global FAMS Settings tidak pernah diterima FE
34. Klik `[Save]` dan tunggu sampai FE menampilkan kegagalan
35. Lepas intercept
36. Verifikasi muncul toast error: "Connection problem. Please try again."
37. Verifikasi tab Global Settings tetap terbuka
38. Verifikasi nilai `9` dipertahankan pada Max custom fields per asset name
39. Verifikasi tombol `[Save]` aktif kembali untuk retry manual
40. Kembalikan Max custom fields per asset name ke nilai tersimpan `5`

## Notes

- Alasan di atas sekitar 35 langkah (40 langkah): keempat blok satu kelas harness (b, kegagalan atau tanpa respons yang dipaksakan), berdiri sendiri (Push Update pada `PT Push Dua` dan Save Global Settings pada form sendiri), dan tiap pasangan blok memakai dialog atau form yang sama sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan lebih lanjut menambah login, hook, dan pemulihan Dataset per spec.
- Penyimpangan urutan (S-10): TC-AC-PF-721 ditulis sebelum TC-AC-PF-299 karena dialog Push Update yang sama dipakai berulang; TC-AC-PF-720 mengikuti TC-AC-PF-299 pada form yang sama.
- Langkah penghubung (S-03): langkah 1 sampai 4 membawa layar ke Tab Assigned Clients `Paket Push`; langkah 2 menemukan baris target (R-16); langkah 13 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 20 menutup dialog; langkah 21 dan 22 membawa layar ke tab Global Settings; langkah 40 memulihkan field form dirty (S-09).
- Langkah 11 dan 12 membaca Plan Version dan jumlah entri Changelog lewat fixture BE (state data) karena dialog Push Update masih terbuka.
- Temuan untuk QA:
  - TC-AC-PF-280: langkah 5 TC meminta kembali ke tab Custom dan membuka Changelog sementara Expected b menyatakan dialog tetap dapat diulang; keduanya tidak dapat dilakukan bersamaan di UI. Spec membaca Plan Version dan Changelog lewat fixture BE.
  - TC-AC-PF-299: langkah 3 menekan F5 saat form dirty memicu dialog `beforeunload`; TC tidak menyebut penanganannya. Spec menuliskannya sebagai kemampuan teknis yang disediakan tim FE.
  - TC-AC-PF-721: pada Dataset Plan P `PT Push Dua` berada di v2; TC tidak menyatakan apakah request sempat diproses server pada skenario tanpa respons, sehingga Plan Version tidak diasersi.
